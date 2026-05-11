[English](./xpro.md) | [简体中文](./xpro.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 Xpro

Xpro 是一个开源的 AI 桌面 IDE，基于 Electron、TypeScript 和 Rust 构建。内置自主 Agent 模式，可以读写文件、执行命令、管理子代理——完整支持 DeepSeek V4，包括思考模式和 100 万 token 上下文窗口。

- **GitHub:** <https://github.com/HopkeyEZ/Xpro>

#### 1. 安装 Xpro

**从源码构建（需要 Node.js 18+ 和 Rust 1.70+）：**

```bash
git clone https://github.com/HopkeyEZ/Xpro.git
cd Xpro
npm install

# 构建 Rust 原生模块
cd native && npm install && npm run build && cd ..

# 编译并启动
npm run build:main
npm start
```

**或下载 Windows 安装包**，前往 [Releases](https://github.com/HopkeyEZ/Xpro/releases) 页面。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 在 Xpro 中配置 DeepSeek

1. 启动 Xpro
2. 点击工具栏中的 **Settings** 按钮
3. 填写以下字段：

| 字段 | 值 |
|------|------|
| Protocol | `OpenAI` |
| Base URL | `https://api.deepseek.com` |
| API Key | 你的 DeepSeek API Key |
| Model | `deepseek-v4-pro` 或 `deepseek-v4-flash` |

配置保存在 `~/.xpro/config.json`，跨会话持久化。

#### 4. 启用思考模式

在设置对话框中勾选 **Thinking Mode** 复选框即可开启 DeepSeek 的推理模式。开启后：

- Agent 在每次请求中发送 `thinking: { type: "enabled" }`
- 推理内容（`reasoning_content`）会自动在后续对话轮次中传回
- 模型推理时聊天界面会显示思考指示器

建议使用 `deepseek-v4-pro` 时将推理强度设为 `max` 以获得最佳编码体验。

#### 5. 开始编码

1. 通过 **Open Folder** 按钮打开项目文件夹
2. 在 AI 聊天面板输入任务（例如"给所有 API 路由添加错误处理"）
3. Agent 会自主读取文件、编辑代码、执行命令并验证结果

通过模型选择器切换模式：

| 模式 | 说明 |
|------|------|
| **Ask** | 只读问答，不修改文件 |
| **Agent** | 完全自主模式，读写文件、执行命令、生成子代理 |

#### DeepSeek 相关特性

| 特性 | 说明 |
|------|------|
| **100 万上下文** | 支持 DeepSeek V4 的完整上下文窗口，适用于大型代码库 |
| **思考模式** | 在设置界面一键开关推理链 |
| **项目记忆** | 对话中提取的记忆本地存储，未来会话自动召回 |
| **子代理** | 复杂任务自动拆分给多个并行子代理执行 |
| **可视化标注** | 截图圈画标注，AI 直接修改对应代码 |
| **变更追踪** | 每次 AI 编辑创建检查点，支持 diff 查看和一键撤回/恢复 |
| **AI 变更归类** | 文件变更自动按影响范围分组（前端UI、后端API 等） |
| **Rust 原生搜索** | 基于 napi-rs 的高速文件遍历和全文搜索 |

#### 配置参考

所有设置存储在 `~/.xpro/config.json`：

```json
{
  "openaiKey": "sk-your-deepseek-key",
  "openaiBase": "https://api.deepseek.com",
  "anthropicKey": "",
  "anthropicBase": "https://api.anthropic.com",
  "thinking": true
}
```

Base URL 支持任何 OpenAI 兼容端点（如本地 Ollama、vLLM、LM Studio）。
