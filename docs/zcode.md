[English](./zcode.md) | [简体中文](./zcode.zh-CN.md) · [← Back](../README.md)

# Integrate with Z Code

Z Code is an open-source AI coding agent built in Zig — a **1.7 MB native binary** with zero dependencies. It provides an interactive REPL with 7 built-in tools, streaming output, session persistence, and multi-provider support (DeepSeek, Moonshot, Ollama). No runtime, no npm install — just a single static executable.

- **GitHub:** <https://github.com/RenovZ/zcode>

#### 1. Install Z Code

**Requirements:** Zig ≥ 0.16.0

```sh
# Clone and build
git clone https://github.com/RenovZ/zcode.git
cd zcode
zig build
```

The compiled binary is a single static executable at `./zig-out/bin/zcode`. Copy it anywhere on your `PATH`:

```sh
cp ./zig-out/bin/zcode /usr/local/bin/
```

Verify:

```sh
zcode --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Set it as an environment variable:

```sh
export DEEPSEEK_API_KEY="sk-..."
```

Optionally, configure the China endpoint:

```sh
export DEEPSEEK_BASE_URL="https://api.deepseeki.com"
```

Z Code detects `DEEPSEEK_API_KEY` at startup and enables the DeepSeek provider automatically. You can also store credentials in `~/.zig-code/agent/auth.json`.

#### 3. Enter a project directory and launch

```sh
cd /path/to/my-project
zcode
```

Z Code launches into an interactive REPL. By default it uses the first available DeepSeek model (typically **deepseek-v4-pro**). Type your prompt and press `Enter` — responses stream in real time.

**Non-interactive mode** (single-shot prompt):

```sh
zcode "explain src/main.zig"
```

**Continue last session:**

```sh
zcode -c
```

#### Interactive Commands (REPL)

| Command | Description |
|---|---|
| `/help` | Show available commands |
| `/quit`, `/exit` | Exit the program |
| `/session` | Show current session info (ID, model, thinking level) |
| `/stats` | Show token usage, cost estimate, and memory |
| `/new` | Start a fresh session |
| `/model <id>` | Switch to a different model (e.g. `deepseek-v4-flash`) |
| `/thinking <level>` | Set thinking level: `off`, `low`, `medium`, `high`, `xhigh` |
| `/name <name>` | Name the current session |
| `/clear` | Clear the screen |

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline (multi-line input) |
| `Ctrl+C` | Interrupt the current model turn |
| `Ctrl+D` | Exit the program |

#### CLI Options

| Flag | Description |
|---|---|
| `--provider <name>` | Provider to use: `deepseek`, `moonshot`, or `ollama` |
| `--model <id>` | Model ID (e.g. `deepseek-v4-pro`, `deepseek-v4-flash`) |
| `--thinking <level>` | Thinking level: `off`, `low`, `medium`, `high`, `xhigh` |
| `-c`, `--continue` | Continue the most recent session |
| `-r`, `--resume <id>` | Resume a specific session by ID |
| `--tools <list>` | Comma-separated list of tools to enable |
| `--debug` | Show debug output |
| `--help` | Show usage |

#### Configuration

Settings are read from `~/.zig-code/agent/settings.json`:

```json
{
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "xhigh",
  "hideThinkingBlock": false
}
```

| Key | Type | Description |
|---|---|---|
| `defaultProvider` | string | Default provider (`deepseek`, `moonshot`, `ollama`) |
| `defaultModel` | string | Default model ID |
| `defaultThinkingLevel` | string | Default thinking level (`off`, `low`, `medium`, `high`, `xhigh`) |
| `hideThinkingBlock` | bool | Hide thinking output during streaming |

> **1M Context Window:** Z Code recognizes DeepSeek-V4's 1,000,000-token context window and 384,000-token max output. Use `/stats` in the REPL to monitor your context usage.

> **Thinking Levels:** DeepSeek-V4-Pro supports multiple reasoning effort levels. Set `--thinking xhigh` (or use `/thinking xhigh` in the REPL) for the best coding experience. See [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode) for details.

#### Built-in Tools

All 7 tools are enabled by default in interactive mode:

| Tool | Description |
|---|---|
| `bash` | Execute shell commands |
| `edit` | Edit files with targeted find-and-replace |
| `read` | Read file contents |
| `write` | Create or overwrite files |
| `ls` | List directory contents |
| `find` | Find files by glob pattern |
| `grep` | Search file contents |

#### Session Persistence

Sessions are stored in `~/.zig-code/agent/sessions/` as SQLite databases. Use `-c` to continue your last session or `-r <id>` to resume a specific one. Token stats and cost estimates are tracked per session.
