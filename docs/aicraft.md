[English](./aicraft.md) | [简体中文](./aicraft.zh-CN.md) · [← Back](../README.md)

# Integrate with AICraft

AICraft is a desktop AI capability launcher — manage your LLM's Skills, MCP tools, RAG, and memory modules through a visual interface, just like loading Minecraft mods.

**Key Highlights:**
- 🚀 One-click DeepSeek setup — paste your API Key and you're ready
- 🧩 Modular architecture — Skills (prompts) + MCP (tools) + RAG (knowledge) + Memory
- 💰 Real-time token billing panel with cache hit tracking
- 🤖 Context budget management — 6-level priority trimming for 1M context

### Installation

#### Option 1: Download Release (Recommended)

1. Go to [AICraft Releases](https://github.com/Easlie114514/AICraft/releases)
2. Download the latest `AICraft-x.x.x.zip`
3. Extract and run `AICraft.exe`

No Python, Node.js, or any other runtime required.

#### Option 2: Run from Source

Prerequisites: Python 3.7+, Node.js 18+

```bash
git clone https://github.com/Easlie114514/AICraft.git
cd AICraft
pip install -r requirements.txt
cd frontend && npm install && npm run build && cd ..
python run.py
```

### Configuring DeepSeek

AICraft provides a one-click DeepSeek integration — no manual config file editing needed.

1. Launch AICraft
2. Click the **「模型」** tab in the top navigation
3. Click **「DeepSeek 一键接入」**
4. Paste your DeepSeek API Key (get one from [DeepSeek Platform](https://platform.deepseek.com/api_keys))
5. Click **「保存」**

<div align="center">
<img src="./assets/aicraft_deepseek.png" width="600" />
</div>

This automatically creates two model configurations:

| Model | Use Case | Context Window |
|-------|----------|----------------|
| `deepseek-v4-pro` | Complex reasoning, coding, deep analysis | 1M tokens |
| `deepseek-v4-flash` | Fast responses, casual chat | 1M tokens |

Both models use the OpenAI-compatible endpoint at `https://api.deepseek.com/`.

### 1M Context Window

DeepSeek V4 models support up to **1 million tokens** of context. AICraft takes full advantage of this:

- **Context Budget Manager** — 6-level priority trimming ensures the most important context is preserved when approaching the limit
- **Auto Router** — Automatically switches between V4 Pro (complex tasks) and V4 Flash (simple queries) based on task complexity
- **Memory Injection** — Cross-session memory is injected into context with priority levels, preventing memory overflow

### Deep Thinking Mode

AICraft supports DeepSeek's deep thinking mode:

1. Toggle the **「深度思考」** switch at the bottom of the chat input
2. The model will perform extended reasoning before responding
3. Thinking content is displayed in a collapsible block

For the best experience, AICraft sends `reasoning_effort: max` when deep thinking is enabled, giving you the full reasoning capability of DeepSeek V4 Pro.

### Token Billing Panel

AICraft includes a real-time token billing panel that tracks:

- Input tokens (cache hit / cache miss separately)
- Output tokens
- Request count
- Estimated cost in USD

Pricing is automatically matched by model name prefix:

| Model | Input / M tokens | Cache Hit / M tokens | Output / M tokens |
|-------|-----------------|---------------------|-------------------|
| `deepseek-v4-pro` | $0.435 | $0.003625 | $0.87 |
| `deepseek-v4-flash` | $0.14 | $0.0028 | $0.28 |

*Pricing sourced from [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing). Verify for the latest rates.*

### First Run

1. Launch AICraft
2. Set up DeepSeek (see above)
3. Toggle **RAG**, **Memory**, and **Deep Thinking** as needed using the switches below the input
4. Start chatting!

<div align="center">
<img src="./assets/aicraft_chat.png" width="600" />
</div>

### Capability Modules

| Module | Description | Factory Preset |
|--------|-------------|----------------|
| **Skill** | Prompt injection for role/style | 4: General / Tech / Creative / Analysis |
| **MCP** | Executable tools (filesystem + Python) | 2: filesystem / code_executor |
| **RAG** | Local vector retrieval (ChromaDB) | 3 docs: Manual / Dev Guide / FAQ |
| **Memory** | 3-tier architecture (L0→L1→L2) | Auto-running |
| **Role** | Preset persona templates | Custom |

### Tech Stack

- **Backend**: Python · FastAPI · ChromaDB · httpx
- **Frontend**: React 19 · Vite 8 · TailwindCSS 4 · Shadcn UI
- **Package**: PyInstaller onedir · 316 MB
- **License**: Apache 2.0
