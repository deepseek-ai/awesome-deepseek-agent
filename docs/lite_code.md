[English](./lite_code.md) | [简体中文](./lite_code.zh-CN.md) · [← Back](../README.md)

# Integrate with lite-code

lite-code is an open-source desktop Code Agent with a hand-written Python kernel, a React UI, and an Electron shell — no LangChain or other high-level frameworks. It ships with 20 built-in tools (file I/O, Ripgrep search, Tree-sitter outlines, precise edits, sandboxed shell, Git, sub-agents, skills), a three-level security model with human-in-the-loop approvals, and prompt-cache-first context management. DeepSeek is the **default built-in provider**.

- **GitHub:** <https://github.com/LaynePeng/lite-code>

#### 1. Install lite-code

Download the installer for your platform from the [Releases](https://github.com/LaynePeng/lite-code/releases) page:

- macOS (Apple Silicon): `lite-code-<version>-arm64.dmg`
- Windows: `lite-code Setup <version>.exe`

> **Note:** The macOS build is unsigned. If macOS says "cannot verify the developer", right-click the app and choose **Open**; if it says "damaged", run `xattr -dr com.apple.quarantine "/Applications/lite-code.app"` and try again.

You can also run it from source (requires Python 3.11+ and Node 18+):

```bash
git clone https://github.com/LaynePeng/lite-code.git
cd lite-code
python3 -m venv .venv
.venv/bin/pip install -e .    # Windows: .venv\Scripts\pip install -e .
npm install
npm run dev                   # dev mode: Python core + Vite + Electron window
```

#### 2. Configure the DeepSeek Provider

DeepSeek is enabled out of the box — no base URL setup needed.

1. Launch lite-code and open **Settings**.
2. Select the **DeepSeek** provider (it is the default active provider).
3. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field. The key is stored locally in `~/.lite-code/config.json`.

Alternatively, set the `DEEPSEEK_API_KEY` environment variable before launching — lite-code picks it up automatically.

#### 3. Select a Model and Start Coding

In **Settings**, pick your model:

- **`deepseek-v4-flash`** — default, cost-efficient
- **`deepseek-v4-pro`** — strongest reasoning for complex tasks

Both models run with the full **1 million token** context window, resolved automatically (with a built-in metadata table as offline fallback) — no manual configuration required.

Open a project folder, and start chatting. Tool calls show up as approval cards — MEDIUM/HIGH-risk operations need your confirmation before running. lite-code tracks prompt-cache hit rate and context usage in the right panel, and compresses context automatically when it grows too large.
