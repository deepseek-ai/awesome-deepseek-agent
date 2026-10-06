[English](./tianshu.md) | [简体中文](./tianshu.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入天枢 (Tianshu)

天枢（Tianshu）是开源的编程智能体运行时，终端 TUI 与桌面端共用同一个内核。内置的 DeepSeek 预设直接请求 `https://api.deepseek.com/v1`，不用手填 Base URL。

预设带两个当前模型 id。两者上下文都是 100 万 token，单次输出上限 256,000 token。天枢会在每次请求里发送 `reasoning_effort`。两个模型的预设默认档都是 `high`。

| 模型 id | 对应模型 | 默认推理档 |
| --- | --- | --- |
| `deepseek-flash` | DeepSeek-V4.1-Flash，这是默认模型 | `high` |
| `deepseek-v4-pro` | DeepSeek-V4-Pro | `high` |

`deepseek-v4-flash` 已于 2026-10-04 从该预设退役。官方 API 仍接受这个旧 id，并由 V4.1 Flash 承接。官方 `deepseek` 提供商上，天枢会把已保存的 `deepseek-v4-flash` 改写成 `deepseek-flash`。请配置新 id。

#### 1. 安装 Node.js

- 安装 [Node.js](https://nodejs.org/en/download/) 24 或更高版本。
- Windows 用户还需安装 [Git for Windows](https://git-scm.com/download/win)。

#### 2. 安装天枢

```bash
npm install -g tianshu-harness
```

`tianshu` 和 `rivet` 是同一个程序。桌面端（macOS、Windows、Linux）在 [GitHub Releases](https://github.com/huiliyi37/Tianshu-harness/releases/latest) 下载，不需要先装 Node.js。

#### 3. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 Key。

```bash
export DEEPSEEK_API_KEY="sk-..."
```

Windows（PowerShell）：

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
```

#### 4. 写入 DeepSeek 预设

第一次启动会打开 `/connect`。选择 **DeepSeek** 并完成 Key 步骤，用的就是内置预设。

也可以在启动前配好：

```bash
tianshu config setup deepseek --key-env DEEPSEEK_API_KEY --default
```

不要另外传一个更小的 `--context-window`。压缩阈值跟着这个数走，而预设里两个模型都是 100 万 token。桌面端在 **设置 → Provider** 里使用同一套预设。

#### 5. 开始一次会话

```bash
cd /path/to/your-project
tianshu
```

在 TUI 里：

```text
/model list
/model deepseek-v4-pro
/effort max
```

`/model deepseek-flash` 切回 V4.1 Flash。`/effort max` 让后续轮次使用 `max` 推理档。写进配置的 `reasoningEffort: max` 会被保留，自动降档不会把它降下去。不要关掉思考模式。

<div align="center">
<img src="https://raw.githubusercontent.com/huiliyi37/Tianshu-harness/main/docs/brand/assets/tianshu-banner-dark.jpg" width="640" alt="天枢" />
</div>
