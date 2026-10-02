# LongClaw Integration Guide for DeepSeek

[简体中文](./longclaw.zh-CN.md)

## Introduction

[LongClaw](https://longclaw.cc) is a cross-platform AI desktop assistant for Windows, macOS, and Linux. It features a built-in ClawHub skill marketplace for extending capabilities and supports the MCP (Model Context Protocol) for integrating external tools. LongClaw can connect to WeChat, QQ, Feishu, and other chat platforms, bringing AI capabilities seamlessly into your daily communication.

## Prerequisites

1. Visit [DeepSeek Platform](https://platform.deepseek.com/) to register and get your API Key.
2. Download and install LongClaw: [https://longclaw.cc/download](https://longclaw.cc/download)

## Installation

### Windows

Download the Windows installer (`.exe`) and run the setup wizard.

### macOS

Download the macOS package (`.dmg`) and drag it to the Applications folder.

### Linux

Download the Linux package (`.AppImage` or `.deb`), grant execution permission, and run:

```bash
chmod +x LongClaw-*.AppImage
./LongClaw-*.AppImage
```

## Configure DeepSeek

1. Open LongClaw and go to Settings → Model Configuration.
2. Click "Add Model" and select "OpenAI Compatible" type.
3. Fill in the following configuration:
   - **API Endpoint**: `https://api.deepseek.com/v1`
   - **Model Name**: `deepseek-v4-pro` (recommended) or `deepseek-v4-flash`
   - **API Key**: Your DeepSeek API Key
   - **Context Window**: `1000000` (1M context support)
   - **Max Tokens**: `384000`
4. Save the configuration.

## Enable Deep Thinking Mode

DeepSeek V4 Pro supports multiple reasoning effort levels (`max` and `high`). In LongClaw:

1. Go to Settings → Model Configuration → select DeepSeek model → Advanced Options.
2. Add the following in "Extra Parameters":
   ```json
   {
     "reasoning_effort": "max"
   }
   ```
3. After saving, all conversations using this model will automatically use the maximum reasoning effort.

## First Run

1. In the LongClaw main interface, click the model selector above the input box and switch to `deepseek-v4-pro`.
2. Start a conversation to test DeepSeek's response quality.
3. To connect chat tools, go to Settings → Chat Tools and follow the instructions to configure WeChat/QQ/Feishu bots.

## Skill Marketplace Extension

LongClaw supports extending AI capabilities via [ClawHub](https://clawhub.ai):

1. Click "Skill Marketplace" in the sidebar.
2. Search for skills you need (e.g., "Code Review", "Document Generation").
3. Install with one click and use immediately.

## MCP Protocol Support

LongClaw natively supports the MCP protocol for integrating external tools:

1. Go to Settings → MCP Tools.
2. Add MCP server configurations (e.g., file system, database, search).
3. The AI will automatically invoke these tools to complete tasks.

## Resources

- [LongClaw Official Website](https://longclaw.cc)
- [LongClaw Documentation](https://docs.longclaw.cc)
- [ClawHub Skill Marketplace](https://clawhub.ai)
- [DeepSeek API Documentation](https://api-docs.deepseek.com/)
