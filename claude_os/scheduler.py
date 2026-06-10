"""
ClaudeOS Scheduler — FIFO task queue with a background worker thread.

Tasks are callables spawned as ProcessTable entries; the scheduler
runs them one at a time in a daemon thread so the shell stays responsive.
"""

from __future__ import annotations

import queue
import threading
import time
from typing import Any, Callable, Dict, List, Optional

from .process import ProcessTable, Status


class Scheduler:
    def __init__(self, processes: ProcessTable) -> None:
        self._processes = processes
        self._queue: queue.Queue[int] = queue.Queue()
        self._thread: Optional[threading.Thread] = None
        self._running = False
        self._log: List[Dict[str, Any]] = []

    def start(self) -> None:
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True, name="sched")
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)

    def enqueue(self, pid: int) -> bool:
        proc = self._processes.get(pid)
        if proc is None or proc.status != Status.READY:
            return False
        self._queue.put(pid)
        return True

    def status(self) -> Dict[str, Any]:
        return {
            "running": self._running,
            "queue_depth": self._queue.qsize(),
            "completed": len(self._log),
            "recent": self._log[-5:],
        }

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _loop(self) -> None:
        while self._running:
            try:
                pid = self._queue.get(timeout=0.2)
            except queue.Empty:
                continue
            proc = self._processes.get(pid)
            if proc is None:
                continue
            proc.run()
            self._log.append(
                {
                    "pid": pid,
                    "name": proc.name,
                    "status": proc.status.value,
                    "ts": time.time(),
                }
            )
            self._queue.task_done()
