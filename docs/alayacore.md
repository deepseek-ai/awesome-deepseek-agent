[English](./alayacore.md) | [简体中文](./alayacore.zh-CN.md) · [← Back](../README.md)

# Integrate with AlayaCore

AlayaCore is a fast, minimal AI Agent that runs in your terminal. It connects to any OpenAI-compatible or Anthropic-compatible LLM and gives it the tools to read, write, and edit files, and execute commands — with streaming output, session persistence, and multi-step agentic tool-calling loops, available in both an interactive TUI and a plain mode for scripting and piping.

AlayaCore is super tiny (~8MB static linked binary) with zero runtime dependencies — no Node.js, no Python, not even libc. This means no libc incompatibility issues, which is a common problem on Linux.

- **GitHub:** <https://github.com/alayacore/alayacore>

#### 1. Install AlayaCore

**Option A: Download from GitHub Releases**

Download the latest binary for your platform from the [GitHub Releases page](https://github.com/alayacore/alayacore/releases).

**Option B: Build with Go**

- Install [Go](https://go.dev/dl/) 1.26.1+.
- Run:

```sh
go install github.com/alayacore/alayacore@latest
```

#### 2. Get a DeepSeek API Key

- Go to <https://platform.deepseek.com/> → sign up / sign in → **API Keys** → **Create API Key**.

#### 3. Configure DeepSeek

AlayaCore stores its configuration in `~/.alayacore/model.conf`. On first run, it creates a default configuration for Ollama. You need to edit it to add DeepSeek.

Press `Ctrl+L` then `e` in the terminal to open the config file in your editor, or edit it directly:

```sh
# Open the config file
$EDITOR ~/.alayacore/model.conf
```

Add the following configuration (replace `YOUR_DEEPSEEK_API_KEY` with your actual key):

```
name: "DeepSeek V4 Pro"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-pro"
context_limit: 1000000
```

For DeepSeek V4 Flash (faster, cheaper):

```
name: "DeepSeek V4 Flash"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-flash"
context_limit: 1000000
```

You can also configure multiple models in one file, separated by `---`:

```
name: "DeepSeek V4 Pro"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-pro"
context_limit: 1000000
---
name: "DeepSeek V4 Flash"
protocol_type: "openai"
base_url: "https://api.deepseek.com/v1"
api_key: "YOUR_DEEPSEEK_API_KEY"
model_name: "deepseek-v4-flash"
context_limit: 1000000
```

#### 4. Start Using AlayaCore

- Run `alayacore` in your terminal.
- Press `Ctrl+L` to open the model selector and choose your DeepSeek model.
- Type a prompt and press `Enter` to start a conversation.

#### Plain IO Mode

Use `--plainio` for scripting and piping without the TUI:

```sh
# Pipe a prompt from stdin
echo "Explain what this project does" | alayacore --plainio

# Read a prompt from a file
alayacore --plainio < myplan.txt
```

## Tips

- **Model switching:** Press `Ctrl+L` to switch between models at runtime.
- **Session persistence:** Use `:save my-session.md` or press `Ctrl+S` to save your conversation.
- **Skills system:** Extend AlayaCore with custom skill packages using the `--skill` flag.
- **Plain IO mode:** Use `--plainio` for scripting and piping without the TUI.

## Resources

- [AlayaCore Documentation](https://github.com/alayacore/alayacore/tree/main/docs)
- [DeepSeek Platform](https://platform.deepseek.com/) — get an API key.
- [DeepSeek API Docs](https://api-docs.deepseek.com/) — API reference and guides.
