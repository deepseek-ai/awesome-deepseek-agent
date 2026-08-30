[English](./deepseek_harness.md) | [简体中文](./deepseek_harness.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Harness

DeepSeek Harness is DeepSeek's own agent harness: every capability is a plugin composed from a `cordis.yml` profile, and the model runs through the same tool seams the plugins extend.

- **GitHub:** <https://github.com/deepseek-ai/deepseek-harness>
- **Docs:** <https://www.deepseek.com/harness>

#### 1. Install DeepSeek Harness

- Install [Node.js](https://nodejs.org/en/download/) 22.19+ (or 24+) and [pnpm](https://pnpm.io/).
- Run from a source checkout:

```sh
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
```

- Verify the installation:

```sh
pnpm dsh --version
```

#### 2. Configure the DeepSeek API

Set your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) in the environment (a root `.env` also works):

```sh
export DEEPSEEK_API_KEY="sk-..."
```

Optionally set `DEEPSEEK_BASE_URL` to override the DeepSeek platform endpoint.

Use current model names `deepseek-v4-pro` (supports `max` / `high` reasoning effort) and `deepseek-v4-flash`; DeepSeek V4 models support up to 1M tokens of context.

#### 3. Run DeepSeek Harness

```sh
pnpm dsh web                                   # Web UI on http://127.0.0.1:3080
pnpm dsh --profile headless "your task"        # one-shot headless run
```

#### Everything is a plugin

Plugins are npm packages that declare a `dsh.bundle` manifest and install into a profile:

```sh
pnpm dsh plugin --profile web add dsh-auto-review   # example: second-model approval review
```

Community plugin registry: <https://awesome-dsh-plugin.com> · Plugin market: <https://deepseek1024.com>
