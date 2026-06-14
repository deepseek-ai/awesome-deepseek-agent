[简体中文](./desca.zh-CN.md) | [English](./desca.md) · [← Back](../README.md)

# Access desca

<div align="center">
<img src="https://raw.atomgit.com/changeden/desca/files/main/assets/logo.svg" width='640' />
</div>

**desca** (short for **De**ep**s**eek **C**oding **A**gent) is a **terminal-based AI coding assistant** built for the DeepSeek model ecosystem. Its core architecture is a **single Agent main loop + tool-driven**, delegating independent tasks to sub-agents via the `task` tool.

## Obtaining an API Key

### 1. Get a DeepSeek API Key

Obtain an `Api-Key` from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys). Edit `~/.desca/settings.json`, modify the value of `models.deepseek.apiKey`, save the file, and restart `desca`.

### settings.json

```json
{
  "models": {
    "default": "deepseek/deepseek-v4-flash",
    "deepseek": {
      "name": "deepseek",
      "baseUrl": "https://api.deepseek.com",
      "protocol": "openai",
      "apiKey": "sk-xxx",
      "defaultModel": "deepseek-v4-flash",
      "models": [
        {
          "id": "deepseek-v4-flash",
          "contextLimit": 1000000,
          "outputLimit": 384000
        },
        {
          "id": "deepseek-v4-pro",
          "contextLimit": 1000000,
          "outputLimit": 384000
        }
      ]
    },
    "opencode": {
      "name": "opencode",
      "baseUrl": "https://opencode.ai/zen/v1",
      "protocol": "openai",
      "apiKey": "",
      "defaultModel": "deepseek-v4-flash-free",
      "models": [
        {
          "id": "deepseek-v4-flash-free",
          "alias": "deepseek-v4-flash (free)",
          "contextLimit": 200000,
          "outputLimit": 32768,
          "ignoreAuthorization": true
        }
      ]
    }
  }
}
```

## Installation and Usage

### 1. Online Installation

```bash
curl -fsSL https://desca.opencj.cn/downloads/install | bash
```

### 2. One-Click Launch
#### Navigate to your working directory
```bash
cd your-working-director
```

#### Start desca
```bash
desca
```

#### Resume the last session

```bash
desca -c
```

#### Resume a specific session

```bash
desca -r
```
