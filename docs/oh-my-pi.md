[English](./oh-my-pi.md) | [简体中文](./oh-my-pi.zh-CN.md) · [← Back](../README.md)

# Using DeepSeek with Oh My Pi

[Oh My Pi](https://github.com/can1357/oh-my-pi) is a terminal AI coding agent. As of v17.0.5, the `deepseek` provider is bundled with full compat support — a custom `models.yml` is no longer required for the standard official API setup.

> **Compatibility snapshot (2026-07-21):** This guide was verified against Oh My Pi v17.0.5. In this version, the bundled `deepseek` provider supports API-key authentication, the `DEEPSEEK_API_KEY` environment variable, the official DeepSeek endpoint, thinking mode, and tool-call compatibility. Earlier versions may behave differently; upgrade before applying legacy workarounds.

## Prerequisites

Install Oh My Pi: <https://github.com/can1357/oh-my-pi#installation>

Verify the installation:

```sh
omp --version
```

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

## Authentication

Two methods are supported.

### Recommended: OMP credential flow

Launch OMP and run the login command inside the session:

```text
omp
/login deepseek
```

Despite the command name, this is an API-key credential flow, not a DeepSeek OAuth flow. OMP stores the key securely through its provider-scoped login interface.

### Alternative: environment variable

```sh
export DEEPSEEK_API_KEY="<your API key>"
```

PowerShell:

```powershell
$env:DEEPSEEK_API_KEY = "<your API key>"
```

## Configuration (reference)

In OMP v17.0.5, the bundled `deepseek` provider already handles the compat fields below. The following `~/.omp/agent/models.yml` is provided as a reference for advanced customization — custom gateways, private aliases, provider overrides, or experimental third-party providers. It is not needed for the standard setup.

```yaml
providers:
  deepseek:
    baseUrl: https://api.deepseek.com
    api: openai-completions
    apiKey: DEEPSEEK_API_KEY
    authHeader: true
    models:
      - id: deepseek-v4-pro
        name: DeepSeek V4 Pro
        reasoning: true
        thinking:
          minLevel: high
          maxLevel: xhigh
          mode: effort
        input: [text]
        contextWindow: 1000000
        maxTokens: 384000
        compat:
          supportsDeveloperRole: false
          supportsReasoningEffort: true
          maxTokensField: max_tokens
          reasoningEffortMap:
            high: high
            xhigh: max
          supportsToolChoice: false
          requiresReasoningContentForToolCalls: true
          requiresAssistantContentForToolCalls: true
          extraBody:
            thinking:
              type: enabled
      - id: deepseek-v4-flash
        name: DeepSeek V4 Flash
        reasoning: true
        thinking:
          minLevel: high
          maxLevel: xhigh
          mode: effort
        input: [text]
        contextWindow: 1000000
        maxTokens: 384000
        compat:
          supportsDeveloperRole: false
          supportsReasoningEffort: true
          maxTokensField: max_tokens
          reasoningEffortMap:
            high: high
            xhigh: max
          supportsToolChoice: false
          requiresReasoningContentForToolCalls: true
          requiresAssistantContentForToolCalls: true
          extraBody:
            thinking:
              type: enabled
```

## Configuration notes

### Basics

| Field | Notes |
| ----- | ----- |
| `baseUrl: https://api.deepseek.com` | DeepSeek OpenAI-compatible endpoint. Do not append `/v1`. |
| `authHeader: true` | Sends `Authorization: Bearer $DEEPSEEK_API_KEY`. |
| `supportsDeveloperRole: false` | Sends system prompt as `system` role. DeepSeek rejects the `developer` role. |
| `maxTokensField: max_tokens` | DeepSeek uses `max_tokens`, not OpenAI's `max_completion_tokens`. |

### Thinking mode

| Field | Notes |
| ----- | ----- |
| `thinking.mode: effort` | Uses effort-based thinking. OMP sends a `reasoning_effort` parameter. |
| `thinking.minLevel: high` / `maxLevel: xhigh` | Locks the selector to DeepSeek's two supported levels. |
| `reasoningEffortMap: { high: high, xhigh: max }` | Maps OMP's `xhigh` to DeepSeek's `max`. Without this, `xhigh` is unrecognized. |
| `extraBody.thinking.type: enabled` | Explicitly enables DeepSeek V4 thinking mode. |
| `supportsReasoningEffort: true` | Allows OMP to send `reasoning_effort`. |

### Tool-call compat

| Field | Notes |
| ----- | ----- |
| `supportsToolChoice: false` | DeepSeek V4 thinking mode rejects the `tool_choice` parameter. |
| `requiresReasoningContentForToolCalls: true` | DeepSeek requires `reasoning_content` to be preserved across tool-call turns in conversation history. Skipping this causes 400. |
| `requiresAssistantContentForToolCalls: true` | Ensures tool-call messages have non-null `content`. Use together with the field above. |

All three fields above are handled automatically by the bundled provider in v17.0.5.

## Usage

```sh
cd /path/to/your-project
omp --model deepseek/deepseek-v4-pro
```

For lower latency:

```sh
omp --model deepseek/deepseek-v4-flash
```

Switch models inside OMP with `/model` or `Ctrl+L`.

## Troubleshooting

Check your version and available models:

```sh
omp --version
omp --list-models deepseek
```

Then:

1. **Upgrade first.** If `omp --version` reports a release older than v17.0.5, upgrade before applying a legacy workaround.
2. **Check for stale overrides.** A leftover `~/.omp/agent/models.yml` may override the bundled provider. Remove or rename it if you rely on the built-in setup.
3. **Re-authenticate.** Run `/login deepseek` again, or verify `DEEPSEEK_API_KEY` is set correctly.
4. **Prefer the official endpoint.** When diagnosing compatibility issues, use the official `api.deepseek.com` endpoint. Third-party OpenAI-compatible gateways may implement `reasoning_content` replay differently.
5. **Treat third-party providers separately.** Compatibility claims in this guide apply to the official DeepSeek API endpoint only.
