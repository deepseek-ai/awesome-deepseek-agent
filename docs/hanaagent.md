[English](./hanaagent.md) | [简体中文](./hanaagent.zh-CN.md) · [← Back](../README.md)

# Integrate with HanaAgent/OpenHanako

HanaAgent/OpenHanako is an open-source cross-platform personal AI agent with memory, personality, multi-agent collaboration, plugins, bridge integrations, sandboxed tools, and a graphical desktop experience. The desktop application is named **HanaAgent**, while the open-source project and repository remain **OpenHanako**.

HanaAgent/OpenHanako supports macOS, Windows, Linux, and a mobile PWA connected to the same HanaAgent Server.

#### DeepSeek-specific optimizations

- **Built-in DeepSeek path**: HanaAgent includes a DeepSeek provider preset and built-in metadata for `deepseek-v4-pro` and `deepseek-v4-flash`.
- **DeepSeek thinking mode**: HanaAgent maps its thinking selector to DeepSeek `high` and `max` effort levels, and keeps the required `reasoning_content` for tool-call rounds.
- **Cache-friendly prompt freezing**: HanaAgent keeps stable system instructions and tool definitions near the front of the prompt, and moves frequently changing information such as memory, workspace, and time toward the end. This helps repeated DeepSeek sessions reuse cached prefixes more reliably.
- **Auxiliary vision**: when the main DeepSeek model should stay in charge but an image needs to be understood first, HanaAgent can ask a separate vision model to look at the image and pass a concise visual note back to DeepSeek.

![HanaAgent running with DeepSeek V4 Pro](./assets/hanaagent-main-deepseek-v4-pro.png)

#### 1. Install HanaAgent

Download the latest desktop build from the [HanaAgent/OpenHanako releases page](https://github.com/liliMozi/openhanako/releases):

- **macOS**: download the `.dmg` package.
- **Windows**: download the `.exe` installer.
- **Linux**: download the `.AppImage` or `.deb` package.

After installation, launch HanaAgent and complete the onboarding wizard.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure the DeepSeek Provider

During onboarding, or later from **Settings → Models / Providers**, choose **DeepSeek** as the provider.

Use the following settings:

| Field | Value |
| ----- | ----- |
| Provider | `DeepSeek` |
| API type | `OpenAI Compatible` |
| Base URL | `https://api.deepseek.com` |
| API key | Your DeepSeek API key |

HanaAgent includes a built-in DeepSeek provider preset, so the base URL and API type are filled automatically when you choose DeepSeek.

#### 4. Select DeepSeek V4 Models

HanaAgent uses separate model slots so that different parts of the agent can use the right model for the job:

| HanaAgent model slot | Recommended DeepSeek model |
| -------------------- | -------------------------- |
| Chat model | `deepseek-v4-pro` |
| Utility model | `deepseek-v4-flash` |
| Utility large model | `deepseek-v4-pro` |

`deepseek-v4-pro` and `deepseek-v4-flash` both support a 1M-token context window and up to 384K output tokens. HanaAgent ships built-in metadata for these models, so the context window, output limit, reasoning capability, and max-effort support are available to the UI and runtime.

![DeepSeek provider, model slots, and auxiliary vision settings in HanaAgent](./assets/hanaagent-deepseek-provider-and-models.png)

#### 5. Enable DeepSeek Thinking Mode

DeepSeek V4 supports thinking mode and effort control. HanaAgent exposes this in the chat input bar through the thinking selector:

- **Auto**: use HanaAgent's session default.
- **High**: use DeepSeek `high` thinking effort.
- **XHigh**: use DeepSeek `max` thinking effort.

![DeepSeek max-effort thinking selector in HanaAgent](./assets/hanaagent-thinking-xhigh.png)

For agent tool calls, DeepSeek thinking mode requires `reasoning_content` to be preserved in later turns. HanaAgent handles this in its DeepSeek compatibility layer, so tool-using sessions can continue across multiple reasoning and tool-call rounds without losing the required thinking history.

#### 6. Optional: Use Auxiliary Vision

DeepSeek V4 Pro and Flash are strong text and reasoning models. When you want image understanding in HanaAgent, enable **Auxiliary Vision** and choose a separate vision-capable model in **Settings → Models**.

With auxiliary vision enabled, HanaAgent sends image attachments to the vision model first, then passes the extracted visual context back into DeepSeek as the main reasoning model. This lets you keep DeepSeek as the primary agent brain while still working with screenshots, documents, UI captures, and other image-based inputs.

![Auxiliary vision image understanding with DeepSeek as the main model](./assets/hanaagent-vision-bridge-chat.png)

#### 7. Start Using HanaAgent

Open a chat and ask HanaAgent to work with your project, files, desktop, or connected chat platforms.

Example first prompt:

```text
Use DeepSeek V4 Pro as your main reasoning model. Please inspect this project, summarize its structure, and suggest the next three improvements.
```

If you attached an image and enabled auxiliary vision, you can also ask:

```text
Look at this screenshot, explain what is happening, and use DeepSeek to reason about the next action.
```

#### Notes

- Use `deepseek-v4-pro` or `deepseek-v4-flash` for new configurations.
- Legacy V3 compatibility aliases should not be used for new HanaAgent setups.
- DeepSeek API details: [DeepSeek API Docs](https://api-docs.deepseek.com/).
- HanaAgent/OpenHanako repository: [liliMozi/openhanako](https://github.com/liliMozi/openhanako).
