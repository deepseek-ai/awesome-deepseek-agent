#!/usr/bin/env python3
"""
ClaudeOS Web Dashboard — HTTP server, no external dependencies.

Usage:
  python web_dashboard.py            # serves on 0.0.0.0:8080
  python web_dashboard.py --port 9090
  python web_dashboard.py --quiet    # no demo jobs
"""

from __future__ import annotations

import json
import os
import signal
import sys
import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Dict, List

from claude_os.kernel import Kernel

# ── kernel bootstrap ──────────────────────────────────────────────────────────

def _register_demo_jobs(kernel: Kernel) -> None:
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

    kernel.coworkers.register("heartbeat",  "10s", [], heartbeat)
    kernel.coworkers.register("fast-tick",  "3s",  [], fast_counter)
    kernel.syscall("secret_set", "DEMO_API_KEY",    "demo-value-hidden")
    kernel.syscall("secret_set", "DEEPSEEK_API_KEY","sk-demo-hidden")
    kernel.syscall("mem_write",  "dashboard.started", time.strftime("%H:%M:%S"))


# ── JSON state builder ────────────────────────────────────────────────────────

def _build_state(kernel: Kernel) -> Dict[str, Any]:
    stats    = kernel.syscall("kernel_stats")
    jobs     = kernel.syscall("cron_list")
    workers  = kernel.syscall("coworker_list")
    mem_keys = kernel.syscall("mem_list")
    secrets  = kernel.syscall("secret_list")
    fire_log = kernel.syscall("cron_log", 8)

    memory = []
    for k in mem_keys[:6]:
        v = kernel.syscall("mem_read", k)
        memory.append({"key": k, "value": repr(v)})
    if len(mem_keys) > 6:
        memory.append({"key": f"… +{len(mem_keys)-6} more", "value": ""})

    return {
        "ts": time.strftime("%H:%M:%S"),
        "stats": stats,
        "secrets": [{"name": s, "value": "***"} for s in secrets],
        "memory": memory,
        "jobs": jobs,
        "workers": workers,
        "fire_log": list(reversed(fire_log)),
    }


# ── HTML page (served once, polls /api/state) ─────────────────────────────────

_HTML = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>ClaudeOS Dashboard</title>
<style>
  :root{--bg:#0d1117;--surface:#161b22;--border:#30363d;--text:#e6edf3;
        --dim:#8b949e;--cyan:#79c0ff;--green:#56d364;--yellow:#d29922;
        --red:#f85149;--purple:#bc8cff}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--text);font-family:'Cascadia Code',
       'Fira Mono',monospace;font-size:13px;padding:16px}
  header{border:2px solid var(--cyan);border-radius:6px;padding:10px 18px;
         margin-bottom:14px;display:flex;justify-content:space-between;
         align-items:center}
  header h1{color:var(--cyan);font-size:15px;font-weight:700}
  header span{color:var(--dim);font-size:12px}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
  .card{background:var(--surface);border:1px solid var(--border);
        border-radius:6px;padding:12px}
  .card h2{color:var(--cyan);font-size:11px;text-transform:uppercase;
           letter-spacing:.08em;margin-bottom:8px;padding-bottom:6px;
           border-bottom:1px solid var(--border)}
  table{width:100%;border-collapse:collapse}
  th{color:var(--dim);font-weight:600;text-align:left;padding:3px 6px;
     font-size:11px;border-bottom:1px solid var(--border)}
  td{padding:4px 6px;vertical-align:top}
  tr:hover td{background:rgba(255,255,255,.03)}
  .tag-yes{color:var(--green)} .tag-no{color:var(--red)}
  .masked{color:var(--purple)} .dim{color:var(--dim)}
  .err{color:var(--red)} .ok{color:var(--green)}
  .kv-key{color:var(--cyan);min-width:130px;display:inline-block}
  .kv-val{color:var(--text)}
  #status{position:fixed;bottom:10px;right:14px;font-size:11px;color:var(--dim)}
  .dot{display:inline-block;width:7px;height:7px;border-radius:50%;
       background:var(--green);margin-right:5px;animation:blink 1.4s infinite}
  @keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}
</style>
</head>
<body>
<header>
  <h1>&#9670; ClaudeOS Live Dashboard</h1>
  <span id="hdr-meta">loading…</span>
</header>
<div class="grid2">
  <div class="card" id="card-stats"><h2>Kernel Stats</h2><div id="stats"></div></div>
  <div class="card" id="card-secrets"><h2>Secrets</h2><div id="secrets"></div></div>
</div>
<div class="grid2">
  <div class="card"><h2>Memory</h2><div id="memory"></div></div>
  <div class="card"><h2>Fire Log</h2><div id="firelog"></div></div>
</div>
<div class="card" style="margin-bottom:12px"><h2>Cron Jobs</h2>
  <table><thead><tr><th>#</th><th>Name</th><th>Interval</th><th>Runs</th>
  <th>Last Run</th><th>Enabled</th><th>Last Error</th></tr></thead>
  <tbody id="cron-body"></tbody></table>
</div>
<div class="card"><h2>Coworkers</h2>
  <table><thead><tr><th>Name</th><th>Schedule</th><th>Enabled</th>
  <th>Secrets</th></tr></thead>
  <tbody id="worker-body"></tbody></table>
</div>
<div id="status"><span class="dot"></span>live</div>

<script>
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function en(v){return v?'<span class="tag-yes">yes</span>':'<span class="tag-no">no</span>'}

async function poll(){
  try{
    const r=await fetch('/api/state');
    const d=await r.json();
    const s=d.stats;

    document.getElementById('hdr-meta').textContent=
      `kernel v${s.version}  ·  uptime ${s.uptime_seconds}s  ·  `+
      `syscalls ${s.syscall_count}  ·  ${d.ts}`;

    document.getElementById('stats').innerHTML=
      Object.entries({
        memory_keys:s.memory_keys, processes:s.processes,
        cron_jobs:s.cron_jobs, coworkers:s.coworkers,
        secrets:s.secrets, fs_entries:s.fs_entries
      }).map(([k,v])=>
        `<div><span class="kv-key">${k}</span><span class="kv-val">${v}</span></div>`
      ).join('');

    document.getElementById('secrets').innerHTML=
      d.secrets.length
        ? d.secrets.map(x=>
            `<div><span class="kv-key">${esc(x.name)}</span>`+
            `<span class="masked">***</span></div>`).join('')
        : '<span class="dim">(none)</span>';

    document.getElementById('memory').innerHTML=
      d.memory.length
        ? d.memory.map(x=>
            `<div><span class="kv-key">${esc(x.key)}</span>`+
            `<span class="kv-val">${esc(x.value)}</span></div>`).join('')
        : '<span class="dim">(empty)</span>';

    document.getElementById('cron-body').innerHTML=
      d.jobs.map(j=>{
        const err=j.last_error
          ?`<span class="err">⚠ ${esc(j.last_error.slice(0,40))}</span>`:'';
        return `<tr><td>${j.id}</td><td>${esc(j.name)}</td><td>${j.interval}</td>`+
               `<td>${j.run_count}</td><td class="dim">${j.last_run||'—'}</td>`+
               `<td>${en(j.enabled)}</td><td>${err}</td></tr>`;
      }).join('') || '<tr><td colspan="7" class="dim">no jobs</td></tr>';

    document.getElementById('worker-body').innerHTML=
      d.workers.map(w=>{
        const sec=w.secrets.length?w.secrets.map(esc).join(', ')
                                  :'<span class="dim">(none)</span>';
        return `<tr><td>${esc(w.name)}</td><td>${w.schedule}</td>`+
               `<td>${en(w.enabled)}</td><td>${sec}</td></tr>`;
      }).join('') || '<tr><td colspan="4" class="dim">no coworkers</td></tr>';

    document.getElementById('firelog').innerHTML=
      d.fire_log.length
        ? d.fire_log.map(e=>{
            const err=e.error?`<span class="err"> ⚠${esc(e.error.slice(0,30))}</span>`:'';
            return `<div class="${e.error?'err':'ok'}">`+
                   `${e.ts} <b>#${e.id}</b> ${esc(e.name)}`+
                   ` <span class="dim">run=${e.run_count}</span>${err}</div>`;
          }).join('')
        : '<span class="dim">(no events yet)</span>';

  }catch(e){
    document.getElementById('hdr-meta').textContent='⚠ connection lost';
  }
  setTimeout(poll,1000);
}
poll();
</script>
</body>
</html>
"""

# ── HTTP handler ──────────────────────────────────────────────────────────────

class _Handler(BaseHTTPRequestHandler):
    kernel: Kernel  # injected as class attribute

    def do_GET(self) -> None:
        if self.path == "/api/state":
            data = json.dumps(_build_state(self.kernel)).encode()
            self._respond(200, "application/json", data)
        elif self.path in ("/", "/index.html"):
            self._respond(200, "text/html; charset=utf-8", _HTML.encode())
        else:
            self._respond(404, "text/plain", b"not found")

    def _respond(self, code: int, ct: str, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: Any) -> None:
        pass  # suppress access log


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    quiet = "--quiet" in sys.argv
    port  = 8080
    for i, arg in enumerate(sys.argv):
        if arg == "--port" and i + 1 < len(sys.argv):
            port = int(sys.argv[i + 1])

    kernel = Kernel()
    kernel.boot_silent()
    if not quiet:
        _register_demo_jobs(kernel)

    _Handler.kernel = kernel

    server = HTTPServer(("0.0.0.0", port), _Handler)

    def _shutdown(sig=None, frame=None):
        print(f"\n[web-dashboard] shutting down…")
        threading.Thread(target=server.shutdown, daemon=True).start()
        kernel.shutdown_silent()
        sys.exit(0)

    signal.signal(signal.SIGINT,  _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    print(f"[web-dashboard] serving on http://0.0.0.0:{port}  (Ctrl+C to stop)")
    server.serve_forever()


if __name__ == "__main__":
    main()
