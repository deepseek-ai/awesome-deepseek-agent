# ClaudeOS

A minimal, AI-native operating system implemented in pure Python.  
ClaudeOS provides a Unix-inspired shell on top of a tiny kernel that manages memory, processes, a virtual filesystem, and a cooperative task scheduler — all designed to run an AI agent as its primary user.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        Shell (REPL)                     │
│   mem  ls  cat  write  ps  spawn  kill  sched  stats    │
└───────────────────────┬─────────────────────────────────┘
                        │ syscalls
┌───────────────────────▼─────────────────────────────────┐
│                        Kernel                           │
│  ┌──────────┐  ┌──────────┐  ┌──────┐  ┌───────────┐  │
│  │ MemoryBus│  │ProcessTbl│  │  VFS │  │ Scheduler │  │
│  │short-term│  │ READY    │  │/tmp  │  │FIFO queue │  │
│  │long-term │  │ RUNNING  │  │/home │  │daemon thrd│  │
│  │ (JSON)   │  │ DONE     │  │/etc  │  │           │  │
│  └──────────┘  └──────────┘  └──────┘  └───────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Components

| Component | File | Purpose |
|-----------|------|---------|
| Kernel | `kernel.py` | Syscall table, subsystem wiring, boot/shutdown |
| MemoryBus | `memory.py` | Two-tier key-value store (volatile + persisted JSON) |
| VirtualFS | `fs.py` | In-memory POSIX-style filesystem |
| ProcessTable | `process.py` | Lightweight cooperative process model |
| Scheduler | `scheduler.py` | FIFO queue with background daemon thread |
| Shell | `shell.py` | Interactive REPL with Unix-style commands |

## Installation

No dependencies — requires Python 3.9+.

```bash
git clone https://github.com/horstducker/awesome-deepseek-agent.git
cd awesome-deepseek-agent
python run_os.py
```

## Quick Start

```
   ___  _                 _        ___  ____
  / __\| |  __ _  _   _ | |  ___ / _ \/ ___|
 / /   | | / _` || | | || | / _ \ | | \___ \
/ /___ | || (_| || |_| || ||  __/ |_| |___) |
\____/ |_| \__,_| \__,_||_| \___|\___/|____/

  AI-Native Operating System  •  kernel v0.1.0
  Type 'help' for available commands.

claude@os:~$ remember name "Claude" --persist
  stored 'name' in long-term memory

claude@os:~$ recall name
  name = 'Claude'

claude@os:~$ write /home/notes.txt "First entry in the AI OS"
  written 24B to /home/notes.txt

claude@os:~$ ls /home
  notes.txt  24B

claude@os:~$ spawn worker "background task done"
  spawned pid=1 name='worker'

claude@os:~$ ps
    PID  NAME                      STATUS      CREATED
      1  worker                    done        14:22:01

claude@os:~$ stats
  version        : 0.1.0
  uptime_seconds : 12.3
  syscall_count  : 9
  memory_keys    : 2
  processes      : 1
  fs_entries     : 5
```

## Shell Commands

### Memory
| Command | Description |
|---------|-------------|
| `mem` | List all keys currently in memory |
| `remember <key> <value> [--persist]` | Store a value; `--persist` survives restarts |
| `recall <key>` | Retrieve a stored value |
| `forget <key>` | Delete a key from memory |

### Filesystem
| Command | Description |
|---------|-------------|
| `ls [path]` | List directory contents |
| `cat <path>` | Print file contents |
| `write <path> <text>` | Create or overwrite a file |
| `rm <path>` | Delete a file |
| `cd [path]` | Change working directory |
| `pwd` | Print working directory |

### Processes
| Command | Description |
|---------|-------------|
| `ps [status]` | List processes (optionally filter by status) |
| `spawn <name> [msg]` | Create and queue a background process |
| `kill <pid>` | Terminate a process |

### System
| Command | Description |
|---------|-------------|
| `sched` | Show scheduler status and recent log |
| `stats` | Kernel statistics |
| `history` | Command history |
| `exit` / `quit` | Shutdown and quit |

## Extending ClaudeOS

### Register a custom syscall

```python
from claude_os import Kernel, Shell

kernel = Kernel()
kernel.boot()

def my_syscall(message: str) -> str:
    return f"[custom] {message}"

kernel.register_syscall("my_call", my_syscall)

shell = Shell(kernel)
shell.run()
```

### Spawn a process programmatically

```python
import time

def long_task(n: int) -> int:
    time.sleep(n)
    return n * 2

pid = kernel.syscall("proc_spawn", "my-task", long_task, 2)
kernel.syscall("sched_queue", pid)
```

## Running Tests

```bash
python -m claude_os.tests
```

All 16 smoke tests cover MemoryBus, VirtualFS, ProcessTable, Scheduler, and the Kernel syscall interface.

## Design Decisions

- **Pure Python, zero deps** — runs anywhere Python 3.9+ is available.
- **Cooperative multitasking** — processes yield naturally; no preemption complexity.
- **Two-tier memory** — short-term (dict) for transient state, long-term (JSON file) for persistence across restarts.
- **Syscall table** — all shell commands go through `kernel.syscall()`, making every action auditable and extensible.
- **Daemon scheduler thread** — the background worker keeps the shell responsive while tasks run.
