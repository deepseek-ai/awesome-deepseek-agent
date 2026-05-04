[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek via CCX — Claude Code CLI & Codex CLI/App

[CCX](https://github.com/BenedictKing/ccx) is a high-performance AI API proxy and protocol translation gateway. It unlocks DeepSeek models for multiple tools through a unified local endpoint:

| Endpoint            | Protocol                                     | Target Tool          |
| ------------------- | -------------------------------------------- | -------------------- |
| `/v1/messages`      | Claude Messages API passthrough              | **Claude Code CLI**  |
| `/v1/responses`     | Responses → Chat Completions translation     | **Codex CLI / App**  |
| `/v1/chat/completions` | OpenAI Chat Completions passthrough       | Any OpenAI-compatible tool |

One CCX instance serves all three paths simultaneously — add a DeepSeek channel and every tool that speaks one of these protocols can use it.

## How It Works

```text
Claude Code CLI ──→  /v1/messages ──→  CCX (:3000)  ──→  DeepSeek API
Codex CLI/App  ──→  /v1/responses ──→  CCX (:3000)  ──→  DeepSeek API
                                            │
                          /v1/chat/completions (passthrough)
```

CCX handles the protocol differences internally: Claude Messages requests are translated to Chat Completions for the upstream DeepSeek channel, and Responses requests are likewise mapped to Chat Completions. The tool sees a native endpoint; DeepSeek receives standard Chat Completions calls.

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

#### 2. Configure a DeepSeek Channel

Open the CCX admin console at `http://localhost:3000`, navigate to **Channels**, and add a new channel:

| Field              | Value                                          |
| ------------------ | ---------------------------------------------- |
| **Type**           | OpenAI Chat                                    |
| **Name**           | DeepSeek                                       |
| **Base URL**       | `https://api.deepseek.com/v1/chat/completions` |
| **API Key**        | `<your DeepSeek API Key>`                      |
| **Models**         | `deepseek-v4-pro`, `deepseek-v4-flash`         |

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Codex CLI/App defaults to `gpt-5` / `mini` as model names and requires model redirection. Claude Code CLI uses `opus` / `sonnet` / `haiku` — redirection is recommended but optional (you can also pass `--model deepseek-v4-pro` directly). Configure **model redirection** in the channel:

| Requested Model  | Redirect To           | Used By            |
| ---------------- | --------------------- | ------------------ |
| `gpt-5`          | `deepseek-v4-pro`     | Codex CLI/App      |
| `mini`           | `deepseek-v4-flash`   | Codex CLI/App      |
| `opus`           | `deepseek-v4-pro`     | Claude Code CLI (推荐) |
| `sonnet`         | `deepseek-v4-pro`     | Claude Code CLI (推荐) |
| `haiku`          | `deepseek-v4-pro`     | Claude Code CLI (推荐) |

Fill in the Model Mapping section in the CCX channel settings to set up the redirection.

After enabling the channel, verify connectivity via "Test Channel":

![Test successful](../assets/ccx/channel-test-success.png)

#### 3. Scenario A: Claude Code CLI

Claude Code CLI speaks the Messages API. Configure a channel of type **Claude Code** with your DeepSeek Base URL, Key, and model remapping rules:

![Claude Messages channel configuration](../assets/ccx/messages-channel-config.png)

Point Claude Code CLI at CCX's `/v1/messages` endpoint:

```bash
export ANTHROPIC_API_KEY="your-strong-proxy-key"
export ANTHROPIC_BASE_URL="http://localhost:3000/v1/messages"
```

Verify:

```bash
claude --model deepseek-v4-pro "hello"
```

Claude Code CLI sends `/v1/messages` requests; CCX translates them and routes to the DeepSeek channel.

#### 4. Scenario B: Codex CLI

Codex CLI speaks the OpenAI Responses API. Configure a channel of type **DeepSeek** (OpenAI Chat) with your DeepSeek Base URL, Key, and model remapping rules:

![DeepSeek Chat channel configuration](../assets/ccx/chat-channel-config.png)

Point Codex CLI at CCX's `/v1` base:

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

Verify:

```bash
codex "hello"
```

Codex CLI defaults to `gpt-5` as the model name; CCX remaps it to `deepseek-v4-pro` via the channel's model redirection rules. You can also specify the model explicitly: `codex --model deepseek-v4-pro "hello"`.

#### 5. Scenario C: Codex App (VS Code / JetBrains)

In the Codex extension settings, set:

| Setting             | Value                        |
| ------------------- | ---------------------------- |
| **API Key**         | `your-strong-proxy-key`      |
| **Base URL**        | `http://localhost:3000/v1`   |
| **Model**           | `gpt-5` (CCX auto-redirects to `deepseek-v4-pro`) |

After saving, Codex App sends Responses API requests with `gpt-5` as the default model; CCX remaps it to `deepseek-v4-pro` via the channel redirection rules and translates the call to Chat Completions for DeepSeek.

#### 6. Optional: View Request Logs

CCX includes built-in log monitoring to inspect model routing, latency, and response status per request in real time:

![Request log monitoring](../assets/ccx/log-monitoring.png)

#### 7. Optional: Verify Model List

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
- Claude Code reports an unexpected response format: Make sure `ANTHROPIC_BASE_URL` ends with `/v1/messages` (not just `/v1`).
