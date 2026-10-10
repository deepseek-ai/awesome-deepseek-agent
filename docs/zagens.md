[English](./zagens.md) | [简体中文](./zagens.zh-CN.md) · [← Back](../README.md)

# Integrate with Zagens

Zagens is a **desktop agent harness** built around DeepSeek — a Tauri 2 UI with a local **runtime sidecar** that talks to `api.deepseek.com` directly. It supports **DeepSeek-V4-Pro** and **DeepSeek-V4-Flash** with the full **1M token** context window, plus tool use, MCP, skills, and session replay. A headless **`zagens`** CLI is available for scripting and automation; a **full-screen terminal TUI (`zagens-tui`) is in development and coming soon.**

- **GitHub:** https://github.com/didclawapp-ai/zagens

**Highlights:**

- **Long-horizon harness** — layered completion gates for multi-step coding tasks, so agents are less likely to stall or claim “done” too early.
- **Hallucination guard & verifiable output** — prompts require evidence-backed claims and explicit “not verified” labels when unsure; “done” means **tests and builds actually run**, and expected files are checked — not the model saying so on its own.
- **Desktop-native control plane** — per-turn **session replay**, diff preview, tool approval UI, embedded terminal, and tray notifications.
- **Code + Office in one runtime** — coding and spreadsheet/document workflows (`write_office`) share the same sidecar — no separate toolchain.

#### 1. Install Zagens

Pick one:

```sh
# Windows desktop (recommended): download from GitHub Releases
#   https://github.com/didclawapp-ai/zagens/releases

# CLI (Windows / macOS / Linux — requires Rust stable)
cargo install zagens-cli --locked --bin zagens
```

Verify the CLI:

```sh
zagens --version
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). On first desktop launch, enter it in **Settings** — it is saved to `~/.zagens/config.toml`. For the CLI, run `zagens login` or set `DEEPSEEK_API_KEY`.

#### 3. Open your project and start

**Desktop:** Launch Zagens, pick a workspace folder, and send your first prompt.

**CLI:**

```sh
cd /path/to/my-project
zagens exec "Summarize this repo's README.md in three bullet points"
```

Zagens defaults to **DeepSeek-V4-Pro** with `reasoning_effort = max` for deep V4 reasoning. Switch to **Flash** in Settings for lower cost, or adjust reasoning effort (`max` / `high`). Check connectivity with `zagens doctor`; expose a local HTTP API with `zagens serve --http`.

<div align="center">
<img src="https://raw.githubusercontent.com/didclawapp-ai/zagens/master/assets/screenshot.png" width="800" />
</div>
