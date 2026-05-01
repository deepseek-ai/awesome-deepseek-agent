[English](./momoka_en.md) | [简体中文](./momoka_cn.md) · [← Back](../README.md)

# Integrate with Momoka

Momoka is an open-source AI agent assistant that supports DeepSeek V4 and other models, extensible via MCP and Skills. It supports Discord, Feishu (Lark), QQ, and more.

## 🚀 Quick Start

### Deploy

#### Download a release (recommended)
Get the latest release from [Momoka Releases](https://github.com/xiaomi2023/Momoka/releases).

Or

#### Clone the repository
```bash
git clone https://github.com/xiaomi2023/Momoka
```

### Install dependencies

```bash
pip install -r requirements.txt
python -m rebrowser_playwright install chromium
```

### Run

```bash
python main.py
```

### Configure

Before you start, register and get an API Key from the [DeepSeek Platform](https://platform.deepseek.com/).

1. After running, enter the following commands to configure the model API Base URL and API Key:
```bash
/set base_url https://api.XXX.com
/set api_key sk-***
```

2. Enter **/model** to select a model (e.g., `deepseek-v4-flash`).

3. (Optional) Enter the command:
```bash
/set work_dir C:\\Users\\...
```
to configure Momoka's working directory.

All configuration may require a restart to take effect. If any errors occur during configuration, you can also edit the relevant fields directly in `config.json`.

Send a test message to make sure everything is ready, then start using it!

## Extend capabilities

- **MCP Server**: See [MCP Integration Guide](https://xiaomi2023.github.io/Momoka/mcp_integration/)
- **Skill**: See [Skill Documentation](https://xiaomi2023.github.io/Momoka/skill/)
- **Momoka Server**: See [Momoka Server Docs](https://xiaomi2023.github.io/Momoka/momoka_server/)

## Connect to more platforms

- [Discord](https://xiaomi2023.github.io/Momoka/discord/)
- [Lark / Feishu](https://xiaomi2023.github.io/Momoka/lark/)
- [QQ](https://xiaomi2023.github.io/Momoka/qq/)

For more information, check out the [Momoka Documentation](https://xiaomi2023.github.io/Momoka/).
