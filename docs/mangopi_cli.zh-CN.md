[English](./mangopi_cli.md) | [简体中文](./mangopi_cli.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Mangopi CLI

Mangopi CLI 是一个单文件 (1732 行)、零依赖的终端 AI 编程助手，仅使用 Python 标准库构建。支持 Python 3.8+，不需要 Node.js、Docker 或任何第三方框架——就是一个 `.py` 文件，一个下午就能读完。

**核心亮点：**
- **单文件架构** — 1732 行，23 个类，13 个内置工具，全在一个 `mangopi_cli.py` 中
- **零运行时依赖** — 纯 Python 标准库；`pip install mangopi-cli` 不拉任何第三方包
- **三层上下文压缩** — micro（截断旧工具输出）→ session（压缩历史轮次，保留最近 10 轮）→ full（LLM 驱动摘要），确保长时间自主会话不超出 1M token 预算
- **多 Provider 支持** — DeepSeek、OpenAI、MiniMax，以及任意 OpenAI 兼容接口
- **多模态支持** — 终端内直接查看图片（PNG/JPG/WebP），通过 `view_image` 工具
- **13 个内置工具** — 文件读写编辑（含 diff 预览）、正则 grep、glob 搜索、bash 执行（含 7 类危险命令检测 + y/n 确认）、网络搜索、图片查看、Skill 系统、长期记忆等
- **安全沙箱** — 危险命令模式需显式确认；文件写入通过 `realpath` 校验限制在项目根目录内
- **Goal Mode** — `/g` 启动自主规划 → 执行 → 验证 → 迭代循环，带持久化检查点
- **13 个测试文件** — 全面覆盖安全检测、三层压缩、路径沙箱（含前缀碰撞攻击测试）、网络搜索、系统提示词组装等
- **Python 3.8–3.12** — 通过 GitHub Actions CI 全版本矩阵测试
- **PyPI 发布** — OIDC 可信发布，`pip install mangopi-cli` 即可安装

### 从零安装 Mangopi CLI

Mangopi CLI 只需要 Python 3.8+，不需要 Node.js、Docker 或任何第三方框架。整个运行时就是一个 `mangopi_cli.py` 文件 (1732 行)。

#### 通过 pip 安装（推荐）

```bash
pip install mangopi-cli
```

#### 从源码安装

```bash
git clone git@github.com:w4n9H/mangopi-cli.git
cd mangopi-cli
python mangopi_cli.py
```

### 配置 Mangopi CLI

Mangopi CLI 支持所有 OpenAI 兼容的 API 端点。设置以下环境变量：

```bash
export MANGO_KEY="<你的 DeepSeek API Key>"
export MANGO_API_URL="https://api.deepseek.com"
export MANGO_MODEL="deepseek-v4-flash"
export MANGO_LANG="zh"                          # 中文界面
```

> **提示**：Mangopi CLI 支持最高 **1,000,000 token** 的上下文窗口（通过 `MANGO_MAX_CONTEXT` 配置）。DeepSeek V4 模型的 1M 上下文窗口与之完美匹配——配合三层压缩策略，你可以运行长时间的自主编程会话而不会耗尽上下文预算。

使用 DeepSeek V4 Pro 并开启推理/思考模式：

```bash
export MANGO_API_URL="https://api.deepseek.com"
export MANGO_MODEL="deepseek-v4-pro"
```

Mangopi CLI 会在模型支持时自动启用思考模式。DeepSeek V4 Pro 开箱即支持 `max` 推理强度级别。

### 使用 Mangopi CLI

进入项目目录，启动 Mangopi CLI：

```bash
cd /path/to/my-project
mangopi-cli
```

进入交互模式后即可开始编程。Mangopi CLI 内置 13 个工具，包括文件读写编辑（含 diff 预览）、正则搜索、glob 文件匹配、bash 命令执行、网络搜索、图片查看等。

#### 目标模式

使用 `/g` 命令让 Mangopi CLI 自主完成规划、执行、验证、迭代的全流程：

```
/g 用 FastAPI 写一个带测试的 Todo API
```

Agent 会持续工作直到任务完成或你手动停止。按 `Ctrl+C` 可暂停；使用 `/g 继续` 恢复执行。
