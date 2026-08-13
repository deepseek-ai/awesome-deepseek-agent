[English](./kimi_code.md) | [简体中文](./kimi_code.zh-CN.md) · [← Back](../README.md)

# Integrate with Kimi Code

Kimi Code is an open-source terminal AI agent developed by Moonshot AI.

- **GitHub:** <https://github.com/MoonshotAI/kimi-code>
- **Docs:** <https://moonshotai.github.io/kimi-code/en/>

#### 1. Install Kimi Code

Run the official installation script for your platform.

Linux / macOS:

```shell
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

Alternatively, install Kimi Code with npm. This requires Node.js 22.19.0 or later:

```shell
npm install -g @moonshot-ai/kimi-code
```

Confirm the installation:

```shell
kimi --version
```

#### 2. Get a DeepSeek API Key

Create and copy an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeek

Create or edit Kimi Code's configuration file:

- Linux / macOS: `~/.kimi-code/config.toml`
- Windows: `C:\Users\<name>\.kimi-code\config.toml`

If the file already contains other settings, merge the following blocks into it instead of replacing the entire file. Replace `YOUR_DEEPSEEK_API_KEY` with your DeepSeek API key:

```toml
default_model = "deepseek-v4-pro"

[thinking]
enabled = true
effort = "max"
keep = "all"

[providers.deepseek]
type = "openai"
base_url = "https://api.deepseek.com"
api_key = "YOUR_DEEPSEEK_API_KEY"

[models.deepseek-v4-pro]
provider = "deepseek"
model = "deepseek-v4-pro"
display_name = "DeepSeek V4 Pro"
max_context_size = 1000000
capabilities = ["always_thinking", "tool_use"]
support_efforts = ["high", "max"]
default_effort = "max"

[models.deepseek-v4-flash]
provider = "deepseek"
model = "deepseek-v4-flash"
display_name = "DeepSeek V4 Flash"
max_context_size = 1000000
capabilities = ["always_thinking", "tool_use"]
support_efforts = ["high", "max"]
default_effort = "max"
```

This configuration adds DeepSeek V4 Pro and DeepSeek V4 Flash with their 1-million-token context window, enables tool use and Thinking mode, and selects DeepSeek V4 Pro with `max` reasoning effort by default.

Kimi Code's OpenAI-compatible provider automatically preserves DeepSeek's `reasoning_content` across tool-call turns. This keeps Thinking mode working during multi-step agent tasks.

#### 4. Validate the Configuration

Validate the configuration without starting the TUI:

```shell
kimi doctor config
```

If the file is valid, Kimi Code reports that `config.toml` is OK.

#### 5. Start Kimi Code

Enter a project directory and launch Kimi Code:

```shell
cd /path/to/your-project
kimi
```

Kimi Code now uses DeepSeek V4 Pro by default. Type `/model` in the interactive session to switch between DeepSeek V4 Pro and DeepSeek V4 Flash.

To run a one-shot task without opening the interactive TUI:

```shell
kimi -p "Inspect this project's top-level files and summarize what the project does."
```

#### Troubleshooting

- `401` or authentication errors: confirm that `api_key` contains a valid DeepSeek API key.
- `402` or insufficient balance: check your DeepSeek Platform balance.
- `404` or model not found: confirm that the model ID is exactly `deepseek-v4-pro` or `deepseek-v4-flash`.
- `No model configured`: make sure `default_model` matches a key under `[models]`, then run `kimi doctor config`.
