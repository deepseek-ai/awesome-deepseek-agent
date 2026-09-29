[English](./dao_code.md) | [简体中文](./dao_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 Dao Code

Dao Code（命令 `dao`）是一个开源（MIT）、面向 DeepSeek-V4（最高 1M 上下文）的终端 AI 编码助手，目标是把这个高性价比模型的性价比用到极致。它的核心原则是缓存经济学：DeepSeek 的前缀缓存命中价比未命中低约两个数量级——deepseek-v4-pro 命中 $0.003625、未命中 $0.435（每 1M 输入 token），约 1/120。于是 Dao Code 把系统前缀、工具表与记忆按字节级稳定组织，以拉高命中率，并让反思与记忆都跑在复用主前缀缓存的 fork 上。结果是：跨会话记忆与持续自纠层（挑战者复审重复失败、纠偏者盯住范围蔓延 scope creep）几乎不增加 token 开销。在 7 道真实开源 bug-fix 任务（389 万输入 token）上，实测聚合缓存命中率 95.8%。

与其他 DeepSeek 终端 agent 相比，真正的不同在于"可信的记忆"：跨会话记忆在每次启动时按当前代码确定性校验——过期事实剔除，而非盲目堆积——再配合挑战者 / 纠偏者持续自纠，普通任务更稳更准，长任务尤其不易跑偏。

它还为长任务兜底：崩溃恢复（`dao -c`）、影子 git 检查点（`/restore`、`/rewind`，不碰你的 `.git`）、验收门（`verify_done`）、卡死检测、自主模式（`/goal`），以及并行 / 后台 / worktree 隔离的子代理。基础也一应俱全：完整 1M 上下文、完备内置工具集、分层 allow/ask/deny 权限 + 安全纵深（密钥扫描 / SSRF 防护 / 钥匙串）、Agent Skills、MCP（stdio + HTTP/SSE）、生命周期 Hooks、自定义子代理 / slash 命令 / 插件、多账户 profile、OS 定时调度。兼容 Claude Code 配置。太极美学 Ink TUI。

- **GitHub:** <https://github.com/tigicion/dao-code>

#### 1. 安装 Dao Code

**方式 A —— 一键安装（无需 Node）：**

```sh
curl -fsSL https://raw.githubusercontent.com/tigicion/dao-code/master/install.sh | sh
```

或到 [Releases](https://github.com/tigicion/dao-code/releases) 下载预编译二进制（macOS arm64/x64、Linux arm64/x64、Windows x64）。

**方式 B —— npm（需 Node ≥ 20，全平台）：**

```sh
npx dao-code        # 零安装试用
npm i -g dao-code   # 全局安装，命令名 dao
```

验证安装：

```sh
dao --version
```

#### 2. 配置 Dao Code

到 [DeepSeek 平台](https://platform.deepseek.com/api_keys)获取 API key。

最简单的方式是直接运行 `dao`：首次启动且未检测到 key 时，会引导你粘贴，并存到 `~/.dao/config.json`（下次自动读）。也可手动设置：

| 方式 | 命令 |
|------|------|
| `.env`（项目根，全平台） | 写一行 `DEEPSEEK_API_KEY=sk-...` |
| macOS / Linux | `export DEEPSEEK_API_KEY=sk-...` |
| Windows PowerShell | `$env:DEEPSEEK_API_KEY="sk-..."` |
| Windows CMD | `set DEEPSEEK_API_KEY=sk-...` |

**配置项：**

| 变量 | 说明 | 默认 |
|------|------|------|
| `DEEPSEEK_API_KEY` | DeepSeek API key | — |
| `DEEPSEEK_BASE_URL` | API 端点 | `https://api.deepseek.com` |
| `DEEPSEEK_MODEL` | 模型名 —— `deepseek-v4-pro` 或 `deepseek-v4-flash` | `deepseek-v4-pro` |
| `DAO_REASONING_EFFORT` | 思考强度 —— 保持 `max` 获得最深推理 | `max` |
| `DAO_CONTEXT_WINDOW` | 上下文预算（token） | `1000000` |
| `DAO_MAX_TURNS` | 单回合最大工具轮数 | `50` |
| `DAO_THEME` | `light` / `dark` 终端背景 | 自动探测 |

DeepSeek-V4 最高支持 1M token 上下文，Dao Code 默认把上下文预算设为 **1,000,000 token**（可用 `DAO_CONTEXT_WINDOW` 覆盖）。思考模式默认以 `max` 强度开启。

#### 3. 进入项目目录并启动 Dao Code

```sh
cd /path/to/my-project
dao
```

一次性任务（跑完即退，适合脚本）：

```sh
dao "把 src/utils.ts 里的 formatDate 改成支持时区"
```

崩溃后恢复上次会话：

```sh
dao -c
```

#### 快捷键

| 键 | 作用 |
|----|------|
| `Enter` | 发送 |
| `↑` / `↓` | 翻输入历史 |
| `Esc` | 打断当前回合（模型流与 shell 一并停） |
| `Shift+Tab` | 循环权限模式（default / acceptEdits / auto / plan） |
| `@` + 路径，再 `Tab` | 引用文件并补全 |
| `Ctrl+O` | 展开 / 收起全量工具输出与思考 |
| `Ctrl+A` / `Ctrl+E` | 光标移到行首 / 行尾 |

#### 常用斜杠命令

| 命令 | 作用 |
|------|------|
| `/init` | 扫描本仓库生成 `DAO.md`（项目概览，后续会话自动加载） |
| `/model [id]` | 切换模型（在 `deepseek-v4-pro` / `deepseek-v4-flash` 间切换） |
| `/mode [x]` | 权限模式：`default` / `acceptEdits` / `auto` / `plan` |
| `/goal <目标>` | 长任务自主模式（自动批准 + 连续推进） |
| `/cost` | 查看 token 用量与前缀缓存命中率 |
| `/skills` | 列出 / 开关技能 |
| `/compact` · `/clear` · `/help` · `/exit` | 压缩 · 清空 · 命令列表 · 退出 |

#### 使用 Agent Skills

Dao Code 支持渐进式披露的 Agent Skills，以及 MCP server 和生命周期 Hooks。它与 Claude Code 配置兼容（`settings.json`、`SKILL.md`、`hooks.json`、`mcp.json`），现成的 CC 技能与配置可直接使用。

- **项目级技能：** `./.dao/skills/<name>/SKILL.md`
- **MCP server：** `./.dao/mcp.json`
- **Hooks：** `./.dao/hooks.json`
