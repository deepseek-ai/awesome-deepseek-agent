[English](./kun.md) | [简体中文](./kun.zh-CN.md) · [← Back](../README.md)

# Integrate with Kun

[Kun](https://github.com/KunAgent/Kun) is an open-source AI agent workspace that combines requirement clarification, design drafts, implementation plans, and agent coding into one GUI workflow. It ships with a local runtime (`kun serve`) that uses DeepSeek as the default text and reasoning model.

- **GitHub:** <https://github.com/KunAgent/Kun>

#### 1. Install Kun

Download the latest release for your platform from the [GitHub Releases](https://github.com/KunAgent/Kun/releases) page, or build from source:

```sh
git clone https://github.com/KunAgent/Kun.git
cd Kun
npm install
npm run dev
```

Requirements:

- [Node.js](https://nodejs.org/en/download/) 20+
- A DeepSeek API Key

> **Note:** The first time you launch Kun, select **DeepSeek** as the model provider and paste your API key in the setup wizard.

#### 2. Configure the Kun runtime for DeepSeek

Kun's local runtime connects to the DeepSeek API directly. The simplest way to start it is with `kun serve`:

```sh
mkdir -p ~/.deepseekgui/kun
kun serve \
  --data-dir ~/.deepseekgui/kun \
  --api-key "$DEEPSEEK_API_KEY" \
  --base-url https://api.deepseek.com/beta \
  --model deepseek-v4-pro
```

You can also set the API key via the environment variable:

```sh
export DEEPSEEK_API_KEY="sk-..."
export KUN_MODEL="deepseek-v4-pro"
kun serve --data-dir ~/.deepseekgui/kun
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

**Key CLI flags:**

| Flag | Description | Default |
|------|-------------|---------|
| `--api-key` | DeepSeek-compatible API key | empty |
| `--base-url` | DeepSeek-compatible API base URL | `https://api.deepseek.com/beta` |
| `--model` | Default model id | `deepseek-v4-pro` |
| `--data-dir` | Runtime data directory | required |
| `--approval-policy` | Tool approval mode: `auto`, `on-request`, `never`, etc. | `auto` |
| `--sandbox-mode` | Filesystem sandbox: `read-only`, `workspace-write`, `danger-full-access` | `workspace-write` |

#### 3. Using DeepSeek V4 models

Kun has built-in model profiles for DeepSeek V4. Both models are pre-configured with a **1 million token** context window and compaction thresholds around 980k input tokens:

| Model | Use case |
|-------|----------|
| `deepseek-v4-pro` | Complex reasoning, planning, code review (default) |
| `deepseek-v4-flash` | Faster, cheaper tasks and quick clarifications |

To switch the default model, either:

- Pass `--model deepseek-v4-flash` to `kun serve`, or
- Set the `KUN_MODEL` environment variable, or
- Edit `~/.deepseekgui/kun/config.json`:

```json
{
  "serve": {
    "model": "deepseek-v4-pro",
    "baseUrl": "https://api.deepseek.com/beta",
    "apiKey": "sk-..."
  }
}
```

#### 4. Run Kun from the terminal

Besides the GUI, you can use Kun as a standalone agent CLI:

```sh
# One-shot task
kun run --data-dir ~/.deepseekgui/kun --workspace "$PWD" "summarize this repo"

# Interactive REPL
kun chat --data-dir ~/.deepseekgui/kun --workspace "$PWD"

# List available tools
kun exec --data-dir ~/.deepseekgui/kun --workspace "$PWD" --list-tools
```

#### 5. Start coding in the GUI

1. Launch Kun and bind a local project folder in **Code** mode.
2. Start a thread and ask a question or give an instruction.
3. Kun reads project context, executes tools, and shows inline diffs for file changes.

> **Tip:** Kun forwards requests to the DeepSeek API, so reasoning/thinking content works out of the box with `deepseek-v4-pro`. No extra reasoning-effort flag is required at the Kun CLI level.
