[English](./deepseek_code_agent.md) | [简体中文](./deepseek_code_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Code Agent

> 🌐 **The only Web UI + System Tray AI desktop agent** in this list — not just a terminal CLI.  
> Built for DeepSeek-V4 with 20+ tools, Knowledge Base, ACL file protection, conversation encryption, and multi-tab session management.

DeepSeek Code Agent is an open-source AI desktop assistant that runs as a **Web service + System Tray** application. It uses DeepSeek-V4 as its core model and comes with **20+ built-in tools** for file operations, code diagnostics, Git queries, regex search, web fetching, and more — all controllable through natural language conversation.

Unlike CLI-only AI coding assistants, it provides a **rich graphical interface** accessible from any browser, making DeepSeek-V4's agent capabilities available to both developers and **non-technical users alike**.

- **GitHub:** <https://github.com/Fan/DeepSeekCodeAgent>

---

### Why DeepSeek Code Agent?

| Feature | DeepSeek Code Agent | Terminal-only CLI tools |
|---------|-------------------|----------------------------------------------|
| **Interface** | 🌐 Web UI + System Tray 🖥️ | ⌨️ Terminal only |
| **Knowledge Base** | ✅ Built-in with GUI file picker | ❌ |
| **Multi-tab Sessions** | ✅ Manage multiple conversations | ❌ Single session |
| **File Browser** | ✅ GUI file picker (@引用) | ❌ Manual path typing |
| **ACL Anti-tampering** | ✅ Auto-locks project files | ❌ |
| **Conversation Encryption** | ✅ Windows DPAPI encrypted | ❌ |
| **Target Users** | 👥 Developers + non-technical | 👨‍💻 Developers only |

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
git clone https://github.com/Fan/DeepSeekCodeAgent.git
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
| `AGENT_SERVER_PORT` | Web UI port (default: 8802) |
| `AGENT_WORKSPACE_DIR` | Default workspace directory |
| `AGENT_KNOWLEDGE_BASE_DIR` | Knowledge base directory |
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

Open your browser and visit `http://127.0.0.1:8802`.

#### 4. Start a Conversation

Type natural language commands and the agent will call tools to complete tasks:

> "Read the contents of test.txt on my desktop"
> "Check the Git log for this project"
> "What files are in the current directory?"
> "Analyze the code quality of main.py"

#### 5. Key DeepSeek Integration Features

| Feature | Description |
|---------|-------------|
| **Function Calling** | DeepSeek-V4's tool-use capabilities drive all 20+ built-in tools |
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

#### Built-in Tools (20+)

`cli_structured_edit` · `cli_python_inline` · `cli_directory_list` · `cli_web_fetch` · `cli_git_workspace` · `cli_regex_locate` · `cli_find_replace` · `cli_file_ops` · `cli_ip_geolocate` · `cli_open_meteo_weather` · `cli_unified_diagnose` · `cli_test_report` · `cli_text_diff` · `cli_patch_apply` · `cli_user_confirm` · `cli_orch_dispatch` · and more.