[English](./anycode.md) | [简体中文](./anycode.zh-CN.md) · [← Back](../README.md)

# Integrate with anyCode

anyCode is an open-source (MIT) Rust agent workbench — a local-first **Digital Workbench** plus a single `AgentRuntime` that orchestrates multi-turn LLM + tool loops (Bash, Edit, Grep, MCP, LSP, Skills, cron, …). Models are BYOK: you pick the provider, keys stay in `~/.anycode/config.json`, and data stays on your machine. DeepSeek is a first-class provider with a built-in model catalog (`deepseek-v4-pro`, `deepseek-v4-flash`) and a quick-auth preset in the `/setup` wizard.

- **GitHub:** <https://github.com/qingjiuzys/anycode>

#### 1. Install anyCode

**macOS (recommended)**

Download **`anyCode_<version>_aarch64.dmg`** from [GitHub Releases](https://github.com/qingjiuzys/anycode/releases), open it, and drag **anyCode** into Applications. The built-in Workbench opens automatically.

**Linux server / headless**

```sh
curl -fsSL --proto '=https' --tlsv1.2 \
  "https://raw.githubusercontent.com/qingjiuzys/anycode/main/scripts/install.sh" | \
  bash -s -- --repo qingjiuzys/anycode
```

Then open the Workbench at `http://127.0.0.1:43180`.

**From source (developers)**

```sh
git clone https://github.com/qingjiuzys/anycode.git
cd anycode
./scripts/sync-desktop-dev.sh --rust   # UI + Rust (release-local, ~1–2 min)
```

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeek

**Option A — Setup wizard (recommended)**

Launch anyCode (or open `http://127.0.0.1:43180`). The first-time wizard (`/setup`) has a quick-auth preset:

1. Choose **DeepSeek API Key** in the presets.
2. Paste your API key. The preset defaults to model **`deepseek-v4-pro`** and endpoint `https://api.deepseek.com/chat/completions`.
3. Finish the wizard — configuration is written to `~/.anycode/config.json`.

**Option B — Edit `~/.anycode/config.json` manually**

```json
{
  "provider": "deepseek",
  "model": "deepseek-v4-pro",
  "api_key": "sk-..."
}
```

- `provider`: `deepseek` (aliases like `deep-seek` are normalized automatically).
- `model`: `deepseek-v4-pro` (flagship MoE; 1M-token context, tool calls, thinking mode) or `deepseek-v4-flash` (fast MoE; 1M-token context, tool calls).
- `base_url`: optional; defaults to `https://api.deepseek.com` (OpenAI-compatible `chat/completions`).
- `api_key`: your DeepSeek key, or set the `DEEPSEEK_API_KEY` environment variable.
- Context window: DeepSeek V4 models support up to **1 million tokens**. anyCode auto-infers the window from provider + model (`session.context_window_auto`, default `true`); set `session.context_window_tokens` to override if needed.

DeepSeek requests go through anyCode's shared OpenAI-compatible client with tool-schema normalization, so tool calling works out of the box.

#### 4. First run

1. In the Workbench, click **New Session** (or open a project).
2. Send a test message:

   > Reply only with: OK

3. Expect the assistant to reply `OK`.

#### Configuration reference

| Option | Description |
|--------|-------------|
| `provider` | `deepseek` (aliases `deep-seek` / `deep_seek` normalized) |
| `model` | `deepseek-v4-pro` or `deepseek-v4-flash` |
| `base_url` | OpenAI-compatible endpoint; defaults to `https://api.deepseek.com` |
| `api_key` | Your DeepSeek API key (or `DEEPSEEK_API_KEY` env var) |
| `session.context_window_auto` | Auto-infer context window from provider + model (default `true`) |
| `session.context_window_tokens` | Manual context window override (tokens) |
| `session.auto_compact` | Auto-compact long conversations (default `true`) |