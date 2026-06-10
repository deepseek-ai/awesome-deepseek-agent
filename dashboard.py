#!/usr/bin/env python3
"""
ClaudeOS Live Dashboard — real-time kernel monitor.

Usage:
  python dashboard.py           # boot kernel + demo coworkers
  python dashboard.py --quiet   # boot kernel, no demo jobs
  python dashboard.py --help
"""

from __future__ import annotations

import os
import shutil
import signal
import sys
import time
from typing import Any, Dict, List

from claude_os.kernel import Kernel

# ── ANSI ──────────────────────────────────────────────────────────────────────
R  = "\033[0m"
BD = "\033[1m"
DM = "\033[2m"
CY = "\033[36m"
GR = "\033[32m"
YL = "\033[33m"
RD = "\033[31m"
MG = "\033[35m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR       = "\033[2J\033[H"

# ── box drawing ───────────────────────────────────────────────────────────────
def _clip(s: str, w: int) -> str:
    return s if len(s) <= w else s[: w - 1] + "…"

def box_top(title: str, w: int) -> str:
    inner = f"─ {title} "
    return "┌" + inner + "─" * max(0, w - 2 - len(inner)) + "┐"

def box_bot(w: int) -> str:
    return "└" + "─" * (w - 2) + "┘"

def box_row(text: str, w: int) -> str:
    visible = _clip(text, w - 2)
    return "│" + visible + " " * (w - 2 - len(visible)) + "│"

def box_sep(w: int) -> str:
    return "├" + "─" * (w - 2) + "┤"

# ── render ────────────────────────────────────────────────────────────────────
def render(kernel: Kernel) -> str:
    cols = max(60, min(120, shutil.get_terminal_size((80, 24)).columns - 2))

    stats:   Dict[str, Any] = kernel.syscall("kernel_stats")
    jobs:    List[Dict]     = kernel.syscall("cron_list")
    workers: List[Dict]     = kernel.syscall("coworker_list")
    mem_keys: List[str]     = kernel.syscall("mem_list")
    secrets:  List[str]     = kernel.syscall("secret_list")
    fire_log: List[Dict]    = kernel.syscall("cron_log", 6)

    out: List[str] = []

    # ── header ────────────────────────────────────────────────────────────────
    ver     = stats["version"]
    uptime  = stats["uptime_seconds"]
    scalls  = stats["syscall_count"]
    ts_now  = time.strftime("%H:%M:%S")
    hdr1    = f"  ClaudeOS Live Dashboard  ·  kernel v{ver}  "
    hdr2    = f"  uptime {uptime}s  ·  syscalls {scalls}  ·  {ts_now}  ·  Ctrl+C to exit  "
    out.append(BD + CY + "╔" + "═" * (cols - 2) + "╗" + R)
    out.append(BD + CY + "║" + hdr1.center(cols - 2) + "║" + R)
    out.append(BD + CY + "║" + hdr2.center(cols - 2) + "║" + R)
    out.append(BD + CY + "╚" + "═" * (cols - 2) + "╝" + R)
    out.append("")

    # ── two-column: stats | secrets+memory ────────────────────────────────────
    half = (cols - 3) // 2

    stat_rows = [
        f" memory_keys   : {stats['memory_keys']}",
        f" processes     : {stats['processes']}",
        f" cron_jobs     : {stats['cron_jobs']}",
        f" coworkers     : {stats['coworkers']}",
        f" secrets       : {stats['secrets']}",
        f" fs_entries    : {stats['fs_entries']}",
    ]
    left = [box_top("Kernel Stats", half)]
    for r in stat_rows:
        left.append(box_row(r, half))
    left.append(box_bot(half))

    right = [box_top("Secrets", half)]
    if secrets:
        for s in secrets:
            right.append(box_row(f" {s}  =  ***", half))
    else:
        right.append(box_row(" (none stored)", half))
    right.append(box_bot(half))
    right.append("")
    right.append(box_top("Memory", half))
    visible_keys = mem_keys[:4]
    for k in visible_keys:
        v = kernel.syscall("mem_read", k)
        right.append(box_row(f" {k} = {v!r}", half))
    if len(mem_keys) > 4:
        right.append(box_row(f" … +{len(mem_keys) - 4} more", half))
    if not mem_keys:
        right.append(box_row(" (empty)", half))
    right.append(box_bot(half))

    for i in range(max(len(left), len(right))):
        l = left[i]  if i < len(left)  else " " * half
        r = right[i] if i < len(right) else ""
        out.append(l + "  " + r)

    out.append("")

    # ── cron jobs ─────────────────────────────────────────────────────────────
    out.append(box_top("Cron Jobs", cols))
    out.append(box_row(
        f"  {'ID':>3}  {'NAME':<18}  {'INTERVAL':<8}  {'RUNS':>4}  {'LAST RUN':<10}  EN",
        cols
    ))
    out.append(box_sep(cols))
    if jobs:
        for j in jobs:
            en  = "yes" if j["enabled"] else "no "
            err = f"  ⚠ {j['last_error'][:20]}" if j["last_error"] else ""
            row = f"  {j['id']:>3}  {j['name']:<18}  {j['interval']:<8}  {j['run_count']:>4}  {j['last_run']:<10}  {en}{err}"
            color = R if j["enabled"] else DM
            out.append(color + box_row(row, cols) + R)
    else:
        out.append(DM + box_row("  (no cron jobs — add one with: coworker add …)", cols) + R)
    out.append(box_bot(cols))
    out.append("")

    # ── coworkers ─────────────────────────────────────────────────────────────
    out.append(box_top("Coworkers", cols))
    out.append(box_row(
        f"  {'NAME':<18}  {'SCHEDULE':<8}  EN   SECRETS",
        cols
    ))
    out.append(box_sep(cols))
    if workers:
        for w in workers:
            en   = "yes" if w["enabled"] else "no "
            secs = ", ".join(w["secrets"]) if w["secrets"] else "(none)"
            row  = f"  {w['name']:<18}  {w['schedule']:<8}  {en}  {secs}"
            color = R if w["enabled"] else DM
            out.append(color + box_row(row, cols) + R)
    else:
        out.append(DM + box_row("  (no coworkers registered)", cols) + R)
    out.append(box_bot(cols))
    out.append("")

    # ── fire log ──────────────────────────────────────────────────────────────
    out.append(box_top("Fire Log", cols))
    if fire_log:
        for e in reversed(fire_log):
            err = f"  ⚠ {e['error']}" if e["error"] else ""
            row = f"  {e['ts']}  #{e['id']} {e['name']:<18}  run={e['run_count']}{err}"
            color = RD if e["error"] else GR
            out.append(color + box_row(row, cols) + R)
    else:
        out.append(DM + box_row("  (no events yet — waiting for first fire …)", cols) + R)
    out.append(box_bot(cols))

    return "\n".join(out)


# ── demo jobs ─────────────────────────────────────────────────────────────────
def register_demo_jobs(kernel: Kernel) -> None:
    """Register a few interesting jobs so the dashboard has something to show."""

    ticks = {"n": 0}

    def heartbeat(secrets: dict) -> str:
        ticks["n"] += 1
        kernel.syscall("mem_write", "demo.ticks", ticks["n"])
        kernel.syscall("fs_write", "/var/log/hb.txt",
                       f"alive tick={ticks['n']} at {time.strftime('%H:%M:%S')}\n")
        return f"tick {ticks['n']}"

    def fast_counter(secrets: dict) -> int:
        ticks["n"] += 1
        kernel.syscall("mem_write", "demo.ticks", ticks["n"])
        return ticks["n"]

    kernel.coworkers.register("heartbeat", "10s", [], heartbeat)
    kernel.coworkers.register("fast-tick", "3s",  [], fast_counter)
    kernel.syscall("secret_set", "DEMO_API_KEY",   "demo-value-hidden")
    kernel.syscall("secret_set", "DEEPSEEK_API_KEY", "sk-demo-hidden")
    kernel.syscall("mem_write", "dashboard.started", time.strftime("%H:%M:%S"))


# ── main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    quiet = "--quiet" in sys.argv

    kernel = Kernel()
    kernel.boot_silent()

    if not quiet:
        register_demo_jobs(kernel)

    def _shutdown(sig=None, frame=None):
        kernel.shutdown_silent()
        sys.stdout.write(SHOW_CURSOR + "\n")
        print("[dashboard] kernel halted — goodbye.")
        sys.exit(0)

    signal.signal(signal.SIGINT,  _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    sys.stdout.write(HIDE_CURSOR)

    try:
        while True:
            frame = render(kernel)
            sys.stdout.write(CLEAR + frame + "\n")
            sys.stdout.flush()
            time.sleep(1.0)
    finally:
        _shutdown()


if __name__ == "__main__":
    main()
