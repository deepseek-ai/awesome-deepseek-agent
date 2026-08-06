[English](./agent_in_terminal.md) | [简体中文](./agent_in_terminal.zh-CN.md) · [← Back](../README.md)

# Integrate with Agent-in-Terminal

Agent-in-Terminal is an ultra-lightweight terminal AI agent for Linux — a single 11.4 KB Python file with zero dependencies, machine-bound encrypted API key storage, and a single gated shell tool.

- **GitHub:** <https://github.com/Xiyinnnnnn/Agent-in-Terminal>

#### 1. Install (one-liner)

```bash
# Global CDN (fast in China, no proxy needed)
curl -fsSL https://cdn.jsdelivr.net/gh/Xiyinnnnnn/Agent-in-Terminal@main/install.sh | bash

# GitHub direct (overseas)
curl -fsSL https://raw.githubusercontent.com/Xiyinnnnnn/Agent-in-Terminal/main/install.sh | bash
```

The installer automatically falls back between the two sources.

#### 2. First run — enter your API key

```bash
python3 ~/.local/bin/term_agent/term_agent.py
```

The key is entered invisibly (`getpass`), encrypted with a machine-bound seed, and stored at `~/.config/term_agent/key.bin` — the only file written, never in plaintext.

#### 3. Use it

Type a prompt and the agent drives a loop of LLM ↔ `tool_calls` (MAX_ROUNDS=30 soft cap), executing shell commands as its single tool. Type `exit` to quit.

#### DeepSeek configuration

Agent-in-Terminal calls `api.deepseek.com/chat/completions` with **`deepseek-v4-flash`** by default — switch to `deepseek-v4-pro` by editing `MODEL` in `term_agent.py`. It already sends `reasoning_effort: "max"` with `thinking: {type: "enabled"}`, so **max thinking effort** works out of the box.

The **1M-token context window** is handled by a 900K-token summary chain: `compress()` summarizes history at the 900K threshold so long sessions keep working within DeepSeek V4's 1M context.

#### Security model

`run_terminal()` is the only tool — all capabilities converge to shell execution. Commands matching the blacklist are intercepted before `subprocess` and require a Y/N confirmation; N or 30s timeout = denied. The LLM cannot bypass the gate.
