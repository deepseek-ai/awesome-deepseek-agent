# Integrate with Revo

[English](./revo.md) | [简体中文](./revo.zh-CN.md) · [← Back](../README.md)

# Integrate with Revo

Revo is an MIT-licensed **terminal agent harness** that runs one continuous agent life instead of a session list.
Launch it and the first work cycle opens with no prompt; each cycle is `observe -> model -> act -> verify -> update
self -> next cycle`, and the agent keeps one append-only life log plus a checksummed sleep snapshot, so unfinished
intentions survive sleep and restarts.

It talks to any OpenAI-compatible **streaming Chat Completions** endpoint with tool calls. DeepSeek-V4 works without
a translation shim: Revo sends `tools`, `reasoning_effort: "high"` and reads `reasoning_content` back from the
response, and its context budget already defaults to 1,048,576 tokens.

#### 1. Install Node.js

- Install [Node.js](https://nodejs.org/en/download/) 22.19 or newer (`node --version`).
- Windows users: PowerShell 7 is the tested shell in the docs.

#### 2. Get a DeepSeek API Key

Create a key at the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Clone and install

```bash
git clone https://github.com/shyringo/revo.git
cd revo
npm ci --ignore-scripts
```

#### 4. Point Revo at DeepSeek

Revo's default provider is OpenCode Go (`https://opencode.ai/zen/go/v1`). Two variables switch it to the DeepSeek API:

```bash
export REVO_API_KEY="<your DeepSeek key>"
export REVO_BASE_URL="https://api.deepseek.com"
export REVO_MODEL="deepseek-v4-flash"
```

PowerShell:

```powershell
$env:REVO_API_KEY = "<your DeepSeek key>"
$env:REVO_BASE_URL = "https://api.deepseek.com"
$env:REVO_MODEL = "deepseek-v4-flash"
```

Use `deepseek-v4-pro` instead of `deepseek-v4-flash` when you want the stronger model — Revo sends
`reasoning_effort: "high"` on every cognitive call, so thinking-capable models are used as intended with no extra
configuration.

Optional, for long-horizon runs on the 1M-token context window:

```powershell
$env:REVO_CONTEXT_WINDOW_TOKENS = "1048576"   # default; state it explicitly if you use a config file
$env:REVO_MAX_OUTPUT_TOKENS = "65536"         # default is 4096 per model call
```

#### 5. Wake it

```bash
npm start -- --for 5m
```

`--for 5m` bounds the first awakening to five minutes. Revo opens a full-screen TUI: `REVO ● AWAKE`, a live
`attention` line, a `cycle` counter, and `LIFE` filling with observations and tool calls. It does **not** wait for a
message. Type at any time to interrupt it; `:sleep` or one `Ctrl+C` consolidates memory and exits.

#### 6. Verify the wiring without spending tokens

```powershell
npm link
revo --doctor
```

`--doctor` checks the configuration, credential, model lock, constitution, state directory, life-log integrity and
the provider's model catalogue. A provider error here (for example HTTP 401) means the key or the base URL is wrong;
fix that before the first awakening.

#### Cost control

Revo keeps calling the model while it is awake. Bound it at the command line or in the environment:

```powershell
npm start -- --for 30m               # hard awake-time limit
npm start -- --token-budget 200000   # hard token limit for one awakening
npm start -- --status --json         # read pending work without waking the model
npm start -- --delivery latest       # print the last durable delivery without waking the model
```

Nothing runs once it sleeps.

#### Notes

- Revo stores state in `<workspace>/.revo/life.jsonl` (git-ignored). A single `stateDir` in a private config file
  keeps one identity across workspaces: [config.example.json](https://github.com/shyringo/revo/blob/main/config.example.json).
- Revo is an experimental v0.1 prototype with a guardrail, not a sandbox. Read
  [Status](https://github.com/shyringo/revo#status) and
  [Security](https://github.com/shyringo/revo/blob/main/docs/security.md) before pointing it at untrusted content.
- Chinese README: [zh-CN.md](https://github.com/shyringo/revo/blob/main/docs/zh-CN.md).
