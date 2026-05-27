[简体中文](./desca.zh-CN.md) | [English](./desca.md) · [← Back](../README.md)

# Access desca

<div align="center">
<img src="https://github.com/ChangedenCZD/desca/raw/refs/heads/develop/assets/logo.svg" width='640' />
</div>

**desca** (**De**ep**s**eek **C**oding **A**gent) is a **terminal AI coding assistant** for the DeepSeek model ecosystem, built with **Go 1.25 + Charmbracelet TUI**. Its core architecture is a **single-agent main loop + tool-driven** approach, delegating independent tasks to sub-agents via the `task` tool.

## Obtaining an API Key

### 1. Get a DeepSeek API Key

Obtain an `Api-Key` from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys). When desca is launched for the first time, a pop-up window will prompt you to enter the `Api-Key`, which will then be persisted in `~/.desca/settings.toml`. Users can also switch the `Api-Key` using the `/connect` command.

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
