[English](./octomind.md) | [简体中文](./octomind.zh-CN.md) · [← Back](../README.md)

# Integrate with Octomind

Octomind is an open-source (Apache-2.0) AI coding agent runtime written in Rust. It is CLI-first, ships as a single binary, works with any model, and is MCP-native. Its built-in `deepseek` provider calls the DeepSeek API directly and supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the 1M-token context window and the `max` reasoning effort.

- **GitHub:** <https://github.com/muvon/octomind>
- **Website:** <https://octomind.run>

#### 1. Install Octomind

- Run the following command in your terminal to install Octomind (Linux and macOS; on Windows, run it from Git Bash or MSYS2):

```bash
curl -fsSL https://raw.githubusercontent.com/muvon/octomind/master/install.sh | bash
```

- The script installs to `~/.local/bin/`. If the command is not found afterwards, add that directory to your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```bash
octomind --version
```

> **Note:** macOS users can also install via Homebrew: `brew install muvon/tap/octomind`.

#### 2. Configure DeepSeek Provider

Octomind selects models with `provider:model` strings, so the DeepSeek models are `deepseek:deepseek-v4-pro` and `deepseek:deepseek-v4-flash`. No base URL is needed: the built-in provider uses the official DeepSeek endpoint.

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Set the environment variable:

Linux / Mac users:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows users:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Generate the default configuration:

```bash
octomind config
```

Octomind merges every `*.toml` file in its config directory, so you can keep the DeepSeek settings in a separate file next to `config.toml`:

- **Linux / macOS**: `~/.local/share/octomind/config/deepseek.toml`
- **Windows**: `%LOCALAPPDATA%\octomind\config\deepseek.toml`

```toml
# Root keys must come before the first [table] header.
# Use the 1M-token context window (the default limit is 200,000 tokens).
max_session_tokens_threshold = 1000000

[model]
name = "deepseek:deepseek-v4-pro"
reasoning_effort = "max"

[supervisor.model]
name = "deepseek:deepseek-v4-flash"

[compression.model]
name = "deepseek:deepseek-v4-flash"
```

- `[model]` is the main agent. `reasoning_effort = "max"` is sent to DeepSeek as `reasoning_effort: "max"`; `"high"` is sent as `high`, and `"none"` switches thinking off.
- `[supervisor.model]` and `[compression.model]` default to `octohub:auto` (Octomind Cloud). Point them at DeepSeek as well so every request uses your DeepSeek key.
- Octomind caps the session at the model's 1M window minus the output reservation (`max_tokens` in `[model]`, 32,768 by default; DeepSeek V4 allows up to 384K output tokens).

Check the configuration:

```bash
octomind config --validate
```

#### 3. Run and Select Model

- Enter the project directory and start the `developer:general` coding agent (plain `octomind run` starts the general-purpose assistant instead). On first run, Octomind may install the agent's tools:

```bash
cd /path/to/my-project
octomind run developer:general
```

- Type `/model deepseek:deepseek-v4-flash` (or `/model deepseek:deepseek-v4-pro`) to switch models mid-session.
- Type `/effort max` (or `/effort high`) to change the reasoning effort for the current session.
- Type `/info` to see token usage and cost.

To use a different model for a single run without editing the config, pass `-m`:

```bash
octomind run -m deepseek:deepseek-v4-flash developer:general
```

> **Note:** The DeepSeek pricing page now lists the Flash model as `deepseek-flash` (DeepSeek-V4.1-Flash); the `deepseek-v4-flash` name is still accepted and billed at the Flash price. Octomind accepts both names.

For more configuration options, see the Octomind [providers guide](https://github.com/muvon/octomind/blob/master/doc/usage/04-providers.md) and [configuration reference](https://github.com/muvon/octomind/blob/master/doc/reference/03-config-reference.md).
