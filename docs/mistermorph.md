[English](./mistermorph.md) | [简体中文](./mistermorph.zh-CN.md) | [日本語](./mistermorph.ja.md) · [← Back](../README.md)

# Integrate with Morph

Morph is an open-source agent runtime and console for building personal or team AI agents. It supports CLI, web console, chat-channel integrations, tools, skills, memory, MCP, and OpenAI-compatible model providers such as DeepSeek.

- **GitHub:** <https://github.com/quailyquaily/mistermorph>

#### 1. Install Morph

For the simplest setup, download the desktop app from [GitHub Releases](https://github.com/quailyquaily/mistermorph/releases). The desktop app starts the local backend and provides the Console UI.

If you prefer the CLI or want to run Morph on a server, install it with the official install script:

```sh
curl -fsSL -o /tmp/install-mistermorph.sh https://raw.githubusercontent.com/quailyquaily/mistermorph/refs/heads/master/scripts/install-release.sh
sudo bash /tmp/install-mistermorph.sh
```

After installation, verify that the CLI is available:

```sh
mistermorph --help
```

#### 2. Configure DeepSeek

The recommended path is to use the Console UI.

For the desktop app, open the app and use Setup or Settings -> LLM.

For a local CLI install, start the Console:

```sh
mistermorph console serve --allow-empty-password
```

Open the local URL printed by the command, then use Setup or Settings -> LLM. Configure:

- Provider: `deepseek`
- Model: `deepseek-v4-pro`
- API Key: your DeepSeek API key

Use `--allow-empty-password` only in a trusted local environment. If the Console is exposed on a network, configure a password instead.

You can get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

For a faster and lower-cost default, use `deepseek-v4-flash` as the model.

If you prefer editing files, run the setup command once to create Morph's default state and config files:

```sh
mistermorph install
```

Then edit `~/.morph/config.yaml` and configure the LLM provider:

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-pro
  api_key: ${DEEPSEEK_API_KEY}
```

For DeepSeek's official API, use `provider: deepseek`. Use `provider: openai` only when you point Morph at a custom OpenAI-compatible endpoint.

Set your DeepSeek API key in the shell:

```sh
export DEEPSEEK_API_KEY="sk-..."
```

For `deepseek-v4-flash`, use:

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
```

#### 3. Run Morph

Run a task from the command line:

```sh
mistermorph run --task "List the files in this project and summarize what it does."
```

Or open the local console server:

```sh
mistermorph console serve
```

#### 4. Optional: use a dedicated LLM profile

Morph also supports named LLM profiles. This is useful when you want to route different tasks to different DeepSeek models:

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
  profiles:
    deepseek_pro:
      provider: deepseek
      model: deepseek-v4-pro
      api_key: ${DEEPSEEK_API_KEY}
      reasoning_effort: high
```

Use Morph's routing configuration to assign that profile to selected workflows when needed.
