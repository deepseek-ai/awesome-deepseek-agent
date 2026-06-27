[English](./gptme.md) | [简体中文](./gptme.zh-CN.md) · [← Back](../README.md)

# 接入 gptme

gptme 是一个 provider 无关、本地优先的终端 AI agent——可替代 Claude Code。内置 shell、Python、web 工具，支持 Anthropic、OpenAI、Google、xAI、**DeepSeek**、OpenRouter，或通过 `llama.cpp` 完全本地运行。

- **GitHub:** <https://github.com/gptme/gptme>

#### 1. 安装 gptme

```sh
pipx install gptme
```

验证：

```sh
gptme --version
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 注册、充值，复制你的 API Key。

#### 3. 配置 DeepSeek provider

gptme 按 `${PROVIDER_NAME}_API_KEY` 约定解析密钥，所以导出为 `DEEPSEEK_API_KEY`：

```bash
echo 'export DEEPSEEK_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

然后在 `~/.config/gptme/config.toml` 中把 DeepSeek 注册为自定义 OpenAI 兼容 provider：

```toml
[[providers]]
name = "deepseek"
base_url = "https://api.deepseek.com/v1"
api_key_env = "DEEPSEEK_API_KEY"
default_model = "deepseek-chat"
```

（`deepseek-chat` 为 V4 对话模型；用 `deepseek-reasoner` 调用 R1 推理模型。）

#### 4. 首次运行

```sh
# 用自定义 provider 的默认模型
gptme --model deepseek "解释这个代码库"

# 或指定具体模型
gptme --model deepseek/deepseek-reasoner "设计一个重试装饰器"

# 列出已配置的 provider
gptme-util providers list
```

gptme 还支持 MCP 服务器（数据库/API/文件系统）、插件系统，以及通过 `llama.cpp` 跑本地模型（无需密钥）——完整能力见 [providers 文档](https://gptme.org/docs/providers.html) 与 [自定义 provider](https://gptme.org/docs/custom-providers.html)。
