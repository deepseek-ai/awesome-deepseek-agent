[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← Back](../README.md)

# Integrate with Pi

Pi (pi-mono) is a minimal, extensible terminal coding harness with built-in provider and model catalogs. Visit the official website at [pi.dev](https://pi.dev/).

#### 1. Install Pi

Use Pi's official installer:

- **Linux / macOS**

  ```bash
  curl -fsSL https://pi.dev/install.sh | sh
  ```

- **Windows (PowerShell)**

  ```powershell
  irm https://pi.dev/install.ps1 | iex
  ```

> **Windows note:** Pi uses a Bash shell for its shell tool. Install [Git for Windows](https://git-scm.com/download/win) or provide another Bash executable.

Verify the installation:

```bash
pi --version
```

#### 2. Configure the DeepSeek Provider

DeepSeek is a built-in API-key provider in Pi. You do not need to create or edit `models.json`.

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then start Pi in your project directory:

```bash
cd /path/to/my-project
pi
```

In Pi:

1. Run `/login`.
2. Select **Sign in with an API key**.
3. Search for and select **DeepSeek**.
4. Paste your DeepSeek API key and press Enter to save it.

Pi stores the credential locally and makes the DeepSeek models available automatically.

#### 3. Select a Model and Start Coding

Run `/model` (or press Ctrl+L), search for `deepseek`, and select a model.

Pi's built-in catalog currently includes `deepseek-v4-pro` and `deepseek-v4-flash`. Both support up to 1M tokens of context and 384K output tokens. For maximum reasoning on coding tasks, select `deepseek-v4-pro` and press Shift+Tab until the thinking level is `max`.

You are ready to start coding.

For further usage and configuration details, see the [Pi documentation](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent/docs).
