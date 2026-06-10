"""
ClaudeOS MemoryBus — hierarchical key-value memory subsystem.

Provides two tiers:
  • short-term  — volatile, cleared on shutdown
  • long-term   — persisted to JSON on disk
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, Dict, List, Optional

_PERSIST_PATH = os.path.join(os.path.dirname(__file__), ".long_term_memory.json")


class MemoryBus:
    def __init__(self) -> None:
        self._short: Dict[str, Any] = {}
        self._long: Dict[str, Any] = {}

    def init(self) -> None:
        if os.path.exists(_PERSIST_PATH):
            try:
                with open(_PERSIST_PATH) as f:
                    self._long = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._long = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def write(self, key: str, value: Any, *, persist: bool = False) -> None:
        entry = {"value": value, "ts": time.time()}
        if persist:
            self._long[key] = entry
            self._flush()
        else:
            self._short[key] = entry

    def read(self, key: str) -> Optional[Any]:
        for store in (self._short, self._long):
            if key in store:
                return store[key]["value"]
        return None

    def delete(self, key: str) -> bool:
        removed = False
        for store in (self._short, self._long):
            if key in store:
                del store[key]
                removed = True
        self._flush()
        return removed

    def list_keys(self, tier: str = "all") -> List[str]:
        if tier == "short":
            return list(self._short)
        if tier == "long":
            return list(self._long)
        return sorted(set(self._short) | set(self._long))

    def dump(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for k in self.list_keys():
            for store in (self._short, self._long):
                if k in store:
                    tier = "long" if store is self._long else "short"
                    out[k] = {"value": store[k]["value"], "tier": tier}
                    break
        return out

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _flush(self) -> None:
        try:
            with open(_PERSIST_PATH, "w") as f:
                json.dump(self._long, f, indent=2, default=str)
        except OSError:
            pass
