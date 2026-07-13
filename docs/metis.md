[English](./metis.md) | [简体中文](./metis.zh-CN.md) | [← Back](../README.md)

# Integrate DeepSeek with Metis

[Metis](https://github.com/Wholiver/metis) is an open-source, terminal-first coding agent with project memory, repository search, verification tools, interactive TUI, print/JSON modes, RPC, and an SDK.

> Metis is an independent third-party project. This guide is not official DeepSeek documentation.

## 1. Install Metis

Metis requires Node.js 22.19 or later.

```bash
npm install -g @wholiver_hu/metis@rc
```

## 2. Create a DeepSeek API key

Create an API key in the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then expose it to Metis:

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

For a persistent shell setup, add the export command to your shell profile. Metis also supports saving the key through `/login` in interactive mode.

## 3. Start Metis with DeepSeek V4 Pro

From a project directory, start an interactive session with the strongest reasoning level:

```bash
cd /path/to/project
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

`xhigh` maps to DeepSeek V4 Pro's `max` reasoning effort. Metis has built-in DeepSeek configuration for `deepseek-v4-pro` and `deepseek-v4-flash`, including the DeepSeek API endpoint and reasoning-content handling.

Both models are configured with DeepSeek V4's 1 million-token context window and up to 384,000 output tokens. No custom endpoint or model definition is needed.

## 4. Choose a model for the task

Use V4 Pro with maximum reasoning for demanding implementation and debugging work:

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

Use V4 Flash for lower-cost, faster iteration. It also supports the 1 million-token context window and `max` reasoning through `xhigh`:

```bash
metis --provider deepseek --model deepseek-v4-flash --thinking xhigh
```

Inside interactive mode, use `/model` to inspect and switch available models, or run `metis --list-models deepseek` from the shell.

## 5. Run a first task

Start Metis in a repository, then describe the task in plain language:

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

```text
Review the authentication flow, identify missing error handling, implement the smallest safe fix, and run the relevant tests.
```

Metis will inspect project instructions and code before changing files, then record the result and run available verification commands. For non-interactive automation, pass a prompt with `--print`:

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh --print \
  "Summarize this repository's test setup without changing files."
```

## Resources

- [Metis repository](https://github.com/Wholiver/metis)
- [Metis documentation](https://github.com/Wholiver/metis/tree/main/docs)
- [DeepSeek API documentation](https://api-docs.deepseek.com/)
