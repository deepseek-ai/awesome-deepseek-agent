[English](./adal.md) | [简体中文](./adal.zh-CN.md) · [← Back](../README.md)

# Integrate with AdaL

AdaL is an AI coding agent for the terminal and browser, with SDK and cloud agent hosting options.

#### 1. Install AdaL

**macOS, Linux, WSL:**

```
curl -fsSL https://adal.sylph.ai/install.sh | bash
```

**Windows PowerShell:**

```
irm https://adal.sylph.ai/install/windows | iex
```

**Windows CMD:**

```
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://adal.sylph.ai/install/windows | iex"
```

Verify the installation:

```
adal --version
```

#### 2. Run and Configure

- Start AdaL in your project directory:

```
cd /path/to/my-project
adal
```

- Switch the active model to DeepSeek-V4-Pro:

```
/model deepseek-deepseek-v4-pro
```

DeepSeek-V4-Flash is also available as `deepseek-deepseek-v4-flash` for faster, lower-cost runs.

AdaL routes DeepSeek usage through its own hosted proxy, billed via AdaL credits/subscription — there is currently no bring-your-own-API-key (BYOAK) option for DeepSeek specifically (BYOAK in AdaL is limited to Anthropic, OpenAI, and Google).

DeepSeek-V4 supports up to 1M tokens of context. AdaL applies this automatically — its model registry sets the input context window to 936K for V4-Pro and 984K for V4-Flash, so no manual configuration is needed.

AdaL does not currently expose a reasoning-effort setting for DeepSeek. Its per-request effort control is wired per provider, and DeepSeek is not among the providers with an effort path today, so V4-Pro runs at the API default rather than a caller-selected level such as `max`.

#### 3. Non-interactive / headless mode

DeepSeek models also work in AdaL's headless mode for scripting and CI:

```
adal -q "Refactor this function for readability" -m deepseek-deepseek-v4-pro
```
