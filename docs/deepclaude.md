[English](./deepclaude.md) | [简体中文](./deepclaude.zh-CN.md) · [← Back](../README.md)

# Integrate with deepclaude

deepclaude is a thin launcher that runs [Claude Code](https://github.com/anthropics/claude-code)'s autonomous agent loop against **DeepSeek V4 Pro** (or any Anthropic-compatible backend) instead of Anthropic — same UX, a fraction of the cost. It is a single shell/PowerShell script plus a local proxy, with no separate runtime to maintain.

- **GitHub:** <https://github.com/aattaran/deepclaude>

#### 1. Get a DeepSeek API Key

Sign up at the [DeepSeek Platform](https://platform.deepseek.com/api_keys), add credit, and copy your API key.

#### 2. Set the environment variable

**macOS / Linux:**

```bash
echo 'export DEEPSEEK_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**

```powershell
setx DEEPSEEK_API_KEY "sk-your-key-here"
```

#### 3. Install deepclaude

Clone the repo and put the launcher on your `PATH`:

```sh
git clone https://github.com/aattaran/deepclaude.git
cd deepclaude
```

**macOS / Linux:**

```bash
chmod +x deepclaude.sh
sudo ln -s "$(pwd)/deepclaude.sh" /usr/local/bin/deepclaude
```

**Windows (PowerShell):**

```powershell
# Copy the script to a directory already in your PATH, or add the repo dir to PATH
Copy-Item deepclaude.ps1 "$env:USERPROFILE\.local\bin\deepclaude.ps1"
```

#### 4. First run

From any project directory:

```sh
deepclaude
```

This launches Claude Code routed through DeepSeek V4 Pro. Other useful flags:

```sh
deepclaude --status        # Show available backends and keys
deepclaude --backend or    # Use OpenRouter (cheapest)
deepclaude --backend fw    # Use Fireworks AI (fastest)
deepclaude --backend anthropic  # Normal Claude Code (when you need Opus)
deepclaude --cost          # Show pricing comparison
deepclaude --benchmark     # Latency test across providers
```

deepclaude also exposes an OpenAI-compatible proxy (`/v1/chat/completions`) so other tools can reach DeepSeek V4 Pro through the same key — see the repo README for the proxy details.
