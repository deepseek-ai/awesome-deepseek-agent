[English](./desca.md) | [简体中文](./desca.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 desca

<div align="center">
<img src="https://github.com/ChangedenCZD/desca/raw/refs/heads/develop/assets/logo.svg" width='640' />
</div>

**desca**（**De**ep**s**eek **C**oding **A**gent）是一个面向 DeepSeek 模型生态的 **终端 AI 编码助手**，使用 **Go 1.25 + Charmbracelet TUI** 构建。核心架构为**单 Agent 主循环 + 工具驱动**，通过 `task` 工具委托子 Agent 执行独立任务。

## 密钥获取

### 1. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取`Api-Key`。desca 首次启动会有以弹窗形式填写`Api-Key`并持久化到 `~/.desca/settings.toml`，且用户可通过`/connect`切换`Api-Key`。


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
