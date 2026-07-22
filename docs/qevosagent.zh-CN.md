# QevosAgent + DeepSeek

[QevosAgent](https://github.com/QHYCCD/QevosAgent) 是一个实用的极简开源的自主 AI Agent 框架，提供 Windows、macOS 和 Linux 平台的桌面应用。它拥有 Web Dashboard 界面、多模型支持、工具自我进化，高级指导员视角和长期记忆等功能。一键安装，部署方便。

- **官网**：<https://qevos.ai>
- **下载地址**：<https://github.com/QHYCCD/QevosAgent/releases>

本指南介绍如何通过**两步**配置 QevosAgent 使用 DeepSeek 模型。

---

## 第一步：配置 API 连接

1. 打开 QevosAgent桌面程序
2. 点击右上角的**设置**图标（⚙️）
3. 进入 **LLM 服务**区域，填写以下信息：

   - **API 服务地址**：`https://api.deepseek.com`
   - **API 密钥**：你的 DeepSeek API Key（在 [DeepSeek 平台](https://platform.deepseek.com/api_keys) 获取）
   - **点击“探测”按钮
   
4. 如果探测成功，会显示连接成功，并显示可选的模型名称，`deepseek-v4-pro` 或 `deepseek-v4-flash`，点击模型按钮就可以自动填入模型名称栏。
5. 点击**保存**

![配置 DeepSeek API 连接](./assets/qevosagent_deepseek_api.png)

## 第二步：启用 1M 上下文窗口

DeepSeek V4 支持最多 100 万 token 的上下文。启用方法：

1. 进入**设置** → **LLM 服务** → **运行参数**标签页
2. 将**上下文窗口 tokens**设置为 `1000000`
3. 点击**保存**

![设置 1M 上下文窗口](./assets/qevosagent_deepseek_context.png)

---

## 故障排除

- **连接失败**：确认 API Key 有效，检查到 `https://api.deepseek.com` 的网络连接
- **模型未找到**：使用准确的模型名称：`deepseek-v4-pro` 或 `deepseek-v4-flash`

## 资源

- [QevosAgent GitHub](https://github.com/QHYCCD/QevosAgent)
- [DeepSeek API 文档](https://api-docs.deepseek.com/)
- [DeepSeek 平台](https://platform.deepseek.com/)
