[English](./luban.md) | [简体中文](./luban.zh-CN.md) · [← Back](../README.md)

# Integrate with Luban

Luban is a coding agent that lives in the VS Code / VSCodium sidebar. It edits files in your workspace, runs commands to verify the result, then shows every change as an editor diff you accept or reject hunk by hunk. It talks to any OpenAI-compatible endpoint, so DeepSeek V4 Pro and V4 Flash work as first-class providers.

- **GitHub:** <https://github.com/eppen/luban>
- **VS Code Marketplace:** <https://marketplace.visualstudio.com/items?itemName=liuhualiang.luban>

#### 1. Install Luban

| Where | How |
| --- | --- |
| VS Code | Extensions panel (`Ctrl+Shift+X`) → search `Luban` → **Install** |
| VSCodium / Open VSX | Extensions panel → search `Luban` → **Install** |
| VSIX | Download `luban-v*.vsix` from [Releases](https://github.com/eppen/luban/releases), then `⋯` → **Install from VSIX…** |
| Built-in extension | `./install-into-vscodium.sh` in the repo — installs Luban as an app-level extension (VSCodium only) |

Requires VS Code / VSCodium **1.100** or newer.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure DeepSeek

Luban ships with a built-in DeepSeek provider template, so you only need to add your key and adjust the model limits.

**Option A — settings panel (recommended)**

1. Open the sidebar with `Ctrl+Shift+L` (`Cmd+Shift+L` on macOS), then click the **⚙** button at the bottom of the chat panel — or run **Provider settings (model / API key)** from the Command Palette.
2. The panel opens on the built-in **DeepSeek** provider (`https://api.deepseek.com/v1`). Paste your API key into the key field: it is stored in VS Code SecretStorage, not written to `providers.json`.
3. For each model, set **max input** to `1000000` (DeepSeek V4 supports a 1M-token context) and **max output** to `65536` (V4 accepts up to 384000 output tokens).
4. Open the model's **thinking** row → **Fill template…** → **DeepSeek**, then change `"reasoning_effort": "high"` to `"max"` in the `on` tier. This is what unlocks DeepSeek's maximum reasoning effort.
5. Click **Test connection** (one `max_tokens=1` request, shows status code and latency), then **Save**. The config is written to `~/.luban/providers.json` (previous file backed up as `providers.json.bak`) and hot-reloaded.

Keep `deepseek-v4-pro` for planning-heavy work and `deepseek-flash` for cheap iteration; both are selectable from the model dropdown at the bottom of the panel.

**Option B — edit `~/.luban/providers.json`**

```json
{
  "defaultModel": "deepseek::deepseek-v4-pro",
  "providers": [
    {
      "id": "deepseek",
      "name": "DeepSeek",
      "baseUrl": "https://api.deepseek.com/v1",
      "apiKeyEnv": "DEEPSEEK_API_KEY",
      "webSearch": {
        "baseUrl": "https://api.deepseek.com/v1/tools",
        "count": 8,
        "engine": "deepseek"
      },
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek V4 Pro",
          "maxInputTokens": 1000000,
          "maxOutputTokens": 65536,
          "toolCalling": true,
          "thinking": {
            "default": "on",
            "on": {
              "thinking": { "type": "enabled" },
              "reasoning_effort": "max"
            },
            "off": {
              "thinking": { "type": "disabled" }
            }
          }
        },
        {
          "id": "deepseek-flash",
          "name": "DeepSeek Flash",
          "maxInputTokens": 1000000,
          "maxOutputTokens": 65536,
          "toolCalling": true,
          "vision": true,
          "thinking": {
            "default": "on",
            "on": {
              "thinking": { "type": "enabled" },
              "reasoning_effort": "high"
            },
            "off": {
              "thinking": { "type": "disabled" }
            }
          }
        }
      ]
    }
  ]
}
```

Run **Reload providers.json** from the Command Palette after saving, or just reopen the panel.

- **Model IDs** are sent to the API verbatim: use `deepseek-v4-pro` and `deepseek-flash` (the current V4.1 Flash name; the legacy `deepseek-v4-flash` alias is still accepted).
- `maxInputTokens` is what Luban budgets against — set `1000000` to use the full V4 context. Lower it (e.g. `262144`) if you want Luban to compact earlier and cap spend, since its high-water mark is 80% of this value.
- `toolCalling` must be `true` for Agent mode, and `vision` only for `deepseek-flash` (V4 Pro does not accept images).
- The `thinking` block is merged into the request body as-is (`{"thinking": {"type": "enabled"}, "reasoning_effort": "max"}`); the `off` tier is used for the closing summary and when you toggle thinking off, which saves tokens.
- **API key resolution order:** the provider's `apiKey` field → VS Code SecretStorage (what the panel writes) → the `apiKeyEnv` environment variable → a same-named variable in `~/.hermes/.env`.
- `webSearch` points at DeepSeek's Search / Fetch endpoints, which powers the `@web` prefix and the `web_search` / `web_fetch` tools. Search and Fetch are billed per successful request — see [Search & Fetch pricing](https://api-docs.deepseek.com/quick_start/pricing).

#### 4. First Run

1. Pick `deepseek-v4-pro` in the model dropdown and stay in **Agent** mode.
2. Ask for something concrete, e.g. `add a debounce utility to src/utils.js and run the tests`:
   - Luban attaches the code around your cursor automatically; add more with `@file`, `@folder/`, `#selection`, or right-click a file in the Explorer → **Add File to Luban Chat**.
   - Every write opens a real diff in the editor; accept or reject hunks from the CodeLens above each hunk or the diff title bar.
3. Switch modes with `Shift+Tab`: **Plan** investigates read-only and writes a plan file before touching anything, **Chat** answers without file access.
4. Reasoning is streamed into a collapsible **Thinking** block above the answer. When the model has a `thinking` config, a **🧠** button appears at the bottom of the panel to cycle *default / on / off* per message.

Optional: enable **Toggle Tab completion** for DeepSeek FIM completions. Luban derives the `/beta` FIM endpoint from `api.deepseek.com` automatically; it is off by default (`luban.inlineCompletion.enabled`).

#### Notes

- Sessions are persisted under `~/.luban/sessions`, so a window reload does not lose history; multi-turn memory is on by default.
- Luban lays messages out for prefix caching, and each turn shows input / output / cache-hit / context usage; the **Token usage dashboard** aggregates the local ledger.
- `run_command` runs in your own shell — there is no OS-level sandbox. Plan mode adds a heuristic read-only check, and `luban.fs.allowOutsideWorkspace=false` confines file tools to the workspace.
- Local stdio MCP servers and `SKILL.md` skills plug into the same tool loop; Plan mode only sees tools declared read-only.
