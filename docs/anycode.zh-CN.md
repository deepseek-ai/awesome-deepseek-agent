[English](./anycode.md) | [简体中文](./anycode.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 anyCode

anyCode 是一款开源（MIT）的 Rust Agent 工作台 —— 本地优先的 **数字工作台**（Digital Workbench）加上单一的 `AgentRuntime`，编排多轮 LLM + 工具循环（Bash、Edit、Grep、MCP、LSP、Skills、定时任务等）。模型采用 BYOK：由你选择服务商，密钥保存在 `~/.anycode/config.json`，数据默认留在本机。DeepSeek 是一等公民提供商，内置模型目录（`deepseek-v4-pro`、`deepseek-v4-flash`），并在 `/setup` 向导中提供快速认证预设。

- **GitHub：** <https://github.com/qingjiuzys/anycode>

#### 1. 安装 anyCode

**macOS（推荐）**

从 [GitHub Releases](https://github.com/qingjiuzys/anycode/releases) 下载 **`anyCode_<version>_aarch64.dmg`**，打开后把 **anyCode** 拖入「应用程序」。内置工作台会自动启动。

**Linux 服务器 / 无头模式**

```sh
curl -fsSL --proto '=https' --tlsv1.2 \
  "https://raw.githubusercontent.com/qingjiuzys/anycode/main/scripts/install.sh" | \
  bash -s -- --repo qingjiuzys/anycode
```

然后在浏览器访问工作台 **`http://127.0.0.1:43180`**。

**从源码构建（开发者）**

```sh
git clone https://github.com/qingjiuzys/anycode.git
cd anycode
./scripts/sync-desktop-dev.sh --rust   # UI + Rust（本地发布构建，约 1–2 分钟）
```

#### 2. 获取 DeepSeek API Key

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

#### 3. 配置 DeepSeek

**方式 A —— 设置向导（推荐）**

启动 anyCode（或访问 `http://127.0.0.1:43180`）。首次进入的设置向导（`/setup`）提供快速认证预设：

1. 在预设中选择 **DeepSeek API Key**。
2. 粘贴你的 API Key。预设默认模型为 **`deepseek-v4-pro`**、端点 `https://api.deepseek.com/chat/completions`。
3. 完成向导 —— 配置写入 `~/.anycode/config.json`。

**方式 B —— 手动编辑 `~/.anycode/config.json`**

```json
{
  "provider": "deepseek",
  "model": "deepseek-v4-pro",
  "api_key": "sk-..."
}
```

- `provider`：`deepseek`（`deep-seek` 等别名会自动规范化）。
- `model`：`deepseek-v4-pro`（旗舰 MoE；100 万 token 上下文、工具调用、思考模式）或 `deepseek-v4-flash`（高速 MoE；100 万 token 上下文、工具调用）。
- `base_url`：可选；默认为 `https://api.deepseek.com`（OpenAI 兼容的 `chat/completions`）。
- `api_key`：你的 DeepSeek 密钥，也可设置环境变量 `DEEPSEEK_API_KEY`。
- 上下文窗口：DeepSeek V4 模型支持高达 **100 万 token** 上下文。anyCode 会按 `provider + model` 自动推断窗口（`session.context_window_auto`，默认 `true`）；需要时可设 `session.context_window_tokens` 覆盖。

DeepSeek 请求走 anyCode 共享的 OpenAI 兼容客户端，并做工具 schema 规范化，因此工具调用开箱即用。

#### 4. 首次运行

1. 在工作台点击 **新建会话**（或进入某个项目）。
2. 发送一条测试消息：

   > 请只回复：OK

3. 预期助手回复 `OK`。

#### 配置参考

| 选项 | 说明 |
|------|------|
| `provider` | `deepseek`（别名 `deep-seek` / `deep_seek` 自动规范化） |
| `model` | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| `base_url` | OpenAI 兼容端点；默认为 `https://api.deepseek.com` |
| `api_key` | 你的 DeepSeek API Key（或 `DEEPSEEK_API_KEY` 环境变量） |
| `session.context_window_auto` | 按 provider + model 自动推断上下文窗口（默认 `true`） |
| `session.context_window_tokens` | 手动指定上下文窗口（token 数） |
| `session.auto_compact` | 长对话自动压缩（默认 `true`） |