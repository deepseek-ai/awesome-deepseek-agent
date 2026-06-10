"""
ClaudeOS Coworker — named background agents built on CronDaemon.

Each coworker has a role name, a schedule, a list of secret names it needs,
and an action callable. The CoworkerRegistry wraps CronDaemon and resolves
secrets from the SecretVault before each invocation.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from .cron import CronDaemon
from .secrets import SecretVault


@dataclass
class Coworker:
    name: str
    schedule: str
    secret_names: List[str]
    action: Callable[[Dict[str, str]], Any]
    job_id: int
    enabled: bool = True
    created_at: float = field(default_factory=time.time)

    def summary(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "schedule": self.schedule,
            "secrets": self.secret_names,
            "job_id": self.job_id,
            "enabled": self.enabled,
        }


class CoworkerRegistry:
    """Manages named coworkers backed by the CronDaemon."""

    def __init__(self, cron: CronDaemon, vault: SecretVault) -> None:
        self._cron = cron
        self._vault = vault
        self._workers: Dict[str, Coworker] = {}
        self._lock = threading.Lock()

    def register(
        self,
        name: str,
        schedule: str,
        secret_names: List[str],
        action: Callable[[Dict[str, str]], Any],
    ) -> int:
        """Register a coworker and return its underlying cron job_id."""
        vault_ref = self._vault
        secret_names_copy = list(secret_names)

        def _wrapped() -> Any:
            secrets = {k: vault_ref.get(k) or "" for k in secret_names_copy}
            return action(secrets)

        with self._lock:
            job_id = self._cron.add(name, schedule, _wrapped)
            self._workers[name] = Coworker(
                name=name,
                schedule=schedule,
                secret_names=secret_names_copy,
                action=action,
                job_id=job_id,
            )
        return job_id

    def unregister(self, name: str) -> bool:
        with self._lock:
            worker = self._workers.pop(name, None)
        if worker is None:
            return False
        return self._cron.remove(worker.job_id)

    def list_workers(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [w.summary() for w in self._workers.values()]

    def fire(self, name: str) -> bool:
        with self._lock:
            worker = self._workers.get(name)
        if worker is None:
            return False
        return self._cron.run_now(worker.job_id)

    def enable(self, name: str) -> bool:
        with self._lock:
            worker = self._workers.get(name)
        if worker is None:
            return False
        worker.enabled = True
        return self._cron.enable(worker.job_id)

    def disable(self, name: str) -> bool:
        with self._lock:
            worker = self._workers.get(name)
        if worker is None:
            return False
        worker.enabled = False
        return self._cron.disable(worker.job_id)
