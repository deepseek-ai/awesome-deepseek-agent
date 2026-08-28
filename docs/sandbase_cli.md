[中文](./sandbase_cli.zh-CN.md) | [← Back](../README.md)

# Integrate DeepSeek with SandBase CLI

SandBase CLI is an Apache-2.0 command-line tool and local MCP bridge. It lets MCP-compatible clients discover and run hosted AI models and APIs, including DeepSeek models, through one authenticated connection.

#### 1. Install

```bash
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz catalog --json
```

This read-only command prints the verified client catalog. On macOS or Linux:

```bash
brew install sandbaseai/tap/sandbaseai-cli
```

#### 2. Connect a client

```bash
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz connect
```

Follow the browser OAuth prompt, then restart the selected client. Credentials are not placed in command-line arguments or URLs.

#### 3. First DeepSeek run

Ask the connected client to use a DeepSeek V4 model such as `deepseek-v4-pro` for a coding or reasoning task. Model availability and pricing come from the live catalog. DeepSeek V4 supports up to 1M tokens of context; configure the client’s context limit when available.

For read-only diagnostics:

```bash
sandbase doctor --json
```

See the [SandBase CLI README](https://github.com/sandbaseai/cli) for clients, checksums, rollback, and the complete MCP tool list.

