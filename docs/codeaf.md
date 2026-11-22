[English](./codeaf.md) | [简体中文](./codeaf.zh-CN.md) · [← Back](../README.md)

# Integrate with codeaf

codeaf is an open-source (Apache 2.0) software factory by AgentField. You describe the work in your terminal, and it runs coding tasks on any model, several at once, each in its own copy of the repository on its own branch. DeepSeek's first-party API is one of its built-in providers.

#### 1. Install codeaf

- macOS and Linux:

```bash
curl -fsSL https://agentfield.ai/get/codeaf | bash
```

- Windows: download `codeaf-windows-amd64.exe` (or `-arm64.exe`) from the [releases page](https://github.com/Agent-Field/CodeAF/releases).

- Check the install. If a version is printed, it worked:

```bash
codeaf --version
```

#### 2. Connect DeepSeek

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then run:

```bash
codeaf connect deepseek
```

Paste the key at the `key:` prompt. codeaf checks it against `GET /models` before saving it, and prints `deepseek is connected` with the number of models it found. To connect from a script instead:

```bash
echo "$DEEPSEEK_API_KEY" | codeaf connect deepseek
```

You can also connect from inside a session with `/connect` → **DeepSeek**. codeaf talks to `https://api.deepseek.com/v1` (OpenAI-compatible) directly; no proxy or router is involved.

#### 3. Pick a model and thinking level

Start codeaf in your project with DeepSeek-V4-Pro and the maximum thinking level:

```bash
cd /path/to/my-project
codeaf chat --model deepseek/deepseek-v4-pro --reasoning max
```

- Models: `deepseek/deepseek-v4-pro` or `deepseek/deepseek-v4-flash`. The `deepseek/` prefix is the name of the connected provider; run `codeaf connect` to see it. If you connected from `/connect` inside a session, the provider may be listed as `deepseek-direct`, so use `deepseek-direct/deepseek-v4-pro`.
- Inside a session, `/model` switches models and saves the choice.
- **Thinking level:** `--reasoning low|high|max` on the command line, `/effort max` inside a session, or the thinking row in `/settings`. codeaf sends DeepSeek's own `reasoning_effort` field (`low`, `high` or `max`). With no level set, DeepSeek's default (`high`) applies.
- **1M context:** DeepSeek V4 models support up to 1 million tokens of context. codeaf reads each model's context window from DeepSeek's model list, so there is nothing to configure.

#### 4. First run

Describe what you want the way you would to a colleague, for example:

```text
Add input validation to the signup handler, and separately fix the flaky date test in utils.
```

Each code task runs in its own copy of the repository and ends on its own branch, so two tasks never edit the same files at once. For a large, well-specified change that should run unattended, use `/senior-dev <brief>` in a session, or `codeaf senior-dev "<brief>"` from a shell (macOS and Linux).
