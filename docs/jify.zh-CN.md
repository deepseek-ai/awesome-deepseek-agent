[English](./jify.md) | [简体中文](./jify.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Jify

Jify 是一款自我进化（self-evolving）的 harness Agent —— 运行在你自有设备上的通用 AI 助手。它内置 Claude Code 风格的工具体循环、Skill 系统、MCP 客户端，以及用于安全任务的 Docker 沙箱。Jify 既支持 Anthropic 兼容端点，也支持 OpenAI 兼容端点，因此可以直接接入 DeepSeek，无需任何代理。

#### 1. 安装 Jify

需要 Python 3.11+。

从源码安装：

```shell
git clone https://github.com/s1mple-top/Jify.git
cd Jify
pip install -e .
```

或使用 uv（推荐）：

```shell
git clone https://github.com/s1mple-top/Jify.git
cd Jify
uv sync
source .venv/bin/activate
```

验证安装：

```shell
jify --help
```

首次运行会在 `~/.jify/config.yaml` 生成配置文件。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并复制。

#### 3. 在 Jify 中配置 DeepSeek

打开 `~/.jify/config.yaml`，把 DeepSeek 模型加入 `models` 列表。Jify 以列表中的**第一个**条目为默认模型，运行时可通过 `/model <name>` 切换。

```yaml
models:
  - name: deepseek-v4-pro
    provider: anthropic
    model: deepseek-v4-pro
    base_url: https://api.deepseek.com/anthropic
    api_key: "sk-your-deepseek-api-key"
    extra_body:
      reasoning_effort: max

  - name: deepseek-v4-flash
    provider: anthropic
    model: deepseek-v4-flash
    base_url: https://api.deepseek.com/anthropic
    api_key: "sk-your-deepseek-api-key"
    extra_body:
      reasoning_effort: max
```

说明：

- `provider: anthropic` 会选用 Jify 的 Anthropic 兼容客户端，配合 `https://api.deepseek.com/anthropic` 端点。若想走 OpenAI 兼容端点，可改为 `provider: openai` 搭配 `base_url: https://api.deepseek.com/v1`。
- `reasoning_effort: max` 会通过 Jify 的 `extra_body` 透传，开启最高推理强度。详见 [思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。
- DeepSeek V4 系列模型支持最高 **100 万 token** 上下文。Jify 会自动管理上下文窗口，无需额外配置 —— 只需注意长会话会消耗较大的上下文预算。

#### 4. 启动 Jify

启动交互式 CLI：

```shell
jify
```

或执行单次非交互式提问：

```shell
jify -q "介绍下这个项目"
```

如需启动 Web UI：

```shell
jify gateway --port 9090
```

#### 验证

在 CLI 中查看当前生效的模型，确认 Jify 已接入 DeepSeek：

```text
/model
```

发起一次测试请求：

```text
jify -q "用一句简短的话打个招呼。"
```

若响应来自 DeepSeek 模型，说明接入成功。你也可以检查 `~/.jify/config.yaml` 中该条目是否包含 `reasoning_effort: max`，以确认推理强度已生效。

#### 常见问题

- 出现 `401` 或认证错误：检查 `~/.jify/config.yaml` 中的 API Key。
- 出现 `402` 或支付错误：检查 DeepSeek 开放平台账户余额。
- 模型未生效：`models` 列表中的**第一个**条目才是默认模型，可调整顺序，或用 `/model <name>` 切换。
- 配置未读取：确认文件位于 `~/.jify/config.yaml`（首次运行会自动生成）。
- `reasoning_effort` 未生效：确认它嵌套在 `extra_body` 之下，而非条目顶层。

#### 相关资源

- [Jify](https://github.com/s1mple-top/Jify)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
