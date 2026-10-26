[English](./jpcode.md) | [简体中文](./jpcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 JPCode

JPCode 是一款面向 Windows 与 macOS 的对话式 AI 开发助手，全栈基于自研 C++20 引擎实现。它是桌面客户端形态：用自然语言描述需求，Agent 负责规划、改代码、构建与测试，命令既可以在本机 PowerShell / zsh 执行，也可以直接下发到远程 SSH 目标机。

JPCode 内置 DeepSeek 服务商预设（`https://api.deepseek.com`，Responses API），同时也支持把任意 OpenAI / Anthropic 兼容服务配成自定义供应商。

> 两种接入方式任选其一：
>
> - **侏罗纪 AI 编程套餐（内置）**：登录 JPCode 即可使用套餐内的模型，无需自备 API Key，按月订阅、统一账单与用量统计。
> - **自备 DeepSeek API 密钥**：把 DeepSeek 作为服务商预设接入，费用由 DeepSeek API 账户直接结算。本指南介绍这种方式的配置步骤。

### 从零安装 JPCode

JPCode 是单文件安装包分发的桌面应用，支持 Windows 与 macOS。

- 前往 [JPCode 官网](https://jpcode.jurassic-period.com/) 点击「下载客户端」，Windows 安装包文件名形如 `JPCode-<版本>-setup.exe`。
- 运行安装包，启动 JPCode。
- 可选：如果不想把密钥存在界面里，可在启动 JPCode 之前设置环境变量 `DEEPSEEK_API_KEY`。环境变量优先级高于界面中保存的值。

### 配置 JPCode

配置服务商前，先在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API 密钥。

4. **选择模型**：打开「模型」下拉，预设含 `deepseek-v4-pro` 与 `deepseek-flash`；也可选「✎ 手动输入」直接填 API 支持的任意模型 ID。其中 `deepseek-flash` 是当前模型名（DeepSeek-V4.1-Flash-1017），旧名 `deepseek-v4-flash` 仍被接受，请求按 Flash 价格计费。
2. **选择服务商**：点击显示当前服务商的按钮，在列表中选择 **DeepSeek**。Base URL 与默认模型会自动填充；DeepSeek 预设走 Responses API（`POST https://api.deepseek.com/responses`）。
3. **填写 API 密钥**：把密钥粘贴到密钥输入框（占位符 `sk-...`）。留空则回退使用环境变量 `DEEPSEEK_API_KEY`。
4. **选择模型**：打开「模型」下拉，预设含 `deepseek-v4-pro` 与 `deepseek-flash`；也可选「✎ 手动输入」直接填 API 支持的任意模型 ID。
5. **确认上下文窗口**：切换模型时会自动重算「上下文上限（token）」，DeepSeek V4 系列为 `1000000`；也可手工填写（1,024 – 10,000,000）。「输出上限（token，0=自动）」可保持 `0`，由 JPCode 按模型取默认值（DeepSeek 为 393,216）。
6. **设置思考强度**：用底部工具条的「思考」下拉选择 `关闭 / 低 / 中 / 高`。DeepSeek 下「低」发送 `reasoning_effort: "low"`，「中」与「高」均发送 `reasoning_effort: "high"`（并带 `thinking: enabled`）；「关闭」发送 `thinking: {"type": "disabled"}`。`max` 档位的说明见下。
7. **保存**：字段提交即写入 `config.json`，没有单独的「应用」按钮。重新打开模型下拉确认当前生效的模型即可。

> 更深的思考档位：DeepSeek V4 接受 `low / high / max`，其中 `max` 为最高档。JPCode 的「思考」下拉目前最高到「高」（`high`），如需 `max` 档，可通过自定义供应商接入，或在自建网关上补齐该字段。遇到报错时请不要以「关闭思考模式」作为规避手段——JPCode 已在 API 要求回传思考内容的场合自动回传。

#### 可选：把 DeepSeek 配成自定义供应商（Chat Completions）

DeepSeek 预设走 Responses API。如果你的 DeepSeek 网关或代理只暴露 Chat Completions，可改为新增自定义供应商：

1. 在服务商列表中选择「＋ 新增自定义供应商…」并填写名称。
2. 填写 `Base URL`（如 `https://api.deepseek.com`）、`模型 ID`（如 `deepseek-v4-pro`）与密钥。
3. 只有在需要非默认端点时才需要自定义供应商；接入官方 API 用预设即可。

### 使用 JPCode

#### 首次运行

1. 打开项目目录作为工作目录（标题栏会显示，点击可修改）。
2. 在窗口底部的模型选择器里选中 DeepSeek 模型。
3. 在输入框描述需求并按回车。Agent 会规划、改文件、跑构建与测试，工具输出与命令输出实时回到对话里。

#### 命令双模执行

- 在对话中以 `!` 开头的一行会在本机 PowerShell（Windows）或 zsh（macOS）执行，stdout/stderr 实时回流，结束时附退出码与 `[文件变更] +N ~M -K` 统计。
- 在底部工具条「机器」里选中 SSH 目标机后，同一条 `!命令` 会下发到远程主机执行，语法自动适配——桌面端保留 DeepSeek 推理循环、构建放到 Linux 机器上跑，是很常见的用法。
- 构建/测试这类长任务可标记为长任务，执行器会持续等待到进程退出，而不是中途超时。

#### subagent 并行

输入 `/agent <任务>`（或 `/subagent <任务>`）可以派生子代理：它们继承当前供应商/模型与上下文并行执行，结果自动写回父会话。一轮里可以同时派发多个子代理（上限取决于套餐并发数），这也是用好 DeepSeek 1M 上下文的常见方式：同一个仓库里，一个 Agent 重构、一个写测试、一个补文档。

#### 技能、KV 缓存与 Git 审查

- **技能**：可复用的指令包（代码审查、测试编写、文档撰写、规划并行等），按会话开关，支持安装第三方技能目录。
- **KV 缓存**：代码智能（类 / 函数 / 枚举 + 文件与行号范围）按工作目录索引，由独立的本地进程经 IPC 提供；Agent 按需只读函数体，不必整文件重读，DeepSeek 的提示词因此更短、更省。
- **Git 审查面板**：变更文件树、逐行 diff、Markdown 预览与 `+N ~M -K` 统计；Token 用量按模型单价折算，可看到每个会话的花费。

#### DeepSeek V4 的长会话

DeepSeek V4 系列支持最高 **1M 上下文**，且思考模式默认开启。JPCode 在每次请求后用 API 返回的实际 usage 校准上下文估算；当会话将要超出配置上限时，会自动开新会话并携带当前消息与交接说明，长重构任务不会直接撞上硬错误。

### 价格（供参考）

数据核对自 [DeepSeek 价格页](https://api-docs.deepseek.com/quick_start/pricing)（单位：元 / 百万 tokens；空闲时段为高峰时段价格的一半，高峰时段为北京时间周一至周五 9:00–12:00、14:00–18:00，不含中国法定节假日）：

| 模型            | 输入（缓存命中） | 输入（缓存未命中） | 输出      |
| --------------- | ---------------- | ------------------ | --------- |
| deepseek-flash  | 0.02 / 0.04      | 1 / 2              | 4 / 8     |
| deepseek-v4-pro | 0.15 / 0.30      | 4.5 / 9.0          | 13.5 / 27.0 |

*（单元格格式：空闲 / 高峰）*。JPCode 的 Agent 循环每轮都会重发工程上下文，账单主要由缓存命中价决定——保持工作目录稳定，让 DeepSeek 的上下文缓存持续命中。

### 常见问题

- **`401 Unauthorized` / 「未携带 Authorization 请求头」**：该服务商的密钥为空。回到「AI 设置」重新填写；同时检查环境里是否有残留的 `DEEPSEEK_API_KEY` 覆盖了界面值（环境变量优先）。
- **验证连接不通过或调用报错**：检查 DeepSeek 账户余额与网络；受限网络可在「AI 设置」的代理输入框配置 `http://`、`socks4://`、`socks5://`（可带 `user:pass@`），代理作用于全部 AI 请求（含流式）。
- **`429` 限流**：DeepSeek 按模型限制并发（`deepseek-flash` 高于 `deepseek-v4-pro`）。可减少同时运行的子代理数量，或在「AI 设置」里把 TPM 上限调成与账号额度一致。
- **`reasoning_text must be passed back`**：JPCode 在工具调用回合会自动回传 DeepSeek 的思考内容；如果中间代理/网关把该字段剥掉了，请让网关透传，而不是关闭思考模式。
- **回答风格**：想要更短的回复 + 更多并行工具调用，保持默认回复风格；需要拆分任务并行时，开启「规划并行」技能。
