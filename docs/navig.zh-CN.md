[English](./navig.md) | [简体中文](./navig.zh-CN.md) · [← Back](../README.md)

# 集成 NAVIG

NAVIG 是一个本地优先的 AI 操作员操作系统（AI operator OS）：一个 Python 内核加 CLI、一个可安装的桌面
外壳，以及一个任何其他编程客户端都能连接的 OpenAI 兼容端点（`navig serve`）。模型密钥保存在你自己机器的
保险库（vault）里，而不是写在某个客户端的配置文件中，并且每一次调用都会被计价。

#### 1. 安装 NAVIG

- 安装 [Python](https://www.python.org/downloads/) 3.10 或更高版本。
- 在终端执行：

```bash
pip install navig
```

- 验证安装：

```bash
navig --version
navig doctor
```

#### 2. 连接 DeepSeek

```bash
navig ai providers --add deepseek
```

NAVIG 会以隐藏输入询问你的 DeepSeek API Key（不会出现在命令行上），并将其随提供商配置一起保存。
如果你更习惯环境变量，直接导出 `DEEPSEEK_API_KEY` 即可，NAVIG 会自动发现。

两种端点形态都受支持，使用同一个 Key：

| 形态 | Base URL |
|---|---|
| OpenAI（`/v1/chat/completions`） | `https://api.deepseek.com` |
| Anthropic（`/v1/messages`） | `https://api.deepseek.com/anthropic` |

#### 3. 首次运行

```bash
navig ask "总结这个仓库里失败的测试"
navig cost history
```

`navig cost history` 会按会话打印带价格的回执——token 数量与美元金额——价格来自 NAVIG 的审计价格表。

#### 4. 在任意其他客户端中使用 DeepSeek

`navig serve` 把 NAVIG 的模型供应商暴露在一个仅本机回环地址的 OpenAI 兼容端点上，因此 Kilo Code、
Cline、opencode、crush、goose、Continue、Aider、OpenHands 都能使用 DeepSeek，而无需持有密钥：

> **先确认再操作。** 发布版可能尚未包含 `navig serve` —— 先运行 `navig serve --help`，若命令不存在，
> 请等待包含它的版本发布后再按本节操作。

```bash
navig serve token new --label crush --budget 5   # 只显示一次的 nv_… 令牌
navig serve start                               # http://127.0.0.1:8788/v1
```

然后在客户端中填写：

- **Base URL**：`http://127.0.0.1:8788/v1`
- **API Key**：上面生成的 `nv_…` 令牌
- **模型**：`deepseek:deepseek-v4-pro` 或 `deepseek:deepseek-flash`

该端点只响应本机回环请求；令牌预算耗尽时会在发请求之前拒绝；每个请求都会写一条带价格的回执。

> **Claude Code** 不使用该端点：它只支持 Anthropic Messages。请直接指向
> `https://api.deepseek.com/anthropic`，并按下面的说明给模型名加 `[1m]`。

#### 说明

- **当前模型名。** DeepSeek 价格页（2026 年 10 月）把两个模型命名为 `deepseek-v4-pro` 与
  `deepseek-flash`。API 仍然接受 `deepseek-v4-flash` 与 `deepseek-v4-flash-vision-exp` 作为别名（由 Flash
  模型服务）；旧的 `deepseek-chat` / `deepseek-r1` 已废弃，同样由 Flash 服务。NAVIG 把当前两个 id 作为
  一等供应商，并对已废弃的名字按 Flash 价格计价，而不是丢弃它们。
- **1M 上下文。** DeepSeek V4 支持最多 1,000,000 token 上下文与 384K 输出。NAVIG 的供应商条目声明
  `context_window=1000000`。对 Anthropic 兼容客户端，请按 DeepSeek 的建议给模型名加 `[1m]`
  （`deepseek-v4-pro[1m]`）。
- **推理强度。** DeepSeek V4 Pro 支持 `max` 与 `high` 两档推理强度，并默认开启思考模式。NAVIG 的供应商
  条目把两个模型都标记为支持推理；直连 `api.deepseek.com` 的客户端可以在请求体中传 `reasoning_effort`。
- **视觉。** `deepseek-flash`（V4.1）支持图片输入；`deepseek-v4-pro` 不支持。
- **价格。** NAVIG 按 DeepSeek 公布的价格表计价（非高峰价，并在源码注释中标注高峰翻倍）。请始终以
  [DeepSeek 价格页](https://api-docs.deepseek.com/quick_start/pricing) 为准。

#### 常见问题

| 现象 | 原因与处理 |
|---|---|
| 客户端返回 `401 invalid_api_key` | 令牌已撤销或尚未创建——执行 `navig serve token new` |
| `429 budget_exhausted` | 该令牌已达到 `--budget` 上限；用更大的预算重新生成一个令牌 |
| `400 … streaming is not implemented` | 发送 `stream: false`；`navig serve` 的流式支持在后续版本提供 |
| `403 permission_error` | 请求并非来自 `127.0.0.1`——该端点按设计只接受回环连接 |
