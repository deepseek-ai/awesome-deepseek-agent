[English](./maxa.md) | [简体中文](./maxa.zh-CN.md) · [← Back](../README.md)

# Integrate with Maxa

[Maxa](https://github.com/maxzhao/maxa) is a free, open-source (Apache-2.0) AI workspace inside Neovim, with agentic coding, MCP tools, on-demand Abilities, and subagents. It connects directly to DeepSeek using your own API key. Maxa does not sell model access; API usage is billed separately by DeepSeek.

#### 1. Install Maxa

The published installer targets **WSL2 with Ubuntu 24.04**, on **x86_64 or aarch64**, using a normal user with sudo access. Maxa requires **Neovim 0.11+**; the installer prepares Neovim and the other dependencies.

> **Back up your existing Neovim configuration before installing.** The clone command below assumes `~/.config/nvim` does not already exist. Do not clone over an existing installation. Maxa runs tools with your user's operating-system permissions.

Clone the public repository, or fork it first and substitute your fork URL:

```bash
git clone https://github.com/maxzhao/maxa.git ~/.config/nvim
```

Review [the installer](https://github.com/maxzhao/maxa/blob/main/install.sh) before running it. It downloads dependencies, uses sudo to install system software, and configures Obsidian and Syncthing user services when systemd is available. Then run it inside the target WSL environment:

```bash
bash ~/.config/nvim/install.sh
```

On a fresh installation, create your local startup configuration from the published example:

```bash
cp ~/.config/nvim/lua/plugins/ai.example ~/.config/nvim/lua/plugins/ai.lua
```

**For an existing installation, keep your current `ai.lua` and merge the relevant settings instead of overwriting it.** See [Maxa's installation instructions](https://github.com/maxzhao/maxa#current-installation-path) for details.

#### 2. Configure DeepSeek

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). Set it in the shell from which you will start Neovim:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Alternatively, set `DEEPSEEK_API_KEY` locally in `~/.config/nvim/.env`, as described in Maxa's README. Do not commit your real API key.

The copied `ai.example` already includes a `deepseek` provider with:

- Base URL: `https://api.deepseek.com`.
- Protocol: `openai_responses`, using the official `/responses` endpoint.
- Models: `deepseek-flash` (the example's default) and `deepseek-v4-pro`.
- The DeepSeek-specific Responses extension, which handles thinking content and tool calls. Keep this extension configured.

In `lua/plugins/ai.lua`, update the existing `main` preset under `opts.maxa.presets` and enable the `model_limits` block under `opts.maxa`. **Merge these fields into the existing configuration; do not replace the whole file or discard your other presets/providers.** The example below selects Pro with maximum reasoning:

```lua
-- Inside opts.maxa
presets = {
  main = {
    type = "chat",
    adapter = "deepseek",
    model = "deepseek-v4-pro",
    thinking_mode = "max",
    visible = true,
  },
  -- Keep your other presets here.
},
model_limits = {
  model_overrides = {
    { pattern = "^deepseek%-", context_window = 1000000, max_output_tokens = 384000 },
  },
},
```

- **1M context:** both models support up to 1,000,000 tokens of context and up to 384,000 output tokens. Maxa's built-in context estimate for these models is 500,000; the override enables the full 1M budget for context reporting and token-threshold handling. Keep `max_output_tokens`, because an override replaces the built-in limits entry.
- **Maximum thinking:** `thinking_mode = "max"` becomes `reasoning.effort = "max"` in the Responses request. DeepSeek maps `xhigh` to `high`, not `max`; see the [Thinking Mode documentation](https://api-docs.deepseek.com/guides/thinking_mode). Do not disable thinking to work around a tool-call or reasoning-passback error; use an up-to-date Maxa version with its DeepSeek extension.
- **Flash:** to use Flash instead, change only `main.model` to `deepseek-flash`. The same context configuration applies. Pro does not support image input.

The published example sets `opts.maxa.defaults.chat = "main"`, so new chats use this preset. Other auxiliary presets can remain unchanged. Save the file and restart Neovim to load the configuration.

#### 3. First Run

Open Neovim from a project directory in WSL:

```bash
cd /path/to/your-project
nvim
```

1. Let the editor plugins finish installing on first startup. Run `:checkhealth maxa` to inspect core dependencies.
2. Run `:Maxa` to open a new Chat. With the configuration above, the default chat uses DeepSeek V4 Pro with maximum reasoning.
3. Ask Maxa to inspect the project and explain a function. Review the displayed tool results and response, then ask a follow-up question to continue the conversation.
4. Use `:MaxaHistory` to reopen saved conversations.

For existing installations, check any project or global chat-default overrides if a new Chat selects a different preset. See the [Maxa README](https://github.com/maxzhao/maxa) for provider and preset configuration.
