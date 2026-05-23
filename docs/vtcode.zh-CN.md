[English](./vtcode.md) | [简体中文](./vtcode.zh-CN.md) · [← Back](../README.md)

# 接入 VT Code

VT Code 是一款 Rust 终端编程 Agent，内置 DeepSeek 支持，因此你可以直接连接 DeepSeek V4，无需代理或自定义接口。

#### 1. 安装 VT Code

使用你习惯的方式安装 VT Code，并确保 `vtcode` 命令已加入 `PATH`。

```shell
cargo install vtcode
```

如果你想生成一份新的项目配置，可以执行：

```shell
vtcode init
```

#### 2. 获取 DeepSeek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 将其保存为环境变量 `DEEPSEEK_API_KEY`。

#### 3. 配置 VT Code

在项目根目录创建或编辑 `vtcode.toml`：

```toml
[agent]
provider = "deepseek"
api_key_env = "DEEPSEEK_API_KEY"
default_model = "deepseek-v4-pro"
reasoning_effort = "max"

[agent.model_settings]
context_window = 1000000
max_output_tokens = 384000
```

说明：

- `deepseek-v4-pro` 是编程任务最合适的默认模型。
- `reasoning_effort = "max"` 对应 DeepSeek V4 Pro 的最高推理强度。
- `context_window = 1000000` 和 `max_output_tokens = 384000` 体现了 DeepSeek V4 的 100 万上下文支持。
- 如果你更重视速度和成本，可以把 `default_model` 改成 `deepseek-v4-flash`。

#### 4. 启动 VT Code

```shell
cd /path/to/your-project
vtcode ask "总结一下这个仓库"
```

如果你想进入完整交互式会话，也可以直接运行 `vtcode`。

#### 相关资源

- [VT Code](https://github.com/vinhnx/vtcode)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
