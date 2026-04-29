[English](./astrbot.md) | [简体中文](./astrbot.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AstrBot

[AstrBot](https://github.com/AstrBotDevs/AstrBot) 是一个开源的一站式 Agent 助手。它支持接入 QQ、微信、飞书、Telegram 等主流消息平台，也可以通过技能、插件和 MCP 扩展能力。

#### 1. 安装 AstrBot

##### 通过 uv 安装 AstrBot

macOS 和 Linux 用户执行以下命令安装 AstrBot：

```bash
curl -LsSf https://docs.astrbot.app/install.sh | bash
```

Windows 用户执行以下命令安装：

```bash
iwr -useb https://docs.astrbot.app/install.ps1 | iex
```

然后初始化并启动 AstrBot：

```bash
astrbot init # 仅首次使用时执行，用于初始化环境。这个指令会将 AstrBot 安装到当前终端所在的目录。
astrbot run  # 启动 AstrBot。这个指令会检测当前目录是否安装了 AstrBot，如果未安装会提示使用 `astrbot init` 初始化。
```

##### 通过 Docker 安装 AstrBot

首先克隆 AstrBot 仓库：

```bash
git clone https://github.com/AstrBotDevs/AstrBot --depth 1
cd AstrBot
```

然后启动服务：

```bash
sudo docker compose up -d
```

#### 2. 配置 AstrBot 中的默认模型

初始化完成后，打开 Web UI：

```bash
http://localhost:6185 # 如果 AstrBot 运行在服务器上，则访问 http://<server-ip>:6185
```

在左侧边栏进入 `模型提供商` 页面，点击 `+ 新增`，选择 `DeepSeek`，将你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 `API Key` 输入框中，然后点击 `保存配置`。

接着在左侧边栏进入 `配置文件（普通配置）` 页面，将 `默认对话模型` 设置为刚刚配置的模型，确认选择后，点击右下角的保存按钮。

其余设置，例如消息平台和技能等，可以按需配置。更多信息请参考 [AstrBot 文档](https://docs.astrbot.app/)。

#### 3. 开始使用

点击右上角的 `Chat`，进入 AstrBot Chat UI。现在你可以开始使用 DeepSeek 模型进行对话。

你也可以配置消息平台，在常用聊天应用中直接使用 AstrBot。
