[English](./anda_bot.md) | [简体中文](./anda_bot.zh-CN.md) · [← Back](../README.md)

# Integrate with Anda Bot

Anda Bot is an open-source Rust agent that runs in the terminal and can also connect to IM platforms such as WeChat, Feishu/Lark, Telegram, Discord, and IRC. Its core is a graph-based long-term memory system powered by Anda Hippocampus: it can learn useful knowledge from experience, recall relationships and timelines across sessions, run long-horizon reasoning tasks, use external tools including Claude Code and Codex, and coordinate work through a powerful subagents system.

#### 1. Install Anda Bot

Install the latest release with Homebrew:

```bash
brew install ldclabs/tap/anda
```

Or install with the one-line script:

```bash
curl -fsSL https://raw.githubusercontent.com/ldclabs/anda-bot/main/scripts/install.sh | sh
```

On Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/ldclabs/anda-bot/main/scripts/install.ps1 | iex
```

You can also run it from source with a recent Rust toolchain:

```bash
git clone https://github.com/ldclabs/anda-bot.git
cd anda-bot
cargo run -p anda_bot --
```

#### 2. Configure DeepSeek

Start Anda Bot once to create the default configuration file:

```bash
anda
```

Edit `~/.anda/config.yaml` and configure DeepSeek as the active provider:

```yaml
model:
  active: "deepseek-v4-pro"
  providers:
    - family: anthropic
      model: "deepseek-v4-pro"
      api_base: "https://api.deepseek.com/anthropic"
      api_key: "YOUR_API_KEY" # optional when DEEPSEEK_API_KEY is set
      labels: ["pro", "hippocampus"]
      disabled: false
```

You can also export the API key before launching Anda Bot:

```bash
export DEEPSEEK_API_KEY="YOUR_API_KEY"
```

The `hippocampus` label lets Anda Bot prefer this provider for memory formation and recall support.

#### 3. Start Using Anda Bot

Run the terminal UI:

```bash
anda
```

After editing `config.yaml`, use `/reload` in the terminal UI to reload the model configuration, or run `anda restart` to restart the agent.

To connect Anda Bot to chat platforms, configure `channels` in `~/.anda/config.yaml`. Supported channel families include IRC, Telegram, WeChat, Discord, and Lark/Feishu.
