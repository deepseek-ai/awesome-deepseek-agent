[English](./claude_code.md) | [简体中文](./claude_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Claude Code

Claude Code is an AI coding assistant that runs in the terminal.

#### 1. Install Claude Code

- Install [Node.js](https://nodejs.org/en/download/) 18+.
- Windows users need to install [Git for Windows](https://git-scm.com/download/win).
- Run the following command in your terminal to install Claude Code:

```
npm install -g @anthropic-ai/claude-code
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```
claude --version
```

#### 2. Configure Environment Variables

Linux / Mac users, run the following commands to configure environment variables for the [DeepSeek Anthropic API](https://api.deepseek.com/anthropic). Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys):

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<your DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash
export CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flash
export CLAUDE_CODE_EFFORT_LEVEL=max
```

Windows users, run:

```
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<your DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_SUBAGENT_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```

#### 3. Enter the project directory and execute the `claude` command to get started.

```
cd /path/to/my-project
claude
```

<div align="center">
<img src="https://cdn.deepseek.com/api-docs/cc_example.png" width='1024' border='1'  />
</div>
