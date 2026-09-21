[English](./openclacky.md) | [简体中文](./openclacky.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 OpenClacky

[OpenClacky](https://github.com/clacky-ai/openclacky) 是目前最省 Token 的开源 AI Agent（MIT 协议）。原生支持 DeepSeek，对 `reasoning_content` 处理良好，缓存命中率接近 100%，一个二进制即可使用 Web UI / 终端 / 飞书 / 企业微信 / 微信 / Discord / Telegram。

#### 1. 安装 OpenClacky

**macOS / Linux**

```bash
/bin/bash -c "$(curl -sSL https://raw.githubusercontent.com/clacky-ai/openclacky/main/scripts/install.sh)"
```

**Windows**

```powershell
powershell -c "& ([scriptblock]::Create((irm 'https://raw.githubusercontent.com/clacky-ai/openclacky/main/scripts/install.ps1')))"
```

**或通过 RubyGems 安装**（需 Ruby >= 3.1.0）：

```bash
gem install openclacky
```

桌面端安装包（`.dmg` / `.exe`）可在 [openclacky.com](https://www.openclacky.com/) 下载。

#### 2. 配置 DeepSeek 作为默认模型

启动 OpenClacky，打开配置菜单：

```bash
openclacky
> /config
```

按下表填写：

| 字段 | 值 |
| --- | --- |
| Provider | **DeepSeek**（内置） |
| Base URL | `https://api.deepseek.com` |
| API Key | 你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| Model | `deepseek-v4-pro`（推荐）或 `deepseek-v4-flash` |
| 上下文窗口 | `1000000`（DeepSeek V4 支持 1M tokens） |
| Reasoning effort | `max`（编码体验最佳），也支持 `high` |

OpenClacky 对 DeepSeek V4 有原生一等支持，正确回传 `reasoning_content`，**无需关闭** Thinking Mode。保持 `reasoning_effort=max` 可以获得最佳编码效果。

#### 3. 开始使用

**Web UI**（推荐，多会话并行 —— 编码 / 研究 / 文案同时跑）：

```bash
openclacky server          # http://localhost:7070
openclacky server --port 8080
openclacky server --host 0.0.0.0   # 允许远程访问
```

**终端模式**：

```bash
openclacky                 # 在当前目录启动交互式 Agent
```

**新建项目脚手架**：

```bash
$ openclacky
> /new my-app
> 帮我加一个邮箱密码登录
```

#### 4. 这套组合为什么省钱

- **~100% Prompt 缓存命中** —— 会话不重启、System Prompt 不被修改、空闲时自动压缩并预热缓存。配合 DeepSeek $0.003625 / M tokens 的缓存命中价，长会话实际花费大幅下降。
- **16 个核心工具 + `invoke_skill`** —— 工具 schema 小，请求体小，1M 上下文窗口能装下更多有效内容。
- **BYOK 多模型路由** —— 主 Agent 用 `deepseek-v4-pro`，子任务路由到 `deepseek-v4-flash`，再省一档。

更多文档：[openclacky.com/docs](https://www.openclacky.com/docs/installation) · [GitHub](https://github.com/clacky-ai/openclacky)
