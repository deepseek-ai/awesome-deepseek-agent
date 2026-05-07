# ⏺ Ctrl

> 基于 DeepSeek 的 CLI 开发者助手 — 在终端里拥有一个能写代码、调试、管文件、记事情的 AI 搭档。

Ctrl 是一个运行在命令行中的 AI 助手。它不只是聊天 — 它可以**读写文件**、**执行命令**、**管理待办**、**长期记忆**用户偏好，甚至会**自我进化**（提出新工具 / 新规则，等你批准）。

---

## 功能

| 能力 | 说明 |
|---|---|
| 💬 **对话** | 基于 DeepSeek API 的流式对话，支持推理内容展示 |
| 📁 **文件操作** | 读取、创建、编辑、删除文件，编辑时展示彩色 diff |
| ⚡ **命令执行** | 在 PowerShell / cmd 中执行命令（带安全防护） |
| ✅ **待办管理** | 持久化的待办列表，支持 `pending` / `in_progress` / `done` / `failed` 状态 |
| 🧠 **长期记忆** | 用户偏好学习 + 关键词记忆 + 向量语义搜索 |
| 🔄 **多会话** | 创建、切换、删除会话，互不干扰 |
| 🛠 **自我优化** | AI 可以提出新工具 / 新规则，经你批准后生效 |
| 🎨 **美化 CLI** | Brain 微调器动画、彩色 diff、图标化工具调用展示 |

---

## 前置条件

- **Node.js** >= 18
- **DeepSeek API Key**（[获取地址](https://platform.deepseek.com/)）

---

## 安装

```bash
# 克隆仓库
git clone https://github.com/Kontirol/KontirolClaw.git
cd KontirolClaw

# 安装依赖
npm install

# 配置 API Key（二选一）
# 方式 1：环境变量（推荐）
set CTRL_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx      # Windows CMD
$env:CTRL_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxx"    # PowerShell

# 方式 2：配置文件（写入 ~/.ctrl/config.json）
node -e "import('./src/config.js').then(m=>m.saveConfig({apiKey:'sk-xxx'}))"

# 启动
npm start
```

> 💡 也可配置 `CTRL_BASE_URL`（自定义 API 地址）和 `CTRL_MODEL`（模型名），默认 `deepseek-v4-pro`。

---

## 使用

### 基本对话

```
Ctrl > 帮我写一个 Express 服务器
Ctrl > 这个函数有什么问题？
Ctrl > 记住：我喜欢用 TypeScript
Ctrl > exit
```

### 会话命令

| 命令 | 作用 |
|---|---|
| `:new [名称]` | 创建新会话 |
| `:switch <ID>` | 切换到指定会话 |
| `:sessions` / `:list` | 列出所有会话 |
| `:delete <ID>` | 删除会话 |
| `:help` | 显示帮助 |
| `Esc` | 中断当前请求 |
| `exit` | 退出程序 |

### AI 可以做的事

自然对话即可，Ctrl 会自动调用对应工具：

| 你说 | 调用的工具 |
|---|---|
| "读取 package.json" | `read_file` |
| "创建 src/utils.ts" | `create_file` |
| "把 app.ts 里端口改成 8080" | `edit_file` |
| "执行 npm run build" | `exec_command` |
| "帮我列个 todo" | `todo_create` |
| "记住：我的项目叫 CineMax" | `memory_store` |

---

## 架构

```
Ctrl/
├── src/
│   ├── index.js           # 入口：REPL 循环、流式对话
│   ├── config.js          # 配置管理（环境变量 / ~/.ctrl/config.json）
│   ├── tools/
│   │   ├── definition.js  # 所有工具的函数定义（OpenAI tool schema）
│   │   └── executor.js    # 工具执行逻辑
│   ├── memory/
│   │   ├── preferences.js # 用户偏好 + 长期记忆（~/.ctrl/memory.json）
│   │   ├── vector.js      # 向量语义记忆（轻量级 RAG）
│   │   ├── sessions.js    # 多会话管理（~/.ctrl/sessions/）
│   │   └── self-improve.js # 自我优化：自定义工具 + 提示词提案
│   └── ui/
│       ├── banner.js      # 启动横幅、工具调用美化输出
│       ├── spinner.js     # 微调器动画（stderr）
│       └── diff.js        # 文件变更 diff 美化
├── package.json
└── README.md
```

### 记忆系统（四层）

| 层级 | 触发方式 | 存储 |
|---|---|---|
| **偏好** | AI 自动学习 | `~/.ctrl/preferences.json` |
| **长期记忆** | 用户说「记住 xxx」 | `~/.ctrl/memory.json` |
| **向量记忆** | AI 自动总结对话 | `~/.ctrl/vectors.json`（带相似度评分） |
| **自我优化** | AI 发现不足时提案 | `~/.ctrl/custom_tools.json` / `custom_prompt.txt` |

---

## 安全

- 命令执行有**黑名单**防护（阻止 `rm -rf /`、`format` 等危险命令）
- 文件操作限制在**当前工作目录**内，不能越界
- 自我优化提案需要**你手动确认**才会生效

---

## 许可

ISC © [nijat (Ctrl)](https://github.com/Kontirol)
