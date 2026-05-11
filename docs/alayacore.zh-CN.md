[English](./alayacore.md) | [简体中文](./alayacore.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AlayaCore

AlayaCore 是一个快速、精简的终端 AI Agent。它连接任何 OpenAI 兼容或 Anthropic 兼容的 LLM，赋予其读取、写入、编辑文件和执行命令的能力——支持流式输出、会话持久化和多步骤代理工具调用循环，可在交互式 TUI 和纯文本模式（用于脚本和管道操作）下使用。

AlayaCore 极其小巧（约 8MB 静态链接二进制文件），零运行时依赖——无需 Node.js、Python，甚至不需要 libc。这意味着不会出现 Linux 上常见的 libc 兼容性问题。

- **GitHub:** <https://github.com/alayacore/alayacore>

#### 1. 安装 AlayaCore

**方式一：从 GitHub Releases 下载**

从 [GitHub Releases 页面](https://github.com/alayacore/alayacore/releases) 下载适合你平台的最新二进制文件。

**方式二：使用 Go 构建**

- 安装 [Go](https://go.dev/dl/) 1.26.1+。
- 运行：

```sh
go install github.com/alayacore/alayacore@latest
```

#### 2. 获取 DeepSeek API Key

- 前往 <https://platform.deepseek.com/> → 注册/登录 → **API Keys** → **创建 API Key**。

#### 3. 配置 DeepSeek

AlayaCore 的配置存储在 `~/.alayacore/model.conf`。首次运行时会创建一个默认的 Ollama 配置。你需要编辑它来添加 DeepSeek。

在终端中按 `Ctrl+L` 然后按 `e` 打开配置文件编辑器，或直接编辑：

```sh
# 打开配置文件
$EDITOR ~/.alayacore/model.conf
```

添加以下配置（将 `YOUR_DEEPSEEK_API_KEY` 替换为你的实际密钥）：

```
name: "DeepSeek V4 Pro"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-pro"
context_limit: 1000000
```

如需使用 DeepSeek V4 Flash（更快、更经济）：

```
name: "DeepSeek V4 Flash"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-flash"
context_limit: 1000000
```

你也可以在一个文件中配置多个模型，用 `---` 分隔：

```
name: "DeepSeek V4 Pro"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-pro"
context_limit: 1000000
---
name: "DeepSeek V4 Flash"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-flash"
context_limit: 1000000
```

#### 4. 开始使用 AlayaCore

- 在终端中运行 `alayacore`。
- 按 `Ctrl+L` 打开模型选择器，选择你的 DeepSeek 模型。
- 输入提示并按 `Enter` 开始对话。

#### 纯文本模式

使用 `--plainio` 进行脚本和管道操作，无需 TUI：

```sh
# 从 stdin 管道输入提示
echo "解释这个项目是做什么的" | alayacore --plainio

# 从文件读取提示
alayacore --plainio < myplan.txt
```

## 技巧

- **模型切换：** 按 `Ctrl+L` 在运行时切换模型。
- **会话持久化：** 使用 `:save my-session.md` 或按 `Ctrl+S` 保存对话。
- **技能系统：** 使用 `--skill` 标志扩展 AlayaCore 的自定义技能包。
- **纯 IO 模式：** 使用 `--plainio` 进行脚本和管道操作，无需 TUI。

## 资源

- [AlayaCore 文档](https://github.com/alayacore/alayacore/tree/main/docs)
- [DeepSeek 平台](https://platform.deepseek.com/) — 获取 API Key。
- [DeepSeek API 文档](https://api-docs.deepseek.com/) — API 参考和指南。
