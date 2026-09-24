[English](./deepseeker_code.md) | [简体中文](./deepseeker_code.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeeker-Code

DeepSeeker-Code is a local-first AI coding assistant powered by DeepSeek. One self-developed agentic engine is shared by three entries — a VS Code extension, a terminal CLI (React Ink), and a local HTTP API — with the same toolchain, approval gateway, and session store across all of them. It talks to `api.deepseek.com` over the OpenAI-compatible API, runs with the full 1M-token context window of DeepSeek V4 models, and supports reasoning effort up to `max`.

- **GitHub:** <https://github.com/xknk/deepseeker-code>

#### 1. Install DeepSeeker-Code

**Terminal CLI** (npm):

```sh
npm install -g deepseeker-code
```

**VS Code extension**: download the `.vsix` from [Releases](https://github.com/xknk/deepseeker-code/releases) and install it:

```sh
code --install-extension deepseeker-code-<version>.vsix
```

The extension is self-contained — the engine ships inside, so no separate CLI install is needed. Both entries share sessions and configuration under `~/.deepseeker-code/`, so a session started in the CLI can be continued in VS Code.

#### 2. Get a DeepSeek API Key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then:

- **CLI**: set it as an environment variable:

  ```sh
  export DEEP_SEEK_API_KEY=sk-***
  ```

- **VS Code extension**: set `deepseekerCode.apiKey` in Settings.

#### 3. Configure the model (optional)

```sh
export DEEP_SEEK_MODEL=deepseek-v4-pro      # default: deepseek-flash
export DEEP_SEEK_AUX_MODEL=deepseek-flash   # light tasks such as summarization
export DEEP_SEEK_REASONING_EFFORT=max       # "high" (default) or "max"; low/medium are deprecated and map to high
export DEEP_SEEK_THINKING=0                 # disable thinking mode (enabled by default)
```

DeepSeek V4 models provide a 1M-token context window; DeepSeeker-Code's automatic context compaction is tuned for DeepSeek-V4, so long sessions keep working without losing detail — archived messages and oversized tool outputs stay retrievable through the built-in `recall` tool.

#### 4. First run

```sh
cd /path/to/your-project
deepseeker-code
```

In VS Code: command palette → `DeepSeeker-Code: Open Chat` (or press `Ctrl+Esc`).

What you get out of the box:

- **Approval gateway**: read-only tools run freely; file mutations and dangerous operations require explicit approval. "Always allow" decisions persist as glob permission rules.
- **Two-phase plan mode**: read-only research first, then an implementation plan you approve before any code is written.
- **Diff review for every edit**: inline red/green diffs in the CLI, side-by-side in VS Code, or the native `vscode.diff` editor.
- **MCP / Hooks / Skills / sub-agents**: four extension mechanisms, including external tools via MCP.

#### Tips

1. Keep the approval gateway on and grant glob allow-rules only for paths you trust.
2. Use plan mode for non-trivial tasks — agree on the plan before the agent starts editing.
