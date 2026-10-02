[English](./mindos_desktop.md) | [简体中文](./mindos_desktop.zh-CN.md) · [← Back](../README.md)

# Integrate with MindOS Desktop

MindOS Desktop is a free, local-first desktop AI coding assistant for Windows, powered by a built-in Codex engine. It runs DeepSeek-V4 models with a 1M-token context window and `Medium` / `High` / `Max` reasoning effort, and ships with approval workflows plus a built-in Git/PR pipeline.

- **GitHub:** <https://github.com/xxcr777/deepseek-mindos-desktop>

![MindOS Desktop main UI](./assets/mindos-main.png)

#### 1. Install MindOS Desktop

- Windows 10 / 11 (64-bit).
- Download the latest build from [GitHub Releases](https://github.com/xxcr777/deepseek-mindos-desktop/releases/latest):
  - `MindOS-Setup-<version>.exe` — installer, choose your install directory;
  - `MindOS-<version>-win.zip` — portable build, extract and run `MindOS.exe`.

The build is not code-signed, so Windows SmartScreen may show "Windows protected your PC" on first launch — click **More info → Run anyway** (first launch only).

#### 2. Connect DeepSeek

1. Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) (`sk-...`).
2. Open **Settings → Model**, find the **`deepseek v4.1 flash`** row and click **Connect**.

![Connect DeepSeek in MindOS Desktop](./assets/mindos-model-settings.png)

3. Paste the API key into the dialog. The API base URL field is optional and defaults to `https://api.deepseek.com/v1` (OpenAI-compatible) — leave it empty unless you use a custom endpoint.
4. Click **Connect & verify**, then pick the model in the chat input bar.

**Notes**

- DeepSeek-V4 supports up to 1M tokens of context; MindOS configures the engine with a **1,000,000-token context window** by default.
- The reasoning-effort selector in the chat input bar offers `Medium`, `High`, and `Max`; `Max` is fully supported and recommended for the hardest tasks.
- Everything runs locally: your code, chats and files are only sent to the DeepSeek (or other) API you configure.

#### 3. Create a project and start coding

1. Click **New project** on the home page and select your code folder (e.g. `D:\my-app`).
2. Wait until the title bar shows **● Ready**.
3. Describe the task, e.g. "fix the login button bug" — MindOS edits files, runs commands, and shows the changes as diff cards in the chat.

#### Approvals and Git workflow

- **Settings → Permission Center** chooses who approves the agent's actions: **Standard approval** (confirm each sensitive action), **AI review** (risk-based, trusted mode), or **Full trust** (sandboxed auto-run).
- The agent works in an **isolated worktree** by default, keeping your main checkout clean. Use the environment panel to **commit**, **push**, and **open a pull request** without leaving the app.
