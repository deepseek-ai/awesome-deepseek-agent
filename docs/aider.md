[English](./aider.md) | [简体中文](./aider.zh-CN.md) · [← Back](../README.md)
# Integrate with Aider
[Aider](https://aider.chat/) is an AI pair programming tool that runs in your terminal. It works with any OpenAI-compatible API, enabling seamless integration with DeepSeek models.

### Installing Aider
```bash
pip install aider-install
aider-install
```

### Configuring Aider
Aider integrates with DeepSeek via its OpenAI-compatible endpoint. You can configure it using environment variables (recommended) or a `.env` file.

#### Step 1: Set Environment Variables
Set your DeepSeek API key and endpoint. Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Mac / Linux:**
```bash
export OPENAI_API_BASE=https://api.deepseek.com
export OPENAI_API_KEY=<your DeepSeek API Key>
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_BASE="https://api.deepseek.com"
$env:OPENAI_API_KEY="<your DeepSeek API Key>"
```

**Windows (setx, restart shell after):**
```cmd
setx OPENAI_API_BASE https://api.deepseek.com
setx OPENAI_API_KEY <your DeepSeek API Key>
```

#### Step 2: Add Model Metadata (Recommended)
Aider does not ship with metadata for DeepSeek V4 models. Create `.aider.model.metadata.json` in your project root (or set `AIDER_MODEL_METADATA_FILE`) to provide context window and pricing information:

```json
{
  "openai/deepseek-v4-pro": {
    "max_tokens": 384000,
    "max_input_tokens": 1000000,
    "max_output_tokens": 384000,
    "input_cost_per_token": 4.35e-7,
    "output_cost_per_token": 8.7e-7,
    "input_cost_per_token_cache_hit": 3.625e-9,
    "cache_read_input_token_cost": 3.625e-9,
    "litellm_provider": "openai",
    "mode": "chat",
    "supports_assistant_prefill": true,
    "supports_prompt_caching": true
  },
  "openai/deepseek-v4-flash": {
    "max_tokens": 384000,
    "max_input_tokens": 1000000,
    "max_output_tokens": 384000,
    "input_cost_per_token": 1.4e-7,
    "output_cost_per_token": 2.8e-7,
    "input_cost_per_token_cache_hit": 2.8e-9,
    "cache_read_input_token_cost": 2.8e-9,
    "litellm_provider": "openai",
    "mode": "chat",
    "supports_assistant_prefill": true,
    "supports_prompt_caching": true
  }
}
```

> **Note:** This file tells Aider about DeepSeek V4's 1M context window and current pricing, suppressing model warnings and enabling accurate token tracking.

### Using Aider
Navigate to your project directory and launch Aider with the DeepSeek model:

```bash
cd /path/to/your/project
aider --model openai/deepseek-v4-pro
```

For DeepSeek V4 Flash (faster, lower cost):
```bash
aider --model openai/deepseek-v4-flash
```

#### Enabling Max Reasoning Effort
DeepSeek V4 Pro supports reasoning effort levels. Use `max` for the best coding experience:

```bash
aider --model openai/deepseek-v4-pro --reasoning-effort max
```

Or add to `.aider.model.settings.yml`:
```yaml
- name: openai/deepseek-v4-pro
  extra_params:
    reasoning_effort: max
```

#### Verifying the Configuration
To confirm Aider is using your DeepSeek configuration correctly, launch with verbose logging:
```bash
aider --model openai/deepseek-v4-pro --verbose
```

Aider will display `API Base: https://api.deepseek.com` and the active model name on startup.

### Model Selection Guide

| Model | Use Case | Key Strength |
|-------|----------|--------------|
| `openai/deepseek-v4-pro` | Complex refactoring, architecture design | Deep reasoning, 1M context |
| `openai/deepseek-v4-flash` | Quick edits, commit messages, chat summaries | Low cost, fast response |

> **Tip:** Set `deepseek-v4-flash` as the `--weak-model` for commit messages and chat history summaries to save costs while keeping `deepseek-v4-pro` for your main coding tasks.
