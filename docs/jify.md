[English](./jify.md) | [简体中文](./jify.zh-CN.md) · [← Back](../README.md)

# Integrate with Jify

Jify is a self-evolving harness agent — a general-purpose AI assistant that runs on your own device. It ships with a Claude-Code-style tool loop, a skills system, MCP client support, and a Docker-backed sandbox for security work. Jify talks to models through either an Anthropic-compatible or an OpenAI-compatible endpoint, so it can use DeepSeek directly with no proxy.

#### 1. Install Jify

Requires Python 3.11+.

Install from source:

```shell
git clone https://github.com/s1mple-top/Jify.git
cd Jify
pip install -e .
```

Or with uv (recommended):

```shell
git clone https://github.com/s1mple-top/Jify.git
cd Jify
uv sync
source .venv/bin/activate
```

Verify the installation:

```shell
jify --help
```

The first run creates a configuration file at `~/.jify/config.yaml`.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure DeepSeek in Jify

Open `~/.jify/config.yaml` and add the DeepSeek model to the `models` list. Jify picks the **first** entry as the default model, and you can switch at runtime with `/model <name>`.

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

Notes:

- `provider: anthropic` selects Jify's Anthropic-compatible client and the `https://api.deepseek.com/anthropic` base URL. Use `provider: openai` with `base_url: https://api.deepseek.com/v1` if you prefer the OpenAI-compatible endpoint.
- `reasoning_effort: max` is passed through Jify's `extra_body` to enable the highest reasoning effort level. See the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode) for details.
- DeepSeek V4 models support up to **1 million tokens** of context. Jify manages the context window automatically, so no extra configuration is required — just be aware that long sessions can consume a large context budget.

#### 4. Start Jify

Launch the interactive CLI:

```shell
jify
```

Or run a single non-interactive query:

```shell
jify -q "Explain what this project does"
```

To launch the Web UI instead:

```shell
jify gateway --port 9090
```

#### Verify

Confirm Jify is talking to DeepSeek by checking the active model inside the CLI:

```text
/model
```

Make a test request:

```text
jify -q "Say hello in one short sentence."
```

If the response comes back through the DeepSeek model, the integration is working. You can also confirm the reasoning level is applied by checking that `reasoning_effort: max` is present in your `~/.jify/config.yaml` entry.

#### Troubleshooting

- `401` or authentication errors: check the API key in `~/.jify/config.yaml`.
- `402` or payment errors: check your DeepSeek Platform balance.
- Model not used: the **first** entry in the `models` list is the default. Reorder entries or switch with `/model <name>`.
- Config not picked up: ensure the file is at `~/.jify/config.yaml` (a fresh config is generated on first run).
- `reasoning_effort` ignored: make sure it is nested under `extra_body`, not at the top level of the entry.

#### Resources

- [Jify](https://github.com/s1mple-top/Jify)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
