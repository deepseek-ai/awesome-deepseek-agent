[English](./codelf.md) | [简体中文](./codelf.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Codelf

Codelf（码灵）是一个内置自主式 AI Agent 的轻量级桌面 IDE（Electron + React），可用自然语言完成开发、文档处理与桌面/浏览器自动化，同时也是功能完整的代码编辑器。它**原生内置 DeepSeek 供应商**，在设置里选择 DeepSeek 类型、填入 API Key 即可使用，无需修改 Base URL 或做兼容层适配。

- **GitHub：** <https://github.com/Liuchun-oss/codelf-agent>

#### 核心功能

- **多 Agent 群聊协作**：创建 AI 团队（产品团队、写作组、头脑风暴等），每个岗位有独立人格、模型与工具权限，Host 自动调度发言权，支持 Host 决策 / 轮询 / 自由发言三种协作策略。
- **浏览器自动化**：内置 Playwright 驱动的浏览器，Agent 可自主导航、点击、填表、截图，处理需要登录或验证码的网页。
- **桌面自动化**：通过无障碍 API 控制 Windows / macOS 桌面应用，支持点击、输入、拖拽、快捷键等操作。
- **定时任务**：支持 Cron / 间隔 / 单次三种调度方式，任务结果可推送至微信，实现 7×24 无人值守。
- **本地 RAG 知识库**：导入文档构建知识库，Agent 基于语义检索回答，支持 PDF、Markdown、Office 等格式。
- **Skills 技能生态**：数十个内置技能（产品设计、文档转换、PPTX / DOCX / PDF 处理等），支持安装社区技能。
- **MCP 协议 + 插件系统**：完整 MCP 支持，可安装 Codex / Claude 社区插件扩展能力。
- **Plan 模式 + Checkpoint 回滚**：复杂任务先只读调研出方案再执行，每轮可整体撤销。
- **微信集成**：绑定微信后可在手机上指挥 Agent，任务完成主动推送通知。
- **长记忆系统**：跨会话自动沉淀知识，越用越懂你的项目习惯。

#### 1. 安装 Codelf

Codelf 支持 Windows 与 macOS，可下载安装包或从源码运行。

**方式一：下载安装包**

前往 [Releases 页面](https://github.com/Liuchun-oss/codelf-agent/releases) 下载对应平台的安装包：

- Windows：NSIS 安装包或免安装目录版
- macOS：dmg（支持 arm64 / x64）

**方式二：从源码运行**

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 18+。
- Windows 用户请安装 [Git for Windows](https://git-scm.com/download/win)。
- 克隆仓库并安装依赖、启动：

```bash
git clone https://github.com/Liuchun-oss/codelf-agent.git
cd codelf-agent
npm install
npm run dev
```

#### 2. 配置 Codelf 使用 DeepSeek

打开应用内的「设置 → AI」，新建一个配置，按下表填写：

| 配置项     | 取值                              |
| ---------- | --------------------------------- |
| 类型       | `DeepSeek`                        |
| Base URL   | `https://api.deepseek.com`（默认）|
| 模型名     | `deepseek-v4-pro`                 |
| API Key    | `<你的 DeepSeek API Key>`         |
| 上下文窗口 | `1M`（100 万 token）              |

DeepSeek API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

填好后点「测试连接」验证，再点「保存」并「设为当前」。

#### 推荐设置

- **上下文窗口**：在下拉中选择 `1M`，充分利用 DeepSeek V4 的 100 万 token 上下文。
- **思考模式**：开启「开启思考」，并将「思考强度」设为 `max`，以获得最佳编码表现。
- **模型分工**（可选）：日常对话与高频补全可新建一个 `deepseek-v4-flash` 配置以降低成本，复杂任务切回 `deepseek-v4-pro`。
- **Tab 补全（FIM）**：如需行内补全，可在 DeepSeek 配置中开启「Tab 补全 (FIM)」。

> Codelf 针对会话组织做了缓存键优化，能显著提升 DeepSeek 的 prompt 缓存命中率，长上下文编码可观地降低费用。

#### 价格参考

| 模型 | 输入 / 百万 token | 输出 / 百万 token | 缓存命中 / 百万 token |
|------|------------------|-------------------|-----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

> 以上价格为参考快照，请以 [DeepSeek 官方价格页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 的最新数据为准。

#### 3. 使用 Codelf

配置完成后，在主界面的 AI 对话面板用自然语言描述你的需求即可。Codelf 会自主读写文件、运行终端命令、检索资料并调用工具完成多步骤任务。复杂任务可先进入只读的 Plan 模式调研出方案，确认后再执行；每个回合都有检查点，可整体撤销。
