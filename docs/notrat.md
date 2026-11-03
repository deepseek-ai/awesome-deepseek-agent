[English](./notrat.md) | [简体中文](./notrat.zh-CN.md) · [← Back](../README.md)

# Integrate with Notrat

Notrat is an AI-native desktop knowledge workspace: a Markdown editor on one side, and an agent with real hands on the other. The agent can read and write the file you are editing, run terminal commands, and call MCP tools — so DeepSeek V4 is not just a chat box inside an editor, it works directly on your workspace (Windows / macOS / Linux).

DeepSeek is a built-in provider preset in Notrat — no JSON files to hand-edit.

- **Website:** <https://notrat.cn>
- **Download:** <https://notrat.cn/download>

#### 1. Install Notrat

- Download Notrat from the [official download page](https://notrat.cn/download) — Windows 10+, macOS 12+, and Linux (AppImage by default; `.deb` / `.rpm` builds are listed on the same page).
- Launch it and sign in. Configuring AI providers requires the **Basic** tier or above; the free tier shows an upgrade prompt.
- Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Add DeepSeek as a provider

1. Open **Settings** and select **AI Model Config** in the left sidebar. The page is titled *AI assistant configuration*.
2. In the **AI providers** section, click **Add**.
3. In the provider grid, pick the **DeepSeek** card under **Cloud services (API key required)**. The card already sets the API type (OpenAI-compatible) and the base URL (`https://api.deepseek.com`), and pre-selects `deepseek-v4-pro` — leave the type and URL untouched.
4. Paste your API key into **API Key**, then click **Test**. Notrat requests the provider's model list; on success the fetched models appear under **Pick a model**.
5. Click `deepseek-v4-pro` (or `deepseek-v4-flash` for cheaper, faster turns).
6. Click **Next: More** to open step 3 — the parameters there are optional — then click **Save & Add**. The new provider automatically becomes the current one; to switch to it again later, click it in the **AI providers** list and use **Set as Current** in the form header.

The add dialog runs in three steps — *Provider → Key & Models → More*. Step 3 (*Params & more*: answer style, reply length, image understanding) unlocks only after **Test** succeeds. If **Test** reports that no models were fetched (some relays and self-hosted gateways do not implement `/models`), step 2 still unlocks — use the **Add a model manually** box there, type `deepseek-v4-pro`, and click **Add**.

#### 3. Pick the model in chat

Click the model chip in the chat composer toolbar (it shows the current model name) to open the model dropdown. Providers are listed as expandable groups — expand **DeepSeek** and select `DeepSeek V4 Pro` or `DeepSeek V4 Flash`. The refresh icon at the top of the dropdown re-reads the provider and model configuration (handy after editing providers in Settings); it does not call DeepSeek's `/models` endpoint. To pull a newly released model id from DeepSeek, open the provider in **Settings → AI Model Config** and click **Refetch models**.

#### 4. 1M context and max thinking — already wired up

- **Context window**: Notrat ships a built-in model spec table that maps `deepseek-v4-pro` / `deepseek-v4-flash` to a **1,048,576-token context** and a **393,216-token max output**. Requests carry DeepSeek V4's full limits out of the box, and the conversation-compression budget uses the same number — no manual configuration needed.
- **Thinking effort**: open the model dropdown and hover over (or keyboard-focus) the model row to open its detail card — clicking a model selects it and closes the dropdown. In the card, set **Reasoning effort** to **Max** (`极高`). Notrat exposes `low` / `medium` / `high` / `max` for DeepSeek and defaults to `high`; `Max` is sent as `reasoning_effort: "max"` to DeepSeek's thinking mode, which is the level this repository's contributor guide recommends so users get the best coding experience.

> Using a relay that renames the model (e.g. `deepseek-pro` instead of `deepseek-v4-pro`)? The spec table still recognizes the common aliases, but if your relay renames it beyond recognition, open the same detail card and fill **Context window** / **Max output** by hand — manual values always win over the spec table, and they change the default `max_tokens` actually sent, not just the label.

#### 5. Optional: verify the API key from the terminal

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"

curl.exe https://api.deepseek.com/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

If the request succeeds, the key and model id are valid.

#### Troubleshooting

- `Authentication Fails` or `401`: the API key is wrong or expired. Make sure the base URL was not pasted into the API Key field.
- `Model Not Found` or `404`: the model id must be exactly `deepseek-v4-pro` or `deepseek-v4-flash`. If you typed it manually, check for stray spaces.
- **Test** fails and no models appear: some relays and self-hosted gateways do not implement `/models`. Type the model id in the **Add a model manually** box in step 2 instead — Notrat will still send the request.
- No network at all: proxy settings live in **Settings → General → HTTP proxy** (not in the AI page). The default `http://127.0.0.1:7890` also accepts `socks5://…`.
- Running on the free tier: configuring AI providers requires the **Basic** tier or above — the free tier shows an upgrade prompt instead.
- The configured model does not appear in the chat dropdown: click the provider in **Settings → AI Model Config** and make sure the header shows **Current** (otherwise click **Set as Current**), then reopen the dropdown and use its refresh icon. If the model id itself is missing from the provider's list, click **Refetch models** in the same form.
- Reasoning gives a long stream of thinking with an empty answer: check **Max output** in the model detail card. If your relay renamed the model so that it matches no known spec, the built-in fallback for unmatched DeepSeek names is only 8K output — set the real limit by hand.

For the full AI configuration reference (OAuth providers, local models, parameter presets), see the [official website](https://notrat.cn) and the help documentation bundled with the app.
