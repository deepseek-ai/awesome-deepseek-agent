[English](./gneol.md) | [简体中文](./gneol.zh-CN.md) · [← Back](../README.md)

# Integrate with Gneol

Gneol is a runtime for `.gneol` files. One plain-text file describes an AI agent — its model, subagents, scheduled triggers, event listeners, tools, and MCP servers — and Gneol runs it locally as a single process. Gneol supports custom models, and DeepSeek V4 can be connected through the built-in `deepseek` provider, which speaks the OpenAI-compatible Chat Completions API.

#### 1. Install Gneol

macOS / Linux:

```bash
curl -sSL https://raw.githubusercontent.com/Gneol/Gneol/main/install.sh | bash
```

Or download a precompiled binary from the [Releases](https://github.com/Gneol/Gneol/releases) page. Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 2. Provide the DeepSeek API Key

Gneol resolves secrets from three sources: a program `.env` file, the global encrypted secret store, and your shell environment. Pick whichever fits your workflow.

**Option A — Global secret store (encrypted on disk)**

```bash
gneol secrets set DEEPSEEK_API_KEY "<your DeepSeek API Key>"
```

**Option B — Per-program `.env` file**

```
# .env
DEEPSEEK_API_KEY=<your DeepSeek API Key>
```

**Option C — Shell environment**

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

#### 3. Configure the DeepSeek Model

Create a `.gneol` program. The `model("<tag>")` block declares the DeepSeek binding; the `program()` header references that model by tag.

```
program("Hello World")
  .model("deepseek")
  .env(".env")

model("deepseek")
  .provider("deepseek")
  .modelId("deepseek-v4-flash")
  .apiKey("DEEPSEEK_API_KEY")
  .temperature(0.7)
  .maxTokens(384000)

subagent().model("deepseek")

summarization().model("deepseek").prompt("tl;dr in 3 bullets")
```

- `.provider("deepseek")` — selects the built-in DeepSeek adapter (base URL `https://api.deepseek.com`).
- `.modelId("deepseek-v4-flash")` — the DeepSeek model id (see [Available Models](#available-deepseek-models)).
- `.apiKey("DEEPSEEK_API_KEY")` — the **name** of the environment variable that holds your key. Never paste the literal key into the program file.
- `.env(".env")` — optional; loads variables from a local `.env` file.

Save it as `hello.gneol` — UTF-8, without a BOM.

#### 4. Deploy and Chat

```bash
gneol start --daemonize          # optional: run the runtime in the background
gneol deploy -f hello.gneol -i   # deploy the program, then open a chat
```

`gneol deploy` reconciles the runtime with your `.gneol` file — creating the agent, applying the model binding, and starting it. The `-i` flag drops you straight into an interactive session:

```
Hello World ❯ hi there
💬 Hello! I'm your Hello World agent running on DeepSeek V4 Flash.
```

Useful follow-up commands:

| Command | Purpose |
|---------|---------|
| `gneol` | Initialize/attach a session in the current directory. |
| `gneol status` | Check whether the runtime is running. |
| `gneol secrets list` | List stored secret names. |
| `gneol stop` | Stop the runtime. |

Run `gneol --help` for the full command list.

#### 5. Optional: Verify the API Key

```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

If the request succeeds, the API Key and model name are valid.

#### Available DeepSeek Models

| Model ID | Notes |
|----------|-------|
| `deepseek-v4-pro` | DeepSeek's flagship reasoning model. Use it for the root agent, or for subagents that need deeper reasoning. |
| `deepseek-v4-flash` | Fast, low-cost model. Gneol's default when scaffolding a new program. |

Both models accept up to **1M tokens of context**, and `deepseek-v4-pro` supports the **max thinking effort** level. Gneol forwards `.temperature` and `.maxTokens` straight to DeepSeek's OpenAI-compatible endpoint, so `.maxTokens(384000)` uses the full output budget.

#### Mixing Providers

Gneol can bind several models at once, so you can route different subagents to different providers and keep DeepSeek as your primary or fallback:

```
model("fast")
  .provider("deepseek")
  .modelId("deepseek-v4-flash")
  .apiKey("DEEPSEEK_API_KEY")

model("eagle-eye")
  .provider("openrouter")
  .modelId("openai/gpt-4o")
  .apiKey("OPENROUTER_API_KEY")

subagent("Reviewer")
  .model("eagle-eye")
  .description("Independent second opinion on DeepSeek's output")
```

#### Troubleshooting

- `Authentication Fails` or `401`: Check that `apiKey` names a variable that actually holds your real DeepSeek API Key. Do not put the API URL in the key field.
- `Model Not Found` or `404`: Check that the model id is exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- The agent does not start: Run `gneol status`; if the runtime is down, start it with `gneol start --daemonize`.
- The API key is not picked up: Make sure the variable is exported in the shell that launched `gneol`, or store it with `gneol secrets set DEEPSEEK_API_KEY ...`.
- The program fails to parse: Confirm the tag in `program().model("<tag>")` matches the `model("<tag>")` block, and that the file is saved as UTF-8 without a BOM.
