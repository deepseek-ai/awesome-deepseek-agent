[English](./veloce_lab.md) | [简体中文](./veloce_lab.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with Veloce Lab

Veloce Lab is a personal-assistant harness built with the YumeriJS framework. It provides a Web administration console for configuring the model channels used by the assistant.

- **GitHub:** <https://github.com/veloce-ailab/veloce-lab>

#### 1. Install and start Veloce Lab

- Install [Node.js](https://nodejs.org/) 24 LTS or newer.
- In an empty project directory, download the Veloce configuration:

```powershell
irm -OutFile yumeri.json https://raw.githubusercontent.com/veloce-ailab/veloce-lab/main/scripts/yumeri.json
```

- Start the service. `npx` is recommended because it does not require Yumeri to be installed beforehand:

```sh
npx yumeri@latest -c yumeri.json --auto-install
```

The `--auto-install` option installs the dependencies declared by the configuration. After Veloce Lab starts, open its Web administration console and sign in with an administrator account.

#### 2. Add a DeepSeek upstream channel

1. Open **Channels** in the administration console and choose **Add upstream**.
2. Fill in the channel form:

| Field | Value |
|-------|-------|
| Name | A label such as `DeepSeek` |
| Type | `DeepSeek` |
| Base URL | `https://api.deepseek.com` |
| API Key | Your key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) |
| Enabled | On |

3. Keep the default priority and weight unless you are configuring routing with multiple channels, then choose **Save**.

The channel type list only shows adapters registered by the running Veloce configuration. If `DeepSeek` is missing, enable the corresponding adapter in `yumeri.json` and restart the service. The Base URL may be entered as the host or with `/v1`; Veloce avoids adding a duplicate `/v1` segment when constructing requests.

#### 3. Add DeepSeek models

Click the model-list action for the new channel to open **Model configs**. There are two ways to add models:

**Sync from the API (recommended)**

1. Leave **Sync format** set to `OpenAI /v1/models`.
2. Click **Sync models**.
3. In the preview, keep the required models selected and click **Submit sync**.

Use current DeepSeek model names such as `deepseek-v4-pro` or `deepseek-v4-flash`. DeepSeek V4 models support up to 1 million tokens of context; the Veloce model dialog does not expose a context-window field, so the selected model name and the downstream client or adapter determine the effective request limits. Veloce supports `max` and custom reasoning-effort identifiers; for clients that expose this setting, use `max` for the highest reasoning effort.

**Add a model manually**

1. Click **Add model config**.
2. Enter the public model name, for example `deepseek-v4-pro`.
3. Leave **Upstream model name** empty when it is the same, or enter the provider's exact upstream name.
4. Leave **Provider** on **Auto detect**. Veloce recognizes names containing `deepseek`; you can choose a provider explicitly or use **Custom provider** when needed.
5. Keep **Enabled** on and click **Save**.

#### 4. Run a first request

After the model is synced or saved, it becomes available to the assistant. Open Veloce Lab's chat, select the newly enabled DeepSeek model, and send a small coding prompt. Confirm that the response arrives and that the channel's request and token counters increase in the administration console.

#### Troubleshooting model sync

- **The server cannot fetch `/v1/models`:** Veloce opens a fallback dialog with the request URL. Choose **Fetch in browser** to retry from the browser, optionally including the channel token, or paste the model-list JSON into **Manual JSON** and choose **Parse JSON**.
- **No models appear:** verify the Base URL, API Key, adapter type, and that the upstream returns a model list from `/v1/models`. You can also choose `Generic /models`, `Generic /api/models`, or `Custom path` when the provider uses another endpoint.
- **The model is not selectable:** check that the model configuration and its upstream channel are both enabled, then refresh the model catalog.
