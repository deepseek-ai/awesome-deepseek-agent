
[English](./infer.md) | [简体中文](./infer.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 Inference Gateway CLI

Inference Gateway CLI（`infer`）是一个基于 Go 的命令行工具，可通过 Inference Gateway 使用 AI 模型。它支持交互式聊天、自主智能体和开发工作流。

### 1. 安装 Inference Gateway CLI

**前置要求：**
- Node.js 18 或更高版本。

检查 Node.js 和 npm 版本：

```bash
node --version
npm --version
```

推荐使用以下命令，无需全局安装即可运行 CLI：

```bash
npx @inference-gateway/cli@latest --help
npx @inference-gateway/cli@latest chat
```

也可以选择全局安装：

```bash
npm install -g @inference-gateway/cli
```

验证安装：

```bash
infer --help
infer --version
```

### 2. 配置 DeepSeek Provider

CLI 可以从环境变量、项目 `.env` 文件或用户目录中的 `~/.infer/auth.yaml` 文件读取 Provider API 密钥。

1. 从 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 获取 API Key。
2. 初始化 CLI 配置：

```bash
infer init
```

3. 打开 `~/.infer/auth.yaml`（Windows 用户路径为 `%USERPROFILE%\.infer\auth.yaml`），添加以下内容：

```yaml
DEEPSEEK_API_KEY: your-deepseek-api-key
```

将占位文本替换为你自己的 API Key。

**重要提示：** 请妥善保管 API Key。不要将真实密钥写入项目文件或提交到 GitHub。

### 3. 运行并选择 DeepSeek 模型

检查 Gateway 状态：

```bash
infer status
```

启动交互式聊天会话：

```bash
infer chat
```

在聊天界面中打开模型选择器：

```text
/model
```

选择一个 DeepSeek 模型，例如：

```text
deepseek/deepseek-v4-flash
```

也可以直接切换模型：

```text
/model deepseek/deepseek-v4-flash
```

现在，你就可以通过 Inference Gateway CLI 与 DeepSeek 进行交互了。

### DeepSeek V4 配置

将 DeepSeek V4-Pro 设置为默认模型，并启用最高推理强度：

```bash
infer config set agent.model deepseek/deepseek-v4-pro
infer config set agent.reasoning_effort max
```

验证配置：

```bash
infer config get agent.model
infer config get agent.reasoning_effort
```

DeepSeek V4 模型支持高达 100 万个 Token 的上下文窗口。具体限制取决于所选模型和 API 配置。


### 4. 故障排除

如果 CLI 无法连接 DeepSeek：

- 检查 DeepSeek API Key 是否有效。
- 确认 CLI 能够读取 `DEEPSEEK_API_KEY`。
- 运行 `infer status` 检查 Gateway 状态。
- 运行 `infer --help` 查看可用命令。

更多信息请访问 [Inference Gateway CLI 官方文档](https://docs.inference-gateway.com/cli/) 和 [官方 GitHub 仓库](https://github.com/inference-gateway/cli)。
