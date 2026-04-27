[English](./claude_code.md) | [简体中文](./claude_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Claude Code

Claude Code 是一个运行在终端内的 AI 编程助手。

#### 1. 安装 Claude Code

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 18+。
- Windows 用户需安装 [Git for Windows](https://git-scm.com/download/win)。
- 在命令行界面，执行以下命令安装 Claude Code：

```
npm install -g @anthropic-ai/claude-code
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```
claude --version
```

#### 2. 配置环境变量

Linux / Mac 用户执行以下命令配置 [DeepSeek Anthropic API](https://api.deepseek.com/anthropic) 环境变量，其中 API Key 在 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 获取：

```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash
export CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flash
export CLAUDE_CODE_EFFORT_LEVEL=max
```

Windows 用户执行：

```
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<你的 DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_SUBAGENT_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```

#### 3. 进入项目目录，执行 `claude` 命令，即可开始使用了。

```
cd /path/to/my-project
claude
```

<div align="center">
<img src="https://cdn.deepseek.com/api-docs/cc_example.png" width='1024' border='1'  />
</div>
