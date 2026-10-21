[English](./astorm_agent.md) | [简体中文](./astorm_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with Astorm Agent

Astorm Agent is an open-source, local-first desktop AI agent built with Electron, Vue 3, and a Rust core. It combines DeepSeek V4 with file, shell, Git, browser, Office, and MCP tools inside a sandboxed desktop workspace.

- **GitHub:** <https://github.com/hxuxingy1212/astorm-desktop-electron>
- **Releases:** <https://github.com/hxuxingy1212/astorm-desktop-electron/releases>

#### 1. Install Astorm Agent

Download the latest macOS build from the [releases page](https://github.com/hxuxingy1212/astorm-desktop-electron/releases):

- **macOS 12+ on Apple Silicon (arm64):** open the `.dmg` and drag **Astorm Agent** into **Applications**.
- The public macOS build is signed with a Developer ID and notarized by Apple.

To build from source on macOS, Windows, or Linux, install Node.js 20.19+ (or 22.12+), pnpm 10, and Rust 1.85+, then run:

```bash
git clone https://github.com/hxuxingy1212/astorm-desktop-electron.git
cd astorm-desktop-electron
pnpm install
pnpm run dev
```

Native components are built for the host platform. Use `pnpm run build` for a production build.

#### 2. Configure the DeepSeek Provider

Get an [API key](https://platform.deepseek.com/api_keys) from the DeepSeek Platform.

1. Open **Settings → Model** and click **Add provider**.
2. Set **Name** to `DeepSeek`.
3. Set **Base URL** to `https://api.deepseek.com`.
4. Set **API format** to **Chat Completions (/chat/completions)**.
5. Paste your **API Key**.
6. Click **Add model** and add:
   - `deepseek-v4-pro` — strongest reasoning, text-only, 1M context.
   - `deepseek-flash` — faster and lower-cost, vision-capable, 1M context.
7. Click **Save**. The first provider and its first model become the default; drag the handles to reorder providers or models.

> **About the Test button:** Astorm's **Test** button sends a text + image prompt to verify both instruction following and image recognition. `deepseek-v4-pro` is text-only, so the test can report that vision is unsupported even though text chat works. Use `deepseek-flash` if you want the test to pass, or skip the test for Pro.

> **Model naming:** DeepSeek's current pricing page lists the Flash model as `deepseek-flash`. The older `deepseek-v4-flash` name is still accepted as a legacy alias; use `deepseek-flash` for new configurations.

#### 3. Start Chatting

1. Create a new chat and choose a workspace folder.
2. At the bottom of the chat input, click the model chip (it shows the current model and reasoning effort).
3. Choose **DeepSeek → `deepseek-v4-pro`** (or `deepseek-flash`).
4. Choose **Reasoning effort → Max** (Astorm 0.1.1+; older versions cap at High).
5. Send a prompt. Astorm streams the answer, shows the reasoning steps, and asks for approval before sensitive file, shell, or network operations.

DeepSeek V4 supports a **1 million token** context window, so long documents and multi-file tasks can be handled without a separate context-window setting. Astorm's conversation summarization and compaction thresholds can be adjusted under **Settings → Session** if you want to tune long-running chats.

#### 4. Reasoning Effort and Model Choice

Astorm exposes five reasoning levels: **None**, **Low**, **Medium**, **High**, and **Max**. It sends the selected level as DeepSeek's `reasoning_effort` field. **Max** maps to `reasoning_effort: "max"` and is available in Astorm **0.1.1 or later**; on older versions, the highest level is High.

- Use **`deepseek-v4-pro` + Max** for coding, planning, and complex tool use.
- Use **`deepseek-flash`** for faster or lower-cost chats that need vision.

Pricing changes frequently, so this guide does not embed a price table. See the official [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing).

#### 5. Troubleshooting

| Symptom | Fix |
| --- | --- |
| `401 Unauthorized` | Check the API key and make sure it belongs to the selected provider. |
| `404` or `Model Not Found` | Use exactly `deepseek-v4-pro` or `deepseek-flash`; the Base URL must be `https://api.deepseek.com` without `/chat/completions`. |
| The **Test** button reports unsupported vision | `deepseek-v4-pro` is text-only. Text chat still works; use `deepseek-flash` for image tasks or skip the test. |
| `reasoning_effort` is rejected | Use **None**, **Low**, **Medium**, **High**, or **Max**. Max requires Astorm 0.1.1 or later; older versions cap at High. |
| macOS says the app is damaged | Verify the notarized build with `spctl -a -vvv --type execute "/Applications/Astorm Agent.app"` and download it from the official releases page. |

#### 6. Going Further

Astorm Agent also includes:

- **Sandboxed tools** — file operations, shell, Git, and network access with approval and audit logs.
- **Built-in browser** — let DeepSeek navigate, click, and extract content from pages.
- **Office and email** — create or edit Word, Excel, PowerPoint, and PDF files, and manage IMAP/SMTP accounts.
- **MCP and plugins** — connect external tools and extend the UI.
- **Local-first data** — conversations, workspaces, and API keys stay on your machine.
