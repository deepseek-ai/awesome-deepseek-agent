[English](./ccx.md) | [简体中文](./ccx.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex CLI / Codex App via CCX

[CCX](https://github.com/BenedictKing/ccx) is a high-performance AI API proxy and protocol translation gateway. It enables Codex CLI and Codex App to use DeepSeek models by providing local `/v1/messages` passthrough and `/v1/responses` → `/v1/chat/completions` translation — bridging the gap between Codex's Responses API and DeepSeek's Chat Completions API.

## How It Works

Codex CLI and Codex App natively speak the OpenAI Responses API (`/v1/responses`), while DeepSeek provides the Chat Completions API (`/v1/chat/completions`). CCX sits between them and:

- Forwards `/v1/messages` requests directly to upstream (Claude-compatible passthrough)
- Translates `/v1/responses` requests into `/v1/chat/completions` requests, so DeepSeek models appear as first-class providers

```text
Codex CLI / Codex App  →  CCX (:3000)  →  DeepSeek API
     /v1/responses           /v1/chat/completions
```

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

| Field              | Value                                        |
| ------------------ | -------------------------------------------- |
| **Type**           | OpenAI Chat                                  |
| **Name**           | DeepSeek                                     |
| **Base URL**       | `https://api.deepseek.com/v1/chat/completions` |
| **API Key**        | `<your DeepSeek API Key>`                    |
| **Models**         | `deepseek-v4-pro`, `deepseek-v4-flash`       |

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Enable the channel, set its priority, and it is ready to serve requests.

#### 3. Configure Codex CLI

Set the following environment variables in your terminal:

```bash
export OPENAI_API_KEY="your-strong-proxy-key"
export OPENAI_BASE_URL="http://localhost:3000/v1"
```

Now run Codex CLI — it will use CCX as its API endpoint, which routes `/v1/responses` requests through the DeepSeek channel.

Verify the model is reachable:

```bash
codex --model deepseek-v4-pro "hello"
```

#### 4. Configure Codex App (VS Code / JetBrains)

In the Codex extension settings, set:

| Setting             | Value                        |
| ------------------- | ---------------------------- |
| **API Key**         | `your-strong-proxy-key`      |
| **Base URL**        | `http://localhost:3000/v1`   |
| **Model**           | `deepseek-v4-pro`            |

After saving, Codex App will send Responses API requests to CCX, which translates them into DeepSeek-compatible Chat Completions calls.

#### 5. Optional: Verify the Setup

Test the endpoint directly:

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer your-strong-proxy-key"
```

If you see `deepseek-v4-pro` and `deepseek-v4-flash` in the list, everything is working.

#### Troubleshooting

- `401 Unauthorized`: Check that `PROXY_ACCESS_KEY` in CCX matches the key set in Codex CLI/App.
- `Model not found`: Verify the model names in the CCX channel match exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- `Connection refused`: Ensure CCX is running on port 3000 and `OPENAI_BASE_URL` points to the correct address.
- Channel shows unhealthy: Verify your DeepSeek API Key in the CCX admin console and check network connectivity to `api.deepseek.com`.
