[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Pi

[Pi](https://github.com/earendil-works/pi) 是一个极简、可扩展的终端编码 Agent，支持树状会话、技能与扩展。当前版本已**内置 DeepSeek 供应商**，接入 DeepSeek 只需要一个 API Key —— 不需要 `models.json`、自定义供应商配置或兼容层代理。

#### 1. 安装 Pi

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 22.19 或更高版本。
- 通过 npm 安装 Pi：

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

Windows 用户请使用上面的 npm 命令。macOS / Linux 用户也可以使用官方安装脚本，该脚本会固定依赖版本，并通过 `pi update` 更新：

```bash
curl -fsSL https://pi.dev/install.sh | sh
```

- 验证安装：

```bash
pi --version
```

#### 2. 配置 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

**方式一：在 Pi 中登录（推荐）**

启动 Pi，执行 `/login deepseek`，然后粘贴 API Key：

```text
$ pi
/login deepseek
```

Pi 会把凭据保存在 `~/.pi/agent/auth.json`。

![Pi 提示输入 DeepSeek API Key](./assets/pi_deepseek_login.png)

**方式二：使用环境变量**

Linux / macOS：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows PowerShell：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

检查 Pi 是否已识别该凭据：

```bash
pi auth check --provider deepseek --json
# {"status":"ready","provider":"deepseek","authType":"api_key"}
```

#### 3. 选择 DeepSeek 模型

在项目目录中启动 Pi，输入 `/model` 打开模型选择器，再输入 `deepseek` 过滤：

```bash
cd /path/to/my-project
pi
```

![Pi 模型选择器中的内置 DeepSeek 模型](./assets/pi_deepseek_model_picker.png)

| 模型 ID           | 模型                 | 适用场景             | 上下文 | 最大输出 |
| ----------------- | -------------------- | -------------------- | ------ | -------- |
| `deepseek-v4-pro` | DeepSeek V4 Pro      | 高难度编码与推理     | 1M     | 384K     |
| `deepseek-flash`  | DeepSeek V4.1 Flash  | 快速、低成本、支持视觉 | 1M     | 384K     |

当 DeepSeek 是唯一配置了凭据的供应商时，Pi 默认选择 `deepseek-v4-pro`。在选择器中按 `Ctrl+S` 可将其设为启动默认模型。

Pi 的模型目录已经声明了 1M 上下文和 384K 最大输出，因此无需再设置 `context_window` 或 `max_tokens`。

也可以在单次运行时固定模型和思考等级：

```bash
pi --model deepseek/deepseek-v4-pro:max
```

> 请使用当前模型 ID。API 仍接受旧名称 `deepseek-v4-flash` 和 `deepseek-v4-flash-vision-exp`，但对应模型已下线：请求会由 DeepSeek-V4.1-Flash 处理，在 Pi 中的模型 ID 为 `deepseek-flash`。

#### 4. 设置思考等级

DeepSeek V4 模型默认启用思考模式。执行 `/thinking` 可以查看或调整：

![Pi 思考等级选择器：off、high、max](./assets/pi_deepseek_thinking_level.png)

- `off` —— 不推理
- `high` —— Pi 对该模型的默认等级
- `max` —— 面向高难度问题的最大推理量

在会话中按 `Shift+Tab` 可循环切换思考等级，按 `Ctrl+S` 保存启动时的等级。如果你是在当前会话中刚完成登录，请执行一次 `/thinking` 并选择 `high` 或 `max`。

#### 5. 首次运行

让 Pi 处理项目里的任务。它会读取和修改文件、执行命令，并把整个会话记录为可回退的树状结构。

![Pi 使用 DeepSeek V4 Pro 执行任务](./assets/pi_deepseek_first_run.png)

状态栏会显示当前模型、思考等级、上下文用量和预估费用。

#### 配置参考

| 项目       | 值                                                       |
| ---------- | -------------------------------------------------------- |
| 供应商 ID  | `deepseek`（内置）                                       |
| Base URL   | `https://api.deepseek.com`                               |
| API 格式   | OpenAI 兼容（`openai-completions`）                      |
| 凭据方式   | `/login deepseek`、`DEEPSEEK_API_KEY` 或 `--api-key`     |
| 上下文长度 | 1,000,000 tokens                                         |
| 最大输出   | 384,000 tokens                                           |
| 思考等级   | `off`、`high`、`max`                                     |

无需编写 `models.json`。如果需要经过网关或自建端点，请在 `~/.pi/agent/models.json` 中新增一个独立的供应商，而不是覆盖内置的 `deepseek` 供应商。

#### 价格

下表中的价格为每 100 万 tokens 的美元价格，来自 [DeepSeek 定价页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。高峰时段为 UTC 周一至周五 01:00–04:00 与 06:00–10:00（中国法定节假日除外），其余时间为低谷时段。

| 模型                         | 缓存命中 | 缓存未命中 | 输出  |
| ---------------------------- | -------- | ---------- | ----- |
| `deepseek-v4-pro`（低谷）    | $0.022   | $0.66      | $1.98 |
| `deepseek-v4-pro`（高峰）    | $0.044   | $1.32      | $3.96 |
| `deepseek-flash`（低谷）     | $0.003   | $0.15      | $0.60 |
| `deepseek-flash`（高峰）     | $0.006   | $0.30      | $1.20 |

Pi 会话中的费用估算使用模型目录里的高峰价格，因此低谷时段的实际账单约为显示值的一半。

#### 常见问题

| 现象                                                           | 处理方式                                                                                     |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `/model` 为空，或提示 "Only showing models from configured providers" | 尚未配置凭据。执行 `/login deepseek` 或导出 `DEEPSEEK_API_KEY`，然后重新打开 `/model`。      |
| `401` 或其他鉴权错误                                           | 到 DeepSeek 开放平台核对 Key，然后重新执行 `/login deepseek`。                               |
| 提示模型不存在                                                 | 使用 `deepseek-v4-pro` 或 `deepseek-flash`；`deepseek-chat`、`deepseek-reasoner` 已不存在。   |
| Pi 版本较旧，没有 DeepSeek                                     | 执行 `pi update` 更新，或从 npm 重新安装。                                                   |

#### 了解更多

- [Pi 文档](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs)
- [Pi 模型配置](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
