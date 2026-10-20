[English](./maxa.md) | [简体中文](./maxa.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Maxa 中使用 DeepSeek

[Maxa](https://github.com/maxzhao/maxa) 是 Neovim 内的免费开源（Apache-2.0）AI 工作空间，支持 Agent 编程、MCP 工具、按需加载的 Abilities 和子代理。它使用你自己的 API Key 直接连接 DeepSeek。Maxa 不售卖模型服务，API 调用由 DeepSeek 单独计费。

#### 1. 安装 Maxa

公开安装脚本面向 **WSL2 + Ubuntu 24.04**，支持 **x86_64 或 aarch64**，要求使用具有 sudo 权限的普通用户。Maxa 要求 **Neovim 0.11+**；安装脚本会准备 Neovim 和其他依赖。

> **安装前请备份已有 Neovim 配置。** 以下克隆命令要求 `~/.config/nvim` 尚不存在，不要覆盖已有安装。Maxa 的工具以你的操作系统用户权限运行。

克隆公开仓库，也可以先 Fork，再将 URL 换成自己的 Fork：

```bash
git clone https://github.com/maxzhao/maxa.git ~/.config/nvim
```

运行前请阅读[安装脚本](https://github.com/maxzhao/maxa/blob/main/install.sh)。它会下载依赖、使用 sudo 安装系统软件，并在 systemd 可用时配置 Obsidian 和 Syncthing 用户服务。然后在目标 WSL 环境中执行：

```bash
bash ~/.config/nvim/install.sh
```

首次安装时，从公开示例创建本地启动配置：

```bash
cp ~/.config/nvim/lua/plugins/ai.example ~/.config/nvim/lua/plugins/ai.lua
```

**已有安装请保留当前 `ai.lua`，合并所需设置，不要直接覆盖。** 详情见 [Maxa 安装说明](https://github.com/maxzhao/maxa/blob/main/README.zh-CN.md#当前提供的安装路径)。

#### 2. 配置 DeepSeek

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。在用于启动 Neovim 的终端中设置：

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

也可以按照 Maxa README，在本地 `~/.config/nvim/.env` 中设置 `DEEPSEEK_API_KEY`。不要提交真实 API Key。

复制得到的 `ai.example` 已包含 `deepseek` Provider：

- Base URL：`https://api.deepseek.com`。
- 协议：`openai_responses`，使用官方 `/responses` 接口。
- 模型：`deepseek-flash`（示例默认值）和 `deepseek-v4-pro`。
- DeepSeek 专用 Responses 扩展，负责思考内容及工具调用处理。请保留该扩展配置。

在 `lua/plugins/ai.lua` 的 `opts.maxa.presets` 中修改已有 `main` Preset，并在 `opts.maxa` 中启用 `model_limits`。**将这些字段合并到现有配置，不要替换整个文件，也不要丢弃其他 Preset 和 Provider。** 以下示例选择 Pro 并开启最大思考强度：

```lua
-- Inside opts.maxa
presets = {
  main = {
    type = "chat",
    adapter = "deepseek",
    model = "deepseek-v4-pro",
    thinking_mode = "max",
    visible = true,
  },
  -- Keep your other presets here.
},
model_limits = {
  model_overrides = {
    { pattern = "^deepseek%-", context_window = 1000000, max_output_tokens = 384000 },
  },
},
```

- **1M 上下文**：两个模型最多都支持 1,000,000 tokens 上下文和 384,000 tokens 输出。Maxa 对它们的内置上下文估算为 500,000；上述覆盖配置将上下文用量显示和 token 阈值处理的预算设为完整 1M。覆盖项会替换整条内置限制，因此请保留 `max_output_tokens`。
- **最大思考强度**：`thinking_mode = "max"` 在 Responses 请求中对应 `reasoning.effort = "max"`。DeepSeek 会将 `xhigh` 映射为 `high`，而不是 `max`，详见[思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。不要通过关闭思考模式来规避工具调用或思考内容回传错误，应使用包含 DeepSeek 扩展的最新 Maxa 版本。
- **Flash**：如需改用 Flash，只需将 `main.model` 改为 `deepseek-flash`，上下文配置不变。Pro 不支持图片输入。

公开示例设置了 `opts.maxa.defaults.chat = "main"`，因此新 Chat 默认使用这个 Preset。其他辅助 Preset 可保持原样。保存文件后重启 Neovim，使配置生效。

#### 3. 首次运行

在 WSL 中进入项目目录并启动 Neovim：

```bash
cd /path/to/your-project
nvim
```

1. 首次启动时等待编辑器插件安装完成。运行 `:checkhealth maxa` 检查核心依赖。
2. 运行 `:Maxa` 打开新 Chat。按照上述配置，默认 Chat 使用最大思考强度的 DeepSeek V4 Pro。
3. 让 Maxa 检查项目并解释一个函数，查看工具结果与回复，再追问一个问题以继续对话。
4. 使用 `:MaxaHistory` 重新打开已保存的会话。

已有安装若在新 Chat 中选择了其他 Preset，请检查项目或全局的 Chat 默认值覆盖。Provider 与 Preset 配置详情见 [Maxa README](https://github.com/maxzhao/maxa/blob/main/README.zh-CN.md)。
