[English](./aipoch_open_science.md) | [简体中文](./aipoch_open_science.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with AIPOCH Open Science

AIPOCH Open Science is an open-source desktop AI workbench for scientific research. It combines persistent projects, sandboxed agent runtimes, Python/R notebooks, Skills, Connectors, file handling, and multiple model providers in one application.

- **GitHub:** <https://github.com/aipoch/open-science>
- **Latest release:** <https://github.com/aipoch/open-science/releases/latest>

This guide was checked against **Open Science v0.7.3**.

#### 1. Install AIPOCH Open Science

Download the appropriate package from the latest GitHub Release:

- Apple Silicon macOS: `open-science-0.7.3-mac-arm64.dmg`
- Intel macOS: `open-science-0.7.3-mac-x64.dmg`
- Windows 10/11 x64: `open-science-0.7.3-win-x64-setup.exe`

<div align="center">
<img src="./assets/aipoch_open_science_release.png" width="720" border="1" />
</div>

On first launch, Open Science checks system compatibility, application storage permission, secure credential storage, and installation-network access. Resolve any item that is not marked **Ready**, then click **Continue**.

<div align="center">
<img src="./assets/aipoch_open_science_environment.png" width="720" border="1" />
</div>

Next, select one Agent Runtime. Only the runtime you want to use must be installed. Click **Install**, wait for detection to finish, and continue when the selected runtime is marked **Active**.

<div align="center">
<img src="./assets/aipoch_open_science_agent_runtime.png" width="720" border="1" />
</div>

#### 2. Configure the Built-in DeepSeek Provider

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

During first launch, the same configuration is available in the **Model provider** step. The screenshots below use **Settings → Model** because this route can also be repeated after onboarding.

From the project home page, click the gear icon in the upper-right corner.

<div align="center">
<img src="./assets/aipoch_open_science_settings.jpg" width="720" border="1" />
</div>

Open **Model**, scroll to the bottom of the provider list, and click **Add provider**.

<div align="center">
<img src="./assets/aipoch_open_science_add_provider.jpg" width="720" border="1" />
</div>

Set **Provider type** to **DeepSeek**. Use the built-in provider rather than **Custom Gateway** for the standard DeepSeek API.

<div align="center">
<img src="./assets/aipoch_open_science_select_deepseek.jpg" width="720" border="1" />
</div>

Paste the API key into **API Key** and click **Save**. Do not put the endpoint URL in the API Key field. The DeepSeek form exposes the three supported V4 model IDs:

<div align="center">
<img src="./assets/aipoch_open_science_supported_models.jpg" width="720" border="1" />
</div>

| Model | Recommended use | Context window |
| --- | --- | --- |
| `deepseek-v4-pro` | Coding, research, and complex agent tasks | 1,000,000 tokens |
| `deepseek-v4-pro[1m]` | Explicit long-context alias for Anthropic-compatible execution | 1,000,000 tokens |
| `deepseek-v4-flash` | Faster interactive work and lower-latency tasks | 1,000,000 tokens |

Use the current V4 model IDs exactly as shown above; do not substitute legacy DeepSeek model IDs.

After saving, Open Science tests the provider. A green status icon on the DeepSeek provider card indicates that the connection check passed. Set the active model to the required DeepSeek model; the example below uses `deepseek-v4-pro[1m]`.

<div align="center">
<img src="./assets/aipoch_open_science_active_deepseek.jpg" width="720" border="1" />
</div>

For `deepseek-v4-pro`, set **Reasoning effort** to **Max** for the strongest reasoning mode. You can set the default on the Model settings page or override it for the current chat from the message toolbar.

<div align="center">
<img src="./assets/aipoch_open_science_reasoning_effort.png" width="720" border="1" />
</div>

The built-in provider supplies the endpoint automatically. Open Science v0.7.3 defines:

- Anthropic-compatible endpoint: `https://api.deepseek.com/anthropic`
- OpenAI-compatible base URL: `https://api.deepseek.com/v1`

You normally should not edit either address manually.

> **Max reasoning is not only a UI label.** In Open Science v0.7.3, the `max` selection is normalized to `reasoningEffort: "max"` with thinking enabled. On the OpenAI-compatible request path, the bridge serializes this value into the request body as `reasoning_effort: "max"`.

The chat context indicator reports usage against the full model window. For example, `71k / 1M tokens (7%)` confirms a 1-million-token ceiling:

<div align="center">
<img src="./assets/aipoch_open_science_context_1m.png" width="520" border="1" />
</div>

#### 3. Finish the First-launch Setup

New installations complete these items immediately after the Model provider step. Existing installations that already show the project home page can skip this section.

The **Notebook runtime** step is optional. Enable a detected Python or R interpreter, install an app-managed runtime, or leave it disabled and configure it later under **Settings → Runtimes**.

Choose a **Data location** for projects, artifacts, notebooks, and runtime files, then click **Finish**. After Open Science starts managing this directory, move it only through **Settings → Storage → Change location**.

#### 4. Create a Project and Run DeepSeek

1. Click **New project**.
2. Enter a project name and, optionally, a description.
3. Click **Create project**.
4. In the model selector above the message box, confirm that `deepseek-v4-pro`, `deepseek-v4-pro[1m]`, or `deepseek-v4-flash` is active.
5. Enter a prompt and send it.

<div align="center">
<img src="./assets/aipoch_open_science_deepseek_project.jpg" width="720" border="1" />
</div>

For the first check, use a small prompt that is easy to verify:

```text
Reply with the active model name, then list three ways an AI agent can help reproduce a scientific paper.
```

A successful response confirms that the project can call DeepSeek. For `deepseek-v4-pro`, keep **Reasoning effort** at **Max** when you want the strongest reasoning for coding or complex research tasks.

#### Troubleshooting

- **401 / authentication failed:** Confirm that the value in **API Key** is a valid DeepSeek API key.
- **Model not found / 404:** Use exactly `deepseek-v4-pro`, `deepseek-v4-pro[1m]`, or `deepseek-v4-flash`.
- **Connection test fails after editing the URL:** Re-select the built-in **DeepSeek** provider and keep its generated endpoint.
- **The model does not appear in a project:** Open **Settings → Model**, test the provider again, and set the DeepSeek model as active.
- **Reasoning is not at the expected strength:** Confirm that the model is `deepseek-v4-pro`, Reasoning effort is enabled, and the selected value is **Max**.
