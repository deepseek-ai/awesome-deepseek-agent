[English](./openclacky.md) | [简体中文](./openclacky.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenClacky

[OpenClacky](https://github.com/clacky-ai/openclacky) is the most token-efficient open-source AI agent (MIT). It ships with native DeepSeek support — proper handling of `reasoning_content`, ~100% prompt-cache hit rate, and a Web UI / Terminal / IM (Feishu, WeCom, WeChat, Discord, Telegram) experience all from one binary.

#### 1. Install OpenClacky

**macOS / Linux**

```bash
/bin/bash -c "$(curl -sSL https://raw.githubusercontent.com/clacky-ai/openclacky/main/scripts/install.sh)"
```

**Windows**

```powershell
powershell -c "& ([scriptblock]::Create((irm 'https://raw.githubusercontent.com/clacky-ai/openclacky/main/scripts/install.ps1')))"
```

**Or via RubyGems** (Ruby >= 3.1.0):

```bash
gem install openclacky
```

Desktop installers (`.dmg` / `.exe`) are available at [openclacky.com](https://www.openclacky.com/).

#### 2. Configure DeepSeek as the Default Model

Start OpenClacky and open the configuration menu:

```bash
openclacky
> /config
```

Set the following fields:

| Field | Value |
| --- | --- |
| Provider | **DeepSeek** (built-in) |
| Base URL | `https://api.deepseek.com` |
| API Key | Your [DeepSeek API key](https://platform.deepseek.com/api_keys) |
| Model | `deepseek-v4-pro` (recommended) or `deepseek-v4-flash` |
| Context window | `1000000` (DeepSeek V4 supports 1M tokens) |
| Reasoning effort | `max` (best coding quality) — `high` also supported |

OpenClacky has first-class DeepSeek V4 support and correctly passes back `reasoning_content`, so you do **not** need to disable thinking mode. Keeping `reasoning_effort=max` gives the best result on coding tasks.

#### 3. Get Started

**Web UI** (recommended — multi-session, parallel coding/research/copywriting):

```bash
openclacky server          # http://localhost:7070
openclacky server --port 8080
openclacky server --host 0.0.0.0   # remote access
```

**Terminal**:

```bash
openclacky                 # interactive agent in current directory
```

**Scaffold a new project**:

```bash
$ openclacky
> /new my-app
> Add user auth with email and password
```

#### 4. Why This Combo Works

- **~100% prompt cache hit** — sessions never restart, the system prompt is never mutated, and idle-time auto-compression pre-warms the cache. Combined with DeepSeek's $0.003625 / M tokens cache-hit price, real spend on long sessions drops dramatically.
- **16 core tools + `invoke_skill`** — small tool schema means a small request payload, which means more of every prompt fits inside the 1M context window without paging.
- **BYOK routing** — keep `deepseek-v4-pro` as the default and let subagents fan out to `deepseek-v4-flash` for cheaper subtasks.

More docs: [openclacky.com/docs](https://www.openclacky.com/docs/installation) · [GitHub](https://github.com/clacky-ai/openclacky)
