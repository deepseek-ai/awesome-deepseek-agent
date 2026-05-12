# Autohand Code × Deepseek

[Autohand Code](https://github.com/autohandai/code-cli) is an open-source CLI for AI-assisted coding that gives you full freedom over which model and provider you use. It connects to any API-compatible backend — including the DeepSeek API — via a simple in-terminal setup.

## Prerequisites

- [Autohand Code CLI](https://github.com/autohandai/code-cli) installed
- A [DeepSeek API key](https://platform.deepseek.com/api_keys)

## Quick Start

### 1. Select Deepseek as your model provider

Inside the Autohand Code CLI, type `/model` to open the model selector. Scroll or search for **deepseek** and press `Enter` to select it.

```
/model
> deepseek
```

### 2. Provide your DeepSeek API Key

After selecting `deepseek`, you will be prompted to enter your API key. Paste the key from [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys).

```
Enter your DeepSeek API key: sk-xxxxxxxxxxxxxxxx
```

The key is stored locally and used for all subsequent requests.

### 3. Select your DeepSeek model

Choose the model that best fits your task:

| Model | Description | Best For |
|-------|-------------|----------|
| `deepseek-chat` | DeepSeek V3 — general-purpose conversational model | Everyday coding, refactoring, explanations |
| `deepseek-reasoner` | DeepSeek R1 — chain-of-thought reasoning model | Complex problem-solving, architecture decisions, debugging |
| `deepseek-coder` | DeepSeek Coder — code-specialized model | Code generation, code review, test writing |

```
Select model: deepseek-reasoner
```

### 4. Start coding

That's it — you're ready to use DeepSeek through Autohand Code. Ask it to write code, review PRs, debug issues, or explore a codebase.

```
> Explain what this repository does and suggest three improvements
```

## Switching between models

You can switch models or providers at any time by running `/model` again. Autohand Code will remember your API key, so switching between DeepSeek models does not require re-entering it.

## Configuration reference

| Setting | Description | Default |
|---------|-------------|---------|
| `provider` | Model provider | `deepseek` |
| `model` | Model identifier | `deepseek-chat` |
| `apiKey` | DeepSeek API key | *(prompted on first use)* |
| `baseUrl` | API base URL for DeepSeek | `https://api.deepseek.com/v1` |

## Troubleshooting

### "Invalid API key" error

- Make sure your key is copied fully from [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys).
- Check that your account has available credits.

### Model not appearing in the selector

- Make sure you have the latest version of Autohand Code: check [code-cli releases](https://github.com/autohandai/code-cli/releases).
- Run `/model` and type `deepseek` to search for it explicitly.

### Rate limiting

- DeepSeek API has rate limits depending on your account tier. See [DeepSeek API docs](https://api-docs.deepseek.com) for details.

## See also

- [DeepSeek API Documentation](https://api-docs.deepseek.com)
- [Autohand Code Repository](https://github.com/autohandai/code-cli)
- [DeepSeek Platform](https://platform.deepseek.com)
