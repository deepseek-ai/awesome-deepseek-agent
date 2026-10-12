[English](./gneol.md) | [简体中文](./gneol.zh-CN.md) · [← Back](../README.md)

# 集成 Gneol

Gneol 是 `.gneol` 文件的运行时。用一个纯文本文件描述你的 AI 智能体——它的模型、子智能体、定时触发器、事件监听器、工具与 MCP 服务器——Gneol 便会在本地以单进程方式运行它。Gneol 支持自定义模型，DeepSeek V4 可通过内置的 `deepseek` provider 接入，它使用与 OpenAI 兼容的 Chat Completions API。

#### 1. 安装 Gneol

macOS / Linux：

```bash
curl -sSL https://raw.githubusercontent.com/Gneol/Gneol/main/install.sh | bash
```

或从 [Releases](https://github.com/Gneol/Gneol/releases) 页面下载预编译二进制文件。在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

#### 2. 提供 DeepSeek API Key

Gneol 支持三种密钥来源：程序级 `.env` 文件、全局加密密钥存储、Shell 环境变量。任选一种即可。

**方式 A —— 全局密钥存储（加密落盘）**

```bash
gneol secrets set DEEPSEEK_API_KEY "<你的 DeepSeek API Key>"
```

**方式 B —— 程序级 `.env` 文件**

```
# .env
DEEPSEEK_API_KEY=<你的 DeepSeek API Key>
```

**方式 C —— Shell 环境变量**

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

#### 3. 配置 DeepSeek 模型

新建一个 `.gneol` 程序。`model("<标签>")` 块声明 DeepSeek 绑定，`program()` 头部通过标签引用该模型。

```
program("Hello World")
  .model("deepseek")
  .env(".env")

model("deepseek")
  .provider("deepseek")
  .modelId("deepseek-v4-flash")
  .apiKey("DEEPSEEK_API_KEY")
  .temperature(0.7)
  .maxTokens(384000)

subagent().model("deepseek")

summarization().model("deepseek").prompt("用 3 条要点总结")
```

- `.provider("deepseek")` —— 选择内置的 DeepSeek 适配器（基础地址 `https://api.deepseek.com`）。
- `.modelId("deepseek-v4-flash")` —— DeepSeek 模型 id（见[可用模型](#可用的-deepseek-模型)）。
- `.apiKey("DEEPSEEK_API_KEY")` —— 存放密钥的**环境变量名**。切勿把真实密钥直接写进程序文件。
- `.env(".env")` —— 可选；从本地 `.env` 文件加载变量。

将文件保存为 `hello.gneol`——UTF-8 编码，不带 BOM。

#### 4. 部署并对话

```bash
gneol start --daemonize          # 可选：在后台启动运行时
gneol deploy -f hello.gneol -i   # 部署程序，随后直接进入对话
```

`gneol deploy` 会将运行时与你的 `.gneol` 文件对齐——创建智能体、应用模型绑定并启动它。`-i` 参数会直接把你带入交互式会话：

```
Hello World ❯ 你好
💬 你好！我是运行在 DeepSeek V4 Flash 上的 Hello World 智能体。
```

常用命令：

| 命令 | 用途 |
|------|------|
| `gneol` | 在当前目录初始化/接入会话。 |
| `gneol status` | 检查运行时是否在运行。 |
| `gneol secrets list` | 列出已存储的密钥名称。 |
| `gneol stop` | 停止运行时。 |

运行 `gneol --help` 查看完整命令列表。

#### 5. 可选：验证 API Key

```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

请求成功即表示 API Key 与模型名有效。

#### 可用的 DeepSeek 模型

| 模型 ID | 说明 |
|---------|------|
| `deepseek-v4-pro` | DeepSeek 旗舰推理模型。适合作为根智能体，或用于需要更强推理的子智能体。 |
| `deepseek-v4-flash` | 快速、低成本模型。创建新程序时 Gneol 的默认选择。 |

两个模型都支持最高 **1M 上下文**，`deepseek-v4-pro` 还支持 **max 级别思考强度**。Gneol 会将 `.temperature` 与 `.maxTokens` 直接转发给 DeepSeek 的 OpenAI 兼容端点，因此 `.maxTokens(384000)` 可用满输出预算。

#### 混合使用多个 Provider

Gneol 可以同时绑定多个模型，因此你可以让不同子智能体使用不同 provider，并把 DeepSeek 作为主模型或兜底：

```
model("fast")
  .provider("deepseek")
  .modelId("deepseek-v4-flash")
  .apiKey("DEEPSEEK_API_KEY")

model("eagle-eye")
  .provider("openrouter")
  .modelId("openai/gpt-4o")
  .apiKey("OPENROUTER_API_KEY")

subagent("Reviewer")
  .model("eagle-eye")
  .description("对 DeepSeek 输出进行独立复核")
```

#### 疑难排查

- `Authentication Fails` 或 `401`：确认 `apiKey` 指向的变量确实存放了你真实的 DeepSeek API Key。不要往密钥字段里填 API 地址。
- `Model Not Found` 或 `404`：确认模型 id 精确为 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 智能体未启动：运行 `gneol status`；若运行时已停止，用 `gneol start --daemonize` 启动。
- API Key 未生效：确认启动 `gneol` 的 Shell 中已导出该变量，或用 `gneol secrets set DEEPSEEK_API_KEY ...` 存储。
- 程序解析失败：确认 `program().model("<标签>")` 中的标签与 `model("<标签>")` 块一致，且文件保存为不带 BOM 的 UTF-8。
