# Raidho

[Raidho](https://github.com/vitaliyfedotovpro-art/raidho) is a coding agent that
**plans with one model and executes with another**, with a durable memory that
carries facts across runs. It is provider-agnostic and runs on your own key —
a natural fit for DeepSeek: put `deepseek-v4-pro` in the reasoning seat and the
cheaper `deepseek-v4-flash` in the execution seat, so the token-heavy tool loop
runs on the fast model while planning uses the strong one.

## Install

Requires Python ≥ 3.11.

```bash
git clone https://github.com/vitaliyfedotovpro-art/raidho
cd raidho
pip install -e '.[openai-compat]'   # DeepSeek / OpenAI-compatible backend
pip install -e '.[embed]'           # optional: semantic memory recall
```

Or use the guided installer, which verifies your key live and runs a smoke test:

```bash
bash install.sh
```

## Configure for DeepSeek

Single provider — everything on DeepSeek:

```bash
export CODER_PROVIDER=deepseek
export CODER_MODEL=deepseek-v4-flash      # execution model
export DEEPSEEK_API_KEY=sk-...
```

Split mode (the point of Raidho) — reason on `deepseek-v4-pro`, execute on
`deepseek-v4-flash`:

```bash
export CODER_PROVIDER=deepseek            # execution (code mode, tool loop)
export CODER_MODEL=deepseek-v4-flash
export CODER_REASON_PROVIDER=deepseek     # reasoning (text mode)
export CODER_REASON_MODEL=deepseek-v4-pro
export DEEPSEEK_API_KEY=sk-...
```

DeepSeek V4 models support a 1M-token context window, so long files and multi-step
tool loops fit without manual truncation. The endpoint
(`https://api.deepseek.com/chat/completions`) is used automatically; no base-URL
override is needed for DeepSeek.

## First run

Headless — run one task and exit:

```bash
coder "create a FastAPI hello-world app and run it"
```

Interactive REPL:

```bash
coder
```

In the REPL:

- `/code` — agentic coding (tool loop, executes on `CODER_MODEL`)
- `/text` — reasoning chat (runs on `CODER_REASON_MODEL` if set)
- `/council <question>` — two providers debate, a neutral pass distills the
  consensus (points of agreement, residual disagreements, recommendation)
- `/ctx` — toggle context-first mode
- `/learn` — toggle auto-distillation of repeated read-only tool loops
- `/quit` — exit

## Memory

Raidho remembers `(subject, relation, object)` facts and recalls the relevant ones
into its prompt each turn. New facts are saved via a `remember` tool, and council
verdicts are distilled into facts automatically. Memory is written per project to
`<workdir>/.raidho/memory` and reloaded on the next run — a decision reached today
resurfaces tomorrow, recalled only when relevant and across languages. It is a
Vector Symbolic Architecture (not RAG); you don't need to know the internals to use
it. The REPL prints how many facts it loaded on start.
