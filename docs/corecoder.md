[English](./corecoder.md) | [简体中文](./corecoder.zh-CN.md) · [← Back](../README.md)

# Integrate with CoreCoder

[CoreCoder](https://github.com/he-yufeng/CoreCoder) is a minimal, fully readable coding-agent engine: about 1.3k lines of engine code inside a ~2.8k-line pure-Python package that you can read end to end in an afternoon, then fork into your own. It reads and writes files, runs shell commands, spawns sub-agents, compacts context in three tiers, and asks for your consent before any tool call that would touch your disk.

#### 1. Install CoreCoder

Requires Python 3.10 or later.

```bash
pip install corecoder
```

Or install from source if you plan to read and modify it (the recommended path for this project):

```bash
git clone https://github.com/he-yufeng/CoreCoder
cd CoreCoder
pip install -e .
```

#### 2. Configure DeepSeek

CoreCoder speaks the OpenAI-compatible API, so DeepSeek works out of the box. Export three variables (or drop them into a `.env` file at the project root, which is loaded on startup):

```bash
export OPENAI_API_KEY=sk-...        # from https://platform.deepseek.com/api_keys
export OPENAI_BASE_URL=https://api.deepseek.com
export CORECODER_MODEL=deepseek-v4-pro
```

`DEEPSEEK_API_KEY` is accepted in place of `OPENAI_API_KEY` if you prefer.

DeepSeek V4 supports up to 1M tokens of context. CoreCoder's context budget defaults to 128k tokens with three-tier compaction; to take advantage of the full window, raise it:

```bash
export CORECODER_MAX_CONTEXT=1000000
export CORECODER_MAX_TOKENS=384000
```

Thinking is first-class in CoreCoder: the chain-of-thought carried in DeepSeek's `reasoning_content` field streams dimmed while the model works and is never sent back into the conversation history, so providers never see it come back. CoreCoder does not currently send a `reasoning_effort` parameter, so the provider's default effort level applies.

#### 3. Get Started

Run CoreCoder in your project directory:

```bash
corecoder
```

Start with a read-only task like `read main.py and explain the entry point`, then one that edits: `add a --version flag to the CLI`. Anything that would mutate files or execute commands pauses for your approval first. For one-shot scripts, `corecoder -p "..."` refuses mutating tools unless you pass `--yes`.

Once it runs, the repo's eight-essay source-reading series walks the engine line by line ([English](https://github.com/he-yufeng/CoreCoder/blob/main/article/00-index_EN.md) / [中文](https://github.com/he-yufeng/CoreCoder/blob/main/article/00-index.md)) — the third essay covers the provider layer this configuration just exercised.
