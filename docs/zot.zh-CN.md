[English](./zot.md) | [简体中文](./zot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 zot

zot 是一个用 Go 编写的轻量级编码代理框架，以单个静态二进制文件分发。它内置了对 DeepSeek 的支持（通过 DeepSeek 的 OpenAI 兼容聊天 API），提供四个内置工具（read、write、edit、bash）、三种运行模式（交互式 TUI、print、JSON），以及通过子进程 + JSON-RPC 实现的任意语言扩展系统。

#### 1. 安装 zot

- **Linux / macOS**（一键脚本）：

```bash
curl -fsSL https://www.zot.sh/install.sh | bash
```

- **Windows**（PowerShell）：

```powershell
iwr -useb https://www.zot.sh/install.ps1 | iex
```

- **通过 Go 安装**：

```bash
go install github.com/patriceckhart/zot/cmd/zot@latest
```

- 安装结束后，执行以下命令验证安装：

```bash
zot --help
```

#### 2. 配置 DeepSeek 供应商

zot 已内置 DeepSeek 支持，无需手动配置供应商。默认设置如下：

- **模型**：`deepseek-v4-pro`
- **基础 URL**：`https://api.deepseek.com/v1`

其中 API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

设置环境变量：

Linux / Mac 用户：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Windows 用户：

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

或者，运行 `zot` 并输入 `/login`，然后选择 **api key** 粘贴你的 DeepSeek 密钥。zot 会请求一次 `/v1/models` 进行验证，并将密钥以 `deepseek` 为键存储在 `$ZOT_HOME/auth.json` 中（权限 0600）。

DeepSeek 的凭证查找顺序：

1. `--api-key` 参数
2. `DEEPSEEK_API_KEY` 环境变量
3. `$ZOT_HOME/auth.json`

> **注意：** DeepSeek 不提供订阅式 OAuth 登录，仅支持通过 API Key 认证。

#### 3. 运行并选择模型

- 进入项目目录并使用 DeepSeek 供应商运行 zot：

```bash
cd /path/to/my-project
zot --provider deepseek
```

- 内置目录提供两个模型，均可在 TUI 中通过 `/model` 切换：
  - `deepseek-v4-pro`（支持推理）
  - `deepseek-v4-flash`

- 也可以直接指定模型：

```bash
zot --provider deepseek --model deepseek-v4-flash
```

- 使用自定义兼容端点（镜像、网关或自托管）：

```bash
zot --provider deepseek \
    --base-url https://my-deepseek-mirror.example.com/v1 \
    --api-key "$DEEPSEEK_API_KEY"
```

#### 4. 添加自定义模型（可选）

在 `$ZOT_HOME` 目录中放置 `models.json` 文件，可以添加内置目录之外的模型：

- **macOS**：`~/Library/Application Support/zot/models.json`
- **Linux**：`~/.local/state/zot/models.json`
- **Windows**：`%LOCALAPPDATA%\zot\models.json`

```json
{
  "providers": {
    "deepseek": {
      "models": [
        {
          "id": "deepseek-v5-preview",
          "name": "DeepSeek V5 Preview",
          "reasoning": true,
          "contextWindow": 128000,
          "maxTokens": 8192
        }
      ]
    }
  }
}
```

> **关于纯文本模式的说明：** DeepSeek 的 chat-completions 接口当前不支持多模态内容格式。当前激活的供应商为 `deepseek` 时，zot 会自动从外发消息中移除图片部分，仅保留文本内容。切换回支持视觉的模型后，由于会话文件仍保留了图片数据，图片会被正常重新发送。

更多配置选项请参阅 [zot README](https://github.com/patriceckhart/zot/blob/main/README.md)。
