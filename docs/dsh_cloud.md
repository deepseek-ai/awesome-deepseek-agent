[English](./dsh_cloud.md) | [简体中文](./dsh_cloud.zh-CN.md) · [← Back](../README.md)

# Integrate with DSH Cloud

DSH Cloud is an open-source platform that turns DeepSeek Harness into a
multi-user product: accounts, credit metering, a server-side model gateway
(DeepSeek API keys stay on the server, never on clients), and optional
per-session cloud agent workspaces. Run it self-hosted, or use the hosted
service.

- **GitHub:** <https://github.com/AgentsDanceAI/deepseek-harness-cloud>
- **Website:** <https://dshcloud.online>

There are two ways to use it with DeepSeek models.

#### Option A — Connect a stock DeepSeek Harness install

If you already run DeepSeek Harness, one command adds DSH Cloud as a model
provider (no API key of your own required; hosted accounts include 500 free
credits):

```bash
npx --yes dsh-plugin-cloud setup
```

The command opens your browser for device approval, fetches the gateway's live
model catalog, and writes the provider into `$DSH_HOME/cordis.patch.yml` (your
own configuration is never touched — the provider lives in its own row).

Restart DeepSeek Harness and pick a model from the **DSH Cloud** group —
`deepseek-v4-pro` and `deepseek-v4-flash` are served with their full
**1M-token context window**, alongside other catalog models.

#### Option B — Self-host the whole platform

With Docker installed:

```bash
npx --yes @agentsdanceai/dsh-cloud start
```

Then put your own [DeepSeek API key](https://platform.deepseek.com/api_keys)
into the generated `./dsh-cloud/.env`:

```
UPSTREAM_BASE_URL=https://api.deepseek.com/v1
UPSTREAM_API_KEY=sk-your-key
```

Run the same command again and open <http://localhost:8787>. Your whole team
now shares one DeepSeek API key through the gateway, with per-user accounts and
credit metering. Python users can use `uvx dsh-cloud start` instead.

#### First run

Sign in, open the workspace (or your connected DeepSeek Harness), select
`deepseek-v4-flash` for fast tasks or `deepseek-v4-pro` for deep reasoning, and
start a conversation. Usage is metered per token against credits.
