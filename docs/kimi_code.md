[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Kimi Code CLI

Kimi Code CLI is an AI coding agent that runs in your terminal — it can read and edit code, run shell commands, search files, fetch web pages, and choose the next step based on the feedback it receives.

### Installing Kimi Code CLI

#### Option 1: Install with Script (Recommended)

The fastest way to install. No Node.js required.

**macOS / Linux:**

```bash
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

#### Option 2: Install with npm

Requires Node.js 24.15.0 or higher.

```bash
npm install -g @moonshot-ai/kimi-code
```

Or with pnpm:

```bash
pnpm add -g @moonshot-ai/kimi-code
```

#### Verify Installation

After installation, verify the CLI is ready:

```bash
kimi --version
```

#### Upgrade & Uninstall

**Upgrade:**
- Script users: re-run the install script
- npm users: `npm install -g @moonshot-ai/kimi-code@latest`

**Uninstall:**
- Script users: delete the `kimi` executable
- npm users: `npm uninstall -g @moonshot-ai/kimi-code`

### Configuring Kimi Code CLI

Kimi Code CLI works out of the box with Moonshot AI's Kimi models and can also be configured to use other compatible providers like DeepSeek.

Run `/connect` in the interactive UI, then:

1. Search and select **DeepSeek**
2. Choose the model you want to use (e.g., `deepseek-v4-pro` or `deepseek-v4-flash`)
3. Press Enter and fill in your DeepSeek API Key

You can get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

### Using Kimi Code CLI

Open a project directory and start the interactive UI:

```bash
cd /path/to/your-project
kimi
```

On first launch with DeepSeek, try your first task:

```
Take a look at this project and explain its main directories.
```

### Key Features

- **Single-binary distribution**: Install with one command — no Node.js setup, PATH gymnastics, or global module conflicts.
- **Blazing-fast startup**: The TUI is ready in milliseconds, so starting a session never feels heavy.
- **Purpose-built TUI**: A carefully tuned interface for long, focused agent sessions.
- **Video input**: Drop a screen recording or demo clip into the chat, and let the agent watch what is hard to describe in words.
- **AI-native MCP configuration**: Add, edit, and authenticate Model Context Protocol servers conversationally with `/mcp-config`, without hand-editing JSON.
- **Subagents for focused, parallel work**: Dispatch built-in coder, explore, and plan subagents in isolated contexts while keeping the main conversation clean.
- **Lifecycle hooks**: Run local commands at key points to gate risky tool calls, audit decisions, trigger desktop notifications, or connect to your own automation.

### Resources

- [Kimi Code GitHub Repository](https://github.com/MoonshotAI/kimi-code)
- [Kimi Code Documentation](https://moonshotai.github.io/kimi-code/)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
- [DeepSeek Platform](https://platform.deepseek.com/)
