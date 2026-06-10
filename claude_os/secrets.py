"""
ClaudeOS SecretVault — in-memory secret store.

Secrets are NEVER persisted to disk, NEVER included in log output,
and values are always masked when displayed. Load from env vars at boot.

Env var patterns loaded by default:
  *_API_KEY   (e.g. DEEPSEEK_API_KEY, OPENAI_API_KEY)
  CLAUDE_SECRET_*
"""

from __future__ import annotations

import os
import threading
from typing import Dict, List, Optional


class SecretVault:
    """Thread-safe in-memory store for API keys and credentials."""

    _DEFAULT_PATTERNS = ("_API_KEY", "CLAUDE_SECRET_")

    def __init__(self) -> None:
        self._store: Dict[str, str] = {}
        self._lock = threading.Lock()

    def set(self, name: str, value: str) -> None:
        with self._lock:
            self._store[name] = value

    def get(self, name: str) -> Optional[str]:
        with self._lock:
            return self._store.get(name)

    def delete(self, name: str) -> bool:
        with self._lock:
            if name in self._store:
                del self._store[name]
                return True
        return False

    def list_names(self) -> List[str]:
        with self._lock:
            return list(self._store.keys())

    def load_env(self, patterns: Optional[List[str]] = None) -> int:
        """Load matching env vars into the vault. Returns count loaded."""
        active = patterns if patterns is not None else list(self._DEFAULT_PATTERNS)
        loaded = 0
        for key, val in os.environ.items():
            if any(key.endswith(p) or key.startswith(p) for p in active):
                self.set(key, val)
                loaded += 1
        return loaded
