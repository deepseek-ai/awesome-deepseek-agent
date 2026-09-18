[English](./deepseek_code.md) | [简体中文](./deepseek_code.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Code

<div align="center">
  <img src="./assets/deepseek_code_logo.png" alt="DeepSeek Code" height="120" />
</div>

DeepSeek Code is an open-source DeepSeek-powered terminal coding agent with a full TUI, multi-provider support, MCP, LSP, and Agent Skills. Both `deepseek-v4-pro` and `deepseek-v4-flash` are supported with the full **1M token context** window.

- **GitHub:** <https://github.com/Hermenics/deepseek-code>

<div align="center">
  <img src="./assets/deepseek_code_demo.gif" alt="DeepSeek Code demo" width="720" />
</div>

#### 1. Install DeepSeek Code

- Install [Node.js](https://nodejs.org/en/download/) 18+ or [Bun](https://bun.sh) 1.1+.
- Run the following command in your terminal:

```sh
npm install -g @hermenics/deepseek-code
```

- Verify the installation:

```sh
deepseek --version
```

#### 2. Configure DeepSeek Code

On first run, DeepSeek Code will prompt you to pick a provider. Choose **DeepSeek API** and enter your API key.

Alternatively, set the environment variable directly:

```sh
export DEEPSEEK_API_KEY=sk-...
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Secrets are stored in `~/.deepseek/config.json`. Non-secret preferences use `settings.json` with `User < Project < Local` precedence.

**Supported providers:**

| Provider | Env / config keys |
|----------|--------------------|
| DeepSeek API (default) | `DEEPSEEK_API_KEY`, `DEEPSEEK_BASE_URL` |
| Amazon Bedrock | `AWS_REGION`, `AWS_PROFILE` |
| Google Vertex AI | `GCP_PROJECT`, `GCP_LOCATION`, `GCP_CREDENTIALS` |
| Local (Ollama / LM Studio) | `LOCAL_BASE_URL`, `LOCAL_MODEL` |

**Supported models:**

| Model | Context | Thinking | Description |
|-------|---------|----------|-------------|
| `deepseek-v4-flash` (default) | 1M | ✅ | Fast, general purpose |
| `deepseek-v4-pro` | 1M | ✅ | Advanced reasoning |

Switch models at any time with `/model`.

**Reasoning effort control:**

DeepSeek Code supports `/effort` to control how much reasoning the model performs:

| Level | Description |
|-------|-------------|
| `low` | Thinking disabled — fastest responses |
| `high` | Thinking enabled, default effort (default) |
| `max` | Deepest reasoning — `reasoning_effort: max` |

```sh
/effort max
```

**Pricing (DeepSeek API, per 1M tokens):**

| Model | Input (cache miss) | Input (cache hit) | Output |
|-------|--------------------|-------------------|--------|
| `deepseek-v4-flash` | $0.14 | $0.0028 | $0.28 |
| `deepseek-v4-pro` | $0.435 | $0.003625 | $0.87 |

Source: [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing)

#### 3. Enter a project directory and launch DeepSeek Code

```sh
cd /path/to/my-project
deepseek
```

For automation, use headless pipe mode:

```sh
echo "explain this project" | deepseek --pipe
```

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline |
| `Esc` | Interrupt the current model turn |
| `/` | Open the slash command menu |
| `/model` | Switch the active model |
| `/agent` | Spawn a sub-agent |
| `/vim` | Toggle vim keybindings |
| `/theme` | Change color theme |
| `/help` | Show all commands |

#### Using Agent Skills

Agent Skills are discovered from:

- **User-level:** `~/.deepseek/skills/<name>/SKILL.md`
- **Project-level:** `./.deepseek/skills/<name>/SKILL.md`

#### Pipe Mode

```sh
cat src/index.tsx | deepseek --pipe --json "summarize this file"
```
