[English](./zcode-zai.md) | [简体中文](./zcode-zai.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 ZCode

ZCode 是支持桌面端与 CLI 的 AI 编程 Agent。它通过 OpenAI 兼容（Chat Completions / Responses）与 Anthropic 兼容（Anthropic Messages）的 API 支持自定义模型供应商，并内置 DeepSeek 供应商目录，几步即可接入 DeepSeek V4。

#### 1. 安装 ZCode

- 前往 [ZCode 官网](https://zcode.z.ai) 下载桌面安装包并安装。
- 启动 ZCode 并登录。
- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 2. 添加 DeepSeek 供应商

打开 **设置 → 模型供应商**，点击 **添加模型供应商**。

**方式一：从供应商目录添加（内置）**

选择 **供应商目录**，搜索 `DeepSeek` 并选中 DeepSeek 供应商条目。目录中已预置以下配置：

- Base URL：`https://api.deepseek.com`
- 模型：`deepseek-v4-pro`、`deepseek-v4-flash`
- 上下文窗口：1,000,000 tokens
- 最大输出 tokens：384,000

填入 DeepSeek API Key 并保存。

**方式二：自定义端点**

选择 **自定义端点**，填写：

- **名称**：`DeepSeek`
- **API 格式**：`Chat completions`（OpenAI 兼容）
- **Base URL**：`https://api.deepseek.com`
- **API Key**：`<your DeepSeek API Key>`

然后添加两个模型：

| 模型 ID | 上下文窗口 | 最大输出 tokens |
| ------- | ---------- | --------------- |
| `deepseek-v4-pro` | 1,000,000 | 384,000 |
| `deepseek-v4-flash` | 1,000,000 | 384,000 |

两个模型默认都支持 `max` 档推理（DeepSeek V4 的完整深度思考），ZCode 中对应 `off` / `high` / `max` 三档。

#### 3. 选择模型

打开对话或新建任务，在对话工具栏的模型切换器中选择：

```
DeepSeek V4 Pro
DeepSeek V4 Flash
```

`deepseek-v4-pro` 适合复杂的 Agent 编程任务；`deepseek-v4-flash` 速度更快、成本更低，适合简单任务。

#### 4. 可选：验证 API Key

Windows 用户可以在 PowerShell 中验证 API Key：

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"

curl https://api.deepseek.com/v1/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

如果请求成功，说明 API Key 和模型名都可用。

#### 常见问题

- `401` 或认证失败：检查 API Key 是否为真实 DeepSeek API Key。不要把接口 URL 填到 API Key 字段。
- `未找到模型` 或 `404`：检查模型 id 是否严格写成 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 模型切换器中不显示该供应商：确认供应商已启用且已填写 API Key，然后重启 ZCode。
- `402` 或配额错误：检查 DeepSeek 开放平台账户余额。

#### 相关资源

- [ZCode](https://zcode.z.ai)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
