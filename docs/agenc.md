[English](./agenc.md) | [简体中文](./agenc.zh-CN.md) · [← Back](../README.md)

# Integrate with AgenC Core

AgenC Core is an open-source AI coding agent for the terminal, released under the MIT license. It has a built-in `deepseek` provider that calls the DeepSeek API directly. Its catalog includes `deepseek-flash` (DeepSeek-V4.1-Flash) and `deepseek-v4-pro`, both with thinking enabled and the full 1M-token context window. You can work in its terminal UI, run it headless with `agenc -p` in scripts and CI, or start background agents.

With `deepseek-flash` at the `max` reasoning effort, in light mode (`agenc --light`, experimental), AgenC Core scored 76.2% on Terminal-Bench 2.1 (339 of 445 trials) for $34, as listed by Harbor Hub ([public run](https://hub.harborframework.com/jobs/71f39f3b-22f8-4dbe-9f25-2b039d3a4534)).

- **GitHub:** <https://github.com/tetsuo-ai/agenc-core>
- **Website:** <https://get.agenc.ag>

#### 1. Install AgenC Core

macOS / Linux:

```bash
curl -fsSL https://get.agenc.ag/install.sh | sh
```

The installer brings its own verified Node.js runtime. It installs the `agenc` command into `~/.local/bin` and starts the AgenC daemon as a user service.

Windows (PowerShell):

```powershell
iwr -useb https://get.agenc.ag/install.ps1 | iex
```

Windows needs [Git for Windows](https://git-scm.com/download/win), because sessions run their shell through its `bash.exe`. AgenC has no native Windows sandbox yet. For sandboxed sessions, install and run AgenC inside WSL2 (with bubblewrap installed) using the macOS / Linux command above.

npm (requires Node.js 26.5 or later in the 26.x line):

```bash
npm install -g @tetsuo-ai/agenc
```

Check the installation:

```bash
agenc --version
```

#### 2. Configure the DeepSeek Provider

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Option A: setup wizard (recommended)**

```bash
agenc onboard
```

- At the **provider** step, select **DeepSeek**.
- At the **model access** step, paste your DeepSeek API Key. AgenC checks the key against the DeepSeek API before it saves it in your operating system's secure storage.
- The **connection-test** step then sends a real request to DeepSeek.

**Option B: environment variable**

Linux / macOS users:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows users:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

**Set the default model and reasoning effort**

Run these commands once, after either option:

```bash
agenc config set model_provider deepseek
agenc config set model deepseek-flash
agenc config set reasoning_effort max
```

They write the following keys to `~/.agenc/config.toml` (run `agenc config path` to see the exact file):

```toml
config_version = 2
model_provider = "deepseek"
model = "deepseek-flash"
reasoning_effort = "max"
```

Available models:

| Model ID | DeepSeek model | Context window | Output per call | Reasoning effort | Image input |
| --- | --- | --- | --- | --- | --- |
| `deepseek-flash` (default) | DeepSeek-V4.1-Flash | 1M tokens | 64,000 by default, up to 384K | `low`, `high` (default), `max` | Yes |
| `deepseek-v4-pro` | DeepSeek-V4-Pro | 1M tokens | 64,000 by default, up to 384K | `low`, `high` (default), `max` | No |

- **1M context.** AgenC's catalog sets a 1,048,576-token context window for both models, so no extra configuration is needed. If you route DeepSeek through a proxy that needs fixed limits from the first turn, set `providers.deepseek.context_window_tokens` and `providers.deepseek.max_output_tokens`.
- **Max thinking.** AgenC sends `thinking: {"type": "enabled"}` and your effort as `reasoning_effort` on every request. `max` reaches DeepSeek unchanged. If you leave the effort unset, the model runs at its default, `high`.
- **Multi-turn tool calls.** AgenC passes `reasoning_content` back to DeepSeek on later requests, as the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode) require for tool calls.
- **Legacy ID.** `deepseek-v4-flash` still works. DeepSeek serves it with DeepSeek-V4.1-Flash. Use `deepseek-flash` for new setups.
- **Base URL.** AgenC uses `https://api.deepseek.com/v1`. Set `DEEPSEEK_BASE_URL` or `providers.deepseek.base_url` only if you go through a proxy.

#### 3. Run and Select Model

Enter a project directory and start AgenC:

```bash
cd /path/to/my-project
agenc
```

Inside the terminal UI:

- `/effort` shows or changes the reasoning effort. `/effort max` applies to the running session and is saved as the default for new sessions.
- `/model` switches between `deepseek-flash` and `deepseek-v4-pro`.
- `/provider` connects another provider or saves a new API key.
- `/help` lists all slash commands.

You can also choose the provider and model for one run from the command line:

```bash
# Interactive session with DeepSeek-V4-Pro
agenc --provider deepseek --model deepseek-v4-pro

# Headless one-shot run, for scripts and CI
agenc --provider deepseek --model deepseek-flash -p "run the tests and fix what fails"
```

Pass `--provider deepseek` together with `--model`. Some model IDs, such as `deepseek-v4-pro`, also appear under other providers in AgenC's catalog, and AgenC rejects a model-only selection that matches more than one provider.

For current prices, see DeepSeek's [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) page. AgenC's session cost estimate uses DeepSeek's peak-hour rates, so off-peak calls cost less than the estimate shows.

#### 4. Going Further

- **MCP servers.** Add a server with `agenc mcp add <name> <command-or-url>` and list them with `agenc mcp list`.
- **Background agents.** Start one with `agenc agent start "<objective>"`. Resume an earlier session with `agenc --continue`.
- **Chat channels.** Run `agenc onboard channel` to reach your agent from Telegram, Discord, Slack, or WebChat.

#### Troubleshooting

- Run `agenc providers` to see each provider's credential status. After setup, the `deepseek` row should show a credential.
- If `DEEPSEEK_MODEL` is set in your environment (some other DeepSeek tools use it), AgenC refuses to start. Unset it and pick the model with `--model`, `AGENC_MODEL`, or `model` in `config.toml`.
- On native Windows, the sandboxed permission modes refuse to start a session (`sandbox_required_unavailable`). Run AgenC inside WSL2 instead.
- Run `agenc doctor` to check the installation itself.
