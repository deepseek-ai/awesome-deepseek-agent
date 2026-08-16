[English](./deepseek-harness.md) | [简体中文](./deepseek-harness.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) is DeepSeek's open-source agent harness — "everything is a plugin", powered by [Cordis](https://github.com/cordiverse/cordis). It runs as a terminal CLI or a local Web UI and talks to DeepSeek V4 Pro / Flash out of the box. This guide covers installation, configuration, and first run.

#### 1. Install Requirements

- [Node.js](https://nodejs.org/en/download/) 18+.

Run dsh directly from npm (no global install needed):

```shell
npx @deepseek-ai/dsh web
```

The first run downloads the package, then starts the Web UI at `http://127.0.0.1:3080`.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure DeepSeek V4

dsh reads its model backend from environment variables. Add these to your shell profile (`~/.zshrc` / `~/.bashrc`):

```shell
export DEEPSEEK_API_KEY="sk-your-deepseek-api-key"
export DEEPSEEK_DEFAULT_MODEL="deepseek-v4-pro"
```

dsh defaults to DeepSeek's official API, so no base URL is required. DeepSeek V4 Pro / Flash support up to **1M tokens** of context, and V4 Pro supports multiple reasoning-effort levels (`max` and `high`) — keep it at `max` for the best coding experience.

#### 4. Run dsh

```shell
source ~/.zshrc
npx @deepseek-ai/dsh web
```

Open `http://127.0.0.1:3080` in your browser.

#### 5. First Run

Start a session and give it a task that reveals the model:

```text
Introduce yourself in one sentence and tell me your current model ID.
```

If the reply mentions `deepseek-v4-pro`, routing works.

#### Optional: third-party OpenAI-compatible endpoint

dsh is OpenAI-compatible, so you can point it at any OpenAI-format endpoint — for example a provider with a free DeepSeek V4 tier:

```shell
export DEEPSEEK_API_KEY="sk-teamo-your-key"
export DEEPSEEK_BASE_URL="https://api.teamorouter.com/v1"
export DEEPSEEK_DEFAULT_MODEL="deepseek-v4-pro-free"
```

This routes dsh to [TeamoRouter](https://teamorouter.com/docs/install-deepseek-harness), which offers `deepseek-v4-pro-free` / `deepseek-v4-flash-free` at 200 requests/day each (no payment info required).
