"""
Smoke tests for ClaudeOS subsystems.
Run with: python -m claude_os.tests
"""

from __future__ import annotations

import time
import sys


def run_tests() -> None:
    passed = 0
    failed = 0

    def ok(name: str) -> None:
        nonlocal passed
        passed += 1
        print(f"  PASS  {name}")

    def fail(name: str, reason: str) -> None:
        nonlocal failed
        failed += 1
        print(f"  FAIL  {name}: {reason}")

    print("\n=== ClaudeOS smoke tests ===\n")

    # ------------------------------------------------------------------
    # MemoryBus
    # ------------------------------------------------------------------
    from claude_os.memory import MemoryBus
    m = MemoryBus()
    m.init()

    m.write("x", 42)
    assert m.read("x") == 42, "read after write"
    ok("memory: basic write/read")

    m.write("y", "hello", persist=False)
    keys = m.list_keys()
    assert "x" in keys and "y" in keys
    ok("memory: list_keys")

    m.delete("x")
    assert m.read("x") is None
    ok("memory: delete")

    # ------------------------------------------------------------------
    # VirtualFS
    # ------------------------------------------------------------------
    from claude_os.fs import VirtualFS
    fs = VirtualFS()
    fs.init()

    fs.write("/tmp/test.txt", "hello world")
    assert fs.read("/tmp/test.txt") == "hello world"
    ok("fs: write/read")

    fs.write("/tmp/test.txt", " more", mode="a")
    assert fs.read("/tmp/test.txt") == "hello world more"
    ok("fs: append mode")

    listing = fs.list_dir("/tmp")
    names = [e["name"] for e in listing]
    assert "test.txt" in names
    ok("fs: list_dir")

    fs.delete("/tmp/test.txt")
    assert fs.read("/tmp/test.txt") is None
    ok("fs: delete")

    # ------------------------------------------------------------------
    # ProcessTable
    # ------------------------------------------------------------------
    from claude_os.process import ProcessTable, Status
    pt = ProcessTable()

    result_holder = []
    pid = pt.spawn("test-task", lambda: result_holder.append(99))
    proc = pt.get(pid)
    assert proc is not None and proc.status == Status.READY
    ok("process: spawn")

    proc.run()
    assert proc.status == Status.DONE and result_holder == [99]
    ok("process: run to completion")

    pid2 = pt.spawn("killable", lambda: None)
    pt.kill(pid2)
    assert pt.get(pid2).status == Status.ZOMBIE
    ok("process: kill → zombie")

    reaped = pt.reap_zombies()
    assert reaped == 1 and pt.get(pid2) is None
    ok("process: reap zombies")

    # ------------------------------------------------------------------
    # Scheduler
    # ------------------------------------------------------------------
    from claude_os.scheduler import Scheduler
    pt2 = ProcessTable()
    sched = Scheduler(pt2)
    sched.start()

    done = []
    pid3 = pt2.spawn("sched-task", lambda: done.append(1))
    queued = sched.enqueue(pid3)
    assert queued
    ok("scheduler: enqueue")

    time.sleep(0.3)
    assert done == [1], f"task not executed, done={done}"
    ok("scheduler: task executed")

    sched.stop()

    # ------------------------------------------------------------------
    # Kernel
    # ------------------------------------------------------------------
    from claude_os.kernel import Kernel
    k = Kernel()
    k.boot()

    k.syscall("mem_write", "greeting", "hello")
    assert k.syscall("mem_read", "greeting") == "hello"
    ok("kernel: mem syscalls")

    k.syscall("fs_write", "/tmp/k.txt", "kernel test")
    assert k.syscall("fs_read", "/tmp/k.txt") == "kernel test"
    ok("kernel: fs syscalls")

    stats = k.syscall("kernel_stats")
    assert stats["version"] == "0.2.0"
    ok("kernel: stats syscall")

    k.shutdown()

    # ------------------------------------------------------------------
    # CronDaemon
    # ------------------------------------------------------------------
    from claude_os.cron import CronDaemon, parse_interval

    assert parse_interval("30s") == 30.0
    assert parse_interval("5m") == 300.0
    assert parse_interval("2h") == 7200.0
    assert parse_interval("1d") == 86400.0
    ok("cron: parse_interval")

    cron = CronDaemon()
    cron.start()

    fired = []
    job_id = cron.add("test-job", "1s", lambda: fired.append(1))
    assert len(cron.list_jobs()) == 1
    ok("cron: add job")

    time.sleep(1.5)
    assert len(fired) >= 1, f"job not fired, fired={fired}"
    ok("cron: job fires on interval")

    cron.disable(job_id)
    fired_before = len(fired)
    time.sleep(1.5)
    assert len(fired) == fired_before, "disabled job should not fire"
    ok("cron: disable prevents firing")

    cron.enable(job_id)
    cron.run_now(job_id)
    assert len(fired) > fired_before
    ok("cron: run_now fires immediately")

    log = cron.get_log()
    assert len(log) > 0
    ok("cron: fire log populated")

    cron.remove(job_id)
    assert len(cron.list_jobs()) == 0
    ok("cron: remove job")

    cron.stop()

    # ------------------------------------------------------------------
    # Kernel cron syscalls
    # ------------------------------------------------------------------
    k2 = Kernel()
    k2.boot()

    hits = []
    jid = k2.syscall("cron_add", "k-job", "1s", lambda: hits.append(1))
    time.sleep(1.5)
    assert len(hits) >= 1
    ok("kernel: cron_add + fires")

    k2.syscall("cron_disable", jid)
    before = len(hits)
    time.sleep(1.5)
    assert len(hits) == before
    ok("kernel: cron_disable via syscall")

    k2.syscall("cron_remove", jid)
    assert k2.syscall("cron_list") == []
    ok("kernel: cron_remove via syscall")

    k2.shutdown()

    # ------------------------------------------------------------------
    # SecretVault tests
    # ------------------------------------------------------------------

    from .secrets import SecretVault

    vault = SecretVault()

    vault.set("MY_KEY", "s3cr3t")
    assert vault.get("MY_KEY") == "s3cr3t"
    ok("secret: set/get")

    assert vault.list_names() == ["MY_KEY"]
    ok("secret: list_names returns names only")

    vault.delete("MY_KEY")
    assert vault.get("MY_KEY") is None
    ok("secret: delete")

    import os as _os
    _os.environ["TEST_API_KEY"] = "val1"
    _os.environ["CLAUDE_SECRET_FOO"] = "val2"
    count = vault.load_env()
    assert count >= 2
    assert vault.get("TEST_API_KEY") == "val1"
    assert vault.get("CLAUDE_SECRET_FOO") == "val2"
    del _os.environ["TEST_API_KEY"]
    del _os.environ["CLAUDE_SECRET_FOO"]
    ok("secret: load_env matches *_API_KEY and CLAUDE_SECRET_*")

    # secrets must not appear in kernel memory
    k3 = Kernel()
    k3.boot_silent()
    k3.syscall("secret_set", "HIDDEN", "topsecret")
    mem_keys = k3.syscall("mem_list")
    assert "HIDDEN" not in mem_keys
    k3.shutdown_silent()
    ok("secret: never stored in memory bus")

    # ------------------------------------------------------------------
    # CoworkerRegistry tests
    # ------------------------------------------------------------------

    from .coworker import CoworkerRegistry
    from .cron import CronDaemon

    cron_d = CronDaemon()
    cron_d.start()
    v2 = SecretVault()
    v2.set("APIKEY", "abc")
    registry = CoworkerRegistry(cron_d, v2)

    received: list = []

    def _worker_action(secrets: dict) -> None:
        received.append(secrets.get("APIKEY"))

    jid2 = registry.register("bot", "1d", ["APIKEY"], _worker_action)
    assert jid2 > 0
    ok("coworker: register returns job_id")

    workers = registry.list_workers()
    assert len(workers) == 1
    assert workers[0]["name"] == "bot"
    ok("coworker: list_workers")

    ok_fired = registry.fire("bot")
    assert ok_fired
    assert received == ["abc"]
    ok("coworker: fire injects secrets into action")

    registry.disable("bot")
    assert registry.list_workers()[0]["enabled"] is False
    registry.enable("bot")
    assert registry.list_workers()[0]["enabled"] is True
    ok("coworker: enable/disable")

    registry.unregister("bot")
    assert registry.list_workers() == []
    ok("coworker: unregister")

    cron_d.stop()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    total = passed + failed
    print(f"\n  {passed}/{total} passed", "✓" if failed == 0 else "✗")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    run_tests()
