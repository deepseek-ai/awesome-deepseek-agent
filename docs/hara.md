[English](./hara.md) | [简体中文](./hara.zh-CN.md) · [← Back](../README.md)

# Integrate with Hara CLI

Hara CLI is an open-source coding agent CLI that runs in the terminal, supports multiple providers, and can use DeepSeek through its OpenAI-compatible endpoint.

- **GitHub:** <https://github.com/hara-cli/hara>
- **Docs:** <https://docs.hara.run/zh/getting-started/installation>

#### 1. Install Hara CLI

- Install [Node.js](https://nodejs.org/en/download/) 20 or later.
- Install Hara CLI 0.113.0 or later:

```bash
npm i -g @nanhara/hara@0.113.0
```

- Verify:

```bash
hara --version
```

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and keep it private.

#### 3. Configure DeepSeek

Hara has a built-in `deepseek` provider. The provider default endpoint is `https://api.deepseek.com`.

You can use the interactive setup wizard:

```bash
hara setup
```

Select DeepSeek, enter your API key, and choose `deepseek-v4-pro` or `deepseek-v4-flash`.

Or configure it with commands:

```bash
hara config set provider deepseek
hara config set model deepseek-v4-pro
hara config set reasoningEffort max
```

Then provide your API key with an environment variable:

```bash
export DEEPSEEK_API_KEY="your-api-key"
```

Alternatively, Hara can store the key in `~/.hara/config.json`:

```bash
hara config set apiKey "your-api-key"
```

Do not commit `~/.hara/config.json` or any API key to your project.

#### 4. Verify the Setup

Run:

```bash
hara doctor
```

The output should show:

```text
provider deepseek · model deepseek-v4-pro · https://api.deepseek.com
auth configured
```

#### 5. First Run

Use Hara interactively in a project:

```bash
cd your-project
hara
```

Or run a one-shot task:

```bash
hara -p "summarize this repository"
```

#### DeepSeek V4 Notes

- Use `deepseek-v4-pro` for the strongest coding and agentic tasks, or `deepseek-v4-flash` for faster and lower-cost runs.
- DeepSeek V4 models support a 1M-token context window. Hara does not currently expose a `context_window` setting for the DeepSeek provider, so there is nothing extra to configure in Hara.
- Hara CLI 0.113.0 and later supports DeepSeek V4 thinking control through `reasoningEffort`. `hara config set reasoningEffort max` sends DeepSeek `thinking: { type: "enabled" }` and `reasoning_effort: "max"` on the OpenAI-compatible chat endpoint.
- Do not use deprecated DeepSeek V3 model names.
