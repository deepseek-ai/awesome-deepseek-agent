"""
ClaudeOS VirtualFS — in-memory hierarchical filesystem.

Paths use POSIX-style slashes.  Everything is stored in a flat dict keyed
by absolute path; directories are inferred from the key prefixes.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional


class VirtualFS:
    def __init__(self) -> None:
        self._files: Dict[str, Dict[str, Any]] = {}

    def init(self) -> None:
        for path in ("/tmp", "/home", "/etc", "/var/log"):
            self._mkdir(path)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def write(self, path: str, content: Any, *, mode: str = "w") -> None:
        path = self._normalise(path)
        existing = self._files.get(path, {})
        if mode == "a" and "content" in existing:
            content = str(existing["content"]) + str(content)
        self._files[path] = {
            "type": "file",
            "content": content,
            "size": len(str(content)),
            "mtime": time.time(),
            "ctime": existing.get("ctime", time.time()),
        }

    def read(self, path: str) -> Optional[Any]:
        entry = self._files.get(self._normalise(path))
        if entry is None or entry["type"] != "file":
            return None
        return entry["content"]

    def delete(self, path: str) -> bool:
        path = self._normalise(path)
        if path in self._files:
            del self._files[path]
            return True
        return False

    def list_dir(self, path: str = "/") -> List[Dict[str, Any]]:
        path = self._normalise(path).rstrip("/")
        results = []
        seen_dirs: set = set()
        for key, meta in self._files.items():
            if not key.startswith(path + "/") and key != path:
                continue
            rel = key[len(path) :].lstrip("/")
            if not rel:
                continue
            parts = rel.split("/")
            if len(parts) == 1:
                results.append({"name": parts[0], "type": meta["type"], "size": meta.get("size", 0)})
            else:
                dname = parts[0]
                if dname not in seen_dirs:
                    seen_dirs.add(dname)
                    results.append({"name": dname, "type": "dir", "size": 0})
        return results

    def entry_count(self) -> int:
        return len(self._files)

    def stat(self, path: str) -> Optional[Dict[str, Any]]:
        entry = self._files.get(self._normalise(path))
        if entry is None:
            return None
        return {k: v for k, v in entry.items() if k != "content"}

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _mkdir(self, path: str) -> None:
        path = self._normalise(path)
        self._files[path] = {"type": "dir", "size": 0, "mtime": time.time(), "ctime": time.time()}

    @staticmethod
    def _normalise(path: str) -> str:
        path = path.strip()
        if not path.startswith("/"):
            path = "/" + path
        return path.rstrip("/") or "/"
