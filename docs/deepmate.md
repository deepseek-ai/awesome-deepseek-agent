[English](./deepmate.md) | [简体中文](./deepmate.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with Deepmate

[Deepmate](https://github.com/kevin0x5/deepmate) is a local-first agent workbench for long-running project work. It provides cost-aware context management, governed skills, MCP servers and tools, task recovery, and self-evolution, with dedicated optimizations for DeepSeek V4.

## 1. Install Deepmate

Deepmate requires Python 3.11 or later.

```bash
python3 -m pip install --upgrade deepmate
```

Verify the installation and local environment:

```bash
deepmate --doctor
```

## 2. Configure a DeepSeek API key

Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/). Store it in an environment variable rather than a project file.

macOS or Linux:

```bash
export DEEPSEEK_API_KEY="<your-api-key>"
```

PowerShell:

```powershell
$env:DEEPSEEK_API_KEY = "<your-api-key>"
```

Deepmate reads the key at runtime and stores only the environment-variable reference in its generated configuration.

## 3. Start Deepmate in a project

Run Deepmate from the project directory you want it to work on:

```bash
cd /path/to/your/project
deepmate
```

On first launch, Deepmate creates its local configuration. The DeepSeek defaults use:

- `deepseek-v4-flash` for routine work;
- `deepseek-v4-pro` when a stronger model is requested;
- a 1,000,000-token context window.

Enter a task in the terminal interface. Deepmate can plan and execute long tasks, create checkpoints, resume interrupted work, and request approval for governed tool operations.

## 4. Use DeepSeek V4 Pro with maximum reasoning

You can select V4 Pro and maximum reasoning for a demanding one-shot task:

```bash
deepmate \
  --model deepseek-v4-pro \
  --thinking enabled \
  --reasoning-effort max \
  "Review this project and propose a safe migration plan."
```

The same model and reasoning options can be used when starting the interactive interface. For task-mode commands, configuration details, and troubleshooting, see the [Deepmate documentation](https://github.com/kevin0x5/deepmate#readme).
