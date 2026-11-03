[English](./notrat.md) | [简体中文](./notrat.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Notrat

Notrat 是一款 AI 原生的桌面知识工作台：一边是 Markdown 编辑器，另一边是能真正动手的 Agent。它可以读写你正在编辑的文件、执行终端命令、调用 MCP 工具——所以 DeepSeek V4 在 Notrat 里不只是一个聊天框，而是直接在你的工作区里干活（支持 Windows / macOS / Linux）。

DeepSeek 是 Notrat 内置的服务商预设，不需要手写任何 JSON 配置文件。

- **官网：** <https://notrat.cn>
- **下载：** <https://notrat.cn/download>

#### 1. 安装 Notrat

- 从[官网下载页](https://notrat.cn/download)下载 Notrat，支持 Windows 10 及以上、macOS 12 及以上、Linux（默认提供 AppImage，`.deb` / `.rpm` 也在同一页面列出）。
- 启动并登录。配置 AI 提供商需要 **基础版** 及以上；纯净版会看到升级提示。
- 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 2. 添加 DeepSeek 服务商

1. 打开 **设置**，在左侧选择 **AI 模型配置**。页面标题是「AI 助手配置」。
2. 在 **AI 服务商** 区块里点 **添加**。
3. 在品牌网格的 **在线服务（需要密钥）** 分组里选 **DeepSeek** 卡片。这张卡片已经预置好正确的 API 类型（OpenAI 兼容）和 Base URL（`https://api.deepseek.com`），并预选了 `deepseek-v4-pro`——类型和地址保持默认即可。
4. 把 API Key 填进 **API Key**，点 **测试**。Notrat 会请求服务商的模型列表；测试通过后，抓到的模型会列在 **挑一个模型** 下面。
5. 点选 `deepseek-v4-pro`（想更便宜更快就选 `deepseek-v4-flash`）。
6. 点 **下一步：更多设置** 进入第 ③ 步（这一步的参数都可以不改），再点 **保存并添加**。新服务商会自动成为当前服务商；以后要切回它，在 **AI 服务商** 列表里点开该服务商，再点表单头部的 **设为当前**。

添加弹窗按三步走——*选服务商 → 密钥/测试 + 挑模型 → 更多设置*。第 ③ 步（*参数与更多设置*：回答风格、回复长度上限、识图能力）只有在 **测试** 通过后才解锁。如果点 **测试** 后提示没抓到模型（部分中转/自建网关不提供 `/models` 接口），第 ② 步照样会解锁——在里面的 **手动添加模型（列表里没有时用）** 输入框填 `deepseek-v4-pro`，点 **添加** 即可。

#### 3. 在对话里选择模型

点对话输入区工具栏里的模型胶囊（显示当前模型名），弹出模型下拉。服务商以可展开的分组列出——展开 **DeepSeek**，选 `DeepSeek V4 Pro` 或 `DeepSeek V4 Flash`。下拉顶部的刷新按钮会重新读取服务商与模型配置（在设置里改过服务商后很好用），但不会去调 DeepSeek 的 `/models` 接口。要拉取 DeepSeek 新发布的模型名，请到 **设置 → AI 模型配置** 里打开该服务商，点 **重新获取模型**。

#### 4. 100 万上下文与最高思考档位——开箱即用

- **上下文窗口**：Notrat 内置的模型规格表已把 `deepseek-v4-pro` / `deepseek-v4-flash` 映射为 **1,048,576 token 上下文** 和 **393,216 token 输出上限**。请求默认就按 DeepSeek V4 的完整上限发送，对话压缩的预算也取同一数值，**无需手动配置**。
- **思考档位**：打开模型下拉，把鼠标悬停在模型行上（或用键盘聚焦该行）即可打开模型详情卡——点模型本身是「选中并收起面板」。在详情卡里点 **推理等级**，设为 **极高**（`Max`）。Notrat 对 DeepSeek 提供 `低` / `中` / `高` / `极高` 四档，默认 `高`；`极高` 会以 `reasoning_effort: "max"` 下发给 DeepSeek 的 thinking mode，也就是本仓库贡献指南推荐的、用于最佳编码体验的那一档。

> 用中转把模型名改掉了（比如用 `deepseek-pro` 而不是 `deepseek-v4-pro`）？规格表认得常见别名；如果改得完全认不出来，就在同一张模型详情卡里手动填写 **上下文窗口** / **输出上限**——手填值优先级最高，而且会真正改变发出的 `max_tokens` 默认值，不只是改显示。

#### 5. 可选：在终端验证 API Key

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"

curl.exe https://api.deepseek.com/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

请求成功即说明 Key 与模型名都正确。

#### 常见问题

- 报 `Authentication Fails` / `401`：API Key 填错或已失效。注意别把 Base URL 粘到 API Key 里。
- 报 `Model Not Found` / `404`：模型名必须正好是 `deepseek-v4-pro` 或 `deepseek-v4-flash`；手动填写的，检查有没有多余空格。
- 点 **测试** 失败、模型列表是空的：部分中转/自建网关没实现 `/models` 接口，在第 ② 步的 **手动添加模型** 输入框里填模型名照样能发请求。
- 完全连不上：代理开关在 **设置 → 通用 → HTTP 代理**（不在 AI 页面里）。默认 `http://127.0.0.1:7890`，也支持 `socks5://…`。
- 在纯净版上：配置 AI 提供商需要 **基础版** 及以上，纯净版会看到升级提示。
- 配好了但对话下拉里没有这个模型：到 **设置 → AI 模型配置** 里点开该服务商，确认表单头部显示 **当前**（否则点 **设为当前**），再重新打开下拉用顶部的刷新按钮。如果服务商的模型列表里根本没有这个模型名，在同一张表单里点 **重新获取模型**。
- 思考输出很长但正文是空的：先看模型详情卡里的 **输出上限**。如果中转把模型名改得对不上任何规格，内置对未知 DeepSeek 名字的兜底只有 8K 输出——手动填上真实上限即可。

AI 配置的完整说明（OAuth 提供商、本地模型、参数预设）见[官网](https://notrat.cn)与应用内自带帮助文档。
