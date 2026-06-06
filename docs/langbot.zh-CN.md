# LangBot 接入DeepSeek AI

[LangBot](https://langbot.app/) 是一个开源的大语言模型原生即时通信机器人开发平台，支持飞书、钉钉、企业微信、个人微信助手、Discord、Slack 等多种平台快速接入，旨在提供开箱即用的 IM 机器人开发体验，具有 Agent、RAG、MCP 等多种 LLM 应用功能，适配全球主流即时通信平台，并提供丰富的 API 接口，支持自定义开发。

结合 DeepSeek V4 Pro 以及其他兼容模型，用户可以实现个人助手、智能客服等多种功能的 IM 机器人。以下为完整的配置教程，简单几步即可拥有专属智能助手。

---

### 第一步：获取DeepSeek API Key

#### 获取 API Key
1. 注册并登录 [DeepSeek API Key官网](https://platform.deepseek.com/sign_in) 。


2. 打开[API 密钥管理页面](https://platform.deepseek.com/api_keys)，生成 API 密钥。


#### 获取模型信息
访问DeepSeek AI 官网的模型文档页面查看可用模型及详细参数。


---

### 第二步：部署并配置 LangBot

#### 使用包管理器部署LangBot
LangBot 已打包发布至 PyPI，请先确保已经安装[uv](https://docs.astral.sh/uv/getting-started/installation/)，然后在空的文件夹下运行该命令:

```bash
uvx langbot@latest
```

这将把该目录作为工作目录，访问该本地地址即可:

```
http://127.0.0.1:5300 #如果是远程云服务器则需要访问 http://服务器公网IP:5300
```

---
#### 使用 Docker 部署 LangBot
确保已安装 Git 和 Docker。

```bash
git clone https://github.com/langbot-app/LangBot
cd LangBot/docker
docker compose up -d
```

> 如果在中国大陆使用，可将 `docker-compose.yaml` 中的镜像替换为：
```
docker.langbot.app/langbot-public/rockchin/langbot:latest
```

#### 访问 WebUI
启动后访问：
```
http://127.0.0.1:5300 #如果是远程云服务器则需要访问 http://服务器公网IP:5300
```
首次运行会提示创建配置文件，请根据提示完成初始化。

#### 配置对话模型
1. 登录 WebUI，进入 **模型配置** 页面。
2. 添加新模型，填写如下信息：

| 字段 | 内容 |
|------|------|
| 模型名称 | 从 DeepSeek api文档中选择的模型名称 |
| 模型提供商 | DeepSeek |
| API Key | 从DeepSeek api网站获取的密钥 |


---

### 第三步：接入平台（以钉钉为例）

> 企业微信、飞书、Discord、Telegram、QQ、微信 等更多平台，请参考 [LangBot 文档](https://docs.langbot.app/zh/usage/platforms/readme)

#### 创建钉钉机器人应用
1. 登录 [钉钉开发者后台](https://open-dev.dingtalk.com/)


1. 进入组织，点击「应用开发」→「创建应用」，填写基本信息。
2. 添加「机器人」能力，完成基础配置并发布。


#### 配置机器人
- 在「机器人」选项卡中填写相关信息并发布。


- 在「版本管理」中配置版本号。


- 在「事件订阅」中选择 **Stream 模式**，无需公网回调地址。
- 在「凭证与基础信息」中记录：
  - Client ID
  - Client Secret
  - RobotCode
  - 机器人名称

#### 配置 LangBot 平台绑定
1. 打开 LangBot WebUI，编辑机器人。


1. 绑定流水线（默认已有 `ChatPipeline`），平台选择 **钉钉**。
2. 编辑流水线，在 AI 能力中选择 **内置 Agent**，并选择此前配置好的DeepSeek 模型。


---

### 第四步：使用机器人

1. 在钉钉搜索机器人名称，点击即可开始聊天。
2. 如需在群聊中使用，可在群设置中点击「添加机器人」，搜索名称添加。
