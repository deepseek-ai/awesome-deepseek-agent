[English](./vtcode.md) | [简体中文](./vtcode.zh-CN.md) · [← Back](../README.md)

# Integrate with VT Code

VT Code is a Rust terminal coding agent with native DeepSeek support, so you can connect it directly to DeepSeek V4 without a proxy or custom endpoint.

#### 1. Install VT Code

Install VT Code using your preferred method, then make sure the `vtcode` binary is on your `PATH`.

```shell
cargo install vtcode
```

If you want a fresh project config, run:

```shell
vtcode init
```

#### 2. Get a DeepSeek API Key

- Go to [DeepSeek Platform](https://platform.deepseek.com/api_keys) and create an API key.
- Save it in your shell as `DEEPSEEK_API_KEY`.

#### 3. Configure VT Code

Create or edit `vtcode.toml` in your project root:

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

Notes:

- `deepseek-v4-pro` is the best default for coding tasks.
- `reasoning_effort = "max"` matches DeepSeek V4 Pro’s highest reasoning setting.
- `context_window = 1000000` and `max_output_tokens = 384000` reflect DeepSeek V4’s 1M context support.
- If you want a faster and cheaper default, switch `default_model` to `deepseek-v4-flash`.

#### 4. Start VT Code

```shell
cd /path/to/your-project
vtcode ask "Summarize this repository"
```

If you prefer the full interactive session, run `vtcode` instead.

#### Resources

- [VT Code](https://github.com/vinhnx/vtcode)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
