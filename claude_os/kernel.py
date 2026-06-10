"""
ClaudeOS Kernel — core of the AI-native operating system.
Manages subsystems: memory, processes, filesystem, scheduler.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from .memory import MemoryBus
from .process import ProcessTable
from .fs import VirtualFS
from .scheduler import Scheduler
from .cron import CronDaemon
from .secrets import SecretVault
from .coworker import CoworkerRegistry


KERNEL_VERSION = "0.2.0"
BOOT_BANNER = r"""
   ___  _                 _        ___  ____
  / __\| |  __ _  _   _ | |  ___ / _ \/ ___|
 / /   | | / _` || | | || | / _ \ | | \___ \
/ /___ | || (_| || |_| || ||  __/ |_| |___) |
\____/ |_| \__,_| \__,_||_| \___|\___/|____/

  AI-Native Operating System  •  kernel v{version}
  Type 'help' for available commands.
""".format(version=KERNEL_VERSION)


@dataclass
class KernelStats:
    boot_time: float = field(default_factory=time.time)
    syscall_count: int = 0
    uptime_seconds: float = 0.0

    def refresh(self) -> None:
        self.uptime_seconds = time.time() - self.boot_time


class Kernel:
    """Central kernel — initialises all subsystems and exposes syscall API."""

    def __init__(self) -> None:
        self.stats = KernelStats()
        self.memory = MemoryBus()
        self.processes = ProcessTable()
        self.fs = VirtualFS()
        self.scheduler = Scheduler(self.processes)
        self.cron = CronDaemon()
        self.secrets = SecretVault()
        self.coworkers = CoworkerRegistry(self.cron, self.secrets)
        self._syscall_table: Dict[str, Callable[..., Any]] = {}
        self._register_builtin_syscalls()

    # ------------------------------------------------------------------
    # Boot / shutdown
    # ------------------------------------------------------------------

    def boot(self) -> None:
        print(BOOT_BANNER)
        self._start_subsystems()

    def boot_silent(self) -> None:
        """Boot without printing the banner — for headless/CI use."""
        self._start_subsystems()

    def _start_subsystems(self) -> None:
        self.memory.init()
        self.fs.init()
        self.scheduler.start()
        self.cron.start()
        self.memory.write("kernel.status", "running")

    def shutdown(self) -> None:
        self._stop_subsystems()
        print(f"\n[kernel] shutdown — uptime {self.stats.uptime_seconds:.1f}s")

    def shutdown_silent(self) -> None:
        """Shutdown without printing — for headless/CI use."""
        self._stop_subsystems()

    def _stop_subsystems(self) -> None:
        self.cron.stop()
        self.scheduler.stop()
        self.memory.write("kernel.status", "halted")
        self.stats.refresh()

    # ------------------------------------------------------------------
    # Syscall interface
    # ------------------------------------------------------------------

    def _register_builtin_syscalls(self) -> None:
        self._syscall_table.update(
            {
                "mem_read": self.memory.read,
                "mem_write": self.memory.write,
                "mem_list": self.memory.list_keys,
                "proc_spawn": self.processes.spawn,
                "proc_kill": self.processes.kill,
                "proc_list": self.processes.list_all,
                "fs_write": self.fs.write,
                "fs_read": self.fs.read,
                "fs_list": self.fs.list_dir,
                "fs_delete": self.fs.delete,
                "sched_queue": self.scheduler.enqueue,
                "sched_status": self.scheduler.status,
                "cron_add": self.cron.add,
                "cron_remove": self.cron.remove,
                "cron_enable": self.cron.enable,
                "cron_disable": self.cron.disable,
                "cron_list": self.cron.list_jobs,
                "cron_log": self.cron.get_log,
                "cron_run": self.cron.run_now,
                "secret_set": self.secrets.set,
                "secret_get": self.secrets.get,
                "secret_delete": self.secrets.delete,
                "secret_list": self.secrets.list_names,
                "secret_load_env": self.secrets.load_env,
                "coworker_register": self.coworkers.register,
                "coworker_unregister": self.coworkers.unregister,
                "coworker_list": self.coworkers.list_workers,
                "coworker_fire": self.coworkers.fire,
                "coworker_enable": self.coworkers.enable,
                "coworker_disable": self.coworkers.disable,
                "kernel_stats": self._get_stats,
            }
        )

    def syscall(self, name: str, *args: Any, **kwargs: Any) -> Any:
        self.stats.syscall_count += 1
        handler = self._syscall_table.get(name)
        if handler is None:
            raise OSError(f"unknown syscall: {name!r}")
        return handler(*args, **kwargs)

    def register_syscall(self, name: str, fn: Callable[..., Any]) -> None:
        """Allow modules to extend the syscall table at runtime."""
        self._syscall_table[name] = fn

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _get_stats(self) -> Dict[str, Any]:
        self.stats.refresh()
        return {
            "version": KERNEL_VERSION,
            "uptime_seconds": round(self.stats.uptime_seconds, 2),
            "syscall_count": self.stats.syscall_count,
            "memory_keys": len(self.memory.list_keys()),
            "processes": len(self.processes.list_all()),
            "cron_jobs": len(self.cron.list_jobs()),
            "coworkers": len(self.coworkers.list_workers()),
            "secrets": len(self.secrets.list_names()),
            "fs_entries": self.fs.entry_count(),
        }
