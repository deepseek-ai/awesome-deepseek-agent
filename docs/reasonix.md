[English](./reasonix.md) | [简体中文](./reasonix.zh-CN.md) · [← Back](../README.md)

# Integrate with Reasonix

Reasonix is a DeepSeek-native coding agent that runs in the terminal. It's designed around DeepSeek's API directly — cache-first loop, flash-first cost control, automatic tool-call repair — and talks to `api.deepseek.com` without a translation shim.

#### 1. Install Node.js

- Install [Node.js](https://nodejs.org/en/download/) 20.10+.
- Windows users need to install [Git for Windows](https://git-scm.com/download/win).

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). The first run of Reasonix prompts for it via a built-in wizard and persists it to `~/.reasonix/config.json` — no environment variable needed.

#### 3. Enter the project directory and run `npx reasonix code` to get started.

```
cd /path/to/my-project
npx reasonix code
```

No global install required. By default Reasonix uses **DeepSeek-V4-Flash** for cost-efficient iteration. Type `/pro` inside the TUI to arm **DeepSeek-V4-Pro** for the next turn, or `/preset max` to use Pro for the whole session. Run `/help` for the full slash-command reference.

<div align="center">
<img src="https://raw.githubusercontent.com/esengine/reasonix/main/docs/logo.svg" width='640' />
</div>
