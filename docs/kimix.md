[English](./kimix.md) | [简体中文](./kimix.zh-CN.md) · [← Back](../README.md)

# Integrate with KimiX

KimiX (Kimi-CLI-X) is a terminal AI coding agent that optimized for DeepSeek models, supports multiple API providers (Anthropic, Kimi, OpenAI, Google GenAI, VertexAI, and more). It features a scriptable workflow system, memory system, and extensible Agent Skills.

- **GitHub:** <https://github.com/Sikao-Engine/kimi-cli-x>

#### 1. Install KimiX

**Quick install via pip:**

```bash
pip install kimix
```

Verify the installation:

```bash
python -m kimix --version
```

**Install from source (Recommended):**

```bash
git clone --recursive https://github.com/Sikao-Engine/kimi-cli-x.git
cd kimi-cli-x
uv sync
uv tool install -e .
```

#### 2. Configure KimiX

##### Manual JSON Configuration (Recommended)

You can manually create JSON config files and pass them via CLI flags.

1. Create your primary model config (e.g., `ds.json`):

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

3. Launch KimiX with your custom configs:

```bash
kimix --config=ds.json
```

> **Tip:** Config files can be placed in any parent directory of your project (e.g., `~/.config/ds.json`). KimiX searches recursively upward from the current working directory to locate them, so you don't need to keep a copy in every project folder.

##### Interactive `/init` Setup (Option B)

Launch KimiX and run the `/init` command to create your configuration interactively:

```bash
kimix
> /init
```

The interactive wizard will guide you through:

1. **Select a provider template** — `deepseek`.
2. **Model name** — e.g. `deepseek-v4-pro`.
3. **Model type** — e.g. `openai_legacy`
4. **API key** — Your provider API key. If `KIMI_API_KEY` or `KIMIX_API_KEY` is already set in your environment, you can skip entering it.
5. **Context size** — Choose `128k`, `200k`, `256k`, `512k`, `1M`, or enter a custom number.
6. **Max tokens** — Maximum tokens per request (must be less than context size minus reserved space).
7. **Thinking effort** — `off`, `low`, `medium`, `high`, `xhigh`, or `max`.
8. **Capabilities** — Comma-separated list: `thinking`, `always_thinking`, `image_in`, `video_in`; or `none` for empty.
9. **API URL** — The base endpoint URL for your provider.
10. **Sub-provider (optional)** — Configure a secondary model for sub-agent tasks, including its own model, type, URL, API key, context size, thinking effort, capabilities, and max tokens. You may configure `deepseek-v4-flash` for this.

The configuration is saved to `default_config.json` and opened in your default editor. You can re-run `/init` at any time to update settings. If no configuration is found when launching KimiX, it will prompt you to initialize automatically.


#### 3. Launch KimiX

Enter your project directory and run:

```bash
cd /path/to/my-project
kimix
```

#### Resources

- [KimiX GitHub Repository](https://github.com/Sikao-Engine/kimi-cli-x)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
- [DeepSeek Platform](https://platform.deepseek.com/api_keys)
