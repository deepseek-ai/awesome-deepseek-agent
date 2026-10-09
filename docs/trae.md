[English](./trae.md) | [简体中文](./trae.zh-CN.md) · [← Back](../README.md)
# Integrate with Trae
Trae is an AI IDE that ships with built-in models, and also supports bringing your own key through its preset model providers. This guide connects DeepSeek-V4-Pro or DeepSeek-V4-Flash to Trae using your own DeepSeek API key.
> Two ways to use DeepSeek — pick either one:
>
> - **Built-in models**: Trae's model selector already lists DeepSeek models, so no extra configuration is needed. Usage is covered by your Trae plan allowance.
> - **Preset provider with your own key**: add DeepSeek as a preset provider and enter your DeepSeek API key. Calling a custom model consumes no Trae plan allowance — usage is billed directly to your DeepSeek API account. This guide covers this approach.
### Installing Trae from Scratch
- Download the installer from the [official website](https://www.trae.ai/download). Trae supports macOS 12.0 and later, Windows 10 / 11 (x64), and Linux (`.deb` and `.rpm`, on x64 and ARM64).
- Run the installer, launch Trae, and sign in with your account.
- Follow the on-screen setup: choose a theme and language, optionally import your configuration from VS Code or Cursor, and add the Trae command-line tools.
> Users in mainland China can download and sign in from [trae.cn](https://www.trae.cn/download) instead.
### Configuring Trae
Before you start, get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
1. **Open the model management panel**: go to `Settings` -> `Models`.
2. **Add a model**: click `Add Model`.
3. **Select the preset provider**: the Add Model window opens with a **Provider** dropdown. Set it to `DeepSeek`. Take the preset-provider path rather than the custom-model path — a preset provider fills in the endpoint and protocol for you, while a custom model requires entering them manually.
4. **Complete the basic configuration**:

| Parameter | Value |
| --- | --- |
| Provider | **DeepSeek** |
| Model | **DeepSeek-V4-Flash** or **DeepSeek-V4-Pro** from the dropdown |
| API Key | Your DeepSeek API key |
- Click `Get API key` next to the API Key field if you need to create one on the DeepSeek platform.
- The model dropdown lists two preset models, **DeepSeek-V4-Pro** and **DeepSeek-V4-Flash**, plus an **Other Models** entry for models outside the list. Choose Pro for complex tasks and Flash for faster, lighter ones.
- To use a model or version not in the list, click **Other Models**. A new **Model ID** field appears in the window; enter the API model ID exactly, such as `deepseek-v4-pro` or `deepseek-v4-flash`. You can also click the lookup link next to the field to check it on the DeepSeek platform.
5. **Expand Advanced Settings**:

| Parameter | Recommended value |
| --- | --- |
| Context Window (Token) — Input | Click the **1M** preset chip |
| Context Window (Token) — Output | Leave empty for the best default, or click the **128k** chip (the largest output chip). A larger value can be typed in manually, but saving it has not been verified |
| Tool Call Rounds | Leave empty for the default, or set a higher value (e.g. `500`) for long agent workflows |
| Thinking Mode | **Follow model default**, or select **Enabled** |
| Temperature / Top P / Top K | Leave empty for the best configuration. Manual ranges: Temperature `0 ~ 2`, Top P `0 ~ 1`, Top K `1 ~ 100` |
- The Input chips are `128k`, `256k`, `512k` and `1M`; the Output chips are `4k`, `16k`, `32k` and `128k`. Any value can also be typed in directly. Leaving a field empty makes Trae use its built-in best default.
- DeepSeek V4 supports up to **1 million tokens of context** with a maximum output of 384K tokens, so the one-click `1M` input chip is the recommended setting. Leave the output field empty unless you have verified in your version that a larger manual value saves successfully.
6. **Add the model**: click `Add Model`. When editing an existing model, this button is `Save Model`. Trae runs a connectivity check against DeepSeek. This check sends one real request and consumes a small amount of model tokens. On success the model is added to the model list; on failure the window shows the provider's error and log for troubleshooting.
### Using Trae
DeepSeek V4 models support up to **1M tokens of context** and thinking effort levels up to `max`. Trae's dialog exposes Thinking Mode as **Follow model default / Enabled / Disabled** rather than a per-level selector, so keep it on follow-default or enabled to retain the model's full reasoning; never disable thinking as a workaround for an API error. With the input context set to `1M`, a single task can hold a full codebase.
Open your project in Trae, click the current model name at the lower right of the chat input box, and select the DeepSeek model you added. It then works in both IDE and SOLO mode.
> The raw API model IDs are `deepseek-v4-pro` and `deepseek-v4-flash`. On the DeepSeek side these are the only current model names; earlier V3 names are deprecated and should no longer be used. For current rates, see the [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing).
For more details, see the [Trae built-in and custom models documentation](https://docs.trae.ai/ide/models).
### Troubleshooting
- Adding or saving the model fails: check that the API key is correct with no extra spaces, and confirm it has not expired or been disabled.
- Connectivity check fails or requests error out: check whether your DeepSeek account has sufficient balance and your network connection is working.
- The model does not appear in the chat model selector: confirm the model is enabled in `Settings` -> `Models`. A disabled model stays in the management panel but is hidden from the selector.
- The preset provider is unavailable in your version: use the custom model route instead — set API Format to OpenAI Chat Completions, request URL to `https://api.deepseek.com/v1/chat/completions`, and Model ID to `deepseek-v4-pro` or `deepseek-v4-flash`.
