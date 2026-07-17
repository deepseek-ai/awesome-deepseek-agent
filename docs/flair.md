[English](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/docs/flair.md) | [简体中文](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/docs/flair.zh-CN.md) · [← Back](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/README.md)

# Integrate with flair

flair is an open-source, DeepSeek-first agentic AI assistant with two sides — advanced **coding** and general **desktop automation** — that runs on Linux, macOS, and Windows. It speaks the OpenAI-compatible protocol, with DeepSeek V4 as its primary provider.

- **GitHub:** <https://github.com/NAST0R/flair>

#### 1. Install flair

Requires Python ≥ 3.10.

```
git clone https://github.com/NAST0R/flair.git
cd flair
pip install -e .
# optional extras (detailed RAM/CPU info, portable clipboard) used by the general agent:
pip install -e ".[extras]"
```

#### 2. Configure flair for DeepSeek

flair loads its configuration from a `.env` file. Copy the template and add your DeepSeek key:

```
cp .env.example .env
```

Then edit `.env` so DeepSeek is the active provider:

```
FLAIR_PROVIDER=deepseek

DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-flash       # fast workhorse (non-thinking)
DEEPSEEK_THINK_MODEL=deepseek-v4-pro   # reasoner used for --think

FLAIR_ROOT=.                           # working root the coding agent is sandboxed to
FLAIR_AUTO_APPROVE=false               # ask for confirmation before destructive tools
```

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Configuration options:**

| Variable | Description |
| --- | --- |
| `FLAIR_PROVIDER` | Active provider — set to `deepseek` |
| `DEEPSEEK_API_KEY` | Your DeepSeek API key |
| `DEEPSEEK_MODEL` | Fast, non-thinking model (default `deepseek-v4-flash`) |
| `DEEPSEEK_THINK_MODEL` | Reasoner used on the `--think` step (default `deepseek-v4-pro`) |
| `FLAIR_ROOT` | Working root the coding agent is confined to |
| `FLAIR_AUTO_APPROVE` | Skip the confirmation prompt for destructive tools (default `false`) |

> **Thinking mode & 1M context.** On DeepSeek **V4**, thinking is turned on by a *parameter* rather than a separate model name. flair enables it automatically only on the `--think` step, using `deepseek-v4-pro` (a genuine reasoner); the fast tool loop stays on `deepseek-v4-flash`. Both V4 models expose a **1M-token** context window — flair measures context exactly from the API's `prompt_tokens` and compacts the history automatically as it nears a threshold (75% of the window by default), keeping the prefix cache active.

> **Cost tracking.** flair estimates cost per turn from a per-model price table (overridable via `FLAIR_PRICE_*`) and can enforce a hard ceiling with `--max-cost <usd>`. Check current DeepSeek rates on the [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing).

#### 3. Run flair

```
flair                                  # interactive REPL, auto-routes between coding and general
flair -p "open youtube for me"         # one-shot task
flair --think -p "refactor the parsing module to reduce complexity"   # reasoner on the first step
flair --root ~/projects/my-repo        # point the coding agent at a project
flair --yes -p "run the tests and fix the errors"                     # no confirmations
```

**Useful REPL commands:**

| Command | Effect |
| --- | --- |
| `/code <task>` | Force the coding agent |
| `/do <task>` | Force the general agent |
| `/think <task>` | Use the thinking model on the first step |
| `/provider [name]` | Show or switch provider at runtime (`deepseek` / `openai`) |
| `/model <name>` | Switch the fast model at runtime |
| `/think-model <name>` | Switch the thinking model at runtime |
| `/cost` | Session token / cost summary |
| `/compact` | Compact the active agent's context now |
| `exit` | Quit |

That's it — flair is now running on DeepSeek V4.
