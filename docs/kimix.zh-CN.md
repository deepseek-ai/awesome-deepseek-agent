[English](./kimix.md) | [简体中文](./kimix.zh-CN.md) · [← 返回](../README.md)

# 集成 KimiX

KimiX（Kimi-CLI-X）是一款终端 AI 编程助手，针对 Deepseek 做了深度优化，支持多种 API （Anthropic、Kimi、OpenAI、Google GenAI、VertexAI 等）。它具有可脚本化的工作流系统、记忆系统和可扩展的 Agent 技能。

- **GitHub:** <https://github.com/Sikao-Engine/kimi-cli-x>

#### 1. 安装 KimiX

**通过 pip 快速安装：**

```bash
pip install kimix
```

验证安装：

```bash
python -m kimix --version
```

**从源码安装（推荐）：**

```bash
git clone --recursive https://github.com/Sikao-Engine/kimi-cli-x.git
cd kimi-cli-x
uv sync
uv tool install -e .
```

#### 2. 配置 KimiX

##### 手动 JSON 配置（推荐）

您可以手动创建 JSON 配置文件，并通过 CLI 标志传递。

1. 创建您的主模型配置（例如 `ds.json`）：

```json
{
    "model": "deepseek-v4-pro",
    "max_context_size": 1048576,
    "capabilities": ["thinking"],
    "url": "https://api.deepseek.com/",
    "type": "openai_legacy",
    "api_key": "sk-xxx",
    "max_tokens": 384000,
    "thinking_effort": "max",
    "sub_provider": {
        "model": "deepseek-v4-flash",
        "max_context_size": 1048576,
        "capabilities": ["thinking"],
        "url": "https://api.deepseek.com/",
        "type": "openai_legacy",
        "api_key": "sk-xxx",
        "loop_control": {
            "max_ralph_iterations": 0
        },
        "max_tokens": 384000,
        "thinking_effort": "off"
    }
}
```

3. 使用您的自定义配置启动 KimiX：

```bash
kimix --config=ds.json
```

> **提示：** 配置文件可以放在项目的任意父目录中（例如 `~/.config/ds.json`）。KimiX 会从当前工作目录开始向上递归搜索以定位它们，因此您无需在每个项目文件夹中都保留一份副本。

##### 交互式 `/init` 设置（选项 B）

启动 KimiX 并运行 `/init` 命令以交互方式创建您的配置：

```bash
kimix
> /init
```

交互式向导将引导您完成以下步骤：

1. **选择提供商模板** — `deepseek`。
2. **模型名称** — 例如 `deepseek-v4-pro`。
3. **模型类型** — 例如 `openai_legacy`
4. **API 密钥** — 您的提供商 API 密钥。如果环境中已设置 `KIMI_API_KEY` 或 `KIMIX_API_KEY`，则可以跳过输入。
5. **上下文大小** — 选择 `128k`、`200k`、`256k`、`512k`、`1M`，或输入自定义数字。
6. **最大 token 数** — 每次请求的最大 token 数（必须小于上下文大小减去预留空间）。例如 `1M`
7. **思考强度** — `off`、`low`、`medium`、`high`、`xhigh` 或 `max`。
8. **能力** — 逗号分隔列表：`thinking`、`always_thinking`、`image_in`、`video_in`；或 `none` 表示空。
9. **API URL** — 您的提供商的基础端点 URL。
10. **子提供商（可选）** — 为子代理任务配置辅助模型，包括其自身的模型、类型、URL、API 密钥、上下文大小、思考强度、能力和最大 token 数。您可以为此配置 `deepseek-v4-flash`。

配置将保存到 `default_config.json` 并在您的默认编辑器中打开。您可以随时重新运行 `/init` 以更新设置。如果启动 KimiX 时未找到配置，它将提示您自动初始化。


#### 3. 启动 KimiX

进入您的项目目录并运行：

```bash
cd /path/to/my-project
kimix
```

#### 资源

- [KimiX GitHub 仓库](https://github.com/Sikao-Engine/kimi-cli-x)
- [DeepSeek API 文档](https://api-docs.deepseek.com/)
- [DeepSeek 平台](https://platform.deepseek.com/api_keys)
