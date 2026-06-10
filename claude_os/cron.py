"""
ClaudeOS CronDaemon — interval-based task scheduler.

Jobs are defined by a name, an interval string, and a shell command string.
The daemon runs in a background thread and fires jobs when their interval
has elapsed since their last run.

Interval formats accepted:
  30s   → 30 seconds
  5m    → 5 minutes
  2h    → 2 hours
  1d    → 1 day
"""

from __future__ import annotations

import itertools
import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


_job_id_counter = itertools.count(1)


def parse_interval(spec: str) -> float:
    """Convert an interval string like '30s', '5m', '2h', '1d' to seconds."""
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    spec = spec.strip().lower()
    if spec[-1] in units:
        try:
            return float(spec[:-1]) * units[spec[-1]]
        except ValueError:
            pass
    try:
        return float(spec)
    except ValueError:
        raise ValueError(f"invalid interval: {spec!r}  (use e.g. 30s, 5m, 2h, 1d)")


@dataclass
class CronJob:
    job_id: int
    name: str
    interval_seconds: float
    interval_spec: str
    action: Callable[[], Any]
    enabled: bool = True
    run_count: int = 0
    last_run: Optional[float] = None
    last_result: Any = None
    last_error: Optional[str] = None
    created_at: float = field(default_factory=time.time)

    def is_due(self) -> bool:
        if not self.enabled:
            return False
        if self.last_run is None:
            return True
        return (time.time() - self.last_run) >= self.interval_seconds

    def fire(self) -> None:
        self.last_run = time.time()
        self.run_count += 1
        try:
            self.last_result = self.action()
            self.last_error = None
        except Exception as exc:
            self.last_result = None
            # Truncate error message to avoid leaking secret values from exception text
            msg = str(exc)
            self.last_error = msg[:120] + "…" if len(msg) > 120 else msg

    def summary(self) -> Dict[str, Any]:
        return {
            "id": self.job_id,
            "name": self.name,
            "interval": self.interval_spec,
            "enabled": self.enabled,
            "run_count": self.run_count,
            "last_run": time.strftime("%H:%M:%S", time.localtime(self.last_run)) if self.last_run else "never",
            "last_error": self.last_error,
        }


class CronDaemon:
    """Background thread that checks and fires due cron jobs every second."""

    TICK = 1.0

    def __init__(self) -> None:
        self._jobs: Dict[int, CronJob] = {}
        self._thread: Optional[threading.Thread] = None
        self._running = False
        self._lock = threading.Lock()
        self._fire_log: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def start(self) -> None:
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True, name="cron")
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)

    # ------------------------------------------------------------------
    # Public API (called from shell / kernel syscalls)
    # ------------------------------------------------------------------

    def add(self, name: str, interval_spec: str, action: Callable[[], Any]) -> int:
        interval_seconds = parse_interval(interval_spec)
        job_id = next(_job_id_counter)
        job = CronJob(
            job_id=job_id,
            name=name,
            interval_seconds=interval_seconds,
            interval_spec=interval_spec,
            action=action,
        )
        with self._lock:
            self._jobs[job_id] = job
        return job_id

    def remove(self, job_id: int) -> bool:
        with self._lock:
            if job_id in self._jobs:
                del self._jobs[job_id]
                return True
        return False

    def enable(self, job_id: int) -> bool:
        return self._set_enabled(job_id, True)

    def disable(self, job_id: int) -> bool:
        return self._set_enabled(job_id, False)

    def list_jobs(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [j.summary() for j in self._jobs.values()]

    def get_log(self, n: int = 10) -> List[Dict[str, Any]]:
        return self._fire_log[-n:]

    def run_now(self, job_id: int) -> bool:
        with self._lock:
            job = self._jobs.get(job_id)
        if job is None:
            return False
        job.fire()
        self._record(job)
        return True

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _loop(self) -> None:
        while self._running:
            time.sleep(self.TICK)
            with self._lock:
                due = [j for j in self._jobs.values() if j.is_due()]
            for job in due:
                job.fire()
                self._record(job)

    def _record(self, job: CronJob) -> None:
        self._fire_log.append(
            {
                "id": job.job_id,
                "name": job.name,
                "ts": time.strftime("%H:%M:%S"),
                "run_count": job.run_count,
                "error": job.last_error,
            }
        )

    def _set_enabled(self, job_id: int, state: bool) -> bool:
        with self._lock:
            job = self._jobs.get(job_id)
            if job is None:
                return False
            job.enabled = state
            return True
