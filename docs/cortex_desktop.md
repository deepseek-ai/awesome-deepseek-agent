[English](./cortex_desktop.md) | [简体中文](./cortex_desktop.zh-CN.md) · [← Back](../README.md)

# Integrate with Cortex Desktop

Cortex Desktop is a local AI workstation that listens, speaks, and acts. It isn't another chat box: speak to it and it answers, let it click and type its way through the apps on your Mac, and when one worker isn't enough it dispatches a squad of subagents in parallel. What you get back is a finished deck, report, or document — produced entirely on your own machine.

You bring your own models. The built-in catalog covers 37 providers and over 1000 models, DeepSeek among them, so integration is a matter of pasting an API key — no proxy, no custom endpoint, no manual model registration.

- **Website:** <https://rambocode.github.io/cortex-work-release/en/>
- **Downloads:** <https://github.com/rambocode/cortex-work-release/releases/latest>

#### 1. Install Cortex Desktop

Cortex Desktop is free to download. Grab the macOS build from the [releases page](https://github.com/rambocode/cortex-work-release/releases/latest):

- Apple Silicon: `Cortex-<version>-arm64.dmg`
- Intel: `Cortex-<version>-x64.dmg`

Open the `.dmg` and drag **Cortex** into `Applications`. The app is signed and notarized, so no Gatekeeper override is needed. Once installed, it updates itself from the same release feed.

#### 2. Get a DeepSeek API Key

Create a key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Copy it now — the platform shows the full key only once.

#### 3. Add the DeepSeek API Key in Settings

1. Open **Settings** from the left sidebar and select the **Models** section.
2. Choose the **API Key** tab. This tab lists every provider that authenticates with a plain API key, DeepSeek included.
3. Find **DeepSeek** in the list and click **Configure**.
4. Paste your key into the **API key** field and click **Save**. The key goes into the macOS keychain: the config file holds only a reference name, nothing is written in plaintext, and the real key is decrypted at the moment of the request. It is never echoed back after saving.
5. Optional: click **Test connection** to verify the key before leaving the page.

Leave **Base URL override** empty. Cortex uses the official DeepSeek endpoint `https://api.deepseek.com` over the OpenAI-compatible API by default. Only fill this field if you route DeepSeek through your own gateway.

If you prefer environment-based configuration, Cortex also reads `DEEPSEEK_API_KEY` from the environment for this provider.

#### 4. Select a DeepSeek V4 Model

Model selection lives on the pill above the chat input, which shows the current agent, model, and reasoning level.

1. Click the pill in the composer.
2. Under **Model**, pick one of:
   - **deepseek-v4-pro** — coding, long-horizon planning, and agent workflows.
   - **deepseek-v4-flash** — lower-latency everyday chat.
3. Send a message. The selection applies to new sessions and to your next send.

Capabilities are resolved from the model catalog, not guessed. Both DeepSeek V4 models are registered with a **1,000,000-token context window** and a 384,000-token max output, so long sessions and large repositories work without any context-window setting of your own. Cortex also won't silently swap your model — the model shown in the composer is the model that runs.

If the composer shows **No provider configured**, no provider has been connected yet — go back to step 3.

#### 5. Set Reasoning to Maximum

DeepSeek V4 exposes two real reasoning levels, `high` and `max`. Cortex reads this from the model catalog and clamps anything lower (`minimal` / `low` / `medium`) up to `high`, so you can never accidentally run DeepSeek V4 below its supported floor.

1. Click the same composer pill.
2. Under **Reasoning**, choose **Thinking · Maximum**.

Use **Maximum** for coding, refactors, and multi-step agent tasks; **Thinking · High** is a reasonable default for lighter chat. Reasoning content streams into the session incrementally, so you can watch the model think while it works.

#### Troubleshooting

- **`401` / authentication failure:** the key was pasted into the wrong field, or it was revoked on the platform. Reopen **Settings → Models → API Key → DeepSeek → Configure**, click **Clear key**, then paste it again. An empty API key box on a configured provider is normal — it means "keep the saved key", not "no key".
- **Model missing from the picker:** the API Key tab entry for DeepSeek must be saved first; providers with no credentials are not offered in the composer.
- **Requests fail only through a proxy:** check **Base URL override**. It must be a full URL including the scheme and must point at a DeepSeek-compatible OpenAI-style endpoint. Click **Clear override** to fall back to the official endpoint.
- **Reasoning stays on High after picking a lower level:** this is intentional. DeepSeek V4 does not support the lower levels, and Cortex raises them to `high` rather than sending an unsupported value.
