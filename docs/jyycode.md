[English](./jyycode.md) | [简体中文](./jyycode.zh-CN.md) · [← Back](../README.md)

# Integrate with JYY-Code

JYY-Code is an open-source terminal coding agent built on OpenCode, with multi-agent orchestration, persistent memory, Agent Skills, MCP, and communication tools.

- **GitHub:** <https://github.com/Reon-Jin/JYY-Code>
- **npm:** <https://www.npmjs.com/package/jyycode-ai>

#### 1. Install JYY-Code

- Install [Node.js](https://nodejs.org/en/download/) 20+.
- Install the published CLI package:

```sh
npm install -g jyycode-ai
```

- Verify the installation:

```sh
jyycode --version
```

`jyy` and `jyycode` start the same CLI.

#### 2. Configure DeepSeek

The simplest setup is to store your DeepSeek API key with the built-in provider login command:

```sh
jyycode auth login --provider deepseek
jyycode models deepseek --refresh
```

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

You can also write the global config file at `~/.config/jyycode/jyycode.jsonc`:

```jsonc
{
  "$schema": "https://jyycode.ai/config.json",
  "model": "deepseek/deepseek-v4-pro",
  "small_model": "deepseek/deepseek-v4-flash",
  "provider": {
    "deepseek": {
      "options": {
        "apiKey": "sk-..."
      },
      "models": {
        "deepseek-v4-pro": {
          "reasoning": true,
          "limit": {
            "context": 1000000,
            "output": 384000
          }
        },
        "deepseek-v4-flash": {
          "limit": {
            "context": 1000000,
            "output": 384000
          }
        }
      }
    }
  }
}
```

Configuration notes:

| Option | Description |
|--------|-------------|
| `model` | Default model in `provider/model` format. Use `deepseek/deepseek-v4-pro` for the strongest coding model. |
| `small_model` | Lightweight model for smaller tasks such as titles and summaries, e.g. `deepseek/deepseek-v4-flash`. |
| `provider.deepseek.options.apiKey` | DeepSeek API key. You can omit this when using `jyycode auth login --provider deepseek`. |
| `limit.context` | DeepSeek V4 supports a 1 million token context window. |
| `limit.output` | Maximum output token limit used by JYY-Code's model metadata. |

JYY-Code recognizes reasoning variants for OpenAI-compatible reasoning models. For `deepseek-v4-pro`, use the `max` variant when you want maximum reasoning effort.

#### 3. Launch JYY-Code in a project

```sh
cd /path/to/my-project
jyy
```

Inside the TUI:

- Run `/connect` if you prefer configuring the DeepSeek API key interactively.
- Run `/models` to select `deepseek/deepseek-v4-pro`.
- Run `/variants` and select `max` for maximum DeepSeek V4 Pro reasoning effort.

#### 4. First run

Ask JYY-Code to inspect the current repository:

```text
Read this project and summarize its architecture, then suggest one safe first improvement.
```

JYY-Code will run in the current terminal directory and can use its filesystem, shell, MCP, memory, skill, and multi-agent tools according to your configured permissions.
