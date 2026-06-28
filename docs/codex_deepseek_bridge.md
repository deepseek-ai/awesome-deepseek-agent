[English](./codex_deepseek_bridge.md) | [简体中文](./codex_deepseek_bridge.zh-CN.md) · [← Back](../README.md)

# Integrate with Codex DeepSeek Bridge

[Codex DeepSeek Bridge](https://github.com/JetXu-LLM/codex-deepseek-bridge) is a small local bridge for running the OpenAI Codex app or CLI with DeepSeek. Codex keeps using its native Responses API workflow, while the bridge translates model calls to DeepSeek's Chat Completions API.

- **GitHub:** <https://github.com/JetXu-LLM/codex-deepseek-bridge>

The bridge uses stable Codex-facing model names (`deepseek-pro` and `deepseek-flash`), maps them to the current DeepSeek models (`deepseek-v4-pro` and `deepseek-v4-flash`), and keeps the DeepSeek API key on your machine.

#### 1. Install Codex and the bridge

Install the [Codex app](https://developers.openai.com/codex/) or Codex CLI first. For CLI usage:

```sh
npm install -g @openai/codex
codex --version
```

Then download a bridge binary. Node.js is not required for the bridge binary.

macOS Apple Silicon:

```sh
curl -L -o codex-deepseek-bridge-macos https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos
./codex-deepseek-bridge-macos --version
```

macOS Intel:

```sh
curl -L -o codex-deepseek-bridge-macos-x64 https://github.com/JetXu-LLM/codex-deepseek-bridge/releases/latest/download/codex-deepseek-bridge-macos-x64
xattr -d com.apple.quarantine ./codex-deepseek-bridge-macos-x64 2>/dev/null || true
chmod +x ./codex-deepseek-bridge-macos-x64
./codex-deepseek-bridge-macos-x64 --version
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
& $out --version
```

#### 2. Get a DeepSeek API Key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Do not pass the key as a command-line argument. The bridge reads it from an interactive prompt, `--from-stdin`, or `DEEPSEEK_API_KEY`, and stores it locally with owner-only file permissions.

#### 3. Run setup

Run `setup` with the binary you downloaded:

macOS:

```sh
./codex-deepseek-bridge-macos setup
```

Windows PowerShell:

```powershell
.\codex-deepseek-bridge-win-x64.exe setup
```

Setup does the following:

- backs up the existing Codex `config.toml`;
- writes one managed Codex provider block pointing to `127.0.0.1`;
- starts the local bridge;
- publishes `deepseek-pro` for Codex by default;
- maps `deepseek-pro` to `deepseek-v4-pro`.

Restart Codex after setup completes.

#### 4. Use Codex with DeepSeek

Open the Codex app, or start Codex CLI inside a project:

```sh
cd /path/to/my-project
codex
```

Codex now sends Responses API requests to the local bridge, and the bridge sends DeepSeek-compatible requests to `deepseek-v4-pro`.

![Codex composer running deepseek-pro](./assets/codex_deepseek_bridge_composer.png)

DeepSeek V4 metadata is written into Codex's local model catalog:

| Codex model | Upstream DeepSeek model | Notes |
|---|---|---|
| `deepseek-pro` | `deepseek-v4-pro` | Default coding model |
| `deepseek-flash` | `deepseek-v4-flash` | Fast model, mapped by the bridge |

The model catalog declares a 1M-token context window and `384000` max output tokens. Reasoning effort maps through to DeepSeek thinking:

| Codex reasoning | DeepSeek behavior |
|---|---|
| `xhigh` / max | maximum thinking |
| `high` | high thinking |
| `none` | thinking off |

#### 5. Keep Codex tools and plugins

Codex still owns the app, approvals, workspace access, plugins, MCP servers, and tool execution. The bridge only translates the model protocol.

It handles Codex Responses tool calls, including function tools, namespace tools, and custom/freeform tools such as `apply_patch`, then returns DeepSeek tool calls back in the shape Codex expects. This lets Codex-side tools such as Browser, Chrome, Computer Use, MCP, document workflows, and plugin-provided search tools stay in the normal Codex workflow while DeepSeek handles the model call.

Image input is off by default because DeepSeek's public API does not yet expose compatible multimodal input. The bridge already has a vision path, so when DeepSeek supports image input, image-dependent plugin flows can be enabled without changing the Codex-side workflow.

#### 6. Verify and view the local report

Check the bridge health:

```sh
./codex-deepseek-bridge-macos doctor
```

If the bridge binary is on your `PATH`, you can use:

```sh
codex-deepseek-bridge doctor
```

Open the local report:

```sh
codex-deepseek-bridge report
```

The report is served from `127.0.0.1`, is read-only, and shows requests, latency, token usage, DeepSeek cache hits, and recent calls.

![Codex DeepSeek Bridge report](./assets/codex_deepseek_bridge_report.png)

#### Optional: show both model labels in Codex Desktop

Current Codex Desktop builds may show `Custom` for local custom models even when the bridge is working. The default setup does not need to modify Codex Desktop.

If you specifically want both `deepseek-pro` and `deepseek-flash` to appear with their labels in the Desktop model picker, read the bridge README and use the optional Desktop compatibility mode only if you accept the local app-bundle change.

![Codex Desktop picker with DeepSeek models](./assets/codex_deepseek_bridge_picker.jpg)

#### Restore

To undo the setup:

```sh
codex-deepseek-bridge restore
```

`restore` removes the managed Codex config block and stops the bridge. To remove the stored key, logs, and local state as well:

```sh
codex-deepseek-bridge restore --purge
```
