[English](./langdriver.md) | [简体中文](./langdriver.zh-CN.md) · [← Back](../README.md)

# Integrate with LangDriver

LangDriver is a minimal ReAct agent — ~500 lines of Ruby. It combines a ReAct loop with a macOS Seatbelt hard sandbox, MCP protocol support, declarative Skill installation, and persistent memory with async compaction. Tuned for DeepSeek out of the box.

- **GitHub:** <https://github.com/kevin0x5/langdriver>

#### 1. Install LangDriver

Requires **macOS** and **Ruby 3.0+** (uses Reline shipped with Ruby 3).

```sh
git clone https://github.com/kevin0x5/langdriver && cd langdriver
```

#### 2. Configure LangDriver

Set your DeepSeek API key:

```sh
export DEEPSEEK_API_KEY=sk-xxx
```

The default `langdriver.yaml` is already tuned for DeepSeek:

```yaml
runtime:
  model: deepseek-v4-pro                # or deepseek-v4-flash (cheaper / faster)
  compact_model: deepseek-v4-flash      # used for async chat compaction
  api_base: https://api.deepseek.com
  api_key_env: DEEPSEEK_API_KEY
  max_steps: 50
  extra:
    max_tokens: 384000                  # DeepSeek v4 single-call max output
    reasoning_effort: max               # recommended for complex agent tasks
    thinking: { type: enabled }         # chain-of-thought (DeepSeek-V3.2+ supports tool calls in thinking mode)
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

> **Note:** 1M context is native on DeepSeek v4 — no extra flags needed. The `runtime.extra` block is forwarded verbatim into the chat/completions request body.

**Key configuration files:**

| File | Purpose |
|---|---|
| `profile.md` | Assistant persona / tone (system prompt) |
| `tools.yaml` | Global safety ceiling — what may be read, written, networked |
| `skills.yaml` | Per-skill enable / trust / priority |
| `mcp.yaml` | MCP server connections |
| `hooks.yaml` | `after_user_prompt` / `after_tool_use` reminder text |

#### 3. Run LangDriver

```sh
ruby langdriver.rb
```

In the REPL:

```
> read sample.txt and summarize it in one sentence
```

The model picks `read`, gets the content, then calls `final_answer`. **No hard-coded flow, no prompt templates — the model decides every step.**

#### Key REPL commands

| Command | Action |
|---|---|
| `/exit` | Exit |
| `/clear` | Clear in-session chat (memory preserved) |
| `/memory` | Show persistent memory |
| `/remember <fact>` | Append a fact to long-term memory |
| `/todos` | Show session todo list |
| `/skill list` | List installed Skills |
| `/skill install <url> <name>` | Install a community Skill (cloned into Seatbelt sandbox) |
| `/mcp` | List MCP-provided tools |

#### Security model

Community Skills downloaded via `skill install` run inside a **macOS Seatbelt sandbox** with a dynamically generated deny-by-default profile. A three-layer permission intersection (Skill frontmatter × local override × global ceiling) and core/external trust levels ensure untrusted scripts cannot access unauthorized files or network.

