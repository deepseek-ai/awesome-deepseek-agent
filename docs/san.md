[English](./san.md) | [简体中文](./san.zh-CN.md) · [← Back](../README.md)

# Integrate with San

San is an open-source terminal agent runtime: one 12 MB Go binary, ~0.01s cold start, zero runtime deps — no Node.js, no Python. Its harness spends ~2.3k tokens before your first message, so DeepSeek's 1M window stays yours.

DeepSeek is a **built-in provider**: the V4 model IDs, the 1M/384K limits, reasoning effort and per-turn cost are already wired in, so all you bring is an API key.

- **GitHub:** <https://github.com/genai-io/san>
- **Docs:** <https://genai-io.github.io/san/>

#### 1. Install San

Homebrew (macOS / Linux):

```bash
brew tap genai-io/san
brew install san
```

Install script (macOS / Linux):

```bash
curl -fsSL https://raw.githubusercontent.com/genai-io/san/main/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://raw.githubusercontent.com/genai-io/san/main/install.ps1 | iex
```

Or with Go 1.25.8+:

```bash
go install github.com/genai-io/san/cmd/san@latest
```

Verify the install:

```bash
san version
```

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Connect DeepSeek

**Option A — in the app.** Launch San and open the model picker:

```bash
san
```

```
/models
```

Select **DeepSeek**, then paste your API key when prompted. San remembers it for later sessions.

**Option B — environment variable.** San picks up `DEEPSEEK_API_KEY` at startup:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

If you go through a gateway or proxy, set `DEEPSEEK_BASE_URL` as well — it defaults to `https://api.deepseek.com`.

#### 4. Pick a Model

Run `/models` again and choose:

- `deepseek-v4-pro` — the strongest coding model
- `deepseek-v4-flash` — faster and cheaper

Both arrive with the full V4 limits already set: **1M tokens of context** and up to **384K output tokens**, so there is no context-window config to fill in. The session cost in the status bar is computed from DeepSeek's official rates, cache-hit pricing included.

#### 5. Turn Thinking Up

DeepSeek V4 thinks by default at effort `high`. San exposes the whole ladder — `off · low · high · xhigh · max` — and you can set it directly:

```
/think max
```

`Ctrl+T` cycles through the same levels without typing. For the hardest coding sessions stay on **`max`**; `xhigh` also works and DeepSeek maps it to `high`. Only `off` disables thinking.

That's it — run `san` in any project directory and you're coding on DeepSeek V4.

> **Tip:** `/context` breaks down what is filling the 1M window, and `/models` switches models mid-session without losing the conversation.
