[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek via CCX — Claude Code CLI & Codex CLI/App

[CCX](https://github.com/BenedictKing/ccx) is a high-performance AI API proxy and protocol translation gateway. It unlocks DeepSeek models for multiple tools through a unified local endpoint:

| Endpoint               | Protocol                                 | Target Tool                |
| ---------------------- | ---------------------------------------- | -------------------------- |
| `/v1/messages`         | Claude Messages API routing              | **Claude Code CLI**        |
| `/v1/responses`        | Responses → Chat Completions translation | **Codex CLI / App**        |
| `/v1/chat/completions` | OpenAI Chat Completions passthrough      | Any OpenAI-compatible tool |

One CCX instance serves all three paths simultaneously — configure the DeepSeek-backed channels for the protocols you need, and every compatible tool can use the same local gateway.

## How It Works

```text
Claude Code CLI       ──→  /v1/messages          ──→  CCX (:3000)  ──→  DeepSeek Anthropic endpoint
Codex CLI/App         ──→  /v1/responses         ──→  CCX (:3000)  ──→  DeepSeek Chat endpoint
OpenAI-compatible app ──→  /v1/chat/completions  ──→  CCX (:3000)  ──→  DeepSeek Chat endpoint
```

CCX handles the protocol differences internally: Claude Messages requests can route to DeepSeek's Anthropic-compatible endpoint, while Responses requests are mapped to Chat Completions. The tool sees a native endpoint; the upstream DeepSeek channel receives the protocol it expects.

#### 1. Set Up CCX

Download the latest binary from [CCX Releases](https://github.com/BenedictKing/ccx/releases/latest) and create a `.env` file next to it:

```bash
PROXY_ACCESS_KEY=your-strong-proxy-key
PORT=3000
ENABLE_WEB_UI=true
APP_UI_LANGUAGE=en
```

Run the binary and open `http://localhost:3000` to access the admin console.

Alternatively, use Docker:

```bash
docker run -d --name ccx \
  -p 3000:3000 \
  -v ./ccx-data:/app/data \
  -e PROXY_ACCESS_KEY="your-strong-proxy-key" \
  -e ENABLE_WEB_UI=true \
  benedictking/ccx:latest
```

#### 2. Configure DeepSeek Channels

##### 2.1 Codex CLI/App: Responses Channel

First, add a Chat service type in the Codex Responses channel page, for example `http://localhost:3000/channels/responses` (replace `3000` with your CCX port). This configures DeepSeek as an OpenAI Chat-compatible upstream. The Base URL is the upstream DeepSeek URL stored in CCX, not the local URL used by Codex:

| Field                 | Value                                      |
| --------------------- | ------------------------------------------ |
| **Service type**      | Chat                                       |
| **Name**              | DeepSeek Chat                              |
| **Base URL (OpenAI)** | `https://api.deepseek.com/`                |
| **API Key**           | `<your DeepSeek API Key>`                  |
| **Models**            | `deepseek-v4-pro`, `deepseek-v4-flash`     |

After saving, **edit** the **DeepSeek Chat** channel you just created and turn on **Normalize non-standard Chat roles** in the edit dialog. This maps to CCX's `normalizeNonstandardChatRoles` option: after Codex Responses requests are converted to Chat Completions, roles unsupported by DeepSeek, such as `developer`, are normalized to `user` before being sent upstream; `function` messages with `tool_call_id` are normalized to `tool`.

![Enable Normalize non-standard Chat roles](assets/ccx/codex-edit-channel-switch.png)

Then configure Model Mapping in the same edit dialog. Codex CLI/App requested models can be tiered with short match keys such as `gpt` / `mini`, so you can redirect different Codex model tiers to the corresponding DeepSeek models:

| Requested Model  | Redirect To           |
| ---------------- | --------------------- |
| `gpt`            | `deepseek-v4-pro`     |
| `mini`           | `deepseek-v4-flash`   |

`gpt` covers regular Codex models such as `gpt-5`, while `mini` covers lightweight models such as `gpt-5-mini`. CCX prefers the longest matching key, so do not use `gpt-5` as the pro redirect key; otherwise `gpt-5-mini` matches `gpt-5` before `mini` and cannot be routed to `deepseek-v4-flash` via the `mini` rule.

Add the mappings above in the Responses Chat service Model Mapping section:

![Responses Chat service model redirection](assets/ccx/codex-responses-redirect.png)

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

##### 2.2 Claude Code CLI: Messages Channel

For Claude Code CLI, open the Claude Messages channel page, for example `http://localhost:3000/channels/messages` (replace `3000` with your CCX port), and add a Claude service type backed by DeepSeek's Anthropic-compatible endpoint:

| Field                    | Value                                      |
| ------------------------ | ------------------------------------------ |
| **Service type**         | Claude                                     |
| **Name**                 | DeepSeek Claude                            |
| **Base URL (Anthropic)** | `https://api.deepseek.com/anthropic`       |
| **API Key**              | `<your DeepSeek API Key>`                  |
| **Models**               | `deepseek-v4-pro`, `deepseek-v4-flash`     |

Claude Code CLI sends requests with Claude model names such as Opus 4.7 by default. DeepSeek's official Anthropic-compatible endpoint may handle some model names automatically; for more predictable routing, it is recommended to configure model redirection explicitly in CCX:

| Requested Model  | Redirect To           |
| ---------------- | --------------------- |
| `opus`           | `deepseek-v4-pro`     |
| `sonnet`         | `deepseek-v4-pro`     |
| `haiku`          | `deepseek-v4-flash`   |

Recommended: configure Model Mapping for the Messages Claude service:

![Claude Code channel model redirection](assets/ccx/channel-test-success-alt.png)

#### 3. Scenario A: Claude Code CLI

Claude Code CLI speaks the Messages API. Use the Claude channel configured above with the Anthropic-compatible DeepSeek Base URL and Key; model remapping is recommended.

Point Claude Code CLI at the local CCX gateway root:

```bash
export ANTHROPIC_API_KEY="your-strong-proxy-key"
export ANTHROPIC_BASE_URL="http://localhost:3000"
```

Verify:

```bash
claude "hello"
```

Claude Code CLI sends `/v1/messages` requests with Claude model names such as Opus 4.7. If model redirection is configured, CCX applies those rules before routing the request to the DeepSeek channel; otherwise, the requested model name is left for DeepSeek's official endpoint to handle.

The Claude Code channel dashboard shows Messages traffic and token metrics:

![Claude Code channel usage stats](assets/ccx/redirect-editing-chat.png)

Messages request logs show protocol, model redirection, and latency:

![Messages request logs](assets/ccx/messages-channel-config.png)

#### 4. Scenario B: Codex CLI

Codex CLI speaks the OpenAI Responses API. Use the Chat service type configured in the Responses channel page with the OpenAI-compatible DeepSeek Base URL, Key, and model remapping rules.

Point Codex CLI at the local CCX `/v1` base:

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

Verify:

```bash
codex "hello"
```

When Codex CLI requests `gpt-5`, CCX remaps it to `deepseek-v4-pro` via the `gpt` rule. When it requests `gpt-5-mini`, the longer `mini` rule takes precedence and remaps it to `deepseek-v4-flash`. You can also specify the model explicitly: `codex --model deepseek-v4-pro "hello"`.

The Responses channel dashboard shows traffic and token metrics:

![DeepSeek Chat channel usage stats](assets/ccx/chat-channel-config.png)

Responses request logs show protocol, model redirection, and latency:

![Responses request logs](assets/ccx/channel-test-success.png)

#### 5. Scenario C: Codex App (VS Code / JetBrains)

In the Codex extension settings, set:

| Setting             | Value                        |
| ------------------- | ---------------------------- |
| **API Key**         | `your-strong-proxy-key`      |
| **Base URL**        | `http://localhost:3000/v1`   |
| **Model**           | `gpt-5` (CCX auto-redirects to `deepseek-v4-pro` via the `gpt` rule) |

After saving, if Codex App sends Responses API requests with `gpt-5`, CCX remaps it to `deepseek-v4-pro` via the `gpt` rule. If it sends `gpt-5-mini`, the `mini` rule takes precedence and remaps it to `deepseek-v4-flash`. CCX then translates the call to Chat Completions for DeepSeek.

#### 6. Optional: Verify Model List

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer your-strong-proxy-key"
```

If you see `deepseek-v4-pro` and `deepseek-v4-flash` in the list, the channel is healthy.

#### Troubleshooting

- `401 Unauthorized`: Check that the key set in the tool matches `PROXY_ACCESS_KEY` in CCX's `.env`.
- `Model not found`: Verify the model names in the CCX channel match exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- `Connection refused`: Ensure CCX is running on port 3000 and the base URL points to the correct address.
- Channel shows unhealthy: Verify your DeepSeek API Key in the CCX admin console and check network connectivity to `api.deepseek.com`.
- Claude Code reports an unexpected response format: Make sure `ANTHROPIC_BASE_URL` points to the CCX gateway root (not `/v1` or `/v1/messages`).
