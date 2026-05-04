[English](./mistermorph.md) | [简体中文](./mistermorph.zh-CN.md) · [← Back](../README.md)

# Integrate with Morph

Morph is an open-source agent runtime and console for building personal or team AI agents. It supports CLI, web console, chat-channel integrations, tools, skills, memory, MCP, and OpenAI-compatible model providers such as DeepSeek.

- **GitHub:** <https://github.com/quailyquaily/mistermorph>

#### 1. Install Morph

Install Morph with the official install script:

```sh
curl -fsSL -o /tmp/install-mistermorph.sh https://raw.githubusercontent.com/quailyquaily/mistermorph/refs/heads/master/scripts/install-release.sh
sudo bash /tmp/install-mistermorph.sh
```

After installation, verify that the CLI is available:

```sh
mistermorph --help
```

#### 2. Configure DeepSeek

Run the setup command once to create Morph's default state and config files:

```sh
mistermorph install
```

Then edit `~/.morph/config.yaml` and configure the LLM provider:

```yaml
llm:
  provider: deepseek
  endpoint: https://api.deepseek.com
  model: deepseek-v4-pro
  api_key: ${DEEPSEEK_API_KEY}
```

Then set your DeepSeek API key in the shell:

```sh
export DEEPSEEK_API_KEY="sk-..."
```

You can get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

For a faster and lower-cost default, use `deepseek-v4-flash` instead:

```yaml
llm:
  provider: deepseek
  endpoint: https://api.deepseek.com
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
  endpoint: https://api.deepseek.com
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
  profiles:
    deepseek_pro:
      provider: deepseek
      endpoint: https://api.deepseek.com
      model: deepseek-v4-pro
      api_key: ${DEEPSEEK_API_KEY}
      reasoning_effort: high
```

Use Morph's routing configuration to assign that profile to selected workflows when needed.
