[English](./deepseekx.md) | [简体中文](./deepseekx.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeekX

DeepSeekX is a downstream adaptation of OpenAI Codex CLI for DeepSeek API
usage. It does not redesign the Codex core agent workflow; the main change is
a DeepSeek `/chat/completions` adapter plus DeepSeek-oriented provider, model,
packaging, and user-facing defaults.

- **GitHub:** <https://github.com/meomeo-dev/deepseekx>

#### 1. Install DeepSeekX

- Install [Node.js](https://nodejs.org/en/download/) 18+.
- Install the CLI from npm:

```sh
npm install -g @meomeo-dev/deepseekx
```

Verify the installation:

```sh
deepseekx --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
DeepSeekX reads it from the `DEEPSEEK_API_KEY` environment variable:

```sh
export DEEPSEEK_API_KEY="sk-..."
```

#### 3. Start in a project directory

```sh
cd /path/to/my-project
deepseekx
```

DeepSeekX uses `~/.deepseekx` as its default user directory and
`.deepseekx/config.toml` for project-level settings. It does not read the
upstream Codex user directory by default.

#### 4. Optional configuration

Create `~/.deepseekx/config.toml`:

```toml
model_provider = "deepseek"
model = "deepseek-v4-pro"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "https://api.deepseek.com"
env_key = "DEEPSEEK_API_KEY"
wire_api = "chat"
requires_openai_auth = false
```

DeepSeekX exposes `deepseek-v4-pro` and `deepseek-v4-flash`. Its built-in model
metadata uses a 384K default context window and a 1M maximum context window for
DeepSeek V4. Reasoning effort supports `high` and `xhigh`; `xhigh` maps to
DeepSeek's max reasoning effort.

Because the Codex configuration model is kept aligned with upstream Codex, most
`config.toml` concepts such as profiles, sandbox mode, approval policy, MCP,
tools, and project configuration follow the Codex configuration documentation.
Adjust only the DeepSeek-specific provider, model, API key, and config
directory values shown above.

#### Project profiles

Create `.deepseekx/config.toml` in a repository:

```toml
model = "deepseek-v4-flash"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[profiles.pro]
model_provider = "deepseek"
model = "deepseek-v4-pro"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

Run a profile:

```sh
deepseekx --profile pro
```

#### Features

- Direct DeepSeek Chat Completions integration, no local translation proxy
  required.
- Sandboxed local command execution with approval controls.
- MCP client support for configured MCP servers and tools.
- Project-level config under `.deepseekx/config.toml`.
- DeepSeek-specific model catalog, tool instructions, and prompt templates.

#### Troubleshooting

- `401` or authentication errors: check `DEEPSEEK_API_KEY`.
- `402` or payment errors: check your DeepSeek Platform balance.
- Config changes do not apply: confirm whether the value is set in the command
  line, project config, or user config. DeepSeekX applies command-line
  overrides first, then project config, then user config.
- Tool execution is blocked: review `approval_policy` and `sandbox_mode`.

#### Resources

- [DeepSeekX](https://github.com/meomeo-dev/deepseekx)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
