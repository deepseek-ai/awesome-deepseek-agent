# DeepSkill with DeepSeek

[DeepSkill](https://github.com/12UE/deepskill) is an open-source `AGENTS.md` skill file that installs five core engineering disciplines into AI coding assistants, optimized for DeepSeek V4 Pro.

## Setup

### 1. Get the AGENTS.md file

```bash
git clone https://github.com/12UE/deepskill.git
```

Or download `AGENTS.md` directly from the [repository](https://github.com/12UE/deepskill).

### 2. Install globally (all projects)

```bash
# Linux / macOS
cp AGENTS.md ~/AGENTS.md

# Windows
copy AGENTS.md %USERPROFILE%\AGENTS.md
```

### 3. Install per-project

```bash
cp AGENTS.md /path/to/your/project/AGENTS.md
```

## What it does

DeepSkill injects five engineering disciplines into the system prompt:

1. **Risk Analysis** - Think before you code. Assess impact before making changes.
2. **Self-Verification** - Verify every change with tools (grep), not memory.
3. **Precision Operations** - Prefer accuracy over speed in batch modifications.
4. **Environment Awareness** - Always confirm the build environment before writing code.
5. **Completeness Assurance** - Fix all instances of a problem in one pass.

## Core Principle

> **Think -> Do once -> Verify -> Done**

## Compatible Tools

Works with any AI coding tool that supports `AGENTS.md` system prompts, including opencode, Cursor, and others.