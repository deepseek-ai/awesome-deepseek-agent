[English](./adal.md) | [简体中文](./adal.zh-CN.md) · [← Back](../README.md)

# Integrate with AdaL

AdaL is an open-source AI coding agent CLI for terminal-based software engineering, with SDK and cloud agent hosting options.

#### 1. Install AdaL

Install the CLI via the install script:

```
curl -fsSL https://adal.sylph.ai/install.sh | bash
```

Or via npm:

```
npm install -g @sylphai/adal-cli
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

- Add your [DeepSeek API Key](https://platform.deepseek.com/api_keys) as a Bring-Your-Own-API-Key (BYOAK), which routes billing directly through DeepSeek instead of AdaL's proxy:

```
/byoak add deepseek
```

- Switch the active model to DeepSeek-V4-Pro:

```
/model deepseek-deepseek-v4-pro
```

DeepSeek-V4-Flash is also available as `deepseek-deepseek-v4-flash` for faster, lower-cost runs.

AdaL's model registry sets the input context window for both models close to the 1M-token limit (936K for V4-Pro, 984K for V4-Flash) automatically — no manual config needed. AdaL does not expose a separate reasoning-effort flag for DeepSeek, since DeepSeek-V4 does not take a per-request effort parameter through AdaL's provider abstraction.

#### 3. Non-interactive / headless mode

DeepSeek models also work in AdaL's headless mode for scripting and CI:

```
adal -q "Refactor this function for readability" -m deepseek-deepseek-v4-pro
```
