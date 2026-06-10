"""
ClaudeOS Shell — interactive REPL on top of the kernel.

Built-in commands mirror a POSIX shell but all operations go through
the kernel syscall interface so every action is auditable.
"""

from __future__ import annotations

import json
import shlex
import sys
import time
from typing import Dict, List, Optional

from .kernel import Kernel


class Shell:
    PS1 = "claude@os:~$ "

    def __init__(self, kernel: Kernel) -> None:
        self.kernel = kernel
        self._history: List[str] = []
        self._cwd = "/"
        self._commands = {
            # memory
            "mem":      self._cmd_mem,
            "remember": self._cmd_remember,
            "recall":   self._cmd_recall,
            "forget":   self._cmd_forget,
            # filesystem
            "ls":       self._cmd_ls,
            "cat":      self._cmd_cat,
            "write":    self._cmd_write,
            "rm":       self._cmd_rm,
            "cd":       self._cmd_cd,
            "pwd":      self._cmd_pwd,
            # processes
            "ps":       self._cmd_ps,
            "spawn":    self._cmd_spawn,
            "kill":     self._cmd_kill,
            # scheduler
            "sched":    self._cmd_sched,
            # cron
            "cron":     self._cmd_cron,
            # secrets
            "secret":   self._cmd_secret,
            # coworkers
            "coworker": self._cmd_coworker,
            # system
            "stats":    self._cmd_stats,
            "history":  self._cmd_history,
            "help":     self._cmd_help,
            "exit":     self._cmd_exit,
            "quit":     self._cmd_exit,
        }

    def run(self) -> None:
        while True:
            try:
                line = input(self.PS1).strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not line:
                continue
            # Redact secret values before storing in history
            _hist_line = line
            _parts = line.split()
            if len(_parts) >= 3 and _parts[0] == "secret" and _parts[1] == "set":
                _hist_line = f"{_parts[0]} {_parts[1]} {_parts[2]} ***"
            self._history.append(_hist_line)
            self._dispatch(line)

    # ------------------------------------------------------------------
    # Dispatcher
    # ------------------------------------------------------------------

    def _dispatch(self, line: str) -> None:
        try:
            parts = shlex.split(line)
        except ValueError as exc:
            print(f"  parse error: {exc}")
            return
        cmd, *args = parts
        handler = self._commands.get(cmd)
        if handler is None:
            print(f"  {cmd}: command not found — type 'help' for a list")
            return
        try:
            handler(args)
        except SystemExit:
            raise
        except Exception as exc:
            print(f"  error: {exc}")

    # ------------------------------------------------------------------
    # Memory commands
    # ------------------------------------------------------------------

    def _cmd_mem(self, args: List[str]) -> None:
        dump = self.kernel.syscall("mem_list")
        if not dump:
            print("  (memory is empty)")
            return
        for key in dump:
            val = self.kernel.syscall("mem_read", key)
            print(f"  {key} = {val!r}")

    def _cmd_remember(self, args: List[str]) -> None:
        if len(args) < 2:
            print("  usage: remember <key> <value> [--persist]")
            return
        persist = "--persist" in args
        if persist:
            args = [a for a in args if a != "--persist"]
        key, value = args[0], " ".join(args[1:])
        self.kernel.syscall("mem_write", key, value, persist=persist)
        tier = "long-term" if persist else "short-term"
        print(f"  stored {key!r} in {tier} memory")

    def _cmd_recall(self, args: List[str]) -> None:
        if not args:
            print("  usage: recall <key>")
            return
        val = self.kernel.syscall("mem_read", args[0])
        if val is None:
            print(f"  {args[0]!r}: not found")
        else:
            print(f"  {args[0]} = {val!r}")

    def _cmd_forget(self, args: List[str]) -> None:
        if not args:
            print("  usage: forget <key>")
            return
        ok = self.kernel.syscall("mem_write", args[0], None)
        self.kernel.memory.delete(args[0])
        print(f"  {args[0]!r} removed from memory")

    # ------------------------------------------------------------------
    # Filesystem commands
    # ------------------------------------------------------------------

    def _cmd_ls(self, args: List[str]) -> None:
        path = args[0] if args else self._cwd
        entries = self.kernel.syscall("fs_list", path)
        if not entries:
            print(f"  (empty)")
            return
        for e in sorted(entries, key=lambda x: x["name"]):
            tag = "/" if e["type"] == "dir" else ""
            size = f"  {e['size']}B" if e["type"] == "file" else ""
            print(f"  {e['name']}{tag}{size}")

    def _cmd_cat(self, args: List[str]) -> None:
        if not args:
            print("  usage: cat <path>")
            return
        path = self._resolve(args[0])
        content = self.kernel.syscall("fs_read", path)
        if content is None:
            print(f"  {args[0]}: no such file")
        else:
            print(content)

    def _cmd_write(self, args: List[str]) -> None:
        if len(args) < 2:
            print("  usage: write <path> <content…>")
            return
        path = self._resolve(args[0])
        content = " ".join(args[1:])
        self.kernel.syscall("fs_write", path, content)
        print(f"  written {len(content)}B to {path}")

    def _cmd_rm(self, args: List[str]) -> None:
        if not args:
            print("  usage: rm <path>")
            return
        path = self._resolve(args[0])
        ok = self.kernel.syscall("fs_delete", path)
        if ok:
            print(f"  deleted {path}")
        else:
            print(f"  {args[0]}: no such file")

    def _cmd_cd(self, args: List[str]) -> None:
        self._cwd = self._resolve(args[0]) if args else "/"
        print(f"  cwd → {self._cwd}")

    def _cmd_pwd(self, args: List[str]) -> None:
        print(f"  {self._cwd}")

    # ------------------------------------------------------------------
    # Process commands
    # ------------------------------------------------------------------

    def _cmd_ps(self, args: List[str]) -> None:
        status_filter = args[0] if args else None
        procs = self.kernel.syscall("proc_list")
        if status_filter:
            procs = [p for p in procs if p["status"] == status_filter]
        if not procs:
            print("  (no processes)")
            return
        print(f"  {'PID':>5}  {'NAME':<24}  {'STATUS':<10}  CREATED")
        for p in procs:
            ts = time.strftime("%H:%M:%S", time.localtime(p["created_at"]))
            print(f"  {p['pid']:>5}  {p['name']:<24}  {p['status']:<10}  {ts}")

    def _cmd_spawn(self, args: List[str]) -> None:
        if not args:
            print("  usage: spawn <name>  (spawns a demo echo process)")
            return
        name = args[0]
        msg = " ".join(args[1:]) if len(args) > 1 else f"process '{name}' completed"

        def _task(message: str) -> str:
            time.sleep(0.05)
            return message

        pid = self.kernel.syscall("proc_spawn", name, _task, msg)
        self.kernel.syscall("sched_queue", pid)
        print(f"  spawned pid={pid} name={name!r}")

    def _cmd_kill(self, args: List[str]) -> None:
        if not args or not args[0].isdigit():
            print("  usage: kill <pid>")
            return
        ok = self.kernel.syscall("proc_kill", int(args[0]))
        if ok:
            print(f"  process {args[0]} killed")
        else:
            print(f"  pid {args[0]}: not found")

    # ------------------------------------------------------------------
    # Scheduler commands
    # ------------------------------------------------------------------

    def _cmd_sched(self, args: List[str]) -> None:
        info = self.kernel.syscall("sched_status")
        print(json.dumps(info, indent=2, default=str))

    # ------------------------------------------------------------------
    # Cron commands
    # ------------------------------------------------------------------

    def _cmd_cron(self, args: List[str]) -> None:
        sub = args[0] if args else "list"
        rest = args[1:]

        if sub == "list":
            jobs = self.kernel.syscall("cron_list")
            if not jobs:
                print("  (no cron jobs)")
                return
            print(f"  {'ID':>4}  {'NAME':<20}  {'INTERVAL':<8}  {'RUNS':>4}  {'LAST RUN':<10}  EN  ERROR")
            for j in jobs:
                en = "yes" if j["enabled"] else "no"
                err = j["last_error"] or ""
                print(f"  {j['id']:>4}  {j['name']:<20}  {j['interval']:<8}  {j['run_count']:>4}  {j['last_run']:<10}  {en:<3}  {err}")

        elif sub == "add":
            # cron add <name> <interval> <shell-command…>
            if len(rest) < 3:
                print("  usage: cron add <name> <interval> <command…>")
                print("  example: cron add heartbeat 10s write /var/log/hb.txt tick")
                return
            name, interval_spec = rest[0], rest[1]
            cmd_str = " ".join(rest[2:])
            # build a closure that replays the shell command
            shell_ref = self

            def _job_action(c: str = cmd_str) -> str:
                parts = c.split(None, 1)
                handler = shell_ref._commands.get(parts[0])
                if handler:
                    handler(parts[1:] if len(parts) > 1 else [])
                    return c
                return f"unknown command: {parts[0]}"

            try:
                job_id = self.kernel.syscall("cron_add", name, interval_spec, _job_action)
                print(f"  job #{job_id} '{name}' added — runs every {interval_spec}")
            except ValueError as exc:
                print(f"  {exc}")

        elif sub == "remove" or sub == "rm":
            if not rest or not rest[0].isdigit():
                print("  usage: cron remove <id>")
                return
            ok = self.kernel.syscall("cron_remove", int(rest[0]))
            print(f"  job #{rest[0]} {'removed' if ok else 'not found'}")

        elif sub == "enable":
            if not rest or not rest[0].isdigit():
                print("  usage: cron enable <id>")
                return
            self.kernel.syscall("cron_enable", int(rest[0]))
            print(f"  job #{rest[0]} enabled")

        elif sub == "disable":
            if not rest or not rest[0].isdigit():
                print("  usage: cron disable <id>")
                return
            self.kernel.syscall("cron_disable", int(rest[0]))
            print(f"  job #{rest[0]} disabled")

        elif sub == "run":
            if not rest or not rest[0].isdigit():
                print("  usage: cron run <id>")
                return
            ok = self.kernel.syscall("cron_run", int(rest[0]))
            print(f"  job #{rest[0]} {'triggered' if ok else 'not found'}")

        elif sub == "log":
            n = int(rest[0]) if rest and rest[0].isdigit() else 10
            entries = self.kernel.syscall("cron_log", n)
            if not entries:
                print("  (no log entries yet)")
                return
            for e in entries:
                err = f"  ERR: {e['error']}" if e["error"] else ""
                print(f"  {e['ts']}  #{e['id']} {e['name']}  run={e['run_count']}{err}")

        else:
            print(f"  unknown subcommand: {sub!r}")
            print("  subcommands: list, add, remove, enable, disable, run, log")

    # ------------------------------------------------------------------
    # Secret commands
    # ------------------------------------------------------------------

    def _cmd_secret(self, args: List[str]) -> None:
        sub = args[0] if args else "list"
        rest = args[1:]

        if sub == "list":
            names = self.kernel.syscall("secret_list")
            if not names:
                print("  (no secrets stored)")
                return
            for n in names:
                print(f"  {n} = ***")

        elif sub == "set":
            if len(rest) < 2:
                print("  usage: secret set <NAME> <VALUE>")
                return
            self.kernel.syscall("secret_set", rest[0], rest[1])
            print(f"  secret {rest[0]!r} stored")

        elif sub == "get":
            if not rest:
                print("  usage: secret get <NAME>")
                return
            val = self.kernel.syscall("secret_get", rest[0])
            if val is None:
                print(f"  {rest[0]!r}: not found")
            else:
                print(f"  {rest[0]} = ***")

        elif sub == "delete" or sub == "rm":
            if not rest:
                print("  usage: secret delete <NAME>")
                return
            ok = self.kernel.syscall("secret_delete", rest[0])
            print(f"  {rest[0]!r} {'deleted' if ok else 'not found'}")

        elif sub == "env":
            count = self.kernel.syscall("secret_load_env")
            print(f"  loaded {count} secret(s) from environment")

        else:
            print(f"  unknown subcommand: {sub!r}")
            print("  subcommands: list, set, get, delete, env")

    # ------------------------------------------------------------------
    # Coworker commands
    # ------------------------------------------------------------------

    def _cmd_coworker(self, args: List[str]) -> None:
        sub = args[0] if args else "list"
        rest = args[1:]

        if sub == "list":
            workers = self.kernel.syscall("coworker_list")
            if not workers:
                print("  (no coworkers registered)")
                return
            print(f"  {'NAME':<20}  {'SCHEDULE':<8}  EN   SECRETS")
            for w in workers:
                en = "yes" if w["enabled"] else "no"
                secs = ", ".join(w["secrets"]) or "(none)"
                print(f"  {w['name']:<20}  {w['schedule']:<8}  {en:<4} {secs}")

        elif sub == "add":
            # coworker add <name> <schedule> [secret_names…]
            if len(rest) < 2:
                print("  usage: coworker add <name> <schedule> [SECRET_NAME…]")
                print("  example: coworker add reporter 1h DEEPSEEK_API_KEY")
                return
            name, schedule = rest[0], rest[1]
            secret_names = rest[2:]
            vault_ref = self.kernel.secrets

            def _demo_action(secrets: dict, _n: str = name) -> str:
                return f"[{_n}] ran at {time.strftime('%H:%M:%S')}"

            try:
                job_id = self.kernel.syscall(
                    "coworker_register", name, schedule, secret_names, _demo_action
                )
                print(f"  coworker '{name}' registered (job #{job_id}) — runs every {schedule}")
                if secret_names:
                    print(f"  uses secrets: {', '.join(secret_names)}")
            except ValueError as exc:
                print(f"  {exc}")

        elif sub == "remove" or sub == "rm":
            if not rest:
                print("  usage: coworker remove <name>")
                return
            ok = self.kernel.syscall("coworker_unregister", rest[0])
            print(f"  coworker '{rest[0]}' {'removed' if ok else 'not found'}")

        elif sub == "fire":
            if not rest:
                print("  usage: coworker fire <name>")
                return
            ok = self.kernel.syscall("coworker_fire", rest[0])
            print(f"  coworker '{rest[0]}' {'triggered' if ok else 'not found'}")

        elif sub == "enable":
            if not rest:
                print("  usage: coworker enable <name>")
                return
            ok = self.kernel.syscall("coworker_enable", rest[0])
            print(f"  coworker '{rest[0]}' {'enabled' if ok else 'not found'}")

        elif sub == "disable":
            if not rest:
                print("  usage: coworker disable <name>")
                return
            ok = self.kernel.syscall("coworker_disable", rest[0])
            print(f"  coworker '{rest[0]}' {'disabled' if ok else 'not found'}")

        else:
            print(f"  unknown subcommand: {sub!r}")
            print("  subcommands: list, add, remove, fire, enable, disable")

    # ------------------------------------------------------------------
    # System commands
    # ------------------------------------------------------------------

    def _cmd_stats(self, args: List[str]) -> None:
        info = self.kernel.syscall("kernel_stats")
        width = max(len(k) for k in info)
        for k, v in info.items():
            print(f"  {k:<{width}} : {v}")

    def _cmd_history(self, args: List[str]) -> None:
        for i, cmd in enumerate(self._history[-20:], 1):
            print(f"  {i:>3}  {cmd}")

    def _cmd_help(self, args: List[str]) -> None:
        sections = {
            "Memory": [
                ("mem",      "list all keys in memory"),
                ("remember", "<key> <value> [--persist]  store a value"),
                ("recall",   "<key>                       retrieve a value"),
                ("forget",   "<key>                       delete a key"),
            ],
            "Filesystem": [
                ("ls",    "[path]          list directory"),
                ("cat",   "<path>          read a file"),
                ("write", "<path> <text>   create/overwrite a file"),
                ("rm",    "<path>          delete a file"),
                ("cd",    "[path]          change directory"),
                ("pwd",   "                show current directory"),
            ],
            "Processes": [
                ("ps",    "[status]        list processes"),
                ("spawn", "<name> [msg]    create and queue a process"),
                ("kill",  "<pid>           terminate a process"),
            ],
            "Scheduler": [
                ("sched", "show scheduler status and recent log"),
            ],
            "Cron": [
                ("cron list",            "list all scheduled jobs"),
                ("cron add <n> <iv> <cmd>", "add a job (iv: 30s / 5m / 2h / 1d)"),
                ("cron remove <id>",     "delete a job"),
                ("cron enable/disable",  "<id>  toggle a job on/off"),
                ("cron run <id>",        "fire a job immediately"),
                ("cron log [n]",         "show last n fire events (default 10)"),
            ],
            "Secrets": [
                ("secret list",          "list secret names (values always masked)"),
                ("secret set <N> <V>",   "store a secret in-memory"),
                ("secret get <N>",       "confirm a secret exists (shows ***)"),
                ("secret delete <N>",    "remove a secret"),
                ("secret env",           "load secrets from env vars (*_API_KEY etc.)"),
            ],
            "Coworkers": [
                ("coworker list",        "list registered background agents"),
                ("coworker add <N> <IV> [SECRETS…]", "register a named coworker"),
                ("coworker remove <N>",  "unregister a coworker"),
                ("coworker fire <N>",    "run a coworker immediately"),
                ("coworker enable/disable <N>", "toggle a coworker on/off"),
            ],
            "System": [
                ("stats",   "kernel statistics"),
                ("history", "command history"),
                ("help",    "this message"),
                ("exit",    "shutdown and quit"),
            ],
        }
        for section, cmds in sections.items():
            print(f"\n  [{section}]")
            for name, desc in cmds:
                print(f"    {name:<12} {desc}")
        print()

    def _cmd_exit(self, args: List[str]) -> None:
        self.kernel.shutdown()
        sys.exit(0)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _resolve(self, path: str) -> str:
        if path.startswith("/"):
            return path
        return self._cwd.rstrip("/") + "/" + path
