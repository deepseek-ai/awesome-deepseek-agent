[English](./deepseek_code_agent.md) | [简体中文](./deepseek_code_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek Code Agent

> 🌐 **开源 Web UI 代码开发助手** —— 轻客户端架构，一键切换 Pro/Flash 模型，任务决策全程透明。  
> 快速上手、日常开发、Agent 进阶，一个工具全搞定。

DeepSeek Code Agent 是一款基于 **Web UI 的轻客户端**代码开发助手。无需安装重型 IDE，打开浏览器即可使用，对话中随时在 **DeepSeek-V4-Pro** 与 **DeepSeek-V4-Flash** 之间切换，每一步工具调用都在侧栏清晰展示，**任务决策透明化**。

无论是**入门学习 AI Agent**，还是作为**日常代码开发助手**，它都能提供简洁直观的体验，随你一起成长。

- **GitHub：** <https://github.com/diky87688973/deepseek-code-agent>

---

### 核心特性

| 特性 | 说明 |
|------|------|
| 🌐 **Web UI** | 图形界面，浏览器即可访问 |
| 📚 **知识库** | 内置文件选择器，注入对话上下文 |
| 📑 **多标签会话** | 同时管理多个对话 |
| 📁 **文件浏览器** | GUI 文件选择器，支持 @ 引用 |
| 🔒 **ACL 防篡改** | 自动锁定项目文件，保障安全 |
| 🔐 **对话加密** | Windows DPAPI 加密存储 |

---

<div align="center">
  <img src="./assets/deepseek_code_agent_ui.png" width="800" alt="DeepSeek Code Agent Web 界面" border="1" />
  <p><em>Web 界面 — 对话、工具调用、多标签会话管理与实时流式响应</em></p>
</div>

<br>

#### 1. 安装 DeepSeek Code Agent

- 安装 [Python](https://www.python.org/downloads/) 3.8+
- 克隆仓库：

```bash
git clone https://github.com/diky87688973/deepseek-code-agent.git
cd deepseek-code-agent
```

- 安装依赖：

```bash
pip install -r requirements.txt
```

#### 2. 配置 DeepSeek

编辑项目根目录下的 `config.json`：

```json
{
    "AGENT_MODEL_API_BASE_URL": "https://api.deepseek.com",
    "AGENT_MODEL_API_KEY": "sk-...",
    "AGENT_SERVER_PORT": 8801
}
```

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**配置项说明：**

| 配置项 | 说明 |
|--------|------|
| `AGENT_MODEL_API_BASE_URL` | API 地址，默认 `https://api.deepseek.com` |
| `AGENT_MODEL_API_KEY` | DeepSeek API 密钥 |
| `AGENT_SERVER_PORT` | Web 界面端口（默认 8801） |
| `AGENT_WORKSPACE_DIR` | 默认工作目录 |
| `AGENT_KNOWLEDGE_BASE_DIR` | 知识库目录 |
| `AGENT_DATA_ROOT_DIR` | 数据存储目录（会话、加密密钥、用量日志） |
| `AGENT_SESSION_ENCRYPTION` | 会话加密模式（`auto`、`on`、`off`；默认 `auto`） |
| `AGENT_REASONING_EFFORT` | 推理强度（`max`、`high`、`medium`；默认 `max`） |
| `CHAT_API_MODELS` | 允许使用的模型列表，默认 `deepseek-v4-pro,deepseek-v4-flash` |

#### 3. 启动 DeepSeek Code Agent

**Windows（推荐）：**

双击 `start.bat` — 自动请求管理员权限（ACL 防篡改保护）、激活虚拟环境、安装依赖、启动服务。

**Linux / macOS：**

```bash
chmod +x start.sh && ./start.sh
```

**或手动启动：**

```bash
python main_tray.py
```

打开浏览器访问 `http://127.0.0.1:8801`。

#### 4. 开始对话

用自然语言下达指令，AI 会自动调用工具完成任务：

> "读取桌面上的 test.txt 文件内容"
> "查看这个项目的 Git 日志"
> "当前目录有哪些文件？"
> "分析 main.py 的代码质量"

#### 5. DeepSeek 集成特性

| 特性 | 说明 |
|------|------|
| **Function Calling** | DeepSeek-V4 驱动全部内置工具调用 |
| **KV 缓存优化** | 流式响应携带 `cache_hit_tokens`，计费区分缓存命中/未命中 |
| **流式响应** | 基于 SSE 的流式输出，支持 `reasoning_content` 推理过程显示 |
| **上下文管理** | 超过 800 条消息自动摘要压缩，保留关键信息 |
| **模型选择** | 每会话可独立指定模型 |

#### 6. 知识库

<div align="center">
  <img src="./assets/deepseek_code_agent_kb.png" width="800" alt="知识库面板" border="1" />
  <p><em>知识库面板 — 勾选本地文件，AI 自动注入对话上下文作为参考</em></p>
</div>

在界面右侧打开 📚 **知识库**面板，勾选需要 AI 参考的文件，Agent 会自动将其内容注入对话上下文，实现基于本地知识库的智能响应。

#### 使用技巧

| 操作 | 说明 |
|------|------|
| 输入 `/plan` | 切换到 Plan 模式（只出方案，不执行写操作） |
| 输入 `/execute` | 切换到 Execute 模式（严格按照执行清单执行） |
| 输入 `@文件路径` | 在消息中引用本地文件 |
| 点击 📁 按钮 | 打开文件浏览器选择文件 |
| 📚 知识库面板 | 勾选知识库文件注入对话上下文 |


`read_file` · `write_file` · `replace_in_file` · `apply_patch` · `grep_files` · `glob_files` · `file_ops` · `archive` · `data_table` · `run_command` · `python_inline` · `git_workspace` · `web_fetch` · `unified_diagnose` · `text_diff` · `env_probe` · `ip_geolocate` · `open_meteo_weather` · `image_ocr` · `user_confirm` · `todo_list` · `run_type` · 等。
