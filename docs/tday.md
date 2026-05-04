[English](./tday.md) | [简体中文](./tday.zh-CN.md) · [← Back](../README.md)

# Integrate with Tday

[Tday](https://github.com/unbug/tday) is a desktop launcher that runs every coding-agent harness (Pi, Claude Code, Codex, OpenCode, …) inside browser-style tabs, with one shared provider config, auto-discovered local inference servers, unified long-term memory, and cross-agent token analytics. DeepSeek is a first-class built-in provider.

<a href="https://github.com/unbug/tday/releases"><img src="https://img.shields.io/badge/release-latest-blue"></a>

<p>
  <a href="https://x.com/i/status/2049935301808935356">
    <img src="https://github.com/user-attachments/assets/ba6c8041-173f-44bb-90d6-cd72071260df">
  </a>
</p>

<p>
  <img src="https://github.com/user-attachments/assets/c196629b-5ee4-46dd-b1e3-d0ba86ab66b9">
  <img src="https://github.com/user-attachments/assets/27bf23af-a5f6-4457-8cc7-7f6085829733">
</p>

<p>
  <img src="https://github.com/user-attachments/assets/9dc6b149-80d4-4175-839a-3102960f2457">
  <img src="https://github.com/user-attachments/assets/4990e941-0b65-4d25-9d3e-b46e3dd1f67e">
</p>

<p>
  <img src="https://github.com/user-attachments/assets/2512a05f-e373-469f-859c-16b745da82a4">
  <img src="https://github.com/user-attachments/assets/01c3ef52-3080-4d73-811d-0cb7759d275d">
</p>

#### 1. Install Tday

Download the latest release for your platform from the [Tday Releases](https://github.com/unbug/tday/releases/latest) page:

- **macOS** — `Tday-<version>-mac-arm64.dmg` (Apple Silicon) or `Tday-<version>-mac-x64.dmg` (Intel)
- **Windows** — `Tday-<version>-win-x64.exe`
- **Linux** — `Tday-<version>-linux-x86_64.AppImage` or `Tday-<version>-linux-x64.tar.gz`

Or build from source:

```bash
git clone https://github.com/unbug/tday.git
cd tday
pnpm install
pnpm build:core   # builds the Rust tday-core binary
pnpm dev          # launches the desktop app
```

> **Prerequisites for source builds:** Node.js ≥ 20, pnpm ≥ 9, Rust ≥ 1.78.

Tday bundles adapters for `pi`, `claude-code`, `codex`, and `opencode`. Install whichever harness(es) you plan to use globally via `npm i -g`, e.g.:

```bash
npm install -g @mariozechner/pi-coding-agent
npm install -g @anthropic-ai/claude-code
npm install -g @openai/codex
npm install -g opencode-ai
```

#### 2. Configure the DeepSeek Provider

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Option A — Use the Settings UI (recommended)**

1. Launch Tday.
2. Open **Settings → Providers** and click **+ Add provider**.
3. From the vendor picker, choose **DeepSeek**.
4. Fill in:
   - **Base URL**: `https://api.deepseek.com` (the default OpenAI-compatible endpoint; do not append `/v1`)
   - **API Key**: paste your DeepSeek API Key
   - **Model**: pick from the latest-models dropdown (e.g. `deepseek-v4-pro` or `deepseek-v4-flash`) or type a model id
5. (Optional) Toggle **Use this provider/model for all agents** to share the same DeepSeek config across every harness you launch.
6. Save.

**Option B — Edit `~/.tday/providers.json` directly**

```json
{
  "providers": {
    "deepseek": {
      "vendor": "deepseek",
      "baseUrl": "https://api.deepseek.com",
      "apiKey": "<your DeepSeek API Key>",
      "models": [
        { "id": "deepseek-v4-pro",   "name": "DeepSeek V4 Pro" },
        { "id": "deepseek-v4-flash", "name": "DeepSeek V4 Flash" }
      ]
    }
  },
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro"
}
```

Restart Tday after editing the file.

#### 3. Open a Tab and Start Coding

1. Press **Cmd+T** (macOS) / **Ctrl+T** (Windows / Linux) to open a new agent tab, or click **+** in the tab bar.
2. From the dropdown, pick the harness you want — **Pi**, **Claude Code**, **Codex**, or **OpenCode**.
3. Set the working directory for the tab (browse or paste a path, then press **Enter** to commit).
4. Tday spawns the agent in a real PTY with your DeepSeek provider injected via env vars and the matching CLI flag, so the agent uses DeepSeek instead of its own default provider.
5. Inside the agent, switch models any time with `/model` (or whatever shortcut your chosen harness exposes) and pick `deepseek-v4-pro` for the strongest reasoning or `deepseek-v4-flash` for faster, cheaper turns.

> **Tip:** Open multiple tabs side by side — e.g. Pi on `~/projects/api`, Claude Code on `~/projects/web` — all sharing the same DeepSeek key and model. Tabs and their working directories persist across restarts.

For more details (architecture, roadmap, local-inference autodetect, token analytics, long-term memory), see the [Tday README](https://github.com/unbug/tday#readme).
