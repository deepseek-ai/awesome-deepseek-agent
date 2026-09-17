[English](./martty.md) | [简体中文](./martty.zh-CN.md) · [← Back](../README.md)

# Integrate with Martty

Martty is an open-source, terminal-native ACP client built with Rust and ratatui. It starts DeepSeek Harness by default and presents streamed reasoning, tool calls, subagents, plans, images, and durable sessions in an extensible TUI.

- **GitHub:** <https://github.com/openma-ai/Martty>
- **Website:** <https://martty.sh>

#### 1. Install Martty

Martty requires Node.js 18 or later. Install the published npm package:

```sh
npm install --global martty
martty --version
```

To preview the interface without an API key or agent runtime:

```sh
martty --demo
```

#### 2. Get a DeepSeek API Key

Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then expose it to the process that launches Martty:

```sh
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Martty also supports ACP authentication from the running interface with `/auth`. Credentials belong to the agent runtime and are not added to the conversation.

#### 3. Enter a project and launch Martty

```sh
cd /path/to/my-project
martty --model deepseek-v4-pro
```

Without `--model`, the default DeepSeek Harness integration starts with `deepseek-v4-flash`. Inside Martty:

1. Type `/model` to switch between `deepseek-v4-pro` and `deepseek-v4-flash`.
2. Type `/effort max` to use the maximum reasoning effort with DeepSeek-V4-Pro.
3. Send a coding request, for example: `Inspect this repository and propose the smallest safe fix for the failing tests.`

DeepSeek-V4-Pro and DeepSeek-V4-Flash support a **1 million token context window** and up to **384K output tokens**. Martty reads the live model and session capabilities advertised by DeepSeek Harness, so no separate context-window setting is required in the client. See the [current model details](https://api-docs.deepseek.com/quick_start/pricing) and [thinking-mode documentation](https://api-docs.deepseek.com/guides/thinking_mode).

#### Useful commands

| Command | Action |
|---|---|
| `/model` | Select a model advertised by the running agent |
| `/effort` | Select reasoning effort (`off`, `high`, or `max`) |
| `/permission` | Select the session permission mode |
| `/new` | Start a new durable session |
| `/resume` | Resume a previous session |
| `/image <path>` | Add a local image to the next prompt |
| `/ui deepseek` | Switch to the built-in DeepSeek UI preset |
| `/auth` | Authenticate through ACP |

During a model turn, `Enter` queues a follow-up, `Ctrl+X` steers the active turn immediately, and `Esc` interrupts it while preserving the draft.

#### Optional: manage Martty as a DeepSeek Harness profile

If DeepSeek Harness is already installed, Martty can be managed as a profile plugin:

```sh
npm install --global @deepseek-ai/dsh
dsh plugin --profile martty add martty@latest
dsh --profile martty
```

This path lets DeepSeek Harness manage the profile, plugins, and upgrades while Martty remains the terminal client.
