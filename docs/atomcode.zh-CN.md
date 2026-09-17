[English](./atomcode.md) | [简体中文](./atomcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AtomCode

AtomCode 是一个用 Rust 编写的开源终端 AI 编程 Agent，支持任意 OpenAI 兼容 API，因此接入 DeepSeek 只需几行配置。

#### 1. 安装 AtomCode

- **Linux / macOS / WSL / Git-Bash**：

```bash
curl -fsSL https://raw.atomgit.com/atomgit_atomcode/atomcode/raw/main/scripts/install.sh | sh
```

- **Windows PowerShell**：

```powershell
irm https://raw.atomgit.com/atomgit_atomcode/atomcode/raw/main/scripts/install.ps1 | iex
```

- **npm**（任意安装了 Node.js 的平台）：

```bash
npm install -g @atomgit.com/atomcode
```

- **Homebrew**（macOS / Linux）：

```bash
brew install --cask atomcode
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```bash
atomcode --version
```

> **注意：** 请勿使用 `sudo` 运行 AtomCode —— 它的配置与会话都存放在 `~/.atomcode` 下。

#### 2. 配置 DeepSeek 供应商

AtomCode 的配置文件位于 `~/.atomcode/config.toml`。将 DeepSeek 添加为 OpenAI 兼容供应商：

```toml
default_provider = "deepseek"

[providers.deepseek]
type           = "openai"
api_key        = "sk-..."
model          = "deepseek-v4-pro"
base_url       = "https://api.deepseek.com/v1"
context_window = 1000000
reasoning_effort = "max"
```

其中 API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

- `context_window = 1000000` —— DeepSeek V4 系列模型最高支持 100 万 token 上下文，显式设置后 AtomCode 的上下文管理可以利用完整预算。
- `reasoning_effort = "max"` —— DeepSeek-V4-Pro 支持多档推理强度，`max` 档能获得最佳编码体验。也可以在运行时通过 `/effort`（high / max / off）或 `Ctrl+T` 切换。

如需同时使用两个模型，再声明一个 provider，并用 `/model` 切换：

```toml
[providers.deepseek-flash]
type           = "openai"
api_key        = "sk-..."
model          = "deepseek-v4-flash"
base_url       = "https://api.deepseek.com/v1"
context_window = 1000000
```

手动修改文件后，在 AtomCode 中执行 `/reload` 即可在不重启的情况下加载更改。

#### 3. 运行并选择模型

- 进入项目目录并执行 `atomcode` 命令：

```bash
cd /path/to/my-project
atomcode
```

- 按 `F2`（或输入 `/model`）打开模型切换器。
- 选择 **deepseek** 供应商，然后选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 开始编码 —— 或使用无头模式执行单次提问：`atomcode -p "解释这个仓库里的 agent 循环"`。
