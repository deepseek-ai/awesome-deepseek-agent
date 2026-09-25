[English](./grok_build.md) | [简体中文](./grok_build.zh-CN.md) · [← Back](../README.md)

# Integrate with Grok Build

Grok Build (`grok`) is xAI's terminal coding agent: a full-screen TUI that reads your codebase, edits files, runs shell commands, and calls MCP tools. It defaults to xAI-hosted Grok models, and also speaks OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages — so DeepSeek V4 can be added as a custom model in `~/.grok/config.toml`.

For custom models Grok uses the OpenAI Chat Completions backend by default, and DeepSeek V4 works on it as-is, including multi-turn tool calling.

#### 1. Install Grok Build

macOS / Linux / Windows via Git Bash:

```shell
curl -fsSL https://x.ai/cli/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

Verify:

```shell
grok --version
```

#### 2. Get a DeepSeek API Key

Create a key at the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Put the Key in an Environment Variable

Linux / macOS:

```shell
export DEEPSEEK_API_KEY="sk-..."
```

Windows (PowerShell):

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

Keep the key in the environment rather than inline in `config.toml`. Grok resolves credentials in this order: `api_key` → `env_key` → **your signed-in grok.com session token** → `XAI_API_KEY`. If the variable named by `env_key` is unset, Grok does not report a missing key — it silently sends your grok.com session token to the DeepSeek endpoint, which rejects it with a misleading authentication error. Set the variable in the same shell session you launch `grok` from.

#### 4. Add DeepSeek V4 to `config.toml`

Config file: `~/.grok/config.toml` (Windows: `%USERPROFILE%\.grok\config.toml`); set `GROK_HOME` to use a different directory. Create the file if it does not exist.

```toml
[models]
default = "deepseek-v4-pro"
default_reasoning_effort = "max"

[model.deepseek-v4-pro]
model = "deepseek-v4-pro"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Pro"
env_key = "DEEPSEEK_API_KEY"
context_window = 1000000
reasoning_efforts = ["low", "high", "max"]

[model.deepseek-v4-flash]
model = "deepseek-v4-flash"
base_url = "https://api.deepseek.com/v1"
name = "DeepSeek V4 Flash"
env_key = "DEEPSEEK_API_KEY"
context_window = 1000000
reasoning_efforts = ["low", "high", "max"]
```

- `api_backend` is omitted on purpose — it defaults to `chat_completions`.
- `context_window` decides when Grok auto-compacts. DeepSeek V4 supports 1M tokens; its `/v1/models` row reports 1,048,576, and 1,000,000 is a safe value to configure.
- `reasoning_efforts` is required for DeepSeek. Grok normally builds the effort menu from the endpoint's `/v1/models` row, where DeepSeek spells the levels as `effort.supported_levels`. Grok does not read that shape, so without this line `default_reasoning_effort` and `/effort` are silently dropped and the model runs at DeepSeek's own default (`high`). With it, `max` is sent as `reasoning_effort` in the request body.
- `deepseek-v4-flash` is the current name; DeepSeek also accepts the `deepseek-flash` alias.

#### 5. First Run

```shell
cd /path/to/my-project
grok
```

Or pin the model for a single run:

```shell
grok -m deepseek-v4-pro --effort max
```

Check the catalog and which model is the default:

```shell
grok models
```

Inside the TUI:

| Command | Action |
| --- | --- |
| `/model deepseek-v4-pro` | Switch model for this session |
| `/effort max` | Set reasoning effort for this session |
| `Ctrl+M` | Open the model picker (from the scrollback pane) |

#### Troubleshooting

- **`Your api key: ****xxxx is invalid` together with `Auth: Oidc`** — the `env_key` variable is not visible to the process, so Grok fell back to your grok.com session token. Re-export `DEEPSEEK_API_KEY` and restart `grok`; a terminal opened before you set the variable will not have it.
- **Reasoning effort seems to have no effect** — add `reasoning_efforts = ["low", "high", "max"]` to the model block, as in step 4.
- **A model is missing from `grok models`** — a `[models] default` that names a model which does not exist is silently ignored. Check the spelling of both the `[model.<name>]` section and the `default` value.
- **Do not set `[endpoints] models_base_url`** — it redirects Grok's built-in models too and switches authentication from session to API key, which breaks `grok login`.
- **BYOK-only setups need no `grok login`** — a custom model with its own credential works on its own. xAI-hosted features (the model catalog, `grok update`, the plugin marketplace) still want a signed-in session.

#### Resources

- [DeepSeek API Docs](https://api-docs.deepseek.com/)
- [DeepSeek Platform](https://platform.deepseek.com/)
