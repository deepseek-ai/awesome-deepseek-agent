[English](./tidecode.md) | [简体中文](./tidecode.zh-CN.md) · [← Back](../README.md)

# Integrate with TideCode

[TideCode](https://github.com/ceciliomichael/TideCode) is a desktop AI workspace for efficient software development. It brings conversations, project files, an editor, terminal, planning, diffs, Git/GitHub, MCP, and reusable skills into one focused workspace.

## 1. Install TideCode

Download the latest release from the [TideCode releases page](https://github.com/ceciliomichael/TideCode/releases).

Available desktop builds include:

- Windows (`.exe` installer)
- macOS (`.dmg` installer)
- Linux (`.AppImage`)

Open TideCode after installation and choose the project folder you want to work on.

## 2. Configure the DeepSeek provider

Get a [DeepSeek API key](https://platform.deepseek.com/api_keys), then:

1. Open **Settings → Providers**.
2. Select **DeepSeek** and click **Set up DeepSeek**.
3. Paste your API key and choose **Save provider**.

TideCode uses DeepSeek's OpenAI-compatible API at `https://api.deepseek.com` for the built-in DeepSeek provider, so no base URL change is required.

## 3. Choose a DeepSeek V4 model

Open **Settings → Models** and make sure one or both of these models are enabled:

- `deepseek-v4-pro` — the strongest choice for complex coding and multi-step work.
- `deepseek-v4-flash` — a faster choice for everyday iteration.

TideCode uses the current DeepSeek V4 model IDs directly. Use the model IDs listed above when configuring a provider or saved model.

## 4. Configure context and reasoning

Open **Settings → Configuration** and select your DeepSeek model for the tasks you want to run:

- **Agent mode model** for implementation work and tool use.
- **Plan mode model** for breaking work into an implementation plan.
- **Summarization** for compacting longer conversations.
- **Git commit and pull request** for source-control summaries.

DeepSeek V4 supports up to a **1,000,000-token context window**. TideCode exposes a `1,000,000 tokens` context budget in the same Configuration panel. Select it when working with large repositories, while keeping automatic compaction enabled to manage long-running conversations.

When a DeepSeek model is active, use the reasoning-effort control in the chat input. Choose **High** for the strongest supported reasoning setting, or **None** when thinking is not needed. TideCode translates this selection into DeepSeek's `thinking` and `reasoning_effort` request fields.

## 5. Start your first DeepSeek session

1. Open or create a project workspace.
2. Start a conversation and select **Agent** or **Plan** mode.
3. Select **DeepSeek V4 Pro** or **DeepSeek V4 Flash** from the model selector.
4. Ask TideCode to inspect the project, explain a change, create a plan, or implement a small improvement.

TideCode keeps the proposed work visible through file changes and diffs. Review changes before committing them, and use the integrated terminal, Git tools, MCP servers, or skills when the project requires them.

Your API key is stored locally by TideCode. Review DeepSeek's terms and data-handling policies before sending sensitive project content to the service.
