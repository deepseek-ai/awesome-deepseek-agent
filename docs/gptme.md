[English](./gptme.md) | [简体中文](./gptme.zh-CN.md) · [← Back](../README.md)

# Integrate with gptme

gptme is a provider-agnostic, local-first terminal AI agent — a capable alternative to Claude Code. It ships shell, Python, and web tools out of the box and works with Anthropic, OpenAI, Google, xAI, **DeepSeek**, OpenRouter, or fully local models via `llama.cpp`.

- **GitHub:** <https://github.com/gptme/gptme>

#### 1. Install gptme

```sh
pipx install gptme
```

Verify:

```sh
gptme --version
```

#### 2. Get a DeepSeek API Key

Sign up at the [DeepSeek Platform](https://platform.deepseek.com/api_keys), add credit, and copy your API key.

#### 3. Configure the DeepSeek provider

gptme resolves the API key by the `${PROVIDER_NAME}_API_KEY` convention, so export it as `DEEPSEEK_API_KEY`:

```bash
echo 'export DEEPSEEK_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

Then register DeepSeek as a custom OpenAI-compatible provider in `~/.config/gptme/config.toml`:

```toml
[[providers]]
name = "deepseek"
base_url = "https://api.deepseek.com/v1"
api_key_env = "DEEPSEEK_API_KEY"
default_model = "deepseek-chat"
```

(`deepseek-chat` for the V4 chat model; use `deepseek-reasoner` for the R1 reasoning model.)

#### 4. First run

```sh
# Use the custom provider with its default model
gptme --model deepseek "explain this codebase"

# Or pick a specific model
gptme --model deepseek/deepseek-reasoner "design a retry decorator"

# List configured providers
gptme-util providers list
```

gptme also supports MCP servers for databases/APIs/filesystems, a plugin system, and local models via `llama.cpp` (no key needed) — see the [providers docs](https://gptme.org/docs/providers.html) and [custom providers](https://gptme.org/docs/custom-providers.html) for the full surface.
