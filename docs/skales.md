[English](./skales.md) | [简体中文](./skales.zh-CN.md) · [← Back](../README.md)

# Integrate with Skales

Skales is a local-first AI desktop agent for Windows, macOS, and Linux, with companion apps for iOS and Android. It installs like an ordinary application — no Docker, no terminal, no cloud account — and gives the model 197 built-in tools: files, shell, browser and computer control, calendar and mail, a media studio, and a voice agent, in 12 interface languages.

- **GitHub:** <https://github.com/skalesapp/skales>
- **Website:** <https://skales.app>

#### 1. Install Skales

Download the installer for your platform from [skales.app](https://skales.app) or the [GitHub releases page](https://github.com/skalesapp/skales/releases/latest).

Available builds:

- Windows (`.exe`)
- macOS (`.dmg` — Intel and Apple Silicon)
- Linux (`.AppImage` / `.deb`)

#### 2. Configure the DeepSeek Provider

DeepSeek is a built-in, first-class provider in Skales with its own tuned profile.

1. Open **Settings → AI Providers** and scroll to the **DeepSeek** card.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API Key** field. The endpoint is preconfigured to `https://api.deepseek.com`.
3. Pick the model: **DeepSeek V4 Flash (Recommended)** for everyday agent work, or **DeepSeek V4 Pro (Reasoning, 1M ctx)** for hard multi-step tasks. Both map to `deepseek-v4-flash` and `deepseek-v4-pro` on the wire, and the 1M-token context is used automatically.
4. Click **Test Connection**, then **Set Active**.

<div align="center">
<img src="./assets/skales_provider.png" width="720" border="1" />
</div>

#### 3. Reasoning effort

Skales forwards `reasoning_effort` to DeepSeek V4. The **Effort** dial next to the chat input controls it per conversation — set it to **max** for the hardest tasks and leave thinking on; Skales never disables the model's reasoning.

#### 4. Going further

- **Goals** run multi-step tasks in the background and report back when done.
- The **Code window** binds a chat to a project folder: diffs, branches, commits and test runs, driven by DeepSeek.
- **Studio · Flow** turns prompts into decks, documents, prototypes and motion clips, exported as PDF, PPTX, DOCX, SCORM or MP4.
- **Iris Orbit** is a voice surface: talk to the same DeepSeek-driven agent instead of typing.
