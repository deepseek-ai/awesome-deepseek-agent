[English](./gebai.md) | [简体中文](./gebai.zh-CN.md) · [← Back](../README.md)

# Integrate with GEBAI

GEBAI (歌白) is an open-source AI agent engine built around one stable core loop: **conversation → tool calls → approval → execution**. The model is stateless and replaceable; memory and accountability live in the agent body — anything that must survive across turns is written to files or session records, and every tool call is approval-gated and auditable. Desktop app, local browser and server deployment share a single codebase.

- **GitHub:** <https://github.com/xuxinle/gebai>

#### 1. Install GEBAI

GEBAI requires [Bun](https://bun.sh) ≥ 1.2. Clone the repository and install dependencies:

```sh
git clone https://github.com/xuxinle/gebai.git
cd gebai
bun install
```

#### 2. Configure DeepSeek

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then create the environment file from the template:

```sh
cp .env.example .env      # Windows: copy .env.example .env
```

Edit `.env` to point GEBAI at DeepSeek:

```
GEBAI_LLM_API_BASE=https://api.deepseek.com
GEBAI_LLM_API_KEY=sk-your-key-here
GEBAI_LLM_MODEL=deepseek-v4-pro

# 1M context window, up to 384K output tokens
GEBAI_LLM_MAX_CONTEXT=1000000
GEBAI_LLM_MAX_OUTPUT_TOKENS=384000

# Pin the max reasoning effort (thinking mode is on by default)
GEBAI_LLM_EXTRA_PARAMS={"reasoning_effort":"max"}
```

- `deepseek-v4-pro` delivers the strongest reasoning; for the faster, lower-cost model use `deepseek-flash` (older docs may refer to it as `deepseek-v4-flash` — still accepted).
- DeepSeek V4 supports a 1M-token context window and the max thinking effort level; `reasoning_effort` accepts `low`, `high` or `max`. See the [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode).
- You can also override model settings entirely from the browser: **Settings → Environment Variables** (kept only in the browser, injected per message).

#### 3. First run

```sh
bun run dev
```

Open <http://127.0.0.1:3000> and start chatting — GEBAI runs on DeepSeek with tool calls, plan approvals, sub-agents and audit records all active out of the box.

To build a standalone single-file binary instead of running from source, see the [GEBAI README](https://github.com/xuxinle/gebai).

#### Troubleshooting

- `401` / authentication errors: check `GEBAI_LLM_API_KEY` in `.env` (no leading or trailing spaces) and confirm `GEBAI_LLM_API_BASE=https://api.deepseek.com`. Make sure `.env` sits at the repository root.
- `Model Not Found` / `404`: make sure `GEBAI_LLM_MODEL` uses a current model ID (`deepseek-v4-pro` or `deepseek-flash`).
- Port 3000 already in use: set `GEBAI_PORT` in `.env` to another port before running `bun run dev`.
