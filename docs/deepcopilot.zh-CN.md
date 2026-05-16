[← 返回](../README.zh-CN.md)

# 接入 Deep Copilot

**Deep Copilot** 是一个开源的 AI 编程 Agent，直接嵌入 VS Code，由 DeepSeek V4（OpenAI 兼容协议）驱动。模型通过工具调用来读写文件、搜索代码、浏览网页、执行 Shell 命令，整个过程实时流式呈现在侧边栏。无需后端、无需 Docker、无需 Rust，纯 Node.js + VS Code API，打包为约 94 KB 的单文件 bundle。

- **仓库地址**：[github.com/ZhouChaunge/DeepCopilot](https://github.com/ZhouChaunge/DeepCopilot)
- **VS Code 扩展商城**：搜索 **Deep Copilot**（发布者 *ZhouChaunge*）
- **环境要求**：VS Code ≥ 1.95.0

---

## 1. 安装

### 方式 A — VS Code 扩展商城（推荐）

1. 打开 VS Code → **扩展** 面板（`Ctrl/Cmd+Shift+X`）。
2. 搜索 **Deep Copilot**。
3. 点击**安装**。

### 方式 B — 安装 VSIX 包

从 [GitHub Releases](https://github.com/ZhouChaunge/DeepCopilot/releases) 下载最新 `.vsix`，然后：

```bash
code --install-extension deep-copilot-<version>.vsix
```

---

## 2. 配置 DeepSeek API Key

1. 点击活动栏中的 **🐋 Deep Copilot** 图标，打开面板。
2. 点击面板**右下角** 🔑 按钮。
3. 粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 并保存。

---

## 3. 选择 DeepSeek 模型

Deep Copilot 默认使用 `deepseek-v4-pro`。在 **VS Code 设置**（`Ctrl/Cmd+,`）中切换：

```jsonc
{
  "deepseekAgent.defaultModel": "deepseek-v4-pro"   // 或 "deepseek-v4-flash"
}
```

| 模型 | 说明 |
|---|---|
| `deepseek-v4-pro` | 完整深度推理（最大思考强度），适合复杂重构与 Bug 排查。 |
| `deepseek-v4-flash` | 速度更快、成本更低，适合快速编辑与问答。 |

两款模型均支持最高 **100 万 token** 上下文窗口。Deep Copilot 会自动管理上下文，详见[§ 上下文管理](#上下文管理)。

---

## 4. 首次运行

在侧边栏直接输入需求，Deep Copilot 启动 Agent 循环：调用工具、读取结果、持续迭代，直到任务完成。

```
把 src/auth/ 目录下的所有回调风格代码改成 async/await
```

```
找出所有调用了废弃函数 getUser() 的地方，并迁移到 fetchUser()
```

```
修复 tests/api.test.ts 中三个失败的测试
```

> 默认情况下，每次写文件或执行 Shell 命令都会弹窗确认。可通过 [§ 审批模式](#7-审批模式) 调整。

---

## 5. 工具集

Deep Copilot 给模型的工具集刻意保持精简，并遵循一个关键的设计原则：**编辑/操作工具排在最前面**。这是为了对抗 DeepSeek 在 RLHF 训练中形成的"先读后动"倾向——把动作工具前置，让 Agent 更果断。

| 工具 | 说明 |
|---|---|
| `apply_patch` | 应用统一格式补丁（多 hunk、多文件），非简单编辑的首选。 |
| `str_replace_in_file` | 通过精确字符串匹配进行原地替换，适合小范围唯一修改。 |
| `write_file` | 新建或覆写文件，仅用于全量写入。 |
| `run_shell` | 在工作区根目录执行 Shell 命令（npm、git、测试运行器等）。 |
| `read_file` | 按行号区间读取文件内容。 |
| `grep_search` | 工作区级正则搜索（ripgrep 风格）。 |
| `find_files` | 按文件名或 Glob 模式查找文件。 |
| `list_dir` | 列出目录内容（限制深度）。 |
| `web_search` | 通过 Tavily 联网搜索（需要[免费 Tavily API Key](https://app.tavily.com)）。 |
| `web_fetch` | 抓取任意公网 URL 并返回纯文本内容。 |
| `spawn_agent` | 派发只读子 Agent，用于复杂的多文件探索任务。 |
| `update_plan` | 向侧边栏 Todos 面板推送结构化任务计划。 |
| `revert_last_turn` | 回滚当前 Agent 轮次对所有文件的修改。 |
| `open_file_in_editor` | 在编辑器中打开文件并跳到指定行。 |
| `mcp__<server>__<tool>` | 已连接 MCP 服务器暴露的任意工具。 |

---

## 6. 联网能力

### 联网搜索（`web_search`）

由 [Tavily](https://app.tavily.com) 驱动。在 🔑 弹窗中填入 Tavily API Key（与 DeepSeek Key 同一弹窗），即可开启。设置后，Agent 在执行任务时可以自主搜索网页——查文档、查报错、查最新 API 变更。

### 网页抓取（`web_fetch`）

无需额外 API Key。抓取任意公网 URL，Deep Copilot 内置 HTML 转纯文本，模型收到的是干净的文章文本而非原始 HTML 标签。自动执行以下安全限制：

- 拦截内网/私有 IP 范围（防 SSRF）
- 禁止跨域重定向
- 响应内容限制 2 MB
- 所有 `http://` 请求静默升级为 `https://`

---

## 7. 审批模式

控制 Agent 的自主权限：

| 模式 | 行为 |
|---|---|
| `manual` | 每次 `write_file` 和 `run_shell` 都弹窗确认（默认，最安全） |
| `auto-edit` | 写文件自动通过，Shell 仍需确认 |
| `autopilot` | 全部自动通过（仅适合受信任工作区） |
| `readonly` | 禁止所有写入与 Shell 操作 |

```jsonc
{ "deepseekAgent.approvalMode": "auto-edit" }
```

---

## 8. MCP 服务器集成

Deep Copilot 内置 MCP stdio 客户端，通过 `settings.json` 连接任意 MCP 兼容工具服务器：

```jsonc
{
  "deepseekAgent.mcp.servers": [
    { "name": "my-db",  "command": "npx", "args": ["my-db-mcp-server"] },
    { "name": "jira",   "command": "node", "args": ["./tools/jira-mcp.js"] }
  ]
}
```

连接后，工具以 `mcp__<server>__<tool>` 的形式出现在模型的 function-calling 接口中。

---

## 9. 上下文管理

Deep Copilot 支持最高 **100 万 token** 上下文（DeepSeek V4 完整窗口）。两套自动机制保障对话健康：

**自动压缩** — 估算 token 超过 `compactBudgetTokens`（默认 `600000`）时，较老的工具结果被替换为简短摘要。首条用户消息始终保留。接近 90 万 token 时触发紧急压缩，防止 API 返回 HTTP 400 上下文超长错误。

**流式参数预览** — 模型生成工具调用时，Deep Copilot 在 `path` 字段刚到达时就立即显示"正在编辑 `src/auth.ts`…"，无需等待完整参数生成。这与 GitHub Copilot 的实时编辑预览体验一致。

---

## 10. 配置参考

所有设置均在 `deepseekAgent.*` 命名空间下：

```jsonc
{
  "deepseekAgent.defaultModel":        "deepseek-v4-pro",
  "deepseekAgent.apiBaseUrl":          "",          // 留空 = api.deepseek.com
  "deepseekAgent.approvalMode":        "manual",
  "deepseekAgent.interactionMode":     "agent",     // "agent" | "ask"
  "deepseekAgent.maxIterations":       15,
  "deepseekAgent.compactBudgetTokens": 600000,
  "deepseekAgent.postEditDiagnostics": true,        // 每次编辑后追加 LSP 诊断
  "deepseekAgent.enableDebugLog":      true,        // 写日志到 .deepcopilot/logs/
  "deepseekAgent.mcp.servers":         []
}
```

---

## 11. 设计亮点

### Skill 热插拔

Skill 就是目录里的 Markdown 文件——不需要插件清单，不需要重载扩展。Deep Copilot 运行时按优先级顺序扫描三个目录：

```
~/.deepcopilot/skills/   ← 首次启动自动创建
~/.claude/skills/        ← 兼容 Claude Code
~/.copilot/skills/       ← 兼容 GitHub Copilot
```

每个 Skill 是一个子目录，包含带 YAML frontmatter 的 `SKILL.md`：

```markdown
---
name: my-skill
description: 显示在斜杠命令弹窗中的一行简介
argument-hint: 可选提示文字
---

... 给模型的指令内容 ...
```

把目录扔进去，下一条消息即可使用——无需重启，无需重载。

**注入原理**

Skill 内容**不是**以用户消息或系统提示插入的。Deep Copilot 在用户消息之前合成一对 `read_file` 工具调用 + 工具结果并注入对话上下文：

```
assistant  →  tool_call: read_file("~/.claude/skills/my-skill/SKILL.md")
tool       →  <SKILL.md 内容>
user       →  <用户的实际消息>
```

模型将 Skill 视为**自己读到的**信息，而非用户施加的指令，指令遵循的可靠性远高于系统提示或用户消息注入。这与 GitHub Copilot 内部注入 Skill 的方式完全一致。

三目录之间采用「先匹配者优先」策略：`~/.deepcopilot/skills/` 中的同名 Skill 静默覆盖 Claude Code 或 GitHub Copilot 目录中的对应项，让你维护个人覆盖层而无需改动共享文件。来自三个目录的所有 Skill 统一列在 `/` 命令弹窗中，附带简介和提示文字。

### 感知上下文缓存的系统提示

系统提示在 `__DYNAMIC_BOUNDARY__` 标记处一分为二：

- **静态部分** — 行为原则、工具规则、语气风格。在所有请求中完全一致，可命中 DeepSeek 上下文缓存。后续轮次只需支付缓存命中价格，而非完整输入价格。
- **动态部分** — 每轮重新计算：宿主系统信息、工作区指令（`DEEPCOPILOT.md`）、用户记忆（`~/.deepcopilot/memory.md`）。

这一设计最大化了高价值静态内容的缓存命中率，同时保持了个性化部分的实时性。

### 工作区级工具钩子

在工作区根目录放置 `.deepcopilot/hooks.json`，可将 Shell 命令挂载到任意工具事件：

```jsonc
{
  "hooks": [
    {
      "event":      "after_tool",
      "tool":       "write_file",
      "run":        "npm test --reporter=dot",
      "on_failure": "inject_error"
    }
  ]
}
```

钩子输出注入回模型上下文。Agent 直接读取测试结果并自我纠错，无需你手动复制终端输出。

### 子 Agent 派发（`spawn_agent`）

对于需要读取大量文件的任务（例如"梳理 `src/` 架构"、"找出 `getUser()` 的所有调用点"），Deep Copilot 可以派发独立的只读子 Agent。每个子 Agent 获得专属的 focused prompt，在独立上下文中运行，返回结构化 Markdown 摘要。同一轮次派发的多个子 Agent 并行执行。

### 多会话并行

Agent 循环以 session ID 为键独立维护。某个会话的任务正在运行时，可以切换到另一个会话开始新对话。事件持续缓冲，切回原会话后自动回放全部进度。

### 零后端架构

全部逻辑运行在 VS Code 扩展主机内。生产构建产物约 94 KB，零运行时 npm 依赖——仅依赖 VS Code API 与 Node.js 内置模块。VS Code 之外无任何需要安装、更新或保持运行的组件。

