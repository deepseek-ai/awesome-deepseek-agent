[English](./bash_agent.md) | [简体中文](./bash_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Bash Agent

**Bash Agent** 是一个极简的 AI 编程 Agent 运行时，纯 Bash + AWK 实现，零运行时依赖。它在任何 POSIX Shell 中运行，直接对接 DeepSeek API，利用 Cache-First 循环大幅降低每次调用成本。

> **生产数据（2026-05-07）：** 输入 73.7M tokens，缓存命中率 99%，输出 215K tokens。（[DeepSeek分享对话](https://chat.deepseek.com/share/28068py62e711nhg57)）

#### 1. 安装

无需 Node.js、Python 或其他运行时，从 [GitHub Releases](https://github.com/lloydzhou/bash-agent/releases) 下载最新版本即可：

```bash
# Bash + AWK 版本（零依赖，推荐）
curl -fsSL https://github.com/lloydzhou/bash-agent/releases/latest/download/agent.sh \
  -o ~/.local/bin/bash-agent && chmod +x ~/.local/bin/bash-agent

# Go 编译版本（自动检测系统与架构）
OS=$(uname -s | tr '[:upper:]' '[:lower:]'); ARCH=$(uname -m); \
  [ "$ARCH" = "x86_64" ] && ARCH=amd64; \
  [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ] && ARCH=arm64; \
  curl -fsSL "https://github.com/lloydzhou/bash-agent/releases/latest/download/goagent-${OS}-${ARCH}" \
  -o ~/.local/bin/goagent && chmod +x ~/.local/bin/goagent

# Rust 编译版本（仅支持 Linux / macOS）
OS=$(uname -s | tr '[:upper:]' '[:lower:]'); ARCH=$(uname -m); \
  [ "$ARCH" = "x86_64" ] && ARCH=amd64; \
  [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ] && ARCH=arm64; \
  case "$OS" in linux|darwin) SUFFIX="${OS}-${ARCH}" ;; \
    *) echo "No prebuilt rustagent for $OS/$ARCH, build locally with: cd rust && cargo build --release"; exit 1 ;; \
  esac; \
  curl -fsSL "https://github.com/lloydzhou/bash-agent/releases/latest/download/rustagent-${SUFFIX}" \
  -o ~/.local/bin/rustagent && chmod +x ~/.local/bin/rustagent
```

确保 `~/.local/bin` 在你的 `PATH` 中。

#### 2. 配置 API Key 与模型

Bash Agent 使用 Anthropic 兼容的 API 格式。在 Shell 配置文件（`~/.zshrc`、`~/.bashrc` 等）中设置环境变量：

```bash
# 示例：添加到 ~/.zshrc
deepseek() {
  DP_P_INNPUT=1 DP_P_OUT=3 DP_P_CACHE=0.02 \
  ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic \
  ANTHROPIC_API_KEY=sk-xxxx \
  bash-agent -m deepseek-v4-flash --max-turns 100 --max-context 1m --max-tokens 81920 --continue $@
}
```

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

可用模型：`deepseek-v4-flash`（低成本）、`deepseek-v4-pro`（最强推理）。

DeepSeek V4 模型支持高达 **100 万 token** 的上下文。Bash Agent 自动配置 1M 上下文窗口，并默认启用最大思考强度，为你提供最佳编程体验。

#### 3. 运行

进入项目目录并启动 Agent：

```bash
cd /path/to/my-project
bash-agent
```

Bash Agent 会读取项目文件，通过完整的上下文缓存发送到 DeepSeek，并实时执行模型的建议——这一切都来自一个单独的 Bash 脚本。

### 为什么选择 Bash Agent？

- **零依赖** — 纯 Bash + AWK，在任何 POSIX 系统（Linux、macOS、WSL）上运行。
- **Cache-First 架构** — 专为最大化 DeepSeek 上下文缓存设计，达到 99% 缓存命中率，显著降低成本。
- **1M 上下文** — 充分利用 DeepSeek V4 的 100 万 token 上下文窗口，轻松应对大型代码库。
- **最大思考强度** — 开箱即用支持 DeepSeek V4 Pro 的 `max` 推理级别。
- **轻量可定制** — `src/agent.sh` 约 1500 行核心代码 + 1600 行 AWK 辅助模块，编译为单个 `dist/agent.sh`（不足 3000 行），几分钟即可阅读、修改和扩展。
- **Skill 扩展** — 支持从 `.claude/skills/`、`./skills/` 和 `~/.claude/skills/` 三个目录加载自定义技能，三层机制：skill-index（摘要）→ selected-skills（通过 `--skill` 完整加载）→ Skill 工具（按需读取）。
