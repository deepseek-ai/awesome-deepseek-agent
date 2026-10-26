[English](./jpcode.md) | [简体中文](./jpcode.zh-CN.md) · [← Back](../README.md)

# Integrate with JPCode

JPCode is a conversational AI development assistant for Windows and macOS, built entirely on a self-developed C++20 engine. It runs as a desktop client: describe a requirement in natural language and the agent plans, edits code, builds and tests — executing commands through your local PowerShell/zsh, or directly on a remote machine over SSH.

JPCode ships with DeepSeek as a built-in provider preset (`https://api.deepseek.com`, Responses API), and also lets you connect any OpenAI/Anthropic-compatible provider as a custom provider.

> Two ways to use DeepSeek — pick either one:
>
> - **Jurassic AI coding plan (built-in)**: sign in to JPCode and use the models included in the plan. No API key to manage; usage is billed per subscription month with unified statements.
> - **Your own DeepSeek API key**: configure DeepSeek as a provider preset. Usage is billed directly to your DeepSeek API account. This guide covers this approach.

### Installing JPCode from Scratch

JPCode is a distributed desktop application (single-file installer), available for Windows and macOS.

- Go to the [official website](https://jpcode.jurassic-period.com/) and click **下载客户端 (Download)**. The Windows installer is named `JPCode-<version>-setup.exe`.
- Run the installer, launch JPCode.
- Optional: if you prefer to keep the key out of the UI, set the `DEEPSEEK_API_KEY` environment variable before launching JPCode. An environment variable takes precedence over the value saved in the UI.

### Configuring JPCode

Before configuring the provider, get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

4. **Pick a model**: open the **模型 (Model)** dropdown — `deepseek-v4-pro` and `deepseek-flash` are preset — or choose **✎ 手动输入 (manual input)** to type any model ID accepted by the API. `deepseek-flash` is the current model name (served by DeepSeek-V4.1-Flash-1017); the legacy name `deepseek-v4-flash` is still accepted and billed at the Flash price.
2. **Choose the provider**: click the provider button (it shows the current provider) and select **DeepSeek** from the list. Base URL and the default model are filled in automatically; the DeepSeek preset uses the Responses API (`POST https://api.deepseek.com/responses`).
3. **Fill in the API key**: paste your key into the key field (placeholder `sk-...`). Leave it empty to fall back to `DEEPSEEK_API_KEY`.
4. **Pick a model**: open the **模型 (Model)** dropdown — `deepseek-v4-pro` and `deepseek-flash` are preset — or choose **✎ 手动输入 (manual input)** to type any model ID accepted by the API.
5. **Confirm the context window**: `上下文上限（token）` (context limit) is recalculated automatically when the model changes and becomes `1000000` for DeepSeek V4 series models; you can also set it by hand (1,024 – 10,000,000). `输出上限（token，0=自动）` (max output tokens) may stay `0` to let JPCode pick a per-model default (393,216 for DeepSeek).
6. **Set thinking effort**: use the **思考 (Thinking)** selector in the bottom toolbar — `关闭 / 低 / 中 / 高` (off / low / medium / high). For DeepSeek, `低` is sent as `reasoning_effort: "low"` and both `中` and `高` as `reasoning_effort: "high"` (with thinking `enabled`); `关闭` sends `thinking: {"type": "disabled"}`. See the note below about the `max` level.
7. **Save**: settings are persisted to `config.json` as soon as a field is committed; there is no separate "apply" button. Reopen the model selector to confirm the active model.

> A deeper effort level: DeepSeek V4 accepts `low / high / max`, and `max` is the highest level. JPCode's thinking selector tops out at `高` (`high`), so if you need the `max` level, either use a custom provider (see below) or send the extra field with your own gateway. Do not disable thinking mode as a workaround for errors — JPCode already passes the reasoning content back where the API requires it.

#### Optional: DeepSeek as a custom provider (Chat Completions)

The DeepSeek preset is Responses-based. If your DeepSeek gateway or proxy only exposes Chat Completions, add it as a custom provider instead:

1. In the provider list, choose **＋ 新增自定义供应商… (add custom provider…)** and give it a name.
2. Fill in `Base URL` (e.g. `https://api.deepseek.com`) and `模型 ID` (e.g. `deepseek-v4-pro`), plus your key.
3. Use a custom provider when you need a non-default endpoint; the preset is enough for the official API.

### Using JPCode

#### First run

1. Open your project directory as the working directory (the title bar shows it; click it to change).
2. Select the DeepSeek model in the model selector at the bottom of the window.
3. Type your request in the input box and press Enter. The agent plans, edits files and runs the build/tests, streaming tool output and command output back into the conversation.

#### Command execution — local and remote

- Prefix a line with `!` in the chat to run it in your local PowerShell (Windows) or zsh (macOS); stdout/stderr stream back, followed by the exit code and a `[文件变更] +N ~M -K` file-change summary.
- Choose an SSH target machine in the bottom toolbar (**机器**) and the same `!command` runs on the remote host, with syntax adapted automatically. This is useful for building on a Linux box while keeping the DeepSeek reasoning loop on your desktop.
- Long-running builds/tests can be flagged as long tasks, so they keep waiting to completion instead of timing out.

#### Parallel subagents

Type `/agent <task>` (or `/subagent <task>`) to spawn subagents that inherit the current provider/model and context, run in parallel, and report back into the parent conversation automatically. A parent turn can dispatch several subagents at once (up to the concurrency limit of your plan), which is a common way to use DeepSeek's 1M context: one agent refactors, one writes tests, one updates docs — in the same repository.

#### Skills, KV cache and Git review

- **Skills**: reusable instruction packs (code review, test writing, documentation, plan-and-parallel, etc.) that can be toggled per conversation; third-party skills can be installed from a skill directory.
- **KV cache**: code intelligence (classes, functions, enums with file + line ranges) is indexed per working directory and served by a separate local process; the agent reads function bodies on demand instead of re-reading whole files, which keeps DeepSeek prompts short and cheap.
- **Git review panel**: changed-file tree, line-by-line diff, Markdown preview and the `+N ~M -K` summary; token usage is costed per model price so you can see spend per conversation.

#### Long sessions on DeepSeek V4

DeepSeek V4 models support up to **1M tokens of context** and the thinking mode is on by default. JPCode estimates the context size after every request (calibrated with the API-reported usage). When a conversation would exceed the configured limit, it automatically starts a new conversation carrying the current message and a hand-over note, so a long refactoring session does not hit a hard error.

### Pricing (for reference)

Verified against the [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing) (CNY per 1M tokens; off-peak price is half of the peak price, peak = Beijing time 09:00–12:00 and 14:00–18:00 on weekdays that are not Chinese public holidays):

| Model           | Input (cache hit) | Input (cache miss) | Output |
| --------------- | ----------------- | ------------------ | ------ |
| deepseek-flash  | ¥0.02 / ¥0.04     | ¥1 / ¥2            | ¥4 / ¥8 |
| deepseek-v4-pro | ¥0.15 / ¥0.30     | ¥4.5 / ¥9.0        | ¥13.5 / ¥27.0 |

*(cell format: off-peak / peak)*. Because the JPCode agent loop re-sends the project context every turn, the cache-hit price dominates the bill — keep the working directory stable so DeepSeek's context cache keeps hitting.

### Troubleshooting

- **`401 Unauthorized` / "未携带 Authorization 请求头"**: the key is empty for that provider. Re-enter it in **AI 设置**, and check that no stale `DEEPSEEK_API_KEY` in your environment is overriding (the environment variable wins).
- **Connection verification fails or requests error out**: check your DeepSeek account balance and network access; for restricted networks configure the proxy field in **AI 设置** — `http://`, `socks4://`, `socks5://`, optionally with `user:pass@`. Proxying applies to all AI requests, including streaming.
- **`429` / rate limited**: DeepSeek limits concurrency per model (higher for `deepseek-flash` than for `deepseek-v4-pro`). Reduce the number of parallel subagents, or set the TPM limit in **AI 设置** to match your account.
- **`reasoning_text must be passed back`**: JPCode passes DeepSeek's reasoning content back on tool-call turns; if a proxy or gateway in between strips the field, request it from the gateway instead of disabling thinking mode.
- **Answer style**: if you want shorter answers with more parallel tool calls, keep the default reply style; select the "plan and parallel" skill when a task should be split into subagents.
