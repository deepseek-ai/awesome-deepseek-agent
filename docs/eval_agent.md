[English](./eval_agent.md) | [简体中文](./eval_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with Eval Agent

[Eval Agent](https://eval.zailink.space/) is an embedded-engineering agent system with built-in model routing and DeepSeek support through the OpenAI-compatible API. It orchestrates 17 specialist agents and 25 engineering tools in five workflows spanning schematic analysis, system architecture, firmware, compilation, flashing, serial and SWD debugging, testing, and documentation.

#### 1. Install Eval Agent

Open the [Eval Agent download page](https://eval.zailink.space/#downloads) and download the latest stable installer. Downloads are public and do not require an account.

The current public release is available for **Windows x64** as an `.exe` installer. Run the installer and launch Eval Agent. Sign in or create an Eval account if prompted.

#### 2. Get a DeepSeek API Key

Create an API Key in the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Keep it private; do not commit it to a project or paste it into prompts.

#### 3. Open Model Management

In the Eval Agent workspace:

1. Click the **gear icon** in the upper-right corner.
2. Select **Model** in the Settings sidebar.
3. Click **Manage Models** under **Models and Routing**.

![Open model management in Eval Agent settings](./assets/eval_agent_model_settings.zh-CN.png)

#### 4. Configure the DeepSeek Provider and Models

Find or add the **DeepSeek** provider, then configure it as follows:

| Provider field | Value |
| --- | --- |
| Provider name | `DeepSeek` |
| Protocol | OpenAI-compatible |
| API Base URL | `https://api.deepseek.com/v1` |
| API Key | Your DeepSeek API Key |
| Provider enabled | On |

Add and enable both current DeepSeek V4 models:

| Model | Model ID | Context window | Maximum output tokens | Reasoning |
| --- | --- | ---: | ---: | --- |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `1000000` | `384000` | Enabled; use `max` effort for complex tasks |
| DeepSeek V4 Flash | `deepseek-v4-flash` | `1000000` | `384000` | Enabled |

Turn on **Participate in routing** for each model that should be available to automatic routing. Keep the reasoning, coding, search, and chat capability tags enabled; leave vision disabled because the DeepSeek V4 API models are text-only. Save the model configuration.

![Configure DeepSeek V4 Pro and Flash in Eval Agent](./assets/eval_agent_deepseek_provider.zh-CN.png)

The screenshot illustrates the field locations in an existing local configuration. Turn on the provider and routing toggles, and use the current values in the table above—especially `384000` for maximum output tokens.

DeepSeek V4 supports a **1 million token context window**, and DeepSeek V4 Pro supports the `max` reasoning-effort level. Eval Agent complements these model capabilities with context-pressure monitoring, automatic compaction, checkpoints, and task recovery for long engineering workflows.

#### 5. Select DeepSeek in Model Routing

Return to **Settings → Model**:

1. Choose **Automatic routing** as the global default model, or select a DeepSeek model directly.
2. Under **Agent-specific routing**, assign `deepseek-v4-pro` to roles that handle architecture and difficult debugging, and use `deepseek-v4-flash` for faster everyday engineering tasks.
3. Enable fallback models if you want Eval Agent to switch models when the primary route fails.
4. Click **Save and Exit**.

#### 6. Run Your First DeepSeek-Powered Task

1. Open or create a project workspace.
2. Select the required Agent or leave automatic routing enabled.
3. Choose an execution scope. Eval Agent provides four permission levels and tool-level `allow` / `ask` / `deny` controls.
4. Describe an engineering goal, for example:

   > Analyze this schematic, identify the MCU and debug interfaces, then create a checkpointed firmware build-and-verify plan. Ask before flashing hardware.

5. Review the proposed plan and approve any sensitive tool actions. Follow progress through live events, tool logs, and checkpoints.

DeepSeek performs the reasoning and tool selection, while Eval Agent orchestrates the specialist agents and engineering tools needed to execute and verify the work.

#### Troubleshooting

- **Authentication fails or returns `401`:** Create a new key in the DeepSeek Platform and paste it into the API Key field without extra spaces.
- **Model not found or returns `404`:** Use the current model IDs exactly: `deepseek-v4-flash` or `deepseek-v4-pro`.
- **Connection test cannot reach DeepSeek:** Verify that the API Base URL is `https://api.deepseek.com/v1` and that your network can reach the DeepSeek API.
- **DeepSeek does not appear in automatic routing:** Enable the provider, enable the model, and turn on **Participate in routing** for that model.
- **Complex tasks stop too early:** Select `deepseek-v4-pro`, use `max` reasoning effort, and confirm the context window is `1000000`.
- **A hardware action is waiting:** Check Eval Agent's approval queue. Flashing, debugging, and other sensitive tools may require explicit confirmation under the selected permission policy.

For product downloads and updates, visit the [Eval Agent website](https://eval.zailink.space/).
