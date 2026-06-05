[English](./desca.md) | [简体中文](./desca.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 desca

<div align="center">
<img src="https://raw.atomgit.com/changeden/desca/files/main/assets/logo.svg" width='640' />
</div>

**desca**（**De**ep**s**eek **C**oding **A**gent）是一个面向 DeepSeek 模型生态的 **终端 AI 编码助手**。核心架构为**单 Agent 主循环 + 工具驱动**，通过 `task` 工具委托子 Agent 执行独立任务。

## 密钥获取

### 1. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取`Api-Key`。编辑 `~/.desca/settings.json`，修改`models.deepseek.apiKey` 值并保存文件，重新启动 `desca`。

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
          "alias": "deepseek-v4-flash (免费)",
          "contextLimit": 200000,
          "outputLimit": 32768,
          "ignoreAuthorization": true
        }
      ]
    }
  }
}
```

## 安装使用

### 1. 在线安装

```bash
curl -fsSL https://desca.opencj.cn/downloads/install | bash
```

### 2. 一键启动

#### 进入工作目录

```bash
cd 你的工作目录
```

#### 启动desca

```bash
desca
```

#### 恢复最后一个会话

```bash
desca -c
```

#### 恢复某个会话

```bash
desca -r
```
