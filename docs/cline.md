[English](./cline.md) | [简体中文](./cline.zh-CN.md) · [← Back](../README.md)

# Integrate with Cline

Cline is an AI coding assistant that runs as a VS Code extension, supporting multiple API providers and models.

#### 1. Install Cline Extension

- Open VS Code.
- Click the **Extensions** icon in the activity bar (or press `Ctrl+Shift+X`).
- Search for `cline`.
- Find the **Cline** extension in the results.

<div align="center">
<img src="./assets/cline_step_1.png" width="250" border="1" />
</div>

#### 2. Install and Trust the Extension

- Click the **Install** button.
- After installation completes, choose to trust the developer when prompted.

#### 3. Choose API Key Mode

- In the Cline settings, select **Bring my own API Key**.

<div align="center">
<img src="./assets/cline_step_3.png" width="250" border="1" />
</div>

#### 4. Configure API Provider

**Method 1: DeepSeek Provider**

- Select **API Provider** as **DeepSeek**.
- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
- Select `deepseek-v4-pro` for the strongest coding performance, or `deepseek-v4-flash` for faster responses.
- Set **Reasoning Effort** to **High**. This is the highest effort currently supported by both Cline and DeepSeek V4.

> **Note:** Cline's built-in DeepSeek provider currently defaults to `deepseek-v4-flash` and supports both V4 models.

<div align="center">
<img src="./assets/cline_step_4_a.png" width="250" border="1" />
</div>

After configuration, you can start using Cline:

<div align="center">
<img src="./assets/cline_step_5_a.png" width="250" border="1" />
</div>

**Method 2: OpenAI Compatible**

- Select **API Provider** as **OpenAI Compatible**.
- Set **Base URL** to `https://api.deepseek.com`.
- Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys).
- Enter **Model ID** as `deepseek-v4-pro` or `deepseek-v4-flash`.
- Open **Model Configuration**, leave **Supports Images** unchecked, set **Context Window Size** to `1000000`, and set **Max Output Tokens** to `384000`.
- Set **Reasoning Effort** to **High**.

<div align="center">
<img src="./assets/cline_step_4_b.png" width="250" border="1" />
</div>

After configuration, you can start using Cline:

<div align="center">
<img src="./assets/cline_step_5_b.png" width="250" border="1" />
</div>
