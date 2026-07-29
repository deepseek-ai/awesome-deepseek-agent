[English](./deepseek_code.md) | [简体中文](./deepseek_code.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Code

DeepSeek Code is an open-source DeepSeek-powered terminal coding agent with a full TUI, multi-provider support, MCP, LSP, and Agent Skills.

- **GitHub:** <https://github.com/Hermenics/deepseek-code>

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
