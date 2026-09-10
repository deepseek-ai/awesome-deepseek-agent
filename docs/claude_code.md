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
## Troubleshooting DeepSeek + Claude Code

### HTTP 400 errors

If Claude Code returns an HTTP 400 error while using the DeepSeek Anthropic-compatible endpoint, do not immediately assume that the API key or network is invalid. First verify the endpoint independently with a minimal API request, then inspect the Claude Code debug output for the exact model name and error text.

Useful checks:

```powershell
claude --version
$env:ANTHROPIC_BASE_URL
$env:ANTHROPIC_MODEL
```

Do not print the real value of `ANTHROPIC_AUTH_TOKEN` in logs or issue reports.

### `unrecognized_model` or model-related 400 responses

A model-related 400 may indicate an incompatibility between the Claude Code version and the DeepSeek Anthropic-compatible endpoint.

One reproducible community report in this repository documents a different version-specific 400: Claude Code v2.1.154 sent a `system` role that the endpoint rejected, while v2.1.153 worked with the same configuration. See [Issue #167](https://github.com/deepseek-ai/awesome-deepseek-agent/issues/167).

In another independent test environment, Claude Code v2.1.266 returned 400 responses containing `unrecognized_model` for DeepSeek V4 Pro/Flash. With the same DeepSeek endpoint and credentials, Claude Code v2.1.153 was then verified to work for both model types, including tool calls.

Because compatibility can be version-specific, use this minimal isolation procedure:

1. Confirm the DeepSeek Anthropic endpoint works outside Claude Code.
2. Record the exact Claude Code version with `claude --version`.
3. Run a minimal request with `--print` or a one-line prompt.
4. Enable `--debug` if the error is still unclear.
5. Check the reported model name and error body.
6. Test a second Claude Code version without deleting the first installation.
7. Re-test both a simple prompt and a tool call before changing the rest of the configuration.

Do not treat a single version pairing as a universal fix. Report the exact Claude Code version, DeepSeek model, endpoint, and error text so others can reproduce the case.

### Windows PowerShell: `.ps1` execution-policy errors

If PowerShell blocks `npm.ps1` or `claude.ps1`, try the Windows command wrappers first:

```powershell
npm.cmd -v
claude.cmd --version
```

This avoids changing the system execution policy just to launch the tools.

### Claude Code native binary replacement problem

If a Windows installation leaves a file such as `claude.exe.old.<timestamp>` but no `claude.exe`, first inspect the installation state and avoid repeatedly running install/upgrade commands while troubleshooting. In a verified v2.1.153 recovery case, the existing `.old` binary was restored to `claude.exe` and the executable then started successfully.

Only restore a renamed binary after confirming that it is the expected version and was previously verified in the same installation. Do not copy binaries from unrelated installations.

### Reporting a reproducible issue

When opening an issue, include:

- Operating system
- Claude Code version
- DeepSeek model
- `ANTHROPIC_BASE_URL`
- Whether the minimal API request succeeds
- Exact HTTP status and error text
- Whether the failure affects normal prompts, tool calls, or both
- Relevant debug-log lines with all API keys and secrets removed
