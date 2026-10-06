[English](./tianshu.md) | [简体中文](./tianshu.zh-CN.md) · [← Back](../README.md)

# Integrate with Tianshu

Tianshu (天枢) is an open-source coding-agent runtime. A terminal TUI and a desktop app share one kernel. The built-in DeepSeek preset talks to `https://api.deepseek.com/v1` — no custom base URL.

The preset ships two current model ids. Both use a 1,000,000-token context window and a 256,000-token output cap. Tianshu sends `reasoning_effort` on each request. The preset default for both models is `high`.

| Model id | What it is | Default effort |
| --- | --- | --- |
| `deepseek-flash` | DeepSeek-V4.1-Flash. This is the default. | `high` |
| `deepseek-v4-pro` | DeepSeek-V4-Pro | `high` |

`deepseek-v4-flash` was retired from this preset on 2026-10-04. The official API still accepts that old id and serves it as V4.1 Flash. On the official `deepseek` provider, Tianshu rewrites a saved `deepseek-v4-flash` entry to `deepseek-flash`. Configure the new id.

#### 1. Install Node.js

- Install [Node.js](https://nodejs.org/en/download/) 24 or newer.
- Windows users also need [Git for Windows](https://git-scm.com/download/win).

#### 2. Install Tianshu

```bash
npm install -g tianshu-harness
```

`tianshu` and `rivet` are the same program. Desktop builds (macOS, Windows, Linux) are on the [GitHub releases](https://github.com/huiliyi37/Tianshu-harness/releases/latest) page and do not need Node.js.

#### 3. Get a DeepSeek API key

Create a key at the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

```bash
export DEEPSEEK_API_KEY="sk-..."
```

Windows (PowerShell):

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 4. Configure the DeepSeek preset

The first launch opens `/connect`. Choose **DeepSeek** and finish the key step. That uses the built-in preset.

To configure it before launch:

```bash
tianshu config setup deepseek --key-env DEEPSEEK_API_KEY --default
```

Do not pass a smaller `--context-window`. Compaction thresholds follow that number, and both preset models are 1,000,000 tokens. The desktop app uses the same preset under **Settings → Provider**.

#### 5. Start a session

```bash
cd /path/to/your-project
tianshu
```

Inside the TUI:

```text
/model list
/model deepseek-v4-pro
/effort max
```

`/model deepseek-flash` switches back to V4.1 Flash. `/effort max` asks for the `max` reasoning level on later turns. A `reasoningEffort` of `max` written in config is kept: automatic effort routing will not step it down. Leave thinking enabled.

<div align="center">
<img src="https://raw.githubusercontent.com/huiliyi37/Tianshu-harness/main/docs/brand/assets/tianshu-banner-dark.jpg" width="640" alt="Tianshu" />
</div>
