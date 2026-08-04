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

By default AdaL routes DeepSeek through its own hosted proxy, billed via AdaL credits/subscription.

To bill DeepSeek usage directly to your own DeepSeek account instead, add your API key with BYOAK (bring your own API key):

```
/byoak add deepseek
```

Run it without a key to get setup instructions, or pass the key inline as `/byoak add deepseek <api-key>`. Create a key at [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys). Once the key is enabled, DeepSeek requests go straight to the DeepSeek API and are billed by DeepSeek rather than deducted from AdaL credits. Manage or remove keys any time with `/byoak`.

Both models run with a 1M-token context window in AdaL — no manual configuration is needed.

AdaL does not currently expose a reasoning-effort setting for DeepSeek. Its per-request effort control is wired per provider, and DeepSeek is not among the providers with an effort path today, so V4-Pro runs at the API default rather than a caller-selected level such as `max`.

#### 3. Non-interactive / headless mode

DeepSeek models also work in AdaL's headless mode for scripting and CI:

```
adal -q "Refactor this function for readability" -m deepseek-deepseek-v4-pro
```
