[English](./dscode.md) | [简体中文](./dscode.zh-CN.md) · [← Back](../README.md)

# Integrate with DSCode

DSCode is an open-source terminal AI coding agent built specifically as a DeepSeek harness — analogous to how Claude Code is the harness for Claude models. It provides file operations, shell execution, code search, permission control, session persistence, context management, memory system, Skills system, and MCP protocol support.

- **GitHub:** <https://github.com/wangcan26/dscode>

#### 1. Install DSCode

- Install [Node.js](https://nodejs.org/en/download/) 20.6+.
- Clone the repository and install dependencies:

```bash
git clone https://github.com/wangcan26/dscode.git
cd dscode
npm install
cp .env.example .env
```

#### 2. Configure DeepSeek API Key

Edit the `.env` file and add your DeepSeek API key:

```bash
DEEPSEEK_API_KEY=sk-...
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure Model and Thinking Mode

DSCode supports two-level configuration (user-level and project-level):

- **User-level:** `~/.dscode/config.json`
- **Project-level:** `<project>/.dscode/config.json`

Priority: **environment variables > project-level config > user-level config > defaults**

```jsonc
{
  "modelId": "deepseek-v4-pro",
  "thinkingLevel": "xhigh",
  "maxTokens": 16384
}
```

**Key configuration options:**

| Option | Env Variable | Default | Description |
|--------|-------------|---------|-------------|
| `modelId` | `AGENT_MODEL` / `DEEPSEEK_MODEL` | `deepseek-v4-flash` | Model ID — `deepseek-v4-pro` or `deepseek-v4-flash` |
| `thinkingLevel` | `AGENT_THINKING_LEVEL` | Pro: `medium`, Flash: `off` | Thinking level — `off`, `medium`, `high`, or `xhigh` (max effort) |
| `maxTokens` | `DSCODE_MAX_TOKENS` | `16384` | Max output tokens per turn |

> **Thinking mode:** Set `thinkingLevel` to `xhigh` or `AGENT_THINKING_LEVEL=xhigh` to enable max reasoning effort (`reasoning_effort: "max"`). The underlying pi-ai framework automatically configures 1M context window (`contextWindow: 1000000`) and DeepSeek-specific thinking format.

#### 4. Run DSCode

```bash
npm start
```

Or specify the project path:

```bash
DSCODE_PROJECT_PATH=/path/to/my-project npm start
```

Once started, you will see the `you ›` prompt:

```
DSCode  (deepseek-v4-pro)
Type a message. /help for commands. exit to quit.

you ›
```

#### Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all commands |
| `/reset` | Clear conversation history |
| `/session list` | List saved sessions |
| `/session save` | Save current session |
| `/session load <id>` | Restore a saved session |
| `/memory list` | View memories |
| `/memory add <text>` | Add a memory entry |
| `/skills` | List Skills and their status |
| `/skills activate <name>` | Activate a Skill |
| `/drivers` | List loaded drivers |
| `/permissions` | View permission grants |
| `/cost` | Show token usage |
| `/compact` | Manually compact context |

Type `exit` or press `Ctrl+C` twice to quit. Press `Ctrl+C` once to interrupt generation.
