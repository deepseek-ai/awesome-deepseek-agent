[English](./atomcode.md) | [简体中文](./atomcode.zh-CN.md) · [← Back](../README.md)

# Integrate with AtomCode

AtomCode is an open-source AI coding agent written in Rust that runs in your terminal. It connects to any OpenAI-compatible API, so wiring up DeepSeek only takes a few lines of config.

#### 1. Install AtomCode

- **Linux / macOS / WSL / Git-Bash**:

```bash
curl -fsSL https://raw.atomgit.com/atomgit_atomcode/atomcode/raw/main/scripts/install.sh | sh
```

- **Windows PowerShell**:

```powershell
irm https://raw.atomgit.com/atomgit_atomcode/atomcode/raw/main/scripts/install.ps1 | iex
```

- **npm** (any platform with Node.js):

```bash
npm install -g @atomgit.com/atomcode
```

- **Homebrew** (macOS / Linux):

```bash
brew install --cask atomcode
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```bash
atomcode --version
```

> **Note:** Do not run AtomCode with `sudo` — it keeps its config and sessions under `~/.atomcode`.

#### 2. Configure DeepSeek Provider

AtomCode's config lives at `~/.atomcode/config.toml`. Add DeepSeek as an OpenAI-compatible provider:

```toml
default_provider = "deepseek"

[providers.deepseek]
type           = "openai"
api_key        = "sk-..."
model          = "deepseek-v4-pro"
base_url       = "https://api.deepseek.com/v1"
context_window = 1000000
reasoning_effort = "max"
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

- `context_window = 1000000` — DeepSeek V4 models support up to 1 million tokens of context; set it explicitly so AtomCode's context windowing fits the full budget.
- `reasoning_effort = "max"` — DeepSeek-V4-Pro supports multiple reasoning effort levels; `max` gives the best coding experience. You can also switch at runtime with `/effort` (high / max / off) or `Ctrl+T`.

To run both models, declare a second provider and switch with `/model`:

```toml
[providers.deepseek-flash]
type           = "openai"
api_key        = "sk-..."
model          = "deepseek-v4-flash"
base_url       = "https://api.deepseek.com/v1"
context_window = 1000000
```

After editing the file by hand, run `/reload` inside AtomCode to pick up the changes without restarting.

#### 3. Run and Select Model

- Enter the project directory and execute the `atomcode` command:

```bash
cd /path/to/my-project
atomcode
```

- Press `F2` (or type `/model`) to open the model switcher.
- Select the **deepseek** provider and choose `deepseek-v4-pro` or `deepseek-v4-flash`.
- Start coding — or use headless mode for a single prompt: `atomcode -p "Explain the agent loop in this repo"`.
