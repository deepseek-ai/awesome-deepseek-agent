[English](./cowagent.md) | [简体中文](./cowagent.zh-CN.md) · [← Back](../README.md)

# Integrate with CowAgent

[CowAgent](https://github.com/zhayujie/CowAgent) is an open-source AI agent that handles autonomous task planning, tool use, skills, long-term memory, and a personal knowledge base. It supports DeepSeek, MiniMax, Claude, Gemini, OpenAI, GLM, Qwen, Doubao, Kimi, and other mainstream models, and can run on a Web console or connect to WeChat, Feishu, DingTalk, WeCom, QQ, and other chat channels. DeepSeek V4 is the default model in CowAgent and supports the full 1M-token context window.

#### 1. Install CowAgent

CowAgent provides a one-line install script for Linux, macOS, and Windows. The script handles dependencies, clones the repo to `~/CowAgent`, installs the `cow` CLI, runs the interactive setup, and starts the service.

Linux / macOS:

```bash
bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)
```

Windows (PowerShell):

```powershell
irm https://cdn.link-ai.tech/code/cow/run.ps1 | iex
```

After it finishes, the Web console is reachable at `http://localhost:9899`.

Useful management commands (see the [CLI docs](https://docs.cowagent.ai/cli/index) for the full list):

```bash
cow start | stop | restart | status | logs | update
```

#### 2. Configure DeepSeek in CowAgent

**Option A — Web console (recommended)**

1. Open `http://localhost:9899`.
2. Go to the **Models** page.
3. Select **DeepSeek** as the provider, paste your [DeepSeek API key](https://platform.deepseek.com/api_keys), and pick a model name: `deepseek-v4-flash` (default) or `deepseek-v4-pro`.
4. Save. The active model switches immediately, no restart needed.

To enable thinking mode and control reasoning depth, open the **Settings → Agent** page and toggle **Deep thinking**. For day-to-day agent tasks the default reasoning effort `high` is enough; for complex coding or long-horizon planning, switch the model to `deepseek-v4-pro` and set `reasoning_effort` to `max`.

**Option B — `config.json`**

Edit `~/CowAgent/config.json`:

```json
{
  "model": "deepseek-v4-flash",
  "deepseek_api_key": "YOUR_API_KEY",
  "deepseek_api_base": "https://api.deepseek.com/v1",
  "enable_thinking": true,
  "reasoning_effort": "high"
}
```

| Parameter | Description |
| --- | --- |
| `model` | `deepseek-v4-flash` (default) or `deepseek-v4-pro` |
| `deepseek_api_key` | Create at the [DeepSeek Platform](https://platform.deepseek.com/api_keys) |
| `deepseek_api_base` | Optional, defaults to `https://api.deepseek.com/v1`. Set to a third-party proxy if needed |
| `enable_thinking` | Enables DeepSeek V4 thinking mode. Web console renders the reasoning trace in real time; IM channels still benefit from higher answer quality |
| `reasoning_effort` | `high` (default) or `max`. Recommended `max` together with `deepseek-v4-pro` for complex agent tasks. Only takes effect when `enable_thinking` is `true` |

DeepSeek V4 supports a context window of up to **1,000,000** tokens. Use the `agent_max_context_tokens` config to control how much CowAgent sends to the model — raise it when you run on very long documents.

Apply changes with `cow restart` (or `./run.sh restart`).

#### 3. Get Started

Open the Web console to start chatting with the agent. The console streams reasoning, tool calls, and the final answer in real time, and lets you manage skills, memory, and the knowledge base from the left sidebar.

To use CowAgent from a chat app instead of the Web UI, configure a messaging channel on the **Channels** page. The same DeepSeek model serves every channel.

For deeper configuration see the [CowAgent docs](https://docs.cowagent.ai/) and the [DeepSeek model page](https://docs.cowagent.ai/models/deepseek).
