[English](./callcopilot.md) | [简体中文](./callcopilot.zh-CN.md) · [← Back](../README.md)

# Integrate with callCopilot

[callCopilot](https://github.com/qoli/callCopilot) is a standalone launcher for GitHub Copilot CLI BYOK providers. It wraps Copilot CLI with DeepSeek V4 aliases, local proxy setup, token-limit metadata, and thinking-block preservation for the official DeepSeek Anthropic-compatible endpoint.

Use it when you want to run GitHub Copilot CLI with DeepSeek without manually exporting every `COPILOT_PROVIDER_*` variable before each session.

#### 1. Install Requirements

Install GitHub Copilot CLI:

```shell
npm install -g @github/copilot
```

Clone callCopilot:

```shell
git clone https://github.com/qoli/callCopilot.git
cd callCopilot
```

Runtime requirements:

- macOS system Python at `/usr/bin/python3`.
- `node` for local provider proxies.
- `npm` for the first `ds` or `dsf` run, when callCopilot installs `opencode-deepseek-thinking-fix` locally.
- `copilot` from GitHub Copilot CLI.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure callCopilot

Create `.env` from the example file:

```shell
cp examples/.env.example .env
```

Set your DeepSeek API key:

```env
DEEPSEEK_API_KEY=sk-your-deepseek-api-key
CALLCOPILOT_DEEPSEEK_PROVIDER_BASE_URL=https://api.deepseek.com/anthropic
```

The official DeepSeek aliases are:

| Alias | Provider | Model |
| ----- | -------- | ----- |
| `ds` | DeepSeek Anthropic-compatible API | `deepseek-v4-pro` |
| `dsf` | DeepSeek Anthropic-compatible API | `deepseek-v4-flash` |

For `ds` and `dsf`, callCopilot sets Copilot CLI's provider type to `anthropic`, starts a local proxy, and forwards requests to `https://api.deepseek.com/anthropic`.

#### 4. Context and Thinking Settings

DeepSeek V4 supports a 1M-token context window. For the official DeepSeek aliases, callCopilot passes these Copilot CLI limits by default:

```env
COPILOT_PROVIDER_MAX_PROMPT_TOKENS=1048576
COPILOT_PROVIDER_MAX_OUTPUT_TOKENS=393216
```

You can override them if needed:

```shell
export CALLCOPILOT_DEEPSEEK_MAX_PROMPT_TOKENS=1048576
export CALLCOPILOT_DEEPSEEK_MAX_OUTPUT_TOKENS=393216
```

DeepSeek V4 thinking mode is enabled through the local Anthropic-compatible proxy. The proxy preserves and re-injects thinking blocks across tool-call turns so DeepSeek can continue reasoning correctly in Copilot CLI agent sessions.

The default thinking budget is `8000` tokens. For more complex coding tasks, increase it before launching callCopilot:

```shell
export DEEPSEEK_THINKING_BUDGET=65536
```

Do not disable thinking mode as the primary workaround for reasoning-content errors.

#### 5. First Run

Run Copilot CLI with DeepSeek V4 Pro:

```shell
bin/callCopilot ds -- -s -p "Reply OK only."
```

Run with DeepSeek V4 Flash:

```shell
bin/callCopilot dsf -- -s -p "Reply OK only."
```

To start an interactive Copilot CLI agent session with DeepSeek V4 Pro:

```shell
cd /path/to/my-project
/path/to/callCopilot/bin/callCopilot ds
```

callCopilot adds `--autopilot` by default unless you pass your own Copilot CLI arguments.

#### Optional: NVIDIA Hosted DeepSeek

callCopilot also includes an NVIDIA-hosted DeepSeek alias:

```env
NVIDIA_DEEPSEEK_API_KEY=your-nvidia-api-key
CALLCOPILOT_NVIDIA_DEEPSEEK_PROVIDER_BASE_URL=https://integrate.api.nvidia.com/v1
```

Run it with:

```shell
bin/callCopilot nds -- -s -p "Reply OK only."
```

This path uses `deepseek-ai/deepseek-v4-pro` through an OpenAI-compatible endpoint. Check the provider's current model limits and availability before relying on it for long-context work.

#### Optional: Local OpenAI-Compatible Models

Any other model ID is routed to the local oMLX OpenAI-compatible backend:

```shell
bin/callCopilot Qwen3.6-35B-A3B-bf16 -- -s -p "Reply OK only."
```

For local models, callCopilot reads `max_context_window` and `max_tokens` from the local `/v1/models/status` response and passes those values to Copilot CLI. The local path is therefore limited by the model server's reported capabilities, not by DeepSeek V4's 1M context.

#### Resources

- [callCopilot GitHub repository](https://github.com/qoli/callCopilot)
- [GitHub Copilot CLI BYOK docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models)
- [DeepSeek Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode)
