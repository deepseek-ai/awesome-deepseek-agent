[English](./goraven.md) | [简体中文](./goraven.zh-CN.md) · [← Back](../README.md)

# Integrate with GoRaven

GoRaven is an open-source, self-hosted team Agent platform. Every team member gets an independent Agent workspace — the Agent reads files, writes code, runs commands, calls APIs, searches the knowledge base, and delivers results. It works with DeepSeek, OpenAI, Claude, Qwen, GLM, or any compatible API.

- **GitHub:** <https://github.com/8treenet/goraven>
- **Website:** <https://goraven.dev>
- **Live preview:** <https://preview.goraven.dev>

#### 1. Deploy GoRaven

```bash
docker pull 8treenet/goraven:latest

docker run -d --restart=always --name goraven-agent \
  -p 8000:8000 \
  8treenet/goraven:latest
```

For persistent data, mount a volume:

```bash
docker run -d --restart=always --name goraven-agent \
  -p 8000:8000 \
  -v /opt/goraven:/goraven/data \
  8treenet/goraven:latest
```

Open <http://localhost:8000> and complete the setup wizard to create your admin account. Then create a DeepSeek API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Add a DeepSeek Model

In the admin console, go to **Models** and click **Add Model**:

1. Select **DeepSeek** as the provider. The **Base URL** is pre-filled with `https://api.deepseek.com/v1`.
2. Paste your DeepSeek API Key into **API Key**.
3. In the **Model** field, enter `deepseek-v4-pro` — or click the dropdown to fetch the recommended model list from DeepSeek.
4. Set **Context Length (K Tokens)** to `1000` — DeepSeek V4 models support a 1M token context window.
5. Optional: enable the **Default Model** label so it is pre-selected in new chats.

Repeat the same steps to add `deepseek-v4-flash` for lower-latency, cheaper everyday tasks, and enable the **Flash Model** label. Connectivity is verified automatically when saving.

#### 3. Start an Agent Session

Open a project or a new chat, then click the model chip to switch between DeepSeek V4 Pro and V4 Flash. V4 Pro is the best choice for coding, long-horizon planning, and multi-step agent tasks. Assign tasks directly — the Agent can read/write files, run shell commands, and call MCP tools on its own.

#### 4. Manage Access and Quotas

As an admin, open the **Models** page and click **Members** on a model to control which users and teams can use it, and set quotas to prevent overuse.

#### Troubleshooting

- `401` or authentication errors: recheck the API Key and the Base URL (`https://api.deepseek.com/v1`).
- Model not responding: confirm the model name is exactly `deepseek-v4-pro` or `deepseek-v4-flash`. Older V3 model names are deprecated and no longer resolve to current models.
- Behind a proxy: fill in the optional **Proxy URL** field, e.g. `http://127.0.0.1:7890`.
- Setting a custom timezone for the container: add `-e TZ=Asia/Shanghai` to the `docker run` command.
