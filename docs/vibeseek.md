[English](./vibeseek.md) | [简体中文](./vibeseek.zh-CN.md) · [← Back](../README.md)

# Integrate with VibeSeek

VibeSeek is an open-source **DeepSeek-native** vibecoding desktop client for Windows. It's built only for DeepSeek and talks straight to `api.deepseek.com` — no protocol shim, no provider setup. It pairs a document-flow chat with a code-editing agent: three permission tiers, a plan-first mode, full-repo context, a git safety net (one-click rollback), and a cost-transparency receipt after every task.

- **GitHub:** <https://github.com/getvibeseek/vibeseek>

<div align="center">
<img src="./assets/vibeseek_home.png" width="720" border="1" />
</div>

#### 1. Install VibeSeek

Download `VibeSeek-Setup-*.exe` from the [Releases page](https://github.com/getvibeseek/vibeseek/releases) and run it. The build is unsigned, so Windows SmartScreen may warn on first launch — click **More info → Run anyway**.

#### 2. Set your DeepSeek API key

Get a key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). On first launch VibeSeek runs a short setup (pick a theme, then paste the key) and stores it encrypted on-device — no environment variables to configure. You can change it anytime under **Settings → API**; the API host defaults to `https://api.deepseek.com`.

#### 3. Start coding

Pick a project folder, describe the task in the composer, and send. The agent reads files, edits code, and runs commands under three permission tiers: reading is allowed outright, edits ask first, and dangerous operations require a second confirmation. Turn on **Plan mode** to have it lay out a step-by-step plan before touching anything.

By default VibeSeek auto-routes between DeepSeek's two models — **`deepseek-v4-flash`** for everyday iteration and **`deepseek-v4-pro`** for complex work — and you can pin either with `/pro` or `/flash`. DeepSeek V4's full **1M-token context** is used out of the box; set the thinking effort to **max** (or `/think`) for the strongest coding and reasoning. VibeSeek never disables thinking mode.

#### 4. Going further

- **Full-repo mode** loads the entire project into context, so the model — backed by the 1M window — locates and edits code without repeatedly grepping or re-reading files.
- **Skills & MCP:** existing skill folders work with zero changes; add MCP servers and the agent can call their tools.
- **Git safety net:** every task auto-creates a restore point — roll back all edits with one click, or accept / reject per file or per hunk.
- **Cost transparency:** a live balance, cache hit rate, and a shareable settlement receipt after every task.
