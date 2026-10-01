[English](./whale.md) | [简体中文](./whale.zh-CN.md) · [← Back](../README.md)

# Integrate with Whale

Whale is a DeepSeek-native AI coding agent that runs in the terminal. It is designed around DeepSeek's API directly — prefix-cache-friendly sessions, thinking controls, tool-call repair, MCP, Agent Skills, and dynamic workflows.

- **GitHub:** <https://github.com/usewhale/DeepSeek-Code-Whale>
- **Platform support:** Whale currently supports macOS, Linux, and Windows.

#### 1. Install Whale

Install on macOS or Linux with the script:

```sh
curl -fsSL https://raw.githubusercontent.com/usewhale/DeepSeek-Code-Whale/main/scripts/install.sh | sh
```

Install on Windows with PowerShell:

```powershell
irm https://raw.githubusercontent.com/usewhale/DeepSeek-Code-Whale/main/scripts/install.ps1 | iex
```

Or install with Homebrew:

```sh
brew install usewhale/tap/whale
```

Verify:

```sh
whale --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Run the setup wizard:

```sh
whale setup
```

You can also set `DEEPSEEK_API_KEY` in your environment. The environment variable takes precedence over the key saved by `whale setup`.

#### 3. Configure DeepSeek V4

Whale uses **DeepSeek-V4-Flash** by default with reasoning effort `high` and thinking enabled. DeepSeek V4 Pro and Flash support up to a 1M-token context window, and Whale uses the current DeepSeek V4 model names directly.

For maximum reasoning on larger coding tasks, create or edit `~/.whale/config.toml`:

```toml
model = "deepseek-v4-pro"
reasoning_effort = "max"
thinking_enabled = true
```

Use `deepseek-v4-flash` instead when you want faster and cheaper iteration:

```toml
model = "deepseek-v4-flash"
reasoning_effort = "high"
thinking_enabled = true
```

Whale sends DeepSeek's `thinking` and `reasoning_effort` fields to the API. No legacy V3 model names are needed.

#### 4. Enter a project directory and launch

```sh
cd /path/to/my-project
whale doctor
whale
```

Inside the TUI:

| Command | What it does |
|---|---|
| `/model` | Change model, reasoning effort, and thinking |
| `/ask [prompt]` | Read-only question mode |
| `/plan [prompt]` | Plan first, then decide whether to execute |
| `/permissions` | Adjust tool approval mode |
| `/skills` | List, insert, enable, or disable local skills |
| `/mcp` | Show MCP server status |
| `/status` | Show session, mode, model, and config status |

You can also run a one-shot prompt:

```sh
whale exec "Explain what this repository does"
printf 'Summarize the current directory\n' | whale exec
```

#### MCP and Skills

Whale reads MCP server configuration from `~/.whale/mcp.json` by default. It supports stdio MCP servers and Streamable HTTP MCP servers, and registers MCP tools with the same approval flow as built-in tools.

Whale discovers Agent Skills from `.whale/skills`, `.agents/skills`, `~/.whale/skills`, and `~/.agents/skills`. Type `$` in the TUI to search and insert a skill, or run `/skills` to manage them.

#### Dynamic Workflows

Whale supports **dynamic workflows**: JavaScript scripts that orchestrate multiple sub-agents deterministically — fan-out research, multi-perspective review, pipeline processing, and more. Workflow scripts are [Claude Code compatible](https://docs.whale-ai.com/workflows) and can be copied between the two tools as-is.

To enable workflows, run `/config` in the TUI and toggle `Dynamic workflows` on, or add to `~/.whale/config.toml`:

```toml
[workflows]
enabled = true
```

Workflow scripts live in `.whale/workflows/<name>.js` (project-level) or `~/.whale/workflows/<name>.js` (user-global). Use `/workflows` to open the workflow panel for managing runs.

Learn more: [Workflow Guide](https://docs.whale-ai.com/workflows)
