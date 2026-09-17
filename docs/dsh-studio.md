[English](./dsh-studio.md) | [简体中文](./dsh-studio.zh-CN.md) · [← Back](../README.md)

# Use DeepSeek with DSH Studio

[DSH Studio](https://github.com/Moresyl/dsh-studio) is an MIT-licensed cross-platform desktop shell for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It installs the upstream harness into an app-private npm prefix, supervises the local service, and hosts the unmodified Harness Web UI.

- **GitHub:** <https://github.com/Moresyl/dsh-studio>
- **Releases:** <https://github.com/Moresyl/dsh-studio/releases>

## 1. Install DSH Studio

DSH Studio currently requires Node.js 20 or newer. Download the current release for your platform:

| Platform | Package |
| --- | --- |
| Windows x64 | `.exe` (NSIS) or `.msi` |
| macOS Apple Silicon / Intel | `.dmg` |
| Linux x64 | `.AppImage`, `.deb`, or `.rpm` |

The macOS builds are not yet signed or notarized. On first launch, approve the application in **System Settings → Privacy & Security**.

You can also build from source:

```sh
git clone https://github.com/Moresyl/dsh-studio.git
cd dsh-studio
pnpm install
pnpm tauri build
```

## 2. Start DeepSeek Harness

Launch DSH Studio. It detects installed Node.js runtimes and checks for `@deepseek-ai/dsh`.

If the harness is missing, select **Install DeepSeek Harness**. DSH Studio installs it into a private prefix in the app data directory rather than changing the global npm root. After installation, start the service and wait for the Harness Web UI to appear in the same window.

The desktop shell chooses an unused loopback port, monitors the service with HTTP health checks, and restarts it with backoff if it becomes unresponsive. It does not fork or modify the upstream Harness UI.

## 3. Configure the DeepSeek provider

In the embedded Harness Web UI:

1. Open **Settings → Models**.
2. Find the **DeepSeek** card.
3. Paste a key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
4. Save the provider.

The key is write-only in the UI and is stored by Harness in its credential store. The model route becomes available immediately; no service restart is required.

The official Harness adapter advertises these models by default:

| Model ID | Suggested use |
| --- | --- |
| `deepseek-v4-pro` | Coding, long-running reasoning, and difficult agent tasks |
| `deepseek-v4-flash` | Lower-latency everyday tasks |

Both default entries use a **1,000,000-token context window**. The adapter enables thinking by default and supports `high` and `max` reasoning effort. Use `max` for difficult coding and multi-step tasks; do not disable thinking as a workaround for provider errors.

## 4. Choose a workspace and run the first task

1. Select a DeepSeek V4 model in the model picker. The selection becomes the default for new sessions.
2. Select **Choose workspace**, add a local project directory, and choose it.
3. Start a new session.
4. Send a task such as:

> Summarize this repository, identify its main packages, and suggest one small verified improvement.

Harness can read and edit workspace files, run commands, delegate work, and maintain a plan. It requests approval for operations that require it under the active permission policy.

## Troubleshooting

- **Harness is not installed** — use the install action in DSH Studio and review the streamed npm output.
- **Node.js is not detected** — install Node.js 20 or newer, then restart DSH Studio.
- **`MISSING_CREDENTIAL`** — save the DeepSeek key again under **Settings → Models**.
- **`UNKNOWN_MODEL`** — select `deepseek-v4-pro` or `deepseek-v4-flash` from the configured provider.
- **The composer is disabled** — choose a workspace and a model before sending the first task.
- **The local service stops responding** — DSH Studio probes it every 10 seconds and recycles it after three consecutive failed health checks.
- **A restart opens a different port** — this is expected. DSH Studio asks the OS for an unused port and follows the new local origin automatically.

## Security notes

DSH Studio binds the service to loopback and does not expose a LAN-listening option. Quitting from the tray stops the supervised process tree; merely closing the window keeps the local service running in the tray.
