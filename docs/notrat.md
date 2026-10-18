[English](./notrat.md) | [简体中文](./notrat.zh-CN.md) · [← Back](../README.md)

# Integrate with Notrat

Notrat is an AI-native desktop knowledge workspace: a Markdown editor on one side, and an agent with real hands on the other. The agent can read and write the file you are editing, run terminal commands, and call MCP tools — so DeepSeek V4 is not just a chat box inside an editor, it works directly on your workspace (Windows / macOS / Linux).

DeepSeek is a built-in provider preset in Notrat — no JSON files to hand-edit.

#### 1. Install Notrat

- Download Notrat from the [official website](https://notrat.com/download) — available for Windows 10 (1809+), macOS 10.15+, and Linux (Ubuntu 20.04+ / Debian 11+ / Fedora 35+).
- Launch it and sign in. Configuring AI providers requires the **Basic** tier or above.
- Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Add DeepSeek as a provider

1. Open **Settings** and select **AI Model Config** in the left sidebar. The page is titled *AI assistant configuration* and lists your configured services.
2. Click **Add** in the configured-services list.
3. In the provider grid, pick the **DeepSeek** card under **Cloud services (API key required)**. The card already sets the right API type (OpenAI-compatible), the base URL (`https://api.deepseek.com`), and pre-fills `deepseek-v4-pro` as the fallback model — leave the first two untouched.
4. Paste your API key into **API Key**, then click **Test**. Notrat requests the provider's model list and fills the **Select Model** field.
5. Choose `deepseek-v4-pro` (or `deepseek-v4-flash` for cheaper, faster turns) and click **Save**.
6. Optional: click **Set as Current** to make it the global default.

The add dialog runs in three steps — *Provider → Key & Models → More*. If **Test** cannot fetch the list (some relays do not expose `/models`), expand the advanced section and type the model id by hand.

#### 3. Pick the model in chat

Click the model-name button in the chat composer toolbar to open the model dropdown, grouped by provider, and select `DeepSeek V4 Pro` or `DeepSeek V4 Flash`. The refresh button in that dropdown re-fetches the provider's model list, so newly released models show up without restarting.

#### 4. 1M context and max thinking — already wired up

- **Context window**: Notrat ships a built-in model spec table that maps `deepseek-v4-pro` / `deepseek-v4-flash` to a **1,048,576-token context** and a **393,216-token max output**. Requests carry DeepSeek V4's full limits out of the box, and the conversation-compression budget uses the same number — no manual configuration needed.
- **Thinking effort**: open the model dropdown, click the model to expand its detail card, and set **Reasoning effort** to **Max** (`极高`). Notrat exposes `low` / `medium` / `high` / `max` for DeepSeek and defaults to `high`; `Max` is sent as `reasoning_effort: "max"` to DeepSeek's thinking mode, which is the level this repository's contributor guide recommends so users get the best coding experience.

> Using a relay that renames the model (e.g. `deepseek-pro` instead of `deepseek-v4-pro`)? The spec table still recognizes the common aliases, but if your relay renames it beyond recognition, open the same detail card and fill **Context window** / **Max output** by hand — manual values always win over the spec table, and they change the default `max_tokens` actually sent, not just the label.

#### 5. Optional: verify the API key from the terminal

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"

curl https://api.deepseek.com/chat/completions `
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
- **Test** fails and no models appear: some relays and self-hosted gateways do not implement `/models`. Type the model id manually instead — Notrat will still send the request.
- No network at all: proxy settings live in **Settings → General → HTTP proxy** (not in the AI page). The default `http://127.0.0.1:7890` also accepts `socks5://…`.
- Running on the free tier: configuring AI providers requires the **Basic** tier or above — the free tier shows an upgrade prompt instead.
- The configured model does not appear in the chat dropdown: click **Save**, then **Set as Current**, and use the dropdown's refresh button.
- Reasoning gives a long stream of thinking with an empty answer: check **Max output** in the model detail card. If your relay renamed the model so that it matches no known spec, the built-in fallback for unmatched DeepSeek names is only 8K output — set the real limit by hand.

For the full AI configuration reference (OAuth providers, local models, parameter presets), see the [official website](https://notrat.com) and the help documentation bundled with the app.
