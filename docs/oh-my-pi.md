[English](./oh-my-pi.md) | [简体中文](./oh-my-pi.zh-CN.md) · [← Back](../README.md)

# Using DeepSeek with Oh My Pi

[Oh My Pi](https://github.com/can1357/oh-my-pi) is a terminal AI coding agent. As of v14.5 it ships DeepSeek V4 model entries, but the built-in compat is incomplete — a custom `models.yml` is still required for reliable use.

## Prerequisites

Install Oh My Pi: <https://github.com/can1357/oh-my-pi#installation>

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys):

```sh
export DEEPSEEK_API_KEY=<your API key>
```

## Configuration

Create `~/.omp/agent/models.yml`:

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
| `authHeader: true` | Sends `Authorization: Bearer $DEEPSEEK_API_KEY`. Does not go through OAuth `/login`. |
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

### Three critical compat fields

These three fields are essential. Without them, DeepSeek V4 will return 400 errors when using tools in thinking mode.

| Field | Notes |
| ----- | ----- |
| `supportsToolChoice: false` | DeepSeek V4 thinking mode rejects the `tool_choice` parameter. |
| `requiresReasoningContentForToolCalls: true` | DeepSeek requires `reasoning_content` to be preserved across tool-call turns in conversation history. Skipping this causes 400. |
| `requiresAssistantContentForToolCalls: true` | Ensures tool-call messages have non-null `content`. Use together with the field above. |

## Usage

```sh
cd /path/to/your-project
omp --model deepseek/deepseek-v4-pro
```

For faster responses:

```sh
omp --model deepseek/deepseek-v4-flash
```

Switch models inside Oh My Pi with `/model` or `Ctrl+L`.

## Known issues

**Do not rely on the built-in model entries.** Recent builds list `deepseek-v4-pro` and `deepseek-v4-flash` via `omp --list-models deepseek`, but they lack the three critical compat fields above. Long thinking-mode conversations with tool calls will 400. Always use the `models.yml` configuration shown above.

Oh My Pi does not currently have a DeepSeek OAuth `/login` entry. API keys must be provided via the `DEEPSEEK_API_KEY` environment variable or the `apiKey` field in `models.yml`.

When using DeepSeek V4 through unofficial providers (DeepInfra, KiloCode, NVIDIA NIM, Zenmux, etc.) via OpenAI-compatible endpoints, `reasoning_content` replay behavior varies and compatibility is unresolved. Prefer the official `api.deepseek.com` endpoint.

In `models.yml`, `compat` replaces the built-in block wholesale — it does not merge. Always specify the full set of compat fields.
