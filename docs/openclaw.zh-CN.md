[English](./openclaw.md) | [简体中文](./openclaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenClaw

OpenClaw 是一个开源的个人 AI 助手，可接入 Telegram、Discord、WhatsApp、Slack、Signal、iMessage 等 15+ 聊天平台，并通过 Skills、定时任务和多智能体编排进行扩展。它可以运行在任何 Linux 服务器上，也是 **Mirinda OS**（一个为 DeepSeek V4 优化的西班牙 Linux 发行版）的核心引擎。

## 1. 安装 OpenClaw

**Linux / Mac：**
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Windows：**
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

> **Mirinda OS 用户**：OpenClaw 已预装并预配置。直接跳转到[第 3 节](#3-开始使用)。

**最低配置要求：**
- Node.js 18+
- 2 GB RAM（多智能体工作负载建议 4 GB）
- 1 GB 可用磁盘空间

## 2. 配置 DeepSeek V4

安装后运行配置向导：

```bash
openclaw onboard --install-daemon
```

配置步骤：
- **Setup mode**：选择 **QuickStart**
- **Model/auth provider**：选择 **DeepSeek**
- **API Key**：填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- **Default model**：输入 `deepseek-v4-pro`（推荐，适合复杂任务）或 `deepseek-v4-flash`（更轻量、更快）

### 手动配置（高级）

编辑 `~/.openclaw/gateway/config.yaml`：

```yaml
models:
  providers:
    deepseek:
      baseUrl: https://api.deepseek.com/v1
      apiKey: ${DEEPSEEK_API_KEY}
  default: deepseek/deepseek-v4-pro

agent:
  thinking: high          # 'max' 最强推理，'high' 平衡模式
  contextWindow: 1000000  # DeepSeek V4 支持 1M token 上下文
  maxTokens: 384000
```

### 模型选择指南

| 模型 | 适用场景 | 上下文 | 推理模式 |
|------|---------|--------|---------|
| `deepseek-v4-pro` | 复杂推理、编程、分析 | 1M tokens | `max` / `high` |
| `deepseek-v4-flash` | 快速任务、简单查询、成本敏感 | 1M tokens | `off` |

> **定价（自 2026 年 5 月起永久 75% 折扣）：**
> - `deepseek-v4-pro`：$0.435/M 输入 · $0.87/M 输出 · $0.0028/M 缓存命中
> - `deepseek-v4-flash`：$0.145/M 输入 · $0.29/M 输出 · $0.0028/M 缓存命中

### 版本要求

确保 OpenClaw >= **v2026.4.24** 以获得 DeepSeek V4 Thinking Mode 支持。旧版本会在 `reasoning_content` 上报 `400` 错误。升级命令：

```bash
openclaw update
```

## 3. 开始使用

### 终端 TUI
```bash
openclaw tui
```

### Web 控制台
```bash
openclaw dashboard
```
打开 `http://localhost:18700` — 完整的聊天界面，支持会话管理、模型切换和推理开关。

### 命令行对话
```bash
openclaw terminal
```

### 接入聊天平台

OpenClaw 支持 15+ 个聊天平台。通过控制台或配置文件进行配置：

```yaml
# ~/.openclaw/gateway/config.yaml
channels:
  telegram:
    token: ${TELEGRAM_BOT_TOKEN}
  discord:
    token: ${DISCORD_BOT_TOKEN}
  whatsapp:
    # 基于 Baileys 的 Web 接入
```

接入后，你可以从任何平台与 OpenClaw 智能体对话 — 所有平台共享同一份记忆、Skills 和上下文。

## 4. 高级配置

### Thinking Mode（推理模式）

DeepSeek V4 Pro 支持多个推理强度级别。可按会话或全局配置：

```bash
# 通过 CLI
openclaw terminal --thinking=max

# 通过 API/配置
thinking: max   # 最强推理深度（适合编程、架构设计）
thinking: high  # 平衡推理（默认，适合大多数任务）
thinking: off   # 无推理 token（最快，V4 Flash 默认）
```

### 上下文窗口优化

DeepSeek V4 支持高达 **1,000,000 token** 的上下文。OpenClaw 通过以下方式充分利用：

- **缓存命中仅 $0.0028/M tokens**：复用之前的上下文，大幅降低成本
- **记忆系统**：跨会话的持久化长期记忆（`MEMORY.md`、`memory/YYYY-MM-DD.md`）
- **自动上下文裁剪**：OpenClaw 管理上下文窗口以防止溢出

**实际缓存命中率：OpenClaw + DeepSeek V4 Pro 达到 85–98%**，使有效成本降至约 $0.03–0.05/M tokens。

### 多智能体编排

OpenClaw 支持创建子智能体进行并行工作：

```bash
# 从聊天或 TUI 中，生成隔离的子智能体
openclaw spawn "分析这个代码库" --model deepseek-v4-pro --thinking=max
```

子智能体继承工作区访问权限，但在隔离的上下文中运行，支持并行任务执行。

### 定时任务与自动化

使用 OpenClaw 的 cron 系统调度周期性任务：

```yaml
# 示例：每天上午 9 点的日报
- name: morning-report
  schedule: { kind: cron, expr: "0 9 * * *", tz: Europe/Madrid }
  payload: { kind: agentTurn, message: "生成今日摘要" }
```

### Skills 生态系统

OpenClaw 通过 Skills（自包含的能力模块）进行扩展。内置和社区 Skills 包括：

| Skill | 描述 |
|-------|------|
| Network Toolbox | DNS、ping、路由追踪、SSL、WHOIS、端口扫描 |
| Browser Automation | 基于 CDP 的浏览器操作，带反检测 |
| Email Monitoring | 多收件箱 IMAP 监控，带去重 |

Skills 通过 `skills/` 目录安装并自动加载。

## 5. 生产环境部署

### 作为守护进程运行
```bash
openclaw gateway start --daemon
```

### Systemd 服务（推荐）
```ini
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=openclaw
ExecStart=/usr/local/bin/openclaw gateway start
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Mirinda OS — 预配置的 DeepSeek 环境

**Mirinda OS** 是一个西班牙 Linux 发行版，预装并优化了 OpenClaw + DeepSeek V4 Pro：

- **为 AI 工作负载调优的内核**：BBR 拥塞控制、ZRAM 压缩、`performance` CPU 调度器
- **DeepSeek V4 Pro 作为默认模型**：1M 上下文、thinking=high、永久 75% 折扣定价
- **预加载 Skills**：网络诊断、浏览器自动化、邮件监控
- **系统仪表盘**：实时 CPU/RAM/磁盘监控，可推送到任意 Web 主机
- **Surface 3 版**：轻量级 XFCE 变体，搭载 `linux-surface` 内核，适配 2–4 GB RAM 设备

**获取 Mirinda OS：** [mirinda-os.github.io](https://mirinda-os.github.io)（提供 General 和 Surface 3 版本的 ISO 下载）

> Mirinda OS 由西班牙 OpenClaw 社区维护。它是从汽车经销商到家庭服务器等各类生产环境中运行 OpenClaw + DeepSeek 的参考部署方案。

## 6. 故障排除

### `400 Bad Request: reasoning_content`
你的 OpenClaw 版本太旧。升级到 >= v2026.4.24：
```bash
openclaw update
```

### `401 Unauthorized: invalid api key`
- 在 [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys) 验证你的 API Key
- 确保 Key 有足够的余额（通过 `openclaw status` 检查）

### 首次消息延迟高
首次消息需要冷启动模型加载。后续消息受益于**缓存命中** — 首次交换后可预期 2–5 倍的速度提升。

### 模型返回截断的回复
在配置中增加 `maxTokens`。DeepSeek V4 支持高达 384,000 个输出 token。
```yaml
agent:
  maxTokens: 384000
```
