[English](./deepseek_harness.md) | [简体中文](./deepseek_harness.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Harness

DeepSeek Harness is DeepSeek's own agent harness built on the Cordis plugin framework: every capability is a plugin composed from a `cordis.yml` profile, and the model runs through the same tool seams the plugins extend. It runs headless from the terminal, as a Web UI, or as an ACP automation server, and installs community plugins from npm or GitHub.

#### 1. Install Node.js and pnpm

- Install [Node.js](https://nodejs.org/en/download/) 22.19+ (or 24+).
- Install [pnpm](https://pnpm.io/installation) 11.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then export it:

```
export DEEPSEEK_API_KEY=sk-...
```

Windows PowerShell: `$env:DEEPSEEK_API_KEY = "sk-..."`.

#### 3. Run the harness

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm dsh web                                  # Web UI at http://127.0.0.1:3080
pnpm dsh --profile headless "your task"       # headless run
```

DeepSeek Harness pairs with the DeepSeek-V4 models, which support up to **1M tokens** of context; **DeepSeek-V4-Pro** additionally supports **max** reasoning effort — see the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode).

#### 4. Install plugins

Plugins are npm packages that declare a `dsh.bundle` manifest and install into a profile:

```
dsh plugin --profile web add dsh-auto-review
```

Browse the community registry at [awesome-dsh-plugin.com](https://awesome-dsh-plugin.com) and the [deepseek1024.com](https://deepseek1024.com) store. Official docs live at [deepseek.com/harness](https://www.deepseek.com/harness).
