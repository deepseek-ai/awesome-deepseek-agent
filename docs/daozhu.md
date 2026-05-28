[English](./daozhu.md) | [简体中文](./daozhu.zh-CN.md) · [← Back](../README.md)

# Integrate with DaoZhu

DaoZhu (岛主) is an open-source, local-first personal AI platform. Its standout feature is **Stick-Figure Theater** — give DeepSeek a one-line premise and it writes a full script, then CSS-animated stick figures perform it automatically.

Beyond the theater, DaoZhu manages isolated "workspaces" (todo lists, accounting, forums, or anything you describe) — all data stays on your machine.

- GitHub: <https://github.com/wengshirui/DaoZhu>
- Gitee: <https://gitee.com/yumen2278/DaoZhu>

## 1. Install DaoZhu

**Option A — Download & run (Windows, recommended):**

Download the latest release from [Gitee Releases](https://gitee.com/yumen2278/DaoZhu/releases), unzip, and double-click `岛主DaoZhu.exe`. It bundles Git and uv — no prerequisites needed.

**Option B — Developer setup:**

```bash
git clone https://github.com/wengshirui/DaoZhu.git
cd DaoZhu
uv venv .venv --python 3.11
# Windows
.venv\Scripts\activate
# Linux / macOS
# source .venv/bin/activate
uv pip install -e .
python daozhu_main.py
```

## 2. Configure DeepSeek

On first launch the browser opens an onboarding page. Select **DeepSeek** as the provider and paste your [DeepSeek API key](https://platform.deepseek.com/api_keys).

If you've already completed onboarding, open **Settings** (gear icon) and update:

| Field | Value |
|-------|-------|
| Provider | DeepSeek |
| Model | `deepseek-v4-pro` (or `deepseek-v4-flash` for lower cost) |
| API Key | Your DeepSeek API key |

DaoZhu uses the OpenAI-compatible endpoint at `https://api.deepseek.com/v1`. DeepSeek V4 models support up to **1 million tokens** of context.

## 3. Try Stick-Figure Theater

In the chat panel, type something like:

```
演一个火柴人剧场：小明迟到了，被老板追着跑
```

DeepSeek will write a multi-scene script with stage directions, then the built-in theater renders CSS-animated stick figures performing the story — no video tools required.

## 4. Get Started

Once configured, you can chat with the AI assistant to:

- Create new workspaces: *"帮我建一个读书笔记工作区"*
- Manage tasks: *"添加一个待办：明天下午开会"*
- Generate stick-figure animations from any story premise
- Query and operate workspace data via natural language

The platform runs at `http://localhost:7788` by default.
