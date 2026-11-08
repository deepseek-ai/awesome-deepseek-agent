
[English](./infer.md) | [简体中文](./infer.zh-CN.md) · [← Back](../README.md)

# Integrate with Inference Gateway CLI

Inference Gateway CLI (`infer`) is a Go-based command-line tool for interacting with AI models through the Inference Gateway. It supports interactive chat, autonomous agents, and developer workflows.

### 1. Install Inference Gateway CLI

**Prerequisites:**
- Node.js 18 or later.

Check your Node.js and npm versions:

```bash
node --version
npm --version
```

The recommended way to run the CLI without installing it globally is:

```bash
npx @inference-gateway/cli@latest --help
npx @inference-gateway/cli@latest chat
```

Alternatively, install the CLI globally:

```bash
npm install -g @inference-gateway/cli
```

Verify the installation:

```bash
infer --help
infer --version
```

### 2. Configure DeepSeek Provider

The CLI can load provider API keys from environment variables, a project `.env` file, or the userspace `~/.infer/auth.yaml` file.

1. Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. Initialize the CLI configuration:

```bash
infer init
```

3. Open `~/.infer/auth.yaml` (on Windows, `%USERPROFILE%\.infer\auth.yaml`) and add:

```yaml
DEEPSEEK_API_KEY: your-deepseek-api-key
```

Replace the placeholder with your actual API key.

**Important:** Keep your API key private. Never add real API keys to project files or commit them to GitHub.

### 3. Run and Select a DeepSeek Model


### DeepSeek V4 Configuration

Set DeepSeek V4-Pro as the default model and enable maximum reasoning effort:

```bash
infer config set agent.model deepseek/deepseek-v4-pro
infer config set agent.reasoning_effort max
```

Verify the configuration:

```bash
infer config get agent.model
infer config get agent.reasoning_effort
```

DeepSeek V4 models support a context window of up to 1 million tokens. The Inference Gateway CLI uses the model metadata provided by the gateway rather than a separate context-window setting in this guide.


Check the gateway status:

```bash
infer status
```

Start an interactive chat session:

```bash
infer chat
```

Inside the chat interface, open the model picker:

```text
/model
```

Select a DeepSeek model, such as:

```text
deepseek/deepseek-v4-flash
```

You can also switch models directly:

```text
/model deepseek/deepseek-v4-flash
```

You can now interact with DeepSeek through the Inference Gateway CLI.


### 4. Troubleshooting

If the CLI cannot connect to DeepSeek:

- Verify that your DeepSeek API key is valid.
- Check that `DEEPSEEK_API_KEY` is available to the CLI.
- Run `infer status` to check gateway health.
- Run `infer --help` to review available commands.

For more information, visit the [Inference Gateway CLI documentation](https://docs.inference-gateway.com/cli/) and the [official GitHub repository](https://github.com/inference-gateway/cli).
