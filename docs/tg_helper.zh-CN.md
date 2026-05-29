[English](./tg_helper.md) | [简体中文](./tg_helper.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 TG HELPER

TG HELPER 是一个运行在 Windows 上的桌面级 AI 智能体，内置 **70+ 工具**，覆盖文件管理、浏览器自动化、物联网控制、QQ 机器人、嵌入式开发（Arduino）等领域。支持云端模型（OpenAI 兼容格式）和本地模型（Ollama），具备插件生态、多人格系统和主动智能巡检功能。

TG HELPER v0.2.5+ **原生支持 DeepSeek V4 模型**，提供思考模式（`reasoning_effort` 控制）、1M 上下文窗口配置，并自动在所有 AI 调用路径中注入相应参数。

#### 1. 安装 TG HELPER

```bash
git clone https://github.com/JXW666NB/TG-HELPER.git
cd TG-HELPER
pip install -r requirements.txt
playwright install chromium
```

#### 2. 在 TG HELPER 中配置 DeepSeek

启动 TG HELPER，打开 **API 设置** 页面：

```bash
python "TG HELPER.py"
```

首次启动会弹出配置向导，按提示填写即可。已安装用户请进入 **设置 → API 设置**（或点击侧栏齿轮图标）。

在 **主 AI 配置** 栏目中填写：

| 字段 | 值 |
|---|---|
| **API Key** | 你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| **Base URL** | `https://api.deepseek.com/v1` |
| **模型名称** | `deepseek-v4-pro` 或 `deepseek-v4-flash` |

> ⚠️ 请勿使用 `deepseek-chat` 或 `deepseek-reasoner`——这两个模型名将于 2026 年 7 月弃用。TG HELPER 使用的是当前模型命名。

点击 **💾 保存 API 设置**。系统会自动检测模型名中的 `deepseek` 关键词。

##### 启用 DeepSeek 深度思考模式

保存后，API 设置页会自动出现 **🧠 DeepSeek 专属配置** 区域：

- **启用深度思考 (Thinking Mode)**：勾选后激活 DeepSeek V4 的思维链推理能力。模型会在输出最终回答前先生成推理内容（`reasoning_content`），显著提升复杂任务的准确性。启用后，`reasoning_effort` 和 `thinking: {type: "enabled"}` 会自动注入所有 API 调用。
- **推理强度**：下拉框选择：
  - `高 (high)`——推荐，适合大多数任务
  - `最大 (max)`——最强推理，自动应用于 Agent 类复杂工作流
- **上下文窗口**：从 16K 到 **1M tokens** 可选（DeepSeek V4 最高支持 100 万 token 上下文）。该选项映射到 `max_tokens` 参数。

TG HELPER 会自动将以上参数注入**全部 8 个 AI 调用路径**，包括：
- 主 Agent 对话循环
- 多模态图片/视频分析
- Arduino 代码生成
- AI 视频生成（HTML+CSS 动画渲染）
- AI 图片生成
- 插件 AI 翻译器
- 网页内容摘要

无需手动修改代码——所有配置通过 GUI 完成。

#### 3. 开始使用

在底部输入框中输入需求，按 **Enter** 发送即可与 DeepSeek V4 驱动的 TG HELPER 交互。**Shift+Enter** 换行。

你可以试试这些：

- `"帮我把桌面的文件按类型整理一下"`
- `"去亚马逊看看今天有什么便宜好用的 USB-C 数据线"`
- `"帮我生成一个 30 秒的小猫气球跳跃动画视频"`
- `"通过物联网把客厅的灯关了"`（需要先配置 MQTT 设备）

TG HELPER 会调用其 70+ 工具来执行你的需求。危险操作（删除文件、键鼠模拟、执行代码）需要用户明确确认后才执行。详见[安全机制说明](https://github.com/JXW666NB/TG-HELPER#%EF%B8%8F-%E5%AE%89%E5%85%A8%E6%9C%BA%E5%88%B6)。
