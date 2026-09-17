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
- Select the model you want to use.

> **Note:** `deepseek-reasoner` and `deepseek-chat` are retired. If Cline's built-in DeepSeek provider does not list `deepseek-flash` yet, use the OpenAI-compatible setup below.

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
- Enter **Model ID**, e.g. `deepseek-flash`.
- (Optional) Click **Model Configuration** to adjust window size, temperature, pricing, and limits.

<div align="center">
<img src="./assets/cline_step_4_b.png" width="250" border="1" />
</div>

After configuration, you can start using Cline:

<div align="center">
<img src="./assets/cline_step_5_b.png" width="250" border="1" />
</div>
