[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← Back](../README.md)

# Integrate with Hermes Agent

Hermes is a self-improving AI agent built by Nous Research. It includes a built-in learning loop: it creates skills from experience, improves them during use, persists knowledge, and builds an evolving model of your preferences across sessions.

#### 1. Install Hermes

##### Quick Install

Get Hermes Agent up and running in under two minutes with the one-line installer.

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

The only prerequisite is Git. The installer automatically handles everything else.

For more installation instructions, please refer to the [Hermes installation page](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

#### 2. Run and Configure

Reload your shell and start Hermes configuration:

- Execute the `hermes setup` command
- Choose the Quick Setup option
- When prompted for the model provider, select **DeepSeek**
- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Enter the Base URL as `https://api.deepseek.com`
- Select the `deepseek-v4-pro` model
- Continue with the remaining options

#### 3. Thinking Mode and Common Errors

##### About Thinking Mode

DeepSeek models have Thinking Mode enabled by default. During tool-calling turns, the model generates `reasoning_content` (chain-of-thought), and per the [DeepSeek Thinking Mode documentation](https://api-docs.deepseek.com/guides/thinking_mode), this `reasoning_content` must be passed back in subsequent requests.

Hermes sets `display.show_reasoning` to `false` by default, which strips `reasoning_content` from the conversation history. This can cause an HTTP 400 error.

##### Handling the 400 Error

If you encounter the following error at runtime:

```
HTTP 400: The `reasoning_content` in the thinking mode must be passed back to the API.
```

This means `reasoning_content` is not being correctly passed back. Here are two solutions:

**Option A: Disable Thinking Mode (Recommended)**

Edit `~/.hermes/config.yaml` and add the following under the `model` section:

```yaml
model:
  default: deepseek-v4-pro
  provider: custom
  base_url: https://api.deepseek.com
  api_mode: chat_completions
  api_key: <your-deepseek-api-key>
  extra_body:
    thinking:
      type: disabled
```

With this option, DeepSeek no longer generates `reasoning_content`, avoiding the passback conflict entirely while also saving context tokens.

**Option B: Keep Thinking Mode**

If you want to keep the reasoning process, enable `show_reasoning` to ensure `reasoning_content` is preserved in the conversation history:

```yaml
model:
  default: deepseek-v4-pro
  provider: custom
  base_url: https://api.deepseek.com
  api_mode: chat_completions
  api_key: <your-deepseek-api-key>
  extra_body:
    thinking:
      type: enabled

display:
  show_reasoning: true
```

With this option, Hermes preserves and forwards `reasoning_content`, but the terminal will display the reasoning process and context consumption will increase.

Restart Hermes after modifying the configuration for changes to take effect.
