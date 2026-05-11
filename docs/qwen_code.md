[English](./qwen_code.md) | [简体中文](./qwen_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Qwen Code

Qwen Code is an open-source AI agent that lives in your terminal, built by the Qwen team at Alibaba Group. It has DeepSeek as a **built-in third-party provider** — just bring your API key.

- **GitHub:** <https://github.com/QwenLM/qwen-code>
- **Docs:** <https://qwenlm.github.io/qwen-code-docs/en/users/overview/>

#### 1. Install Qwen Code

- Install [Node.js](https://nodejs.org/en/download/) 20 or later.
- Install Qwen Code:

```bash
npm install -g @qwen-code/qwen-code@latest
```

Or via the quick-install script:

```bash
bash -c "$(curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh)"
```

Or Homebrew:

```bash
brew install qwen-code
```

- Verify:

```bash
qwen --version
```

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure DeepSeek via /auth

Launch Qwen Code, then run the `/auth` command:

```bash
qwen
```

Inside the interactive session:

```
/auth
```

The `/auth` menu will appear. Follow these steps:

1. Select **Third-party Providers**
2. Select **DeepSeek API Key**
3. **Step 1/2** — paste your DeepSeek API key and press Enter
4. **Step 2/2** — confirm the model IDs: `deepseek-v4-pro, deepseek-v4-flash` (or edit if needed), press Enter

After confirmation, you'll see: `Successfully configured DeepSeek API Key`.

#### 4. Switch to a DeepSeek Model

Run the `/model` command and select `deepseek-v4-pro` or `deepseek-v4-flash`:

```
/model
```

You're ready to go. Qwen Code will now use DeepSeek V4 models for coding.

> **Tip:** Use `/model` to switch between models at any time. Use `/auth` again if you need to reconfigure your API key.