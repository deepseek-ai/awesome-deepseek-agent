[English](./nika.md) · [← Back](../README.md)

# Integrate with Nika

Nika is an intent-as-code workflow engine in a single Rust binary (AGPL-3.0). Repeated AI work becomes a reviewable `.nika.yaml` DAG — statically checked (schema, permits, an honest cost floor) **before a single token is spent**, then executed budget-capped with a tamper-evident trace. DeepSeek is a first-class provider in the catalog.

#### 1. Install Nika

- macOS / Linux, via Homebrew:

```bash
brew install supernovae-st/tap/nika
```

- Or download a release tarball (with `SHA256SUMS` to verify) from [GitHub releases](https://github.com/supernovae-st/nika/releases/latest).
- Check the install:

```bash
nika --version
```

#### 2. Configure the DeepSeek provider

Nika reads the key from the environment — never from the workflow file:

```bash
export DEEPSEEK_API_KEY="sk-..."
nika doctor        # confirms: provider deepseek ready
```

#### 3. Author a workflow on DeepSeek

Models use the combined `provider/name` form. Save as `hello.nika.yaml`:

```yaml
# yaml-language-server: $schema=https://nika.sh/spec/v1/workflow.schema.json
nika: v1
workflow: hello-deepseek
model: deepseek/deepseek-chat

tasks:
  - id: hello
    infer:
      prompt: "Say hello in five words."
      max_tokens: 64        # the cost report becomes a hard ceiling
```

#### 4. Check, then run

```bash
nika check hello.nika.yaml   # audit: schema · permits · cost — zero tokens spent
nika run   hello.nika.yaml   # budget-capped run · tamper-evident trace
nika trace verify            # prove the trace afterwards
```

`nika check` is the point: an invalid workflow (wrong schema, undeclared secret flow, unbounded cost) never reaches the API.

#### More

- Docs: [docs.nika.sh](https://docs.nika.sh) · the full integrations map: [docs.nika.sh/integrations/everywhere](https://docs.nika.sh/integrations/everywhere)
- Agents author Nika too: `nika init` teaches Claude Code / Codex / Cursor the language, and `nika mcp` exposes a read-only validation oracle over MCP.
