[English](./limitcode.md) | [简体中文](./limitcode.zh-CN.md) · [← Back](../README.md)

# Integrate with Limitcode

Limitcode is a lightweight AI coding agent for Sublime Text — side-by-side streaming chat, multi-provider support, and a deliberately small, reviewable tool surface.

#### 1. Install Limitcode

Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`), run `Package Control: Install Package`, and search for `Limitcode`.

#### 2. Run and Configure

- Run `Limitcode: Setup Provider API Key` from the Command Palette<br/>
- Select the `deepseek` provider and paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys)<br/>
- Run `Limitcode: Change Model` and select `deepseek-v4-pro` (or `deepseek-v4-flash` for faster, cheaper responses)<br/>
- Run `Limitcode: Open Chat` and start asking

#### 3. Reasoning Effort

For the best coding experience, run `Limitcode: Set Reasoning Effort` and pick `high` — Limitcode's highest available level, mapped to `reasoning_effort` in the request body.

#### Context Window

DeepSeek-V4 models support up to **1 million tokens** of context. Limitcode does not expose a context-window setting; it relies on the model's supported context, so large files and long sessions work out of the box.

#### Notes

- The agent only reads and edits files you have open in a tab — open every file you want it to work on before sending a request.
- Optional: if the [LSP](https://packagecontrol.io/packages/LSP) package is installed, Limitcode uses its diagnostics after each edit so the agent can catch syntax and type errors automatically.
