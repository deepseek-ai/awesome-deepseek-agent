[English](./deepseek_code_agent.md) | [简体中文](./deepseek_code_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Code Agent

> 🌐 **Open-source Web UI coding assistant** — lightweight client architecture, one-click Pro/Flash model switching, transparent task decision-making.  
> Perfect for quick start, daily development, and advancing your Agent skills.

DeepSeek Code Agent is an open-source Web UI coding assistant built for **rapid development** with DeepSeek-V4. Its lightweight client architecture runs in the browser — no heavy IDE, no terminal needed. Switch between **DeepSeek-V4-Pro** and **DeepSeek-V4-Flash** anytime during a conversation, and watch every tool-call decision unfold transparently in the side panel.

Whether you're **getting started with AI agents** or looking for a **daily coding companion**, DeepSeek Code Agent offers a clean, intuitive interface that grows with you.

- **GitHub:** <https://github.com/Fan/deepseek-code-agent>

---

### Key Features

| Feature | Description |
|---------|-------------|
| 🌐 **Web UI** | Graphical interface accessible from any browser |
| 📚 **Knowledge Base** | Built-in file picker for context injection |
| 📑 **Multi-tab Sessions** | Manage multiple conversations simultaneously |
| 📁 **File Browser** | GUI-based file picker with @-syntax for quick file referencing |
| 🔒 **ACL Anti-tampering** | Auto-locks project files for security |
| 🔐 **Conversation Encryption** | Windows DPAPI encrypted storage |

---

<div align="center">
  <img src="./assets/deepseek_code_agent_ui.png" width="800" alt="DeepSeek Code Agent Web UI" border="1" />
  <p><em>Web UI — chat interface with tool-calling, multi-tab sessions, and real-time streaming</em></p>
</div>

<br>

#### 1. Install DeepSeek Code Agent

- Install [Python](https://www.python.org/downloads/) 3.8+
- Clone the repository:

```bash
git clone https://github.com/Fan/deepseek-code-agent.git
cd deepseek-code-agent
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

#### 2. Configure DeepSeek

Edit `config.json` in the project root:

```json
{
    "AGENT_MODEL_API_BASE_URL": "https://api.deepseek.com",
    "AGENT_MODEL_API_KEY": "sk-...",
    "AGENT_SERVER_PORT": 8802
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Configuration options:**

| Option | Description |
|--------|-------------|
| `AGENT_MODEL_API_BASE_URL` | API base URL, defaults to `https://api.deepseek.com` |
| `AGENT_MODEL_API_KEY` | Your DeepSeek API key |
| `AGENT_SERVER_PORT` | Web UI port (default: 8801) |
| `AGENT_WORKSPACE_DIR` | Default workspace directory |
| `AGENT_KNOWLEDGE_BASE_DIR` | Knowledge base directory |
| `AGENT_DATA_ROOT_DIR` | Data storage root (sessions, encryption keys, usage logs) |
| `AGENT_SESSION_ENCRYPTION` | Session encryption mode (`auto`, `on`, `off`; default: `auto`) |
| `AGENT_REASONING_EFFORT` | Reasoning effort level (`max`, `high`, `medium`; default: `max`) |
| `CHAT_API_MODELS` | Allowed models, defaults to `deepseek-v4-pro,deepseek-v4-flash` |

#### 3. Launch DeepSeek Code Agent

**Windows (recommended):**

Double-click `start.bat` — it automatically requests admin privileges for ACL protection, activates the virtual environment, installs dependencies, and starts the service.

**Linux / macOS:**

```bash
chmod +x start.sh && ./start.sh
```

**Or manually:**

```bash
python main_tray.py
```

Open your browser and visit `http://127.0.0.1:8801`.

#### 4. Start a Conversation

Type natural language commands and the agent will call tools to complete tasks:

> "Read the contents of test.txt on my desktop"
> "Check the Git log for this project"
> "What files are in the current directory?"
> "Analyze the code quality of main.py"

#### 5. Key DeepSeek Integration Features

| Feature | Description |
|---------|-------------|
| **Function Calling** | DeepSeek-V4's tool-use capabilities drive all built-in tools |
| **KV Cache Optimization** | Streams `usage` info including `cache_hit_tokens`; pricing distinguishes cache hit/miss for cost savings |
| **Streaming Responses** | SSE-based streaming with reasoning content support (`reasoning_content`) |
| **Context Management** | Auto-summarizes after 800 messages to stay within context limits, preserving key information |
| **Model Selection** | Per-conversation model override via `CHAT_API_MODELS` |

#### 6. Knowledge Base

<div align="center">
  <img src="./assets/deepseek_code_agent_kb.png" width="800" alt="Knowledge Base Panel" border="1" />
  <p><em>Knowledge Base panel — select local files to inject into conversation context as context references</em></p>
</div>

Toggle the 📚 **Knowledge Base** panel on the right side of the interface, check the files you want the AI to reference, and the agent automatically injects their content into the conversation for context-aware responses.

#### Usage Tips

| Command | Action |
|---------|--------|
| `/plan` | Switch to Plan mode (output plan only, no writes) |
| `/execute` | Switch to Execute mode (strictly follow Todo-List) |
| `@/path/to/file` | Reference a local file in your message |
| 📁 button | Open the file browser to pick files |
| 📚 panel | Toggle knowledge base files as context reference |

#### Built-in Tools

`read_file` · `write_file` · `replace_in_file` · `apply_patch` · `grep_files` · `glob_files` · `file_ops` · `archive` · `data_table` · `run_command` · `python_inline` · `git_workspace` · `web_fetch` · `unified_diagnose` · `text_diff` · `env_probe` · `ip_geolocate` · `open_meteo_weather` · `image_ocr` · `user_confirm` · `todo_list` · `run_type` · and more.