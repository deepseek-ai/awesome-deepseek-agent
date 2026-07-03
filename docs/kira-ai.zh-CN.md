[English](./kira-ai.md) | [简体中文](./kira-ai.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 KiraAI

[KiraAI](https://github.com/xxynet/KiraAI) 是一个开源的模块化 AI 数字生命平台，支持将大语言模型接入 QQ、Telegram、微信、Discord 等多个聊天平台。它提供 WebUI 管理界面、插件系统、具备 MCP 支持的 Agent 能力，并内置了 DeepSeek 专用集成，支持思维模式和推理强度控制。

#### 1. 安装 KiraAI

##### 通过脚本安装（推荐）

前置要求：系统 PATH 中需有 Python 3.10+。

从 [GitHub Releases](https://github.com/xxynet/KiraAI/releases) 下载最新源码压缩包，然后运行：

```bash
# Windows
scripts\run.bat

# Linux / macOS
bash scripts/run.sh
```

脚本会自动创建虚拟环境、检测最快的 pip 镜像源、安装依赖并启动 KiraAI。

##### 通过 Docker 安装

```bash
docker pull xxynet/kira-ai:latest
docker compose up -d
```

或克隆仓库后本地构建：

```bash
git clone https://github.com/xxynet/KiraAI.git --depth 1
cd KiraAI
docker compose up -d
```

启动后访问 `http://localhost:5267` 即可使用。

更多信息请参阅 [KiraAI 文档](https://docs.kira-ai.top/zh/)。

#### 2. 在 KiraAI 中配置 DeepSeek

打开 KiraAI WebUI `http://localhost:5267` 并登录。

**添加 DeepSeek 提供商：**

1. 在侧边栏进入 **提供商** 页面。
2. 点击 **添加提供商**，选择 **DeepSeek**。
3. 在 `API Key` 输入框中填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
4. `Base URL` 默认为 `https://api.deepseek.com`，无需修改。
5. 点击 **保存**。

**添加模型：**

1. 在刚创建的提供商中，点击 **添加模型**。
2. 从自动发现的模型列表中选择，或手动输入模型名称：
   - `deepseek-v4-pro` — 适合复杂推理、Agent 任务和多步骤工作流
   - `deepseek-v4-flash` — 适合快速、轻量级的对话响应
3. 在模型设置中配置：
   - **思维模式**：默认开启。启用 DeepSeek 的思维链推理。
   - **推理强度**：设为 `max` 以获得最佳编程和 Agent 体验，或设为 `high` 以获得平衡性能。
4. 点击 **保存**。

**设为默认模型：**

1. 进入 **设置** > **模型**。
2. 将 `默认 LLM` 设置为刚配置的 DeepSeek 模型。

#### 3. 开始使用

返回对话界面，即可开始与 DeepSeek 模型交互。

你也可以在 **适配器** 设置中接入聊天平台（QQ、Telegram、微信、Discord），在常用聊天应用中使用 KiraAI 作为数字助手。各平台的配置指南请参阅 [KiraAI 文档](https://docs.kira-ai.top/zh/)。
