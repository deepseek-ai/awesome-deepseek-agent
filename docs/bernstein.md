[English](./bernstein.md) | [简体中文](./bernstein.zh-CN.md) · [← Back](../README.md)

# Integrate with Bernstein

Bernstein is an open-source (Apache-2.0) governance layer for AI coding agents. It does not call a model itself: it runs an agent CLI (Claude Code, Codex, Kilo Code, Crush, Aider and others) for each task in its own git worktree, gates the result with tests and policy checks, and records every step in a tamper-evident audit log with a run receipt you can verify offline.

This guide shows two ways to run DeepSeek V4 under Bernstein:

- **A. DeepSeek API** through an agent CLI — the common case. The example uses Claude Code; any agent CLI from the other guides in this repository works the same way once that CLI is configured for DeepSeek.
- **B. Self-hosted DeepSeek V4 weights** through Bernstein's `ollama` adapter (Ollama or vLLM on your own hardware).

### Installing Bernstein

- Install Python 3.11+ and [uv](https://docs.astral.sh/uv/) (or pipx).
- Install Bernstein and create a workspace in your repository:

```
uv tool install bernstein      # or: pipx install bernstein
cd your-project
bernstein init                 # creates .sdd/ and bernstein.yaml
bernstein doctor               # checks that an agent CLI is installed and authenticated
```

`bernstein doctor` prints the adapters it found. For path A you need at least one agent CLI installed (the example below uses Claude Code; see its own guide in this repository for installing it).

### A. DeepSeek API through an agent CLI

#### 1. Configure the agent CLI for DeepSeek

Bernstein starts each worker with a filtered environment: variables you `export` in your shell are **not** inherited by the worker. Configure the agent CLI through its own configuration file, which the CLI reads by itself.

For Claude Code, put the DeepSeek settings in `~/.claude/settings.json` (create the file if it does not exist):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<your DeepSeek API Key>",
    "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash[1m]",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_EFFORT_LEVEL": "max"
  }
}
```

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). The `[1m]` suffix enables the 1M-token context window.

Check that the CLI alone works before adding Bernstein:

```
claude -p "Reply with the model name you are running as."
```

#### 2. Point Bernstein at that CLI and model

Edit `bernstein.yaml` in your project. The `model` value is passed to the CLI unchanged (`claude --model deepseek-v4-pro[1m]`), and `effort: max` becomes `--effort max`:

```yaml
goal: "Describe the task for the agents here."
cli: claude
max_agents: 2

role_model_policy:
  manager:
    cli: claude
    model: deepseek-v4-pro[1m]
    effort: max
  backend:
    cli: claude
    model: deepseek-v4-pro[1m]
    effort: max
  docs:
    cli: claude
    model: deepseek-v4-flash[1m]
    effort: high

quality_gates:
  enabled: true
  tests: true
  test_command: python -m pytest -q
```

Use `deepseek-v4-pro[1m]` for roles that plan, implement and review; `deepseek-v4-flash[1m]` is a cheaper choice for documentation or housekeeping roles. Bernstein adds no `--fallback-model` for DeepSeek model names, so a failed request fails the task instead of silently switching models.

#### 3. First run

```
bernstein run --audit
```

Bernstein creates one worktree per task, runs the agent CLI in it, executes `test_command`, and writes the run to `.sdd/runs/<run_id>/`. To check the audit chain and the run receipt:

```
bernstein audit verify
bernstein verify receipt .sdd/runs/<run_id>/run-receipt.json
```

The receipt records which CLI and which model name each task ran with, so a reviewer can see that the run used `deepseek-v4-pro[1m]` without access to your API account.

#### Other agent CLIs

The same `bernstein.yaml` shape works with any adapter that `bernstein adapters list` reports. Configure the CLI for DeepSeek as described in that CLI's guide in this repository, then set `cli:` and `model:` per role, for example `cli: codex` with the model name that CLI expects. Keep `effort: max` for roles that write code.

### B. Self-hosted DeepSeek V4 weights

DeepSeek V4 Flash and Pro ship as open MoE weights. Bernstein's `ollama` adapter talks to any OpenAI-compatible `/v1/chat/completions` endpoint, so both an Ollama daemon and a vLLM server work:

```
# Flash on a single GPU through Ollama
export OLLAMA_API_BASE=http://10.0.0.5:11434

# Pro on a multi-GPU vLLM server
python -m vllm.entrypoints.openai.api_server \
    --model deepseek-ai/deepseek-v4-pro \
    --tensor-parallel-size 8 --host 10.0.0.5 --port 8000
export OLLAMA_API_BASE=http://10.0.0.5:8000/v1
```

```yaml
cli: ollama
role_model_policy:
  backend:
    cli: ollama
    model: deepseek-v4-pro
    effort: max
```

Note: for the DeepSeek V4 model names the `ollama` adapter enforces a data-residency guard and only accepts loopback, private-network or internal-suffix endpoints (`localhost`, `10.x`, `192.168.x`, `*.internal` and similar). Pointing this adapter at the public DeepSeek API is refused at spawn time with `RESIDENCY_VIOLATION`; use path A for the public API.

### Checking the run

- `bernstein status` shows running and finished tasks.
- `.sdd/runs/<run_id>/` holds the audit log, the lineage records and the run receipt.
- `bernstein verify receipt <file>` needs only the file: no network, no API key.

### Links

- Bernstein: https://github.com/sipyourdrink-ltd/bernstein
- Docs: https://docs.bernstein.run
- DeepSeek API docs: https://api-docs.deepseek.com/
- DeepSeek thinking mode: https://api-docs.deepseek.com/guides/thinking_mode
