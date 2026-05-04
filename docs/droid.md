[English](./droid.md) | [简体中文](./droid.zh-CN.md) · [← Back](../README.md)

# Integrate with Droid

Droid is an AI-native software development agent that runs in the terminal.

#### 1. Install Droid

```bash
# macOS / Linux
curl -fsSL https://app.factory.ai/cli | sh

# Homebrew
brew install --cask droid

# Windows
irm https://app.factory.ai/cli/windows | iex

# npm
npm install -g droid
```

#### 2. Configure DeepSeek as a Custom Model

Open `~/.factory/settings.json` and add to `customModels`:

```json
{
  "customModels": [
    {
      "model": "deepseek-v4-pro",
      "id": "custom:deepseek-v4-pro-0",
      "index": 0,
      "baseUrl": "https://api.deepseek.com/anthropic",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "displayName": "deepseek-v4-pro",
      "noImageSupport": true,
      "provider": "anthropic"
    },
    {
      "model": "deepseek-v4-flash",
      "id": "custom:deepseek-v4-flash-1",
      "index": 1,
      "baseUrl": "https://api.deepseek.com/anthropic",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "displayName": "deepseek-v4-flash",
      "noImageSupport": true,
      "provider": "anthropic"
    }
  ]
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Login to Droid

Run `droid` in your terminal and follow the prompts to log in to Factory via browser using your Google account.

#### 4. Set Chinese Interface (Optional)

If the interface is not in your preferred language, set the environment variable:

```bash
# macOS / Linux
export LANG=zh_CN

# Windows
$env:LANG="zh_CN"
```

Then run `droid` again.

#### 5. Optional Settings

**Reasoning Effort:** Add `reasoningEffort` to `~/.factory/settings.json` (default: `none`):

```json
{
  "reasoningEffort": "high"
}
```

Options:
- `none` — No reasoning, fastest response
- `low` — Low reasoning, suitable for simple tasks
- `medium` — Medium reasoning, recommended for daily tasks
- `high` — High reasoning, best for complex tasks

**Other Settings:** Run `/settings` in Droid to open the settings panel:

- Default compaction token limit — Set context window size
- Preferences:
  - Cloud session sync — Recommended to disable
  - Show thinking process in main view — Recommended to enable
  - Show context window usage rate — Recommended to enable
- Other settings as needed
