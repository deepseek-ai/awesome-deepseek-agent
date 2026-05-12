# Contributing to awesome-deepseek-agent

Thanks for helping build the community knowledge base for DeepSeek integrations!

## Before You Start

- Check [open PRs](https://github.com/deepseek-ai/awesome-deepseek-agent/pulls) to avoid duplicating existing work.
- If you're fixing or extending an existing guide (e.g., Claude Code, Pi), check whether there's already an open PR touching the same files.
- Read the [DeepSeek API docs](https://api-docs.deepseek.com/) — guides must reflect the current API, not outdated configurations.

## What Makes a Good Integration Guide

Each guide should walk through **installation → configuration → first run** for a specific tool. Follow the format of existing guides in `docs/`.

### Required: Bilingual

Every guide must include both an English version (`docs/tool_name.md`) and a Simplified Chinese version (`docs/tool_name.zh-CN.md`). Submit them in a single PR — do not split into two PRs.

### Required: README Table Entry

Add your guide to the tools table in **both** `README.md` and `README.zh-CN.md`. Insert the entry in **alphabetical order** within the table rather than appending to the end. This prevents merge conflicts with other PRs.

## 🔴 Critical Checks

Before submitting, verify these items. PRs missing any of them will be flagged during review.

### 1. Model Naming

```
❌ deepseek-chat / deepseek-reasoner / deepseek-coder   (V3, deprecated)
✅ deepseek-v4-pro / deepseek-v4-flash                   (current)
```

DeepSeek renamed its models in April 2026. All code examples, config snippets, and prose must use the current names. Search your diff for `deepseek-chat` — if you find it, fix it.

### 2. 1M Context Window

DeepSeek V4 models support up to **1 million tokens** of context. Make sure your configuration reflects this:

- **Claude Code / Anthropic-compatible**: append `[1m]` to model names, e.g. `deepseek-v4-pro[1m]`
- **OpenAI-compatible configs**: set `context_window: 1000000` / `max_tokens: 384000` where the tool supports it
- **Other tools**: at minimum, note in prose that DeepSeek V4 supports 1M context

If the tool doesn't expose a context window config, mention it in the description so users are aware.

### 3. Max Thinking / Reasoning Effort

DeepSeek V4 Pro supports multiple reasoning effort levels (`max` and `high`). Your guide should be compatible with the `max` level so users get the best coding experience. See [Thinking Mode docs](https://api-docs.deepseek.com/guides/thinking_mode) for details.

- **Claude Code**: `CLAUDE_CODE_EFFORT_LEVEL=max` (or equivalent `settings.json` config)
- **Anthropic-compatible endpoint**: set `thinking: { type: "enabled" }` with max budget
- **OpenAI-compatible endpoint**: include `reasoning_effort` in the request body where the tool supports it

Don't recommend disabling thinking mode as the primary workaround for API errors. If the tool has a reasoning-content passback bug, point users to the upstream fix rather than advising them to degrade model performance.

### 4. Pricing (if included)

If your guide includes pricing tables, always verify the numbers against the official DeepSeek pricing pages ([English](https://api-docs.deepseek.com/quick_start/pricing) / [中文](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)). The pricing below is a snapshot for reference only — use the latest values from the API docs:

| Model | Input / M tokens | Output / M tokens | Cache Hit / M tokens |
|-------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

## Common Pitfalls

### Don't document workarounds for upstream bugs

If the tool you're documenting has a known bug with DeepSeek (e.g., reasoning content passback errors), check whether the upstream project has already fixed it **before** writing a workaround guide. A documented workaround that degrades model performance is worse than pointing users to the upstream fix.

### Ensure config fields take effect in the agent

Only document configuration options that actually exist and have been verified to work in the tool. If you're unsure whether a config key is effective, test it first.

### Keep it one PR per guide

One tool = one PR. Don't split the English and Chinese versions into separate PRs. Don't combine two unrelated tools in one PR unless they share a common dependency (e.g., a proxy server that serves multiple tools).

### Images

Place screenshots in `docs/assets/`. Use descriptive filenames, keep file sizes reasonable, and verify that images render correctly in both the English and Chinese versions.

## Review Process

A maintainer or community reviewer will check:

### Agent Configuration

- [ ] Model names are current (v4-pro / v4-flash, not v3 names)
- [ ] 1M context is configured or mentioned
- [ ] Max thinking effort level is supported
- [ ] Pricing is current (input, output, cache hit), verified against [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing)
- [ ] Config fields are verified to work in the agent
- [ ] No workarounds for already-fixed upstream bugs

### Documentation

- [ ] Both English and Chinese versions included in a single PR
- [ ] README table entry inserted in alphabetical order
- [ ] One tool per PR; unrelated tools not combined
- [ ] Images placed in `docs/assets/` with descriptive filenames and reasonable sizes

Thank you for contributing! 🐋
