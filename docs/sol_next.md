[English](./sol_next.md) | [简体中文](./sol_next.zh-CN.md) · [← Back](../README.md)

# Integrate with Sol Next

[Sol Next](https://github.com/chongyangzhang92-hub/Sol-Next) is an independent, open-source (Apache-2.0) Android 10–16/17 & HarmonyOS multimodal AI mobile OS agent with a pure-Rust 16KB JNI kernel, 1:1 physical-DPI background VirtualDisplay (`0.0px` tap drift), 20-language phone-language auto-localization, Wi-Fi-off persistent wireless debugging, and a zero-dependency stdio MCP Server.

Sol Next works out of the box with built-in encrypted `deepseek-v4-flash` and supports full BYOK (Bring Your Own Key) configuration for `deepseek-v4-pro` and `deepseek-v4-flash` with their **1M token context window** and `max` / `high` reasoning effort.

#### 1. Install Sol Next

Download the latest `v9.0.4-public` APK (`ARM64` recommended, or `Universal`) from [GitHub Releases](https://github.com/chongyangzhang92-hub/Sol-Next/releases/tag/v9.0.4-public) or install over ADB using the bundled zero-dependency CLI:

```bash
python3 scripts/sol-cli.py install --abi arm64 --verify-sha256 --grant-permissions
```

#### 2. Configure DeepSeek V4 (BYOK)

Sol Next ships with free built-in encrypted `deepseek-v4-flash` so you can test immediately after install. To connect your own DeepSeek API key and unlock `deepseek-v4-pro` (with 1M context window & `max` reasoning effort):

1. Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. Open **Sol Next** on your Android or HarmonyOS device and go to **Settings › Model API Configuration (BYOK)**.
3. Configure the OpenAI-compatible DeepSeek endpoint:
   - **API Base URL**: `https://api.deepseek.com/v1`
   - **Model ID**: `deepseek-v4-pro` (for complex multi-app planning with `max` reasoning effort) or `deepseek-v4-flash` (for ultra-fast low-latency daily phone actions)
   - **API Key**: your DeepSeek API key (`sk-...`)
4. DeepSeek V4 models support up to a **1,000,000-token (1M) context window** (`max_tokens` up to `384000` where supported) and multi-level `reasoning_effort` (`max` / `high`), allowing Sol Next to retain long multi-step UI histories and screen context across complex phone workflows without truncating prior steps.

#### 3. First Run (Voice, Text, or MCP)

- **On-Device Voice / Text**: Tap the Dawn Orbit voice orb or type a natural-language task (e.g., compare prices across shopping apps, summarize messages, or schedule a calendar event). Sol Next executes in a 1:1 background VirtualDisplay without interrupting your foreground screen, while guarding payments and sensitive actions with explicit user confirmation.
- **Connect via MCP (Claude Code / Cursor / Codex)**:
  ```json
  {
    "mcpServers": {
      "sol-next": {
        "command": "python3",
        "args": ["/path/to/Sol-Next/mcp/sol_mcp_server.py"]
      }
    }
  }
  ```

For full documentation, SHA-256 verification, and 20-language guides, see the [Sol Next repository](https://github.com/chongyangzhang92-hub/Sol-Next) and [project website](https://chongyangzhang92-hub.github.io/Sol-Next/).
