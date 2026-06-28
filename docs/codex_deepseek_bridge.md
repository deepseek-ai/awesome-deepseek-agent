[English](./codex_deepseek_bridge.md) | [简体中文](./codex_deepseek_bridge.zh-CN.md) · [← Back](../README.md)

# Run Codex App on DeepSeek

[Codex DeepSeek Bridge](https://github.com/JetXu-LLM/codex-deepseek-bridge) lets the official OpenAI Codex app use DeepSeek with one local setup command. You keep Codex Desktop, approvals, plugins, MCP servers, and tool workflows; the bridge sends model calls to DeepSeek.

- **One command sets it up** after download. No build step, and no Node.js runtime for the bridge binary.
- **No ChatGPT subscription needed.** Use your own DeepSeek API key.
- **Your key stays local.** It is never passed as a command-line argument, printed, or logged.
- **Your Codex stays your Codex.** Plugins and tools remain in Codex while DeepSeek handles the model call.
- **One command restores everything.** `restore` removes the managed Codex config block.

![Codex composer running deepseek-pro](./assets/codex_deepseek_bridge_composer.png)

#### 1. Quick Start

You need a DeepSeek API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and the Codex app on macOS or Windows. Copy the command for your platform, run it, paste your DeepSeek API key when asked, then restart Codex.

macOS Apple Silicon:

```sh
curl -L -o codex-deepseek-bridge-macos https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos
./codex-deepseek-bridge-macos setup
```

macOS Intel:

```sh
curl -L -o codex-deepseek-bridge-macos-x64 https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos-x64
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos-x64 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos-x64
./codex-deepseek-bridge-macos-x64 setup
```

Windows PowerShell:

```powershell
$ErrorActionPreference = "Stop"
$url = "https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-win-x64.exe"
$out = ".\codex-deepseek-bridge-win-x64.exe"
Remove-Item $out -ErrorAction SilentlyContinue
curl.exe -L --fail --progress-bar -o $out $url
if ($LASTEXITCODE -ne 0) { throw "Download failed." }
if ((Get-Item $out).Length -lt 10MB) { throw "Download looks incomplete. Run the commands again." }
& $out setup
```

When setup finishes, restart Codex. The app will use `deepseek-pro` by default.

#### 2. What setup does

`setup` writes one reversible block into Codex's `config.toml`, points Codex at a local bridge on `127.0.0.1`, starts the bridge, and maps Codex's default `deepseek-pro` model to `deepseek-v4-pro`.

It also backs up your existing Codex config. The DeepSeek key is read from the terminal prompt, `--from-stdin`, or `DEEPSEEK_API_KEY`; it is stored locally with owner-only permissions.

#### 3. Models and reasoning

The bridge uses stable Codex-facing model names and maps them to the current DeepSeek V4 models:

| Codex model | DeepSeek model | Notes |
|---|---|---|
| `deepseek-pro` | `deepseek-v4-pro` | Default coding model |
| `deepseek-flash` | `deepseek-v4-flash` | Fast model mapped by the bridge |

The local model metadata declares a 1M-token context window and `384000` max output tokens. Codex reasoning efforts map to DeepSeek thinking:

| Codex reasoning | DeepSeek behavior |
|---|---|
| `xhigh` / max | maximum thinking |
| `high` | high thinking |
| `none` | thinking off |

#### 4. Keep Codex tools and plugins

Codex still owns the app, approvals, workspace access, plugins, MCP servers, and tool execution. The bridge only translates the model protocol.

It handles Codex Responses tool calls, including function tools, namespace tools, and custom/freeform tools such as `apply_patch`, then returns DeepSeek tool calls in the shape Codex expects. Browser, Chrome, Computer Use, MCP, document workflows, and plugin-provided search tools can stay in the normal Codex workflow when they are available in your Codex environment.

Image input is off by default because DeepSeek's public API does not yet expose compatible multimodal input. The bridge already has a vision path, so future image-input support can use the same Codex-side workflow.

#### 5. See every call

Every request passes through the bridge. Open the local report to see latency, token usage, DeepSeek cache hits, and recent calls:

```sh
codex-deepseek-bridge report
```

If you used a downloaded binary that is not on your `PATH`, call it the same way you ran setup, for example `./codex-deepseek-bridge-macos report`.

![Codex DeepSeek Bridge report](./assets/codex_deepseek_bridge_report.png)

#### 6. Restore

To remove the managed Codex config block and stop the bridge:

```sh
codex-deepseek-bridge restore
```

To remove the stored key, logs, and local state as well:

```sh
codex-deepseek-bridge restore --purge
```

#### Optional: model labels in Codex Desktop

Current Codex Desktop builds may show `Custom` for local custom models even when the bridge is working. The default setup does not need to modify Codex Desktop; the bridge README describes an optional Desktop compatibility mode for users who specifically want both model labels in the picker.

![Codex Desktop picker with DeepSeek models](./assets/codex_deepseek_bridge_picker.jpg)
