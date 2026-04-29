[English](./astrbot.md) | [简体中文](./astrbot.zh-CN.md) · [← Back](../README.md)

# Integrate with AstrBot

[AstrBot](https://github.com/AstrBotDevs/AstrBot) is an open-source all-in-one agent assistant that integrates with mainstream messaging platforms such as QQ, WeChat, Feishu, and Telegram, and can be extended with skills, plugins, and MCPs to enhance its functionality.

#### 1. Install AstrBot

##### Install AstrBot via uv

For macOS and Linux users, run the following command to install AstrBot:

```bash
curl -LsSf https://docs.astrbot.app/install.sh | bash
```

For Windows users, run the following command instead:

```bash
iwr -useb https://docs.astrbot.app/install.ps1 | iex
```

Then initialize and start AstrBot:

```bash
astrbot init # Run this only once to initialize the environment. This command installs AstrBot into the current terminal directory.
astrbot run  # Start AstrBot. This command checks whether AstrBot is installed in the current directory; if not, it prompts you to initialize it with `astrbot init`.
```

##### Install AstrBot via Docker

First, clone the AstrBot repository:

```bash
git clone https://github.com/AstrBotDevs/AstrBot --depth 1
cd AstrBot
```

Then, start the service:

```bash
sudo docker compose up -d
```

#### 2. Configure the Default Model in AstrBot

After initialization, open the Web UI:

```bash
http://localhost:6185 # Or http://<server-ip>:6185 if AstrBot runs on a server
```

In the left sidebar, open the `Providers` page, click `+ Add`, select `DeepSeek`, paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the `API Key` field, and click `Save Configuration`.

Next, open the `Config(Normal Config)` page, set `Default Chat Model` to the model you just configured, confirm the selection, and click the save button in the bottom-right corner.

For the remaining settings, such as messaging platforms and skills, configure them as needed. See the [AstrBot Docs](https://docs.astrbot.app/) for details.

#### 3. Get Started

Click `Chat` in the top-right corner to switch to the AstrBot Chat UI. You can now start chatting with the DeepSeek model.

You can also configure messaging platforms to use AstrBot directly from your preferred chat app.
