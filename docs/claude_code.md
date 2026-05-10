[English](./claude_code.md) | [简体中文](./claude_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Claude Code

Claude Code is an AI coding assistant that runs in the terminal (or VSCode Extension).

### Installing Claude Code from Scratch

Claude Code can be used via CLI or VSCode Extension. Choose whichever you prefer.

#### Option 1: Install Claude Code CLI

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

#### Option 2: Install Claude Code VSCode Extension

- Install [VSCode](https://code.visualstudio.com/)
- Install [Claude Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)

After installation, search for the VSCode setting `claudeCode.disableLoginPrompt` and enable it.

### Configuring Claude Code

Claude Code can be configured via a configuration file or environment variables. In most cases, prefer the configuration file approach, as settings in the configuration file can be read by both Claude Code CLI and VSCode Extension.

#### Option 1: Configure via Configuration File

Configuration file location:
- Linux / Mac: `~/.claude/settings.json`
- Windows: `C:\Users\<your username>\.claude\settings.json`
- **If the file does not exist, create it.**

Configuration file content:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<your DeepSeek API Key>",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash[1m]",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

#### Option 2: Configure Environment Variables

Linux / Mac users, run the following commands to configure environment variables for the [DeepSeek Anthropic API](https://api.deepseek.com/anthropic). Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys):

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<your DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash[1m]
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
export CLAUDE_CODE_EFFORT_LEVEL=max
```

Windows users, run:

```
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<your DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash[1m]"
$env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```

### Using Claude Code

#### Using Claude Code CLI

Enter the project directory and execute the `claude` command to get started.

```
cd /path/to/my-project
claude
```

<div align="center">
<img src="https://cdn.deepseek.com/api-docs/cc_example.png" width='1024' border='1'  />
</div>

#### Using Claude Code VSCode Extension

Open your project directory in VSCode, click the Claude Code icon in the sidebar, and click `New session` to get started.

![Using Claude Code in VSCode Extension](./assets/claude_code_vsc_ext.png "Using Claude Code in VSCode Extension")
