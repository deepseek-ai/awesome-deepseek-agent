# Integrating DeepSeek AI with LangBot

[LangBot](https://langbot.app/) is an open-source, LLM-native instant messaging bot development platform. It supports rapid integration with various platforms, including Lark, DingTalk, WeCom, personal WeChat assistants, Discord, and Slack. LangBot is designed to provide an out-of-the-box IM bot development experience, offering a wide range of LLM application capabilities such as Agents, RAG, and MCP. It is compatible with major global instant messaging platforms and provides rich API interfaces for custom development.

By integrating DeepSeek V4 Pro and other compatible models, users can build IM bots for various use cases, such as personal assistants and intelligent customer service. The following is a complete configuration guide that enables you to set up your own intelligent assistant in just a few simple steps.

---

### Step 1: Obtain a DeepSeek API Key

#### Obtain an API Key

1. Register and log in to the [DeepSeek API Key official website](https://platform.deepseek.com/sign_in).

2. Open the [API key management page](https://platform.deepseek.com/api_keys) and generate an API key.

#### Obtain Model Information

Visit the model documentation page on the official DeepSeek AI website to view available models and their detailed parameters.

---

### Step 2: Deploy and Configure LangBot

#### Deploy LangBot Using a Package Manager

LangBot has been packaged and published to PyPI. Please ensure that [uv](https://docs.astral.sh/uv/getting-started/installation/) has been installed, then run the following command in an empty folder:

```bash
uvx langbot@latest
```

This directory will be used as the working directory. You can access the local service at:

```text
http://127.0.0.1:5300 # If using a remote cloud server, access http://<server-public-IP>:5300
```

---

#### Deploy LangBot Using Docker

Ensure that Git and Docker have been installed.

```bash
git clone https://github.com/langbot-app/LangBot
cd LangBot/docker
docker compose up -d
```

> If you are using LangBot in mainland China, you may replace the image in `docker-compose.yaml` with:
>
```text
docker.langbot.app/langbot-public/rockchin/langbot:latest
```

#### Access the WebUI

After startup, visit:

```text
http://127.0.0.1:5300 # If using a remote cloud server, access http://<server-public-IP>:5300
```

When running for the first time, you will be prompted to create a configuration file. Follow the on-screen instructions to complete the initialization.

#### Configure the Conversation Model

1. Log in to the WebUI and go to the **Model Configuration** page.
2. Add a new model and fill in the following information:

| Field | Content |
|------|------|
| Model Name | The model name selected from the DeepSeek API documentation |
| Model Provider | DeepSeek |
| API Key | The key obtained from the DeepSeek API website |

---

### Step 3: Connect to a Platform — DingTalk as an Example

> For more platforms, including WeCom, Lark, Discord, Telegram, QQ, and WeChat, please refer to the [LangBot documentation](https://docs.langbot.app/zh/usage/platforms/readme).

#### Create a DingTalk Bot Application

1. Log in to the [DingTalk Developer Console](https://open-dev.dingtalk.com/).

2. Enter your organization, click **Application Development** → **Create Application**, and fill in the basic information.
3. Add the **Bot** capability, complete the basic configuration, and publish the application.

#### Configure the Bot

- Fill in the relevant information under the **Bot** tab and publish it.

- Configure the version number under **Version Management**.

- Under **Event Subscription**, select **Stream Mode**. A public callback URL is not required.
- Under **Credentials and Basic Information**, record the following:
  - Client ID
  - Client Secret
  - RobotCode
  - Bot name

#### Configure Platform Binding in LangBot

1. Open the LangBot WebUI and edit the bot.

2. Bind a pipeline. The default `ChatPipeline` is already available. Select **DingTalk** as the platform.
3. Edit the pipeline, select **Built-in Agent** under AI capabilities, and choose the previously configured DeepSeek model.

---

### Step 4: Use the Bot

1. Search for the bot name in DingTalk and click it to start chatting.
2. To use the bot in a group chat, click **Add Bot** in the group settings and search for the bot name to add it.