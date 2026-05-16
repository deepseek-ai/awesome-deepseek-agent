[← Back](../README.md)

# Integrate with Deep Copilot

**Deep Copilot** is an open-source AI coding agent embedded directly in VS Code, powered by DeepSeek V4 (OpenAI-compatible protocol). The model calls tools to read/write files, search code, browse the web, and run shell commands — all streamed live into the sidebar. No backend, no Docker, no Rust — pure Node.js + VS Code APIs, packaged as a single ~94 KB bundle.

- **Repository**: [github.com/ZhouChaunge/DeepCopilot](https://github.com/ZhouChaunge/DeepCopilot)
- **VS Code Marketplace**: search **Deep Copilot** (publisher *ZhouChaunge*)
- **Requires**: VS Code ≥ 1.95.0

---

## 1. Install

### Option A — VS Code Marketplace (recommended)

1. Open VS Code → **Extensions** (`Ctrl/Cmd+Shift+X`).
2. Search **Deep Copilot**.
3. Click **Install**.

### Option B — Install from VSIX

Download the latest `.vsix` from [GitHub Releases](https://github.com/ZhouChaunge/DeepCopilot/releases), then:

```bash
code --install-extension deep-copilot-<version>.vsix
```

---

## 2. Set Your DeepSeek API Key

1. Click the **🐋 Deep Copilot** icon in the activity bar to open the panel.
2. Click the **🔑** button at the bottom-right.
3. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) and save.

---

## 3. Select a DeepSeek Model

Deep Copilot defaults to `deepseek-v4-pro`. Switch in **VS Code Settings** (`Ctrl/Cmd+,`):

```jsonc
{
  "deepseekAgent.defaultModel": "deepseek-v4-pro"   // or "deepseek-v4-flash"
}
```

| Model | Description |
|---|---|
| `deepseek-v4-pro` | Full extended thinking (max reasoning effort). Best for complex refactors and bug hunts. |
| `deepseek-v4-flash` | Faster and more cost-efficient. Good for quick edits and Q&A. |

Both models support up to **1 million tokens** of context. Deep Copilot guards this automatically — see [§ Context Management](#context-management).

---

## 4. First Run

Start chatting. Deep Copilot runs an agentic loop: it calls tools, reads results, and keeps going until the task is done.

```
Refactor src/auth/ to use async/await throughout
```

```
Find all usages of the deprecated `getUser()` function and migrate them to `fetchUser()`
```

```
Fix the three failing tests in tests/api.test.ts
```

> Every file write and shell command requires your approval by default. Adjust this in [§ Approval Modes](#approval-modes).

---

## 5. Tool Set

Deep Copilot exposes a small, deliberate tool set. The schema is designed with a specific ordering principle: **edit/action tools are listed first**, which counteracts DeepSeek's RLHF-induced bias toward reading before acting, making the agent more decisive.

| Tool | Description |
|---|---|
| `apply_patch` | Apply a unified-diff patch (multi-hunk, multi-file). Preferred for any non-trivial edit. |
| `str_replace_in_file` | Precise in-place replacement by exact string match. For small, unique edits. |
| `write_file` | Create or overwrite a file. Used only for new files or full rewrites. |
| `run_shell` | Execute a shell command (npm, git, test runners, etc.) in the workspace root. |
| `read_file` | Read a file with optional line range. |
| `grep_search` | Ripgrep-style regex search across the workspace. |
| `find_files` | Locate files by name or glob pattern. |
| `list_dir` | List directory contents (depth-limited). |
| `web_search` | Search the web via Tavily (requires a [free Tavily API key](https://app.tavily.com)). |
| `web_fetch` | Fetch any public URL and return its text content. |
| `spawn_agent` | Dispatch a read-only sub-agent for complex multi-file exploration. |
| `update_plan` | Push a structured plan to the sidebar Todos panel. |
| `revert_last_turn` | Rollback all file edits made in the current agent turn. |
| `open_file_in_editor` | Open a file at a specific line in the VS Code editor. |
| `mcp__<server>__<tool>` | Any tool exposed by a connected MCP server. |

---

## 6. Web Capabilities

### Web Search (`web_search`)

Powered by [Tavily](https://app.tavily.com). Enter your Tavily API key in the **🔑** dialog (same panel as the DeepSeek key). Once set, the model can search the web autonomously during an agent turn — useful for finding library docs, error messages, or recent API changes.

### Web Fetch (`web_fetch`)

Fetches any public URL and returns its text content to the model — no API key required. Deep Copilot handles HTML-to-text conversion internally, so the model receives clean prose rather than raw markup. Security constraints applied automatically:

- Private/internal IP ranges blocked (SSRF prevention)
- Cross-host redirects blocked
- Response size capped at 2 MB
- All `http://` requests silently upgraded to `https://`

---

## 7. Approval Modes

Control how much the agent can do autonomously:

| Mode | Behaviour |
|---|---|
| `manual` | Prompt before every `write_file` and `run_shell` (default, safest) |
| `auto-edit` | Auto-approve file writes; still prompt for shell commands |
| `autopilot` | Auto-approve everything (trusted workspaces only) |
| `readonly` | Deny all writes and shell commands |

```jsonc
{ "deepseekAgent.approvalMode": "auto-edit" }
```

---

## 8. MCP Server Integration

Deep Copilot ships a built-in MCP stdio client. Any MCP-compatible tool server connects via `settings.json`:

```jsonc
{
  "deepseekAgent.mcp.servers": [
    { "name": "my-db",  "command": "npx", "args": ["my-db-mcp-server"] },
    { "name": "jira",   "command": "node", "args": ["./tools/jira-mcp.js"] }
  ]
}
```

Connected tools appear as `mcp__<server>__<tool>` in the model's function-calling interface.

---

## 9. Context Management

Deep Copilot supports up to **1 million tokens** of context (DeepSeek V4's full window). Two automatic mechanisms keep conversations healthy:

**Auto-compaction** — when estimated tokens exceed `compactBudgetTokens` (default `600000`), older tool results are replaced with a compact summary. The first user message is always preserved. An emergency pass activates at ~900K tokens to prevent HTTP 400 errors from the API.

**Streaming argument preview** — while the model is still generating a tool call, Deep Copilot streams the `path` field the moment it arrives, so you see "Editing `src/auth.ts`…" before the full arguments finish streaming. This mirrors GitHub Copilot's live-edit preview.

---

## 10. Configuration Reference

All settings live under `deepseekAgent.*`:

```jsonc
{
  "deepseekAgent.defaultModel":        "deepseek-v4-pro",
  "deepseekAgent.apiBaseUrl":          "",          // empty = api.deepseek.com
  "deepseekAgent.approvalMode":        "manual",
  "deepseekAgent.interactionMode":     "agent",     // "agent" | "ask"
  "deepseekAgent.maxIterations":       15,
  "deepseekAgent.compactBudgetTokens": 600000,
  "deepseekAgent.postEditDiagnostics": true,        // append LSP errors after each edit
  "deepseekAgent.enableDebugLog":      true,        // write logs to .deep-copilot/logs/
  "deepseekAgent.mcp.servers":         []
}
```

---

## 11. Design Highlights

### Skill Hot-plug

Skills are plain Markdown files in a directory — no plugin manifest, no extension reload. Deep Copilot scans three locations at runtime in priority order:

```
~/.deepcopilot/skills/   ← created automatically on first launch
~/.claude/skills/        ← Claude Code compatible
~/.copilot/skills/       ← GitHub Copilot compatible
```

Each skill is a subdirectory with a `SKILL.md` containing YAML frontmatter:

```markdown
---
name: my-skill
description: One-line summary shown in the slash-command popup
argument-hint: Optional hint
---

... instructions for the model ...
```

Drop a directory in and it is available on the very next message — no restart, no reload.

**How injection works**

Skills are injected as a *synthetic tool call + tool result pair* immediately before the user message, not as user text or system prompt additions:

```
assistant  →  tool_call: read_file("~/.claude/skills/my-skill/SKILL.md")
tool       →  <contents of SKILL.md>
user       →  <the user's actual message>
```

The model treats the skill as something it *read itself*, which produces significantly more reliable instruction-following than injecting the same text as a user message. This approach matches how GitHub Copilot injects skills internally.

First-match-wins across directories: a skill in `~/.deepcopilot/skills/` silently overrides a same-named skill from the Claude Code or GitHub Copilot directories, giving you a personal override layer without touching shared files. Skills from all three sources are listed together in the `/` command popup with their descriptions and argument hints.

### Context-Cache-Aware System Prompt

The system prompt is split at a `__DYNAMIC_BOUNDARY__` marker:

- **Static half** — principles, tool rules, tone. Identical across every request; eligible for DeepSeek's context cache. Subsequent turns pay cache-hit price, not full input price.
- **Dynamic half** — recomputed each turn: host OS, workspace instructions (`DEEPCOPILOT.md`), and user memory (`~/.deepcopilot/memory.md`).

The result is that most of the expensive system prompt content is cached, while per-user and per-workspace personalisation remains fresh.

### Per-Workspace Tool Hooks

`.deepcopilot/hooks.json` in the workspace root wires shell commands to tool events:

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

Hook output is injected back into the model context. The agent reads test results from the hook and self-corrects without you copying terminal output into the chat.

### Sub-agent Dispatch (`spawn_agent`)

For tasks that require reading many files (e.g. "summarise the architecture of `src/`", "find all call sites of `getUser()`"), Deep Copilot can spawn isolated read-only sub-agents. Each sub-agent gets its own focused prompt, runs in a separate context, and returns a structured Markdown summary. Multiple sub-agents dispatched in the same turn run in parallel.

### Parallel Sessions

The agent loop is keyed by session ID. You can switch to a new chat while a task is still running in another session. Events continue to buffer; switching back replays all progress live.

### Zero-backend Architecture

Everything runs inside the VS Code extension host. The production bundle is approximately 94 KB with zero runtime npm dependencies — only VS Code APIs and Node.js built-ins.
