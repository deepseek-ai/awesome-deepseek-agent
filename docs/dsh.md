[English](./dsh.md) | [简体中文](./dsh.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Harness (dsh)

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) is DeepSeek's official open-source agent runtime — an "everything is a plugin" framework (built on Cordis) with `web` and `headless` profiles.

> 📚 New to dsh? The community handbook **dsh-handbook** (bilingual 中文/EN, 9 chapters + PDF) covers it from zero to plugin development: https://github.com/Electricitysheep/dsh-handbook

#### 1. Install

Requires Node.js ≥ 22.

```bash
# run directly (no install)
npx -y @deepseek-ai/dsh --version

# or global install
npm install -g @deepseek-ai/dsh
```

#### 2. Run and configure

**Web UI:**

```bash
dsh web   # → http://127.0.0.1:3080
```

**Headless (one-shot task, scripts/CI):**

```bash
dsh --profile headless "Hello, introduce yourself in one sentence"
```

**Set the DeepSeek model & API key** in `~/.dsh/settings.yaml`:

```yaml
agent-default-model:
  model: deepseek-v4-flash    # or deepseek-v4-pro
  reasoningEffort: high       # low / high / max
```

#### 3. Reasoning effort tiers

`low` (fastest, simple rounds) · `high` (default) · `max` (strongest, hard reasoning). Key insight: the model re-thinks before every tool call — lowering effort is the highest-leverage speedup for tool chains.

#### 4. Plugins

Everything is a plugin. Add a plugin in two steps (see [dsh-handbook ch.3](https://github.com/Electricitysheep/dsh-handbook)):

```yaml
# ~/.dsh/profiles/web/cordis.patch.yml
- insert:
    - id: <plugin-id>
      name: <npm-package>
```

Community plugins: [dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) (tool-call latency optimizer), [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) (file/terminal/git sidebar).
