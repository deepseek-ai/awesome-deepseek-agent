[English](./cursor.md) | [简体中文](./cursor.zh-CN.md) · [↩ Back](../README.md)

# Integrate with Cursor

Cursor does not natively handle DeepSeek thinking-mode tool calls correctly, so the recommended setup is to place a compatibility proxy in front of the DeepSeek API. A practical reference implementation is [deepseek-cursor-proxy](https://github.com/yxlao/deepseek-cursor-proxy).

#### 1. Prepare ngrok

Cursor custom providers require a public HTTPS endpoint, so `localhost` is usually not enough. The easiest option is [ngrok](https://ngrok.com/).

- First create an ngrok account.
- Then install ngrok.
- Finally add your authtoken once.

The flow below is the clearest way to set it up.

**Step 1: Install ngrok**

On Windows, it is better to download the zip package from the official site instead of using a command-line installer:

1. Open the [ngrok Windows download page](https://ngrok.com/download/windows).
2. Click `Download` and download the Windows zip package.
3. Extract it and place `ngrok.exe` in a fixed folder such as `D:\\tools\\ngrok\\`.

On macOS, you can install it with Homebrew:

```bash
brew install ngrok
```

If you already use another tunnel service such as Cloudflare Tunnel, you can use that instead.

**Step 2: Add your authtoken**

Open the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) and copy your authtoken, then run the setup command once.

Windows example:

```bash
cd D:\tools\ngrok
.\ngrok.exe config add-authtoken <your-ngrok-token>
```

On macOS, or anywhere `ngrok` is already in your PATH, you can run:

```bash
ngrok config add-authtoken <your-ngrok-token>
```

**Step 3: Optional connectivity test**

If you want to confirm ngrok is working before setting up the proxy, you can do a quick HTTP connectivity test:

```bash
# Terminal 1: start any local test server on port 8080
python -m http.server 8080

# Terminal 2: expose port 8080 publicly
ngrok http 8080
```

When ngrok prints a public URL such as `https://xxxx.ngrok-free.app`, open it in your browser. If you can see the directory listing or the default `python -m http.server` page, ngrok is working.

This step is only a temporary ngrok test, not the final proxy URL for Cursor. After testing, stop both processes, especially `ngrok http 8080`, with `Ctrl+C`. `deepseek-cursor-proxy` will later start its own local port and, when ngrok is enabled, create the correct tunnel automatically. If you leave the 8080 test tunnel running, it becomes easy to copy the wrong URL into Cursor.

#### 2. Clone and Start the Proxy

If you already have `uv` on your machine, it is the recommended way to run the proxy because it is the simplest setup:

```bash
git clone https://github.com/yxlao/deepseek-cursor-proxy.git
cd deepseek-cursor-proxy
uv run deepseek-cursor-proxy
```

If you do not have `uv`, you can install it into a Python environment first:

```bash
git clone https://github.com/yxlao/deepseek-cursor-proxy.git
cd deepseek-cursor-proxy
pip install -e .
deepseek-cursor-proxy
```

On first run, the proxy creates:

- `~/.deepseek-cursor-proxy/config.yaml`
- `~/.deepseek-cursor-proxy/reasoning_content.sqlite3`

When ngrok is enabled, the proxy prints a public HTTPS URL that Cursor can use. When you fill in the Base URL in Cursor, use the URL printed by `deepseek-cursor-proxy`, not the temporary URL from the earlier `ngrok http 8080` connectivity test.

#### 3. Add a Custom Model in Cursor

Open Cursor settings and add a custom OpenAI-compatible model:

- Model: `deepseek-v4-pro` or `deepseek-v4-flash`
- API Key: your DeepSeek API key
- Base URL: your tunnel URL with the `/v1` suffix

For example:

```text
https://example.ngrok-free.dev/v1
```

The proxy forwards the model name that Cursor sends, so you can switch between `deepseek-v4-pro` and `deepseek-v4-flash` directly in Cursor.

#### 4. Start Chatting in Cursor

Select the custom DeepSeek model in Cursor and use chat or agent mode as usual.

The proxy mainly solves the DeepSeek thinking-mode tool-call issue by restoring the required `reasoning_content` field that Cursor does not send back. It can also surface thinking traces inside Cursor and improve compatibility for tool usage.

#### Optional Flags

Useful startup options from the reference proxy:

```bash
# Hide thinking traces in Cursor
deepseek-cursor-proxy --no-display-reasoning

# Print verbose request logs
deepseek-cursor-proxy --verbose

# Use a custom local port
deepseek-cursor-proxy --port 9000

# Disable ngrok and run locally only
deepseek-cursor-proxy --no-ngrok
```

<div align="center">
<img src="https://raw.githubusercontent.com/yxlao/deepseek-cursor-proxy/main/assets/cursor_config.png" width='900' border='1' />
</div>
