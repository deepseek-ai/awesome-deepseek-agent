[English](./dotcraft.md) | [简体中文](./dotcraft.zh-CN.md) · [← Back](../README.md)

# Integrate with DotCraft

DotCraft is a project-scoped .NET/C# Agent Harness. Desktop, TUI, CLI, bots, and automations share the same workspace sessions, skills, tools, approvals, and observability surface.

- **GitHub:** <https://github.com/DotHarness/dotcraft>
- **Documentation:** <https://dotharness.github.io/dotcraft/en/>

DotCraft connects to DeepSeek through the OpenAI-compatible Chat Completions API. Its Deep Thinking adapter preserves `reasoning_content` during tool-call rounds, and DeepSeek V4 model context windows can be configured as 1,000,000 tokens.

#### 1. Install DotCraft

Download the latest DotCraft Desktop release from:

```text
https://github.com/DotHarness/dotcraft/releases
```

Install the package for your operating system and launch DotCraft Desktop.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeek in Desktop

Open a real project folder as your DotCraft workspace, then open **Settings -> Model Providers** and create a provider:

| Field | Value |
|-------|-------|
| Provider id | `deepseek` |
| Display name | `DeepSeek` |
| Protocol | `openai` |
| Endpoint | `https://api.deepseek.com/v1` |
| API Key | Your DeepSeek API key |
| Model | `deepseek-v4-pro` |
| Reasoning | Enabled |
| Reasoning effort | Extra High |
| Context window | `1000000` tokens |

Use `deepseek-v4-flash` as the lighter model option when you prefer lower latency or cost.

DotCraft's built-in Deep Thinking adapter applies to DeepSeek models and DeepSeek endpoints automatically. During tool-call conversations, it round-trips the model's reasoning metadata with assistant tool calls so thinking mode remains compatible with agent workflows.

#### 4. First Run

In DotCraft Desktop:

1. Open the project workspace.
2. Create a new session.
3. Select the DeepSeek provider and `deepseek-v4-pro` model if they are not already selected.
4. Send a repository-understanding request:

```text
Read this repository's README and docs, then tell me how to start the project.
```

The session should stream an answer through DeepSeek V4 Pro. Reasoning content is displayed according to DotCraft's default reasoning display behavior.

#### Other DotCraft Entry Points

After Desktop setup, the same workspace configuration can be reused by other DotCraft entry points:

| Entry point | Use case |
|-------------|----------|
| Desktop | Graphical workspace, provider setup, sessions, traces, approvals |
| TUI | Full terminal interface connected through DotCraft AppServer |
| CLI | One-shot project tasks and local automation commands |
| ACP | Editor and IDE integrations through Agent Client Protocol |
| Bots and automations | Shared workspace sessions for chat platforms and scheduled tasks |

#### Resources

- [DotCraft](https://github.com/DotHarness/dotcraft)
- [DotCraft Getting Started](https://dotharness.github.io/dotcraft/en/getting-started)
- [DotCraft Configuration Guide](https://dotharness.github.io/dotcraft/en/config_guide)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
