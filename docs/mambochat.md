[English](./mambochat.md) | [简体中文](./mambochat.zh-CN.md) · [← Back](../README.md)

# Integrate with MamboChat

**MamboChat** is an open-source web harness platform supporting Linux/Windows deployment. It integrates multiple service provider APIs for synchronized access from desktop and mobile browsers. The built-in **Mambo Agent** can handle complex tasks such as file read/write, command execution, and nested sub-agent calls, and also supports RAG knowledge bases, MCP tools, and Skill packs.

- **GitHub:** <https://github.com/RAmenLch/mambochat>
- **Deployment:** Docker Compose / Windows desktop client / source code

#### 1. Prepare MamboChat and a DeepSeek API Key

Deploy or launch MamboChat in one of the following ways:

- **Docker deployment**:

  ```bash
  git clone https://github.com/RAmenLch/mambochat.git
  cd mambochat
  docker compose up -d --build
  ```

  Then visit `http://localhost:24911`.

- **Windows desktop client**: download the latest installer (`MamboChat-Setup-x.x.x.exe`) from the [Releases](https://github.com/RAmenLch/mambochat/releases) page, run the wizard, and launch from the desktop shortcut. The installer bundles the complete Python runtime, frontend assets, and backend code, so no manual Python setup is needed.

Then create an API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Add the DeepSeek Provider

1. Click the **Settings** button (gear icon) at the bottom-left corner to open the system settings page.
2. In the **Provider Management** section, click **Add Provider** and select the built-in **DeepSeek** preset (API Host is auto-filled as `https://api.deepseek.com/v1` with the DeepSeek Native worker type).
3. Paste your DeepSeek API Key into the **API Key** field and save.

> **Automatic model capability detection**: MamboChat ships with DeepSeek model presets. When you connect the `api.deepseek.com` host, model capabilities (context length, thinking mode, etc.) are detected automatically — no manual configuration required.

![Configure the DeepSeek provider](./assets/mambochat_provider.png)  

#### 3. Fetch and Confirm the DeepSeek V4 Models

1. In the provider details, click **Fetch Models** to pull the model list from DeepSeek.
2. Confirm the list includes **`deepseek-v4-pro`** and **`deepseek-v4-flash`** (plus the experimental vision model `deepseek-v4-flash-vision-exp`).
3. The model list shows a **Context** column — DeepSeek V4 models are preset with a **1M token context window** (`context_length=1_000_000`, max output `384_000` tokens), so no extra setup is needed.

#### 4. Start a Conversation

1. Right-click in the session list on the left and choose **New Session**.
2. Click the **Settings** icon in the toolbar above the input area, then select a model for the session: choose **DeepSeek V4 Pro** for coding, long-horizon planning, and agent workflows, or **DeepSeek V4 Flash** for lower-latency everyday chat.
3. Send a message to start the conversation.

#### 5. Configure Thinking Mode (Reasoning Effort)

DeepSeek V4 thinking mode is configured via **dynamic parameters** (enabled in session settings or in the Agent editor's model configuration):

- **Thinking Type (DeepSeek)**: `enabled` / `disabled`, default `enabled`. When enabled, the model performs chain-of-thought reasoning before producing the final answer.
- **Reasoning Effort (DeepSeek)**: `high` (regular deep thinking) / `max` (strongest reasoning, best for complex agent scenarios). Keep the default `high` for everyday use; switch to **`max`** for difficult coding, planning, and multi-step agent tasks.

![Configure DeepSeek dynamic parameters](./assets/mambochat_agent_modelParameters.png)  

#### 6. Going Further: Mambo Agent / MCP / Knowledge Base

The built-in agent capabilities all run on DeepSeek V4:

- **Mambo Agent**: file read/write, command execution, nested sub-agents, AI safety pre-review, long-term memory, task loops, and more.
- **MCP support**: mount MCP servers onto an agent to extend tool capabilities (with Human-in-the-Loop review support).
- **Local knowledge base (RAG)**: upload Markdown/TXT/PDF/Word documents, vectorize them, mount them to a session, and let the AI retrieve answers automatically.

![Configure DeepSeek in Mambo Agent](./assets/mambochat_agent.png)  
See the [MamboChat tutorial](https://github.com/RAmenLch/mambochat/blob/master/doc/Tutorial_EN.md) for full details.

#### Troubleshooting

- `401` or authentication errors: recheck the API Key and make sure it is pasted into the **API Key** field.
- V4 models not found: click **Fetch Models** to refresh the model list and confirm the enabled model ids are `deepseek-v4-pro` / `deepseek-v4-flash`.
- Thinking parameters missing: make sure the current model is **DeepSeek V4 Pro** or **DeepSeek V4 Flash**, and enable Thinking Type / Reasoning Effort under **dynamic parameters** in session settings.
- Need the 1M context window: DeepSeek V4 models come with a 1M context preset — no manual setting required; you can verify it in the **Context** column of the model list.
