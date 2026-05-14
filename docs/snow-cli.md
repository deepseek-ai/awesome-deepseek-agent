[English](./snow-cli.md) | [简体中文](./snow-cli.zh-CN.md) · [← Back](../README.md)

# Integrate with Snow CLI

[Snow CLI](https://github.com/MayDay-wpf/snow-cli) (npm package: `snow-ai`) is an open-source agentic AI coding assistant that runs directly in your terminal. It pairs an Ink/React TUI with rich LLM adapters, MCP-style tools, a local offline codebase, and first-class IDE integrations.

- **GitHub:** <https://github.com/MayDay-wpf/snow-cli>
- **npm:** <https://www.npmjs.com/package/snow-ai>
- **VSCode Extension:** [mufasa.snow-cli](https://marketplace.visualstudio.com/items?itemName=mufasa.snow-cli)
- **JetBrains Plugin:** [Snow CLI plugin](https://plugins.jetbrains.com/plugin/28715-snow-cli)

## Highlights

- **All DeepSeek API request modes supported** — OpenAI Chat Completion, OpenAI Responses, Anthropic, and Gemini adapters are all built in, so you can use any DeepSeek-compatible endpoint (including the native `https://api.deepseek.com` and the `https://api.deepseek.com/anthropic` Anthropic-compatible endpoint).
- **Complete VSCode & JetBrains plugins** — synchronize editor context, diagnostics, code navigation, terminal panel, Git blame, and commit message generation between the IDE and the CLI over WebSocket.
- **Local offline codebase** — a vector-search SQLite database that indexes your code + comments, with optional Agent Review or Rerank model to refine search results. Run fully offline once configured.
- **Agentic toolset** — built-in MCP-style tools for filesystem, terminal, web search, TODOs, notebooks, scheduling, IDE diagnostics, sub-agents, skills, and ACE Code Search / LSP intelligence.
- **Multiple run modes** — interactive TUI, headless `--ask` mode, background `--task` queue, SSE server, ACP server, YOLO and Plan modes.

#### 1. Install Snow CLI

Requires Node.js 18+ (Node 22 recommended).

```sh
npm install -g snow-ai
```

Verify the installation:

```sh
snow --version
```

> Tip: Windows users are recommended to use PowerShell 7+ together with Windows Terminal for the best rendering.

#### 2. Configure DeepSeek

Run `snow` to launch the TUI, then open **API and Model Settings** (`/home` → API and Model Settings) and fill in the following fields. Snow CLI supports four request methods — pick the one that matches the DeepSeek endpoint you want to use.

##### Option A — DeepSeek native (OpenAI Chat Completion)

| Field              | Value                      |
| ------------------ | -------------------------- |
| **Request Method** | `OpenAI Chat Completion`   |
| **Base URL**       | `https://api.deepseek.com` |
| **API Key**        | `<your DeepSeek API Key>`  |
| **Advanced Model** | `deepseek-v4-pro`          |
| **Basic Model**    | `deepseek-v4-flash`        |

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

##### Option B — DeepSeek via Anthropic-compatible endpoint

| Field                      | Value                                  |
| -------------------------- | -------------------------------------- |
| **Request Method**         | `Anthropic`                            |
| **Base URL**               | `https://api.deepseek.com/anthropic`   |
| **API Key**                | `<your DeepSeek API Key>`              |
| **Advanced Model**         | `deepseek-v4-pro[1m]`                  |
| **Basic Model**            | `deepseek-v4-flash[1m]`                |
| **Thinking Enabled**       | `true` (recommended for v4-pro)        |
| **Thinking Budget Tokens** | `10000` or higher for deeper reasoning |


##### Option C — DeepSeek via OpenAI Responses

| Field                           | Value                                            |
| ------------------------------- | ------------------------------------------------ |
| **Request Method**              | `OpenAI Responses`                               |
| **Base URL**                    | `https://api.deepseek.com`                       |
| **API Key**                     | `<your DeepSeek API Key>`                        |
| **Responses Reasoning Enabled** | `true`                                           |
| **Responses Reasoning Effort**  | `HIGH` or `XHIGH` for the best coding experience |

> Recommendation: set reasoning effort to `HIGH` / `XHIGH` so the model uses **max thinking** on long coding tasks.

#### 3. Enable the Local Offline Codebase (Optional)

Snow CLI ships with a vector-search codebase backed by SQLite. Configure it once in `/home` → **Codebase Config** with any DeepSeek-compatible embedding endpoint, then enable it per project:

```text
/codebase on        # enable for the current project
/codebase status    # show current state
/codebase off       # disable
```

- Project-level config lives in `.snow/codebase.json` (indexing parameters, agent review, rerank).
- Global config lives in `~/.snow/codebase.json` (embedding service, shared across projects).
- Once indexed, semantic search runs **fully offline** against the local SQLite store.

#### 4. Launch Snow CLI

```sh
cd /path/to/my-project
snow
```

Other useful entry points:

```sh
# One-shot headless prompt
snow --ask "explain this project"

# Continue your last session
snow -c

# Background async task
snow --task "review the authentication module"
snow --task-list

# SSE / ACP server modes (for IDE & external integrations)
snow --sse --sse-port 3000
snow --acp
```

#### 5. Install the IDE Plugins (Optional)

- **VSCode:** search "Snow CLI" in the Marketplace or install [`mufasa.snow-cli`](https://marketplace.visualstudio.com/items?itemName=mufasa.snow-cli). The extension embeds a Snow terminal in the sidebar / split panel and streams editor context, diagnostics, and selections to the agent.
- **JetBrains:** install [Snow CLI](https://plugins.jetbrains.com/plugin/28715-snow-cli) from the JetBrains Marketplace for the same context bridge inside IntelliJ IDEA, PyCharm, GoLand, WebStorm, and others.

#### Key Shortcuts (Part)

| Key           | Action                           |
| ------------- | -------------------------------- |
| `Enter`       | Send the prompt                  |
| `Shift+Enter` | Insert a newline                 |
| `Esc`         | Interrupt the current model turn |
| `/`           | Open the command / skills menu   |
| `/clear`        | Start a fresh conversation       |
| `/resume`     | Resume a previous session        |
| `/codebase`   | Toggle the local codebase index  |
| `/quit`       | Quit Snow CLI                    |

#### User Configuration Directory

After the first run, Snow CLI creates `~/.snow/` containing `config.json`, `mcp-config.json`, profiles, sessions, async tasks, hooks, and runtime logs. You can manage multiple **profiles** to switch between different DeepSeek endpoints or models in one keystroke.

## Full Documentation

Snow CLI ships with an extensive, fully bilingual user manual. All of the following guides live in the [official repository](https://github.com/MayDay-wpf/snow-cli/tree/main/docs/usage/en).

### Getting Started

- [01. Installation Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/01.Installation%20Guide.md) — system requirements, install / update / uninstall, IDE extension installation
- [02. First Time Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/02.First%20Time%20Configuration.md) — API configuration, model selection, basic settings
- [19. Startup Parameters Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/19.Startup%20Parameters%20Guide.md) — CLI flags, quick-start modes, headless mode, async tasks, developer mode

### Advanced Configuration

- [03. Proxy and Browser Settings](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/03.Proxy%20and%20Browser%20Settings.md) — network proxy and browser configuration
- [04. Codebase Setup](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/04.Codebase%20Setup.md) — local offline codebase, vector search, agent review, rerank
- [05. Sub-Agent Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/05.Sub-Agent%20Configuration.md) — sub-agent management, custom sub-agents
- [06. Sensitive Commands Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/06.Sensitive%20Commands%20Configuration.md) — sensitive command protection, custom rules
- [07. Hooks Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/07.Hooks%20Configuration.md) — workflow automation, hook types, examples
- [08. Theme Settings](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/08.Theme%20Settings.md) — UI theme configuration, custom color schemes, simplified mode
- [16. Third-Party Relay Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/16.Third-Party%20Relay%20Configuration.md) — Claude Code relay, Codex relay, custom headers

### Feature Guide

- [09.0 Command Panel Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.0.Command%20Panel%20Guide.md) — full command reference and tips, split by category into 09.1–09.7:
  - [09.1 Session Management Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.1.Session%20Management%20Commands.md)
  - [09.2 Mode Switching Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.2.Mode%20Switching%20Commands.md)
  - [09.3 Code Review and Analysis Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.3.Code%20Review%20and%20Analysis%20Commands.md)
  - [09.4 Configuration and Management Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.4.Configuration%20and%20Management%20Commands.md)
  - [09.5 Custom Extension Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.5.Custom%20Extension%20Commands.md)
  - [09.6 Special Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.6.Special%20Commands.md)
  - [09.7 Goal Management Commands](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/09.7.Goal%20Management%20Commands.md)
- [10. Command Injection Mode](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/10.Command%20Injection%20Mode.md) — execute commands directly inside prompts, syntax & security
- [11. Vulnerability Hunting Mode](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/11.Vulnerability%20Hunting%20Mode.md) — professional security analysis with verification scripts
- [12. Headless Mode](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/12.Headless%20Mode.md) — one-shot conversations, session management, script integration
- [13. Keyboard Shortcuts Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/13.Keyboard%20Shortcuts%20Guide.md) — editing, navigation, rollback shortcuts
- [14. MCP Configuration](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/14.MCP%20Configuration.md) — MCP service management, enable / disable, troubleshooting
- [15. Async Task Management](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/15.Async%20Task%20Management.md) — background tasks, task UI, sensitive-command approval, task-to-session conversion
- [17. LSP Configuration and Usage](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/17.LSP%20Configuration.md) — LSP config, language servers, ACE tools (definition / outline)
- [18. Skills Command Detailed Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/18.Skills%20Command%20Detailed%20Guide.md) — skill creation, Claude Code Skills compatibility, tool restrictions
- [20. SSE Service Mode](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/20.SSE%20Service%20Mode.md) — SSE server, API endpoints, permission flow, YOLO mode, client integration
- [21. Custom StatusLine Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/21.Custom%20StatusLine%20Guide.md) — user-level StatusLine plugins, hook structure, bilingual examples
- [22. Team Mode Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/22.Team%20Mode%20Guide.md) — multi-agent collaboration, parallel task execution
- [23. Custom Search Engine Guide](https://github.com/MayDay-wpf/snow-cli/blob/main/docs/usage/en/23.Custom%20Search%20Engine%20Guide.md) — user-level search engine plugins, engine contract, minimal template
