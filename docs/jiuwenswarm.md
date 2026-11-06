[English](./jiuwenswarm.md) | [简体中文](./jiuwenswarm.zh-CN.md) · [← Back](../README.md)

# Integrate with JiuwenSwarm

JiuwenSwarm is an open-source (Apache-2.0) multi-agent workbench built on [openJiuwen](https://openjiuwen.com/en/). In cluster mode a **Leader** agent breaks a complex task into stages and assembles a team of specialist **Teammates**; Skills are reused, shared through the Swarm Skills Hub, and improved from execution feedback. The same agent is reachable from the browser, a terminal TUI, or the chat apps you already use (Feishu, DingTalk, WeCom, WeChat and Xiaoyi; Telegram, Discord, Slack and WhatsApp). It supports OpenAI-compatible model providers, including DeepSeek.

#### 1. Install JiuwenSwarm

##### Prerequisites

- Python 3.11–3.13 for the `workswarm` PyPI package (`>=3.11,<3.14`); a source install also supports 3.14.
- Node.js 18+ only for source installs (front-end build) and 20+ for browser automation; normal chat does not need it.

##### pip install

```bash
# Create and activate a virtual environment
python -m venv jiuwenswarm-env
source jiuwenswarm-env/bin/activate   # Windows: jiuwenswarm-env\Scripts\activate

# Install JiuwenSwarm (PyPI package: workswarm)
pip install workswarm

# First-time initialization
jiuwenswarm-init

# Start the service
jiuwenswarm-start
```

> The PyPI package is `workswarm` (renamed from `jiuwenswarm`); the CLI commands (`jiuwenswarm-init`, `jiuwenswarm-start`, and the `jiuwenswarm chat` subcommand) and the `~/.jiuwenswarm` data directory keep the JiuwenSwarm name.

##### Desktop app

Prebuilt installers are also available for Windows 10/11 and macOS 11+ (Apple Silicon only); on HarmonyOS PC, install from the official site <https://openjiuwen.com/en/jiuwenswarm>. After installing, launch it from the desktop and skip the `jiuwenswarm-*` commands above.

#### 2. Configure DeepSeek

1. Start JiuwenSwarm and open the Web UI (default <http://localhost:5173>).
2. In the left sidebar open **Settings → Models** (older builds: **More → Configuration**).
3. Add or edit the default model. Select **Model provider** first, then fill in:

| Field          | Value                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| Model provider | `DeepSeek` (built-in preset; choose **Custom** or `OpenAI` only if your build has no DeepSeek preset)         |
| Model name     | `deepseek-v4-pro` (best for complex multi-agent and coding tasks) or `deepseek-v4-flash` (faster and cheaper) |
| API Key        | Your [DeepSeek API key](https://platform.deepseek.com/api_keys)                                               |
| API URL        | `https://api.deepseek.com` — shown only for **Custom**; the DeepSeek preset already uses this endpoint. Do **not** append `/chat/completions` |

4. Mark the entry as the **Primary** (default) model, click **Test** to verify the connection, then confirm the dialog and save. Saving hot-reloads the configuration; a few changes trigger a service restart.

> Out of the box JiuwenSwarm uses a 256K context window and the provider's default reasoning effort. DeepSeek V4 supports 1M context and `max` effort — enable both in the next step.

#### 3. Enable 1M context and max thinking

DeepSeek V4 models support up to **1 million tokens** of context and a **`max`** reasoning effort. JiuwenSwarm does not infer either from the model name, so set them explicitly in `~/.jiuwenswarm/config/config.yaml` (created on first start; on Windows `%USERPROFILE%\.jiuwenswarm\config\config.yaml`).

Add the keys to the model entry marked `is_default: true`, and raise the context-engine budget to the same value:

```yaml
models:
  defaults:
    - model_id: mdl_default_primary   # keep the model_id already present in your file
      model_client_config:
        api_base: https://api.deepseek.com
        api_key: sk-your-deepseek-api-key
        model_name: deepseek-v4-pro
        client_provider: DeepSeek
      model_config_obj:
        temperature: 0.95
        reasoning_level: max        # DeepSeek V4 exposes off / low / high / max
        context_window: 1000000     # 1M tokens (256K is the built-in default)
      is_default: true
react:
  context_engine_config:
    context_window_tokens: 1000000
```

- `reasoning_level: max` is sent to DeepSeek V4 as reasoning effort `max`; `off`, `low` and `high` are the other supported levels. The model dialog under **Settings → Models → Edit model** exposes the same setting as **Reasoning**, so you can pick `max` there instead of editing YAML.
- `model_config_obj.context_window` declares the model's real window to the model layer, while `react.context_engine_config.context_window_tokens` is the budget used by JiuwenSwarm's context-compression engine (it falls back to 256K when unset and takes precedence over the per-model value). Set both so the 1M window is used by the model layer and by context compression; compression kicks in at 80% of the budget.

> If `jiuwenswarm-init` left `${API_BASE}` / `${API_KEY}` / `${MODEL_NAME}` placeholders in the file, replace them with literal values or export matching `API_BASE`, `API_KEY`, `MODEL_NAME` and `MODEL_PROVIDER` environment variables. Configurations saved from the Web UI are written with literal values.

Save the file — JiuwenSwarm watches it and reloads automatically. Restart the service if a change does not take effect.

#### 4. Start your first conversation

- **Web UI**: open the Web UI (default <http://localhost:5173>) and go to **Chat**. Pick the execution mode in the chat input area:
  - **Agent mode** — a single agent plans and executes; good for everyday Q&A and code generation.
  - **Cluster mode** — a Leader agent decomposes the task and coordinates specialist teammates; pick this for large, multi-step work.
- **Terminal TUI**: `jiuwenswarm chat "..."` for a one-off prompt, or `jiuwenswarm chat` for an interactive session. Use `/mode` to switch sub-modes (`agent.plan`, `agent.fast`, `code.normal`, `code.team`, `team`) and `/model` to switch models.
- **Chat apps**: enable a channel in the Web UI channel settings (or in `config.yaml` with `enabled: true` plus that platform's credentials) to talk to the same agent from Feishu, DingTalk, WeCom, WeChat, Xiaoyi, Telegram, Discord, Slack or WhatsApp. In group chats, @mention the bot.

Example prompt for cluster mode:

```text
Conduct an in-depth research on the new energy vehicle industry and generate an analysis report.
```

#### 5. Troubleshooting

- **Model test fails**: check that the API key is valid, the base URL is reachable, and `api_base` has no `/chat/completions` suffix; the model name and provider must match the endpoint.
- **Web UI not reachable**: check the service banner (`http://localhost:5173`; if the port is taken the launcher picks the next free port group and prints it) and `~/.jiuwenswarm/logs/` for errors.
- **Changes ignored**: save again from the Web UI or restart with `jiuwenswarm-start`; verify YAML indentation.
- **1M context or max effort not applied**: confirm the keys are on the entry marked `is_default: true`, then check `~/.jiuwenswarm/logs/` for configuration errors.
- **Context window stays at 256K**: an invalid `context_window` / `context_window_tokens` value is ignored silently — use a positive integer such as `1000000`.
- **Remote access**: run `FRONTEND_HOST=0.0.0.0 jiuwenswarm-start` to expose the Web UI, then open `http://<server-ip>:5173` from another machine.

Upstream references: [Install guide](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/InstallGuide.md) · [Configuration](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/Configuration.md) · [FAQ](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/FAQ.md)
