[English](./bash_agent.md) | [简体中文](./bash_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with Bash Agent

**Bash Agent** is a minimal AI coding agent runtime built with pure Bash + AWK — zero runtime dependencies. It runs in any POSIX shell, talks directly to the DeepSeek API, and leverages a cache-first loop to dramatically reduce cost per token.

> **Production Stats (2026-05, 11 days):** 723.9M input tokens, avg cache hit rate 99.15%, 2.5M output tokens. ([Dashboard](https://lloydzhou.github.io/bash-agent/))

#### 1. Install

No Node.js, Python, or other runtime required. Download the latest release from [GitHub Releases](https://github.com/lloydzhou/bash-agent/releases):

```bash
# macOS — Homebrew (includes all 4 versions: bash/go/rust/c)
brew install lloydzhou/tap/bash-agent

# Or manually install Bash version (zero dependencies, single file)
curl -fsSL https://github.com/lloydzhou/bash-agent/releases/latest/download/agent.sh \
  -o ~/.local/bin/bash-agent && chmod +x ~/.local/bin/bash-agent

# Go compiled version (auto-detect OS & arch)
OS=$(uname -s | tr '[:upper:]' '[:lower:]'); ARCH=$(uname -m); \
  [ "$ARCH" = "x86_64" ] && ARCH=amd64; \
  [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ] && ARCH=arm64; \
  curl -fsSL "https://github.com/lloydzhou/bash-agent/releases/latest/download/goagent-${OS}-${ARCH}" \
  -o ~/.local/bin/goagent && chmod +x ~/.local/bin/goagent

# Rust compiled version
OS=$(uname -s | tr '[:upper:]' '[:lower:]'); ARCH=$(uname -m); \
  [ "$ARCH" = "x86_64" ] && ARCH=amd64; \
  [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ] && ARCH=arm64; \
  curl -fsSL "https://github.com/lloydzhou/bash-agent/releases/latest/download/rustagent-${OS}-${ARCH}" \
  -o ~/.local/bin/rustagent && chmod +x ~/.local/bin/rustagent

# C compiled version
OS=$(uname -s | tr '[:upper:]' '[:lower:]'); ARCH=$(uname -m); \
  [ "$ARCH" = "x86_64" ] && ARCH=amd64; \
  [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ] && ARCH=arm64; \
  curl -fsSL "https://github.com/lloydzhou/bash-agent/releases/latest/download/cagent-${OS}-${ARCH}" \
  -o ~/.local/bin/cagent && chmod +x ~/.local/bin/cagent
```

Ensure `~/.local/bin` is in your `PATH`.

#### 2. Configure API Key & Model

Bash Agent uses the Anthropic-compatible API format. Set the environment variables in your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
# Example: add to ~/.zshrc

# Option 1: Use DEEPSEEK_API_KEY (auto-detected, simplest)
export DEEPSEEK_API_KEY="sk-xxxx"
deepseek() {
  DP_P_IN=1 DP_P_OUT=3 DP_P_CACHE=0.02 \
  bash-agent -m deepseek-v4-flash --max-turns 100 --max-context 1m --max-tokens 81920 --continue $@
}

# Option 2: Use ANTHROPIC_BASE_URL explicitly
deepseek() {
  DP_P_IN=1 DP_P_OUT=3 DP_P_CACHE=0.02 \
  ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic \
  ANTHROPIC_API_KEY=sk-xxxx \
  bash-agent -m deepseek-v4-flash --max-turns 100 --max-context 1m --max-tokens 81920 --continue $@
}
```

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Available models: `deepseek-v4-flash` (cost-efficient), `deepseek-v4-pro` (maximum reasoning).

DeepSeek V4 models support up to **1 million tokens** of context. Bash Agent automatically configures the 1M context window and enables max thinking effort for the best coding experience.

#### 3. Run

Navigate to your project directory and start the agent:

```bash
cd /path/to/my-project
bash-agent
```

Bash Agent will read your project files, send them to DeepSeek with full context caching, and execute the model's suggestions in real time — all from a single Bash script.

### Why Bash Agent?

- **Zero dependencies** — pure Bash + AWK, runs on any POSIX system (Linux, macOS, WSL).
- **Cache-first architecture** — designed to maximize DeepSeek's context cache, achieving 99% cache hit rate, significantly reducing costs.
- **1M context** — fully leverages DeepSeek V4's 1 million token context window for large codebases.
- **Max thinking effort** — supports DeepSeek V4 Pro's `max` reasoning level out of the box.
- **Lightweight & hackable** — `src/agent.sh` (~1,600 lines) + 1,600 lines of AWK modules, compiled into a single `dist/agent.sh`. Also available in Go, Rust, and C for compiled performance. Read, modify, and extend in minutes.
- **Skill extensions** — supports custom skill loading from `.claude/skills/`, `./skills/`, and `~/.claude/skills/`, with a three-layer mechanism: skill-index (summary) → selected-skills (full load via `--skill`) → Skill tool (on-demand read).
