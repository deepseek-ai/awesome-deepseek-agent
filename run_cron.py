#!/usr/bin/env python3
"""
Headless ClaudeOS runner for CI / GitHub Actions cron jobs.

Usage:
    python run_cron.py

Secrets are loaded automatically from environment variables matching:
  *_API_KEY  (e.g. DEEPSEEK_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY)
  CLAUDE_SECRET_*

Add coworker registrations below and they will be fired immediately.
"""

from __future__ import annotations

import sys
import time

from claude_os.kernel import Kernel


def register_coworkers(kernel: Kernel) -> None:
    """Register project-specific coworkers here."""

    def heartbeat(secrets: dict) -> str:
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        kernel.syscall("fs_write", "/var/log/heartbeat.txt", f"alive at {ts}\n")
        return ts

    kernel.coworkers.register(
        name="heartbeat",
        schedule="1d",
        secret_names=[],
        action=heartbeat,
    )

    # Example: add an API-key-dependent coworker
    # def fetch_data(secrets: dict) -> str:
    #     api_key = secrets.get("DEEPSEEK_API_KEY", "")
    #     # ... call external service with api_key ...
    #     return "done"
    #
    # kernel.coworkers.register(
    #     name="data-fetcher",
    #     schedule="1h",
    #     secret_names=["DEEPSEEK_API_KEY"],
    #     action=fetch_data,
    # )


def main() -> int:
    kernel = Kernel()
    kernel.boot_silent()

    loaded = kernel.secrets.load_env()
    print(f"[cron-worker] loaded {loaded} secret(s) from environment")

    register_coworkers(kernel)

    workers = kernel.coworkers.list_workers()
    if not workers:
        print("[cron-worker] no coworkers registered — nothing to do")
        kernel.shutdown_silent()
        return 0

    print(f"[cron-worker] firing {len(workers)} coworker(s):")
    errors = 0
    for w in workers:
        name = w["name"]
        ok = kernel.coworkers.fire(name)
        status = "OK" if ok else "FAIL"
        print(f"  [{status}] {name}")
        if not ok:
            errors += 1

    kernel.shutdown_silent()
    return errors


if __name__ == "__main__":
    sys.exit(main())
