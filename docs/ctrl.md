# ⏺ Ctrl

> DeepSeek-powered CLI developer assistant — an AI partner in your terminal that writes code, debugs, manages files, and remembers things.

Ctrl is a command-line AI assistant. It doesn't just chat — it **reads/writes files**, **executes commands**, **manages TODOs**, **remembers** your preferences long-term, and can even **self-evolve** by proposing new tools and rules for your approval.

---

## Features

| Capability | Description |
|---|---|
| 💬 **Chat** | Streaming conversation via DeepSeek API, with reasoning content display |
| 📁 **File Ops** | Read, create, edit, delete files — with colorized diff on edit |
| ⚡ **Commands** | Execute PowerShell / cmd commands (with safety guard) |
| ✅ **Todos** | Persistent todo list with `pending` / `in_progress` / `done` / `failed` statuses |
| 🧠 **Memory** | User preference learning + keyword memory + vector semantic search |
| 🔄 **Sessions** | Create, switch, delete sessions — isolated conversation contexts |
| 🛠 **Self-improve** | AI proposes new tools / rules — takes effect after you approve |
| 🎨 **Pretty CLI** | Brain spinner animation, colorized diff, icon-rich tool-call display |

---

## Prerequisites

- **Node.js** >= 18
- **DeepSeek API Key** ([get one here](https://platform.deepseek.com/))

---

## Install

```bash
# Clone
git clone https://github.com/Kontirol/KontirolClaw.git
cd KontirolClaw

# Install dependencies
npm install

# Configure API Key (pick one)
# Option 1: Environment variable (recommended)
set CTRL_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx      # Windows CMD
$env:CTRL_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxx"    # PowerShell

# Option 2: Config file (writes to ~/.ctrl/config.json)
node -e "import('./src/config.js').then(m=>m.saveConfig({apiKey:'sk-xxx'}))"

# Start
npm start
```

> 💡 You can also set `CTRL_BASE_URL` (custom API endpoint) and `CTRL_MODEL` (model name). Default model: `deepseek-v4-pro`.

---

## Usage

### Basic Chat

```
Ctrl > Write me an Express server
Ctrl > What's wrong with this function?
Ctrl > Remember: I prefer TypeScript
Ctrl > exit
```

### Session Commands

| Command | Action |
|---|---|
| `:new [name]` | Create a new session |
| `:switch <ID>` | Switch to a session |
| `:sessions` / `:list` | List all sessions |
| `:delete <ID>` | Delete a session |
| `:help` | Show help |
| `Esc` | Abort current request |
| `exit` | Quit |

### What the AI Can Do

Just ask naturally — Ctrl will invoke the right tool automatically.

| Ask | Tool invoked |
|---|---|
| "Read package.json" | `read_file` |
| "Create src/utils.ts" | `create_file` |
| "Change the port in app.ts to 8080" | `edit_file` |
| "Run npm run build" | `exec_command` |
| "Make a todo list" | `todo_create` |
| "Remember: my project is called CineMax" | `memory_store` |

---

## Architecture

```
Ctrl/
├── src/
│   ├── index.js           # Entry: REPL loop, streaming chat
│   ├── config.js          # Config (env vars / ~/.ctrl/config.json)
│   ├── tools/
│   │   ├── definition.js  # OpenAI tool schemas
│   │   └── executor.js    # Tool execution logic
│   ├── memory/
│   │   ├── preferences.js # User preferences + long-term memory
│   │   ├── vector.js      # Lightweight RAG vector memory
│   │   ├── sessions.js    # Multi-session management
│   │   └── self-improve.js # Custom tools + prompt proposals
│   └── ui/
│       ├── banner.js      # Startup banner, tool-call display
│       ├── spinner.js     # Brain spinner animation (stderr)
│       └── diff.js        # Colorized file diff
├── package.json
└── README.md
```

### Memory System (4 layers)

| Layer | Trigger | Storage |
|---|---|---|
| **Preferences** | AI auto-learns | `~/.ctrl/preferences.json` |
| **Long-term Memory** | User says "Remember..." | `~/.ctrl/memory.json` |
| **Vector Memory** | AI auto-summarizes | `~/.ctrl/vectors.json` (with similarity scoring) |
| **Self-improvement** | AI proposes when needed | `~/.ctrl/custom_tools.json` / `custom_prompt.txt` |

---

## Safety

- Commands are filtered through a **blocklist** (prevents `rm -rf /`, `format`, etc.)
- File operations are **scoped to the current working directory**
- Self-improvement proposals require **your explicit approval** before taking effect

---

## License

ISC © [nijat (Ctrl)](https://github.com/Kontirol)
