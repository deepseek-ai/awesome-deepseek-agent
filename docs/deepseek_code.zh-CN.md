[English](./deepseek_code.md) | [简体中文](./deepseek_code.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 DeepSeek Code

DeepSeek Code 是一款开源的 DeepSeek 驱动终端编程 Agent，具备完整 TUI、多供应商支持、MCP、LSP 与 Agent Skills。

- **GitHub：** <https://github.com/Hermenics/deepseek-code>

#### 1. 安装 DeepSeek Code

- 安装 [Node.js](https://nodejs.org/en/download/) 18+ 或 [Bun](https://bun.sh) 1.1+ 版本。
- 在终端中运行以下命令：

```sh
npm install -g @hermenics/deepseek-code
```

- 验证安装是否成功：

```sh
deepseek --version
```

#### 2. 配置 DeepSeek Code

首次运行时，DeepSeek Code 会引导你选择供应商。选择 **DeepSeek API** 并输入你的 API Key。

也可以直接设置环境变量：

```sh
export DEEPSEEK_API_KEY=sk-...
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

密钥存储在 `~/.deepseek/config.json` 中。非敏感偏好设置使用 `settings.json`，优先级为 `User < Project < Local`。

**支持的供应商：**

| 供应商 | 环境变量 / 配置键 |
|----------|--------------------|
| DeepSeek API（默认） | `DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL` |
| Amazon Bedrock | `AWS_REGION`、`AWS_PROFILE` |
| Google Vertex AI | `GCP_PROJECT`、`GCP_LOCATION`、`GCP_CREDENTIALS` |
| 本地模型（Ollama / LM Studio） | `LOCAL_BASE_URL`、`LOCAL_MODEL` |

#### 3. 进入项目目录并启动 DeepSeek Code

```sh
cd /path/to/my-project
deepseek
```

自动化场景可使用无头管道模式：

```sh
echo "解释一下这个项目" | deepseek --pipe
```

#### 快捷键

| 按键 | 功能 |
|------|------|
| `Enter` | 发送消息 |
| `Shift+Enter` | 换行 |
| `Esc` | 中断当前模型回复 |
| `/` | 打开斜杠命令菜单 |
| `/model` | 切换模型 |
| `/agent` | 启动子 Agent |
| `/vim` | 切换 Vim 键位 |
| `/theme` | 切换颜色主题 |
| `/help` | 显示所有命令 |

#### 使用 Agent Skills

Agent Skills 从以下位置自动发现：

- **用户级别：** `~/.deepseek/skills/<name>/SKILL.md`
- **项目级别：** `./.deepseek/skills/<name>/SKILL.md`

#### 管道模式

```sh
cat src/index.tsx | deepseek --pipe --json "总结这个文件"
```
