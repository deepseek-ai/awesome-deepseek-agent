[English](./momoka_en.md) | [简体中文](./momoka_cn.md) · [← 返回](../README.zh-CN.md)

# 接入 Momoka

Momoka 是一个开源的 AI Agent 助手，支持 DeepSeek V4 等模型，可通过 MCP、Skills 进行拓展，支持接入 Discord、飞书、QQ等平台。

## 🚀 快速开始

### 部署

#### 下载发行版本（推荐）
在[这里](https://github.com/xiaomi2023/Momoka/releases)获取最新的Momoka版本。

或

#### 拉取仓库
```bash
git clone https://github.com/xiaomi2023/Momoka
```

### 安装依赖

```bash
pip install -r requirements.txt
python -m rebrowser_playwright install chromium
```

### 运行

```bash
python main.py
```

### 配置
开始前，需要在[Deepseek 开放平台](https://platform.deepseek.com/)注册并获取API Key。

1、运行后，输入以下命令以配置模型 API 的 Base Url 和 API Key：
```bash
/set base_url https://api.XXX.com
/set api_key sk-***
```

2、输入 **/model** 以选择模型（例如deepseek-v4-flash）。

3、（可选）输入命令：
```bash
/set work_dir C:\\Users\\...
```
配置Momoka工作的位置。  

所有配置可能需要重启后才能生效。如果配置过程中出现异常，可以在config.json中配置相关字段）  
发送测试信息确保一切就绪，然后开始使用吧！

## 拓展能力

- **MCP Server**: 参考 [MCP 集成文档](https://xiaomi2023.github.io/Momoka/mcp_integration/)
- **Skill**: 参考 [Skill 文档](https://xiaomi2023.github.io/Momoka/skill/)
- **Momoka Server**: 参考 [Momoka Server 文档](https://xiaomi2023.github.io/Momoka/momoka_server/)

## 接入更多平台

- [Discord](https://xiaomi2023.github.io/Momoka/discord/)
- [Lark / 飞书](https://xiaomi2023.github.io/Momoka/lark/)
- [QQ](https://xiaomi2023.github.io/Momoka/qq/)

更多信息请参考 [Momoka 文档](https://xiaomi2023.github.io/Momoka/)。
