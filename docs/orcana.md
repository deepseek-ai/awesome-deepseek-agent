# Connect Orcana

[简体中文](./orcana.zh-CN.md) · [← Back](../README.md)

Orcana is a DeepSeek-native terminal Coding Agent runtime built for long-running software engineering tasks.

Its core direction is constraint-first coding workflow: task triage, planning gates, task packets, controlled tool calls, patch transactions, evidence-based completion, and an interactive TUI for coding sessions.

- GitHub: https://github.com/Leo-Ayh-Oday/deepseek-orcana

## 1. Install Orcana

Orcana requires Node.js 18+ or Bun.

Install via npm:

```bash
npm install -g deepseek-orcana
```

Or from source:

```bash
git clone https://github.com/Leo-Ayh-Oday/deepseek-orcana.git
cd deepseek-orcana
bun install
bun run build
```

Verify the installation:

```bash
orcana --version
```

## 2. Get a DeepSeek API Key

Get your API key from the DeepSeek Platform:

```
https://platform.deepseek.com
```

Orcana uses DeepSeek via environment variables or a local settings file.

## 3. Configure DeepSeek

### Option A: Environment variables

Linux / macOS:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export DEEPSEEK_MODEL_OVERRIDE="deepseek-v4-pro"
```

Windows PowerShell:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:DEEPSEEK_MODEL_OVERRIDE="deepseek-v4-pro"
```

### Option B: Configuration file

Copy the example settings and edit:

```bash
mkdir -p ~/.deepseek-code
cp settings.example.json ~/.deepseek-code/settings.json
```

The file uses nested structure:

```json
{
  "provider": {
    "baseUrl": "https://api.deepseek.com/anthropic",
    "apiKey": "${DEEPSEEK_API_KEY}",
    "modelOverride": "deepseek-v4-pro",
    "costMode": "normal",
    "idleTimeoutMs": 60000
  },
  "loop": {
    "maxSteps": 100,
    "autoContinue": false
  },
  "memory": {
    "compactionEnabled": true
  },
  "sandbox": {
    "enabled": true
  }
}
```

Orcana's ModelRouter uses `deepseek-v4-pro` for planning, coding, and review, and `deepseek-v4-flash` for task triage, lightweight judgments, and auxiliary calls. Complex coding tasks use max reasoning effort by default.

DeepSeek V4 supports 1M token context — Orcana tracks context budget and warns at 524K, blocks at 629K.

## 4. Start Orcana in Your Project

Enter your project directory:

```bash
cd /path/to/your-project
```

Start the interactive TUI:

```bash
orcana
```

Non-interactive one-shot prompt:

```bash
orcana "Explain this repository and identify the main entry points."
```

Other commands:

```bash
orcana --cli "fix the type error in src/utils.ts"   # CLI mode
orcana list                                           # List saved sessions
orcana last                                           # Resume latest session
```

## 5. First Coding Task

Start with a small, verifiable task:

```
Find a simple TypeScript type error in this project, explain the root cause, fix it, and run the relevant verification command.
```

For more complex tasks, Orcana will plan before editing:

```
Refactor the TUI input composer so long pasted text does not block rendering.
First inspect the relevant files, produce a plan, then implement the smallest safe change and verify it.
```

## 6. How Orcana Uses DeepSeek

Orcana is designed around a DeepSeek-native coding workflow:

- `deepseek-v4-pro` for planning, coding, repair, and review.
- `deepseek-v4-flash` for fast task triage, lightweight judgments, and auxiliary calls (6 independent Flash roles).
- Max reasoning effort for complex engineering tasks.
- Context-cache-aware prompt layout: stable prefix (system rules + tool schema + project constitution) computed once and reused across rounds.
- FIM-backed scoped file edits via the Anthropic-compatible endpoint, with PatchTransaction protection.
- Thinking token capture and preservation across context compaction cycles.
- Long-context task execution with context budget tracking.

## 7. Key Features

### Planning and Task Control

Orcana uses a planning gate and TaskPacket to reduce blind editing. Complex tasks must produce a plan, scope, completion criteria, and verification requirements before implementation.

### Patch Transaction

Code edits are recorded as patch transactions: `read → record baseHash → propose → check scope → apply → verify → commit / rollback`. File modifications stay scoped, auditable, and reversible on verification failure.

### Ripple Engine 2.0

Before any file write, the Ripple Engine traces how the change propagates through the codebase. 7 layers: API Diff → Semantic References → Usage Classification → Verification Map → Obligation Gate. Writes are blocked until all affected callers are handled. 212 tests, 8.5/10.

### Evidence-Based Completion

Orcana records verification evidence — typecheck, test, build, or manual inspection. Without required evidence, the agent is blocked from claiming completion. The Final Truthfulness Gate cross-references completion text against the EvidenceLedger.

### TUI for Long Tasks

The interactive TUI is designed for coding sessions that involve planning, tool calls, code edits, verification, and repair loops. It shows current mode, plan node, task packet, tool stream, patch status, evidence status, and gate block reasons.

### Tool Risk Taxonomy

Tools are classified into 5 risk levels: Risk 0 (read-only, auto-allow), Risk 2 (file write, policy decision), Risk 4–5 (git mutation, external effects — require user confirmation, no session allow).

## 8. Recommended Use Cases

Good fits for Orcana:

- TypeScript / JavaScript repository understanding.
- Bug fixes with verification.
- TUI / CLI feature iteration.
- Refactoring tasks that benefit from planning and controlled edits.
- DeepSeek-native Coding Agent experiments.

Start with small, verifiable tasks before attempting broad multi-file changes.

## 9. Known Limitations

Orcana is an experimental Coding Agent runtime. Some capabilities are still evolving: lifecycle hooks, long-task memory, end-to-end replay, and full rewind workflows.

For high-risk operations, inspect the plan, changes, and verification output before accepting results. Do not use auto-approve mode in production repositories unless you fully understand the tool permissions and rollback behavior.

Current version: v0.2.1. Target: v1.0 (10 phases, 32 PR groups, 17 verifiable acceptance criteria).

## 10. Troubleshooting

### API Key not found

Check that `DEEPSEEK_API_KEY` is set:

```bash
echo $DEEPSEEK_API_KEY
```

Windows PowerShell:

```powershell
echo $env:DEEPSEEK_API_KEY
```

### Model name error

Use current DeepSeek V4 model names:

```
deepseek-v4-pro
deepseek-v4-flash
```

Avoid deprecated names like `deepseek-chat`, `deepseek-reasoner`, or `deepseek-coder`.

### Context window not configured

DeepSeek V4 supports a 1M token context window. Orcana manages this automatically via ContextEpoch — no manual configuration needed.

### Reasoning effort too low

For complex coding tasks, Orcana uses max reasoning effort by default. You can verify in `~/.deepseek-code/settings.json`.

### Commands not found

Available commands: `orcana`, `deepseek-orcana`, `deepseek-code`, `deepseek`. If `orcana` is not found, try `npx deepseek-orcana`.
