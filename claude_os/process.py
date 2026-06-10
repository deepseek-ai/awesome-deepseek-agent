"""
ClaudeOS ProcessTable — lightweight cooperative-multitasking process model.

Each process is a Python callable tagged with a PID, name, and status.
Processes are cooperative (no preemption) and run to completion when
the scheduler dispatches them.
"""

from __future__ import annotations

import itertools
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class Status(str, Enum):
    READY = "ready"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    ZOMBIE = "zombie"


_pid_counter = itertools.count(1)


@dataclass
class Process:
    pid: int
    name: str
    fn: Callable[..., Any]
    args: tuple = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    status: Status = Status.READY
    created_at: float = field(default_factory=time.time)
    finished_at: Optional[float] = None
    result: Any = None
    error: Optional[str] = None

    def run(self) -> Any:
        self.status = Status.RUNNING
        try:
            self.result = self.fn(*self.args, **self.kwargs)
            self.status = Status.DONE
        except Exception as exc:
            self.error = str(exc)
            self.status = Status.FAILED
        finally:
            self.finished_at = time.time()
        return self.result

    def summary(self) -> Dict[str, Any]:
        return {
            "pid": self.pid,
            "name": self.name,
            "status": self.status.value,
            "created_at": round(self.created_at, 2),
            "finished_at": round(self.finished_at, 2) if self.finished_at else None,
            "error": self.error,
        }


class ProcessTable:
    def __init__(self) -> None:
        self._table: Dict[int, Process] = {}

    def spawn(self, name: str, fn: Callable[..., Any], *args: Any, **kwargs: Any) -> int:
        pid = next(_pid_counter)
        proc = Process(pid=pid, name=name, fn=fn, args=args, kwargs=kwargs)
        self._table[pid] = proc
        return pid

    def get(self, pid: int) -> Optional[Process]:
        return self._table.get(pid)

    def kill(self, pid: int) -> bool:
        proc = self._table.get(pid)
        if proc is None:
            return False
        proc.status = Status.ZOMBIE
        proc.finished_at = time.time()
        return True

    def list_all(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        procs = list(self._table.values())
        if status:
            procs = [p for p in procs if p.status.value == status]
        return [p.summary() for p in procs]

    def reap_zombies(self) -> int:
        dead = [pid for pid, p in self._table.items() if p.status == Status.ZOMBIE]
        for pid in dead:
            del self._table[pid]
        return len(dead)

    def next_ready(self) -> Optional[Process]:
        for proc in self._table.values():
            if proc.status == Status.READY:
                return proc
        return None
