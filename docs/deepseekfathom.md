[English](./deepseekfathom.md) | [简体中文](./deepseekfathom.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeekFathom

DeepSeekFathom is an open-source, DeepSeek-first coding agent with a Windows desktop app and a cross-platform CLI. It includes local coding tools, resumable sessions, permission and thinking controls, MCP, plugins, Hooks, and Agent Skills.

- **GitHub:** <https://github.com/ffffff233/DeepSeekFathom>

#### 1. Install DeepSeekFathom

**Windows desktop:** download and run the installer from the GitHub release:

- [DeepSeekFathom-0.1.17-Setup.exe](https://github.com/ffffff233/DeepSeekFathom/releases/download/desktop-v0.1.17/DeepSeekFathom-0.1.17-Setup.exe)

The per-user installer adds DeepSeekFathom to the desktop and Start menu. Python is not required for this option.

**CLI:** install Python 3.11 or later, then install the tagged release:

```sh
# Windows PowerShell or Command Prompt
py -3 -m pip install --upgrade https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz

# Linux or macOS
python3 -m pip install --upgrade https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz
```

Verify the CLI installation:

```sh
deepseekfathom version
```

#### 2. Configure the DeepSeek API

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then save it with the official endpoint and a current model:

```sh
deepseekfathom config set --base-url https://api.deepseek.com --api-key sk-... --model deepseek-v4-pro
deepseekfathom doctor --live
```

Use `deepseek-v4-flash` instead when you prefer faster responses. In the desktop app, open **Settings**, select the DeepSeek provider, and enter the same Base URL, API key, and model.

DeepSeekFathom budgets both DeepSeek V4 models against their **1,000,000-token context window**. Its five public thinking levels map to DeepSeek's native `reasoning_effort` values:

| DeepSeekFathom level | Upstream `reasoning_effort` |
|---|---|
| `fast` | `low` |
| `balanced` | `medium` |
| `deep` | `high` |
| `ultra` | `xhigh` |
| `max` | `max` |

The `max` level uses real upstream support with `deepseek-v4-pro`: DeepSeekFathom sends `reasoning_effort: "max"` to DeepSeek unchanged.

#### 3. Enter a project directory and start

```sh
cd /path/to/my-project
deepseekfathom start --mode agent --think max
```

Type `/` to open the command palette. Use `/model`, `/think`, and `/mode` to change the active model, thinking level, and permission mode. Conversations are saved automatically and can be reopened with `deepseekfathom sessions list` and `deepseekfathom sessions resume <SESSION_ID>`.

To launch the desktop app from a Python installation, install the desktop extra and start it:

```sh
python3 -m pip install --upgrade "deepseekfathom[desktop] @ https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz"
deepseekfathom-desktop
```

Windows installer users can launch **DeepSeekFathom** directly from the desktop or Start menu.
