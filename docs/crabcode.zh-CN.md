[English](./crabcode.md) | [简体中文](./crabcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 CrabCode

CrabCode（蟹码）是 Acosmi 打造的 AI 编程助手与一站式个人 AI 工作台，提供终端原生的 TUI 与桌面 GUI 两种形态。与列表中大多数工具不同，**DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 已内置开箱即用** —— 登录后选个模型即可开始编码，无需配置代理或 API Key。

- **官方网站：** <https://acosmi.com/zh>
- **Releases（命令行 TUI 版）：** <https://github.com/acosmi/crabcode/releases/latest>

#### 1. 安装 CrabCode

**命令行 TUI — macOS / Linux**（自动识别平台、校验 SHA-256、配置 `PATH`）：

```bash
curl -fsSL https://updates.acosmi.com/crabcode/install.sh | sh
```

**命令行 TUI — Windows**（在 PowerShell 中执行）：

```powershell
irm https://updates.acosmi.com/crabcode/install.ps1 | iex
```

验证安装：

```bash
crabcode --version
```

**桌面 GUI 版** —— 前往[官方下载页](https://acosmi.com/zh/downloads)下载安装包（macOS / Linux），或从 [GitHub Releases](https://github.com/acosmi/crabcode/releases/latest) 下载（Windows）。

#### 2. 登录 —— DeepSeek 已内置

在 <https://acosmi.com/zh> 注册账号，然后在 CrabCode 内执行 `/login` 完成认证：

```bash
crabcode
/login
```

新用户注册即享**免费一个月 Basic 基础版会员，赠送 6000 万 Credits**，畅用 DeepSeek、Qwen3.7、MiniMax-M3、GLM-5.2 等国内主流模型。DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 均在内置模型目录中，无需额外 API Key。

#### 3. 切换到 DeepSeek 模型

在 TUI 中执行 `/model`（或使用 GUI 的模型选择器），选择：

- `deepseek-v4-pro` —— 旗舰模型，适合复杂编码任务
- `deepseek-v4-flash` —— 高速高性价比模型（也是默认模型）

DeepSeek V4 系列支持 **100 万 token（1M）上下文窗口**。受支持模型的思考模式默认自动开启；按 `Tab` 循环切换推理强度，或通过 `/effort` 显式设置（`low` → `medium` → `high` → `max`）——在 DeepSeek-V4-Pro 上使用 `max` 可获得最佳编码体验。

#### 4. 首次运行

```bash
cd /path/to/my-project
crabcode
```

也可以不进入交互界面，直接一次性提问：

```bash
crabcode -p "解释当前目录的代码结构"
```

#### 可选：使用自己的 DeepSeek API Key

如果你已有 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 的 API Key，CrabCode 同样支持自定义 OpenAI / Anthropic 兼容提供商。在模型设置中添加 DeepSeek 为自定义提供商（Base URL 为 `https://api.deepseek.com/v1`，模型 ID 为 `deepseek-v4-pro` / `deepseek-v4-flash`），CrabCode 即可将请求路由到你自己的 DeepSeek 账户。

#### 速查表

| 命令 / 按键 | 作用 |
|---|---|
| `/login` | 登录或切换账号 |
| `/model` | 查看和切换模型 |
| `/effort` | 设置推理强度（low / medium / high / max） |
| `Tab` | 循环切换推理强度 |
| `Esc` | 中断当前回合 |
| `/update` | 更新 CrabCode 到最新版本 |
