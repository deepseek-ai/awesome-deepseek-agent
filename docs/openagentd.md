[English](./openagentd.md) | [简体中文](./openagentd.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenAgentd

OpenAgentd is an open-source, mobile-first cockpit for local AI agents. It features a cross-platform desktop app (macOS, Windows, Linux), mobile shell, FastAPI backend, React Web UI, multi-agent orchestration, CLI, and native MCP support.

#### 1. Install OpenAgentd

You can install OpenAgentd either as a standalone **Desktop App** or as a **CLI / Backend Service**.

##### Option A: Desktop App (Command Line Installer)

Run the one-command installer in your terminal:

**macOS / Linux**:
```bash
curl -fsSL https://raw.githubusercontent.com/lthoangg/openagentd/main/install.sh | sh
```

**Windows (PowerShell)**:
```powershell
irm https://raw.githubusercontent.com/lthoangg/openagentd/main/install.ps1 | iex
```

**Windows (Command Prompt / CMD)**:
```cmd
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/lthoangg/openagentd/main/install.ps1 | iex"
```

> **Note:** Standalone installers (DMG, MSI, AppImage, Deb) are also available on the [OpenAgentd Releases](https://github.com/lthoangg/openagentd/releases/latest) page. Launch **OpenAgentd** from your Applications folder or Start menu.

##### Option B: CLI / Backend Service

Install via `uv` or `pip`:

```bash
uv tool install openagentd
```

Or using `pip`:

```bash
pip install openagentd
```

Verify the installation:

```bash
openagentd --version
```

#### 2. Configure DeepSeek Provider

OpenAgentd supports DeepSeek out of the box using direct API keys or keyless free models via OpenCode Zen (`opencode:deepseek-v4-flash-free`).

To configure direct DeepSeek API access:

1. Obtain an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. Set the `DEEPSEEK_API_KEY` environment variable:

**macOS / Linux**:
```bash
export DEEPSEEK_API_KEY="sk-..."
```

**Windows (PowerShell)**:
```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

**Windows (CMD)**:
```cmd
set DEEPSEEK_API_KEY=sk-...
```

Alternatively, configure the API key:
- In the Web / Desktop UI: **Settings → Providers → DeepSeek**
- Or in `~/.config/openagentd/.env`:
  ```env
  DEEPSEEK_API_KEY=sk-...
  ```

#### 3. Select Model and Configure Agent

Agent configurations live in `~/.config/openagentd/agents/` as Markdown files with YAML frontmatter.

To set your lead agent model to DeepSeek V4:

Edit `~/.config/openagentd/agents/lead.md`:

```yaml
---
name: lead
description: Lead orchestrator agent
model: deepseek:deepseek-v4-flash
---
```

For complex reasoning tasks, use `deepseek-v4-pro`:

```yaml
---
name: lead
description: Lead orchestrator agent
model: deepseek:deepseek-v4-pro
---
```

OpenAgentd natively handles DeepSeek V4 capabilities:
- **1M Context Window**: Full 1,048,576 token context window support.
- **Thinking / Reasoning Mode**: Native payload configuration (`thinking: {type: "enabled"}`) and proper handling of `reasoning_content` in assistant messages during agent tool turns.

#### 4. Run OpenAgentd

Launch the OpenAgentd desktop app from your system menu, or run the server from your terminal:

```bash
openagentd
```

For network / LAN access:

```bash
openagentd start --lan --key
```

Or launch an interactive CLI chat session:

```bash
openagentd chat
```

You can also dynamically switch models at any time from the in-app model selector or agent settings panel.
