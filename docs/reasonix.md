[English](./reasonix.md) | [简体中文](./reasonix.zh-CN.md) · [← Back](../README.md)

# Integrate with Reasonix

Reasonix is a cross-platform coding agent with DeepSeek as a native backend. It is designed around the DeepSeek API — a cache-first loop, Flash-first cost control, and automatic tool-call repair — and connects directly to `api.deepseek.com` without an additional protocol-conversion proxy. Reasonix provides both a terminal CLI/TUI and a desktop app, includes DeepSeek V4 Flash and DeepSeek V4 Pro, and supports their 1-million-token context window and `max` reasoning effort.

- [Reasonix GitHub repository](https://github.com/esengine/DeepSeek-Reasonix)
- [Download the Reasonix desktop app](https://reasonix.io/?download=desktop#start)

#### 1. Install Reasonix

Choose either the terminal or desktop edition. The desktop app does not require Node.js or a prior CLI installation.

**Terminal CLI/TUI**

The npm installation requires [Node.js](https://nodejs.org/en/download/) 18 or later:

```sh
npm install -g reasonix
```

On macOS, you can install the native build with Homebrew instead:

```sh
brew install esengine/reasonix/reasonix
```

If you prefer not to install it globally, replace `reasonix` in the commands below with `npx --yes reasonix`. On Windows, [Git for Windows](https://git-scm.com/download/win) is recommended when you need Git, Git Bash, or POSIX hooks, but it is not a hard Reasonix runtime dependency.

**Desktop app**

Choose the appropriate package on the [official download page](https://reasonix.io/?download=desktop#start):

| Platform | Package |
| --- | --- |
| macOS | Universal `.dmg` or `.zip` for Apple Silicon and Intel |
| Windows | Signed `.exe` installer or portable `.zip` for x64 and ARM64 |
| Linux | `.deb` or `.tar.gz` for x64 |

#### 2. Get a DeepSeek API Key

Create an API Key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys). The terminal and desktop editions save it to Reasonix's managed global credential file, so you do not need to define a system environment variable manually.

#### 3. Configure DeepSeek

**Terminal CLI/TUI**

Run the setup manager, add the official DeepSeek service, enter the API Key, and choose the default model:

```sh
reasonix setup
```

For the no-install form, run:

```sh
npx --yes reasonix setup
```

**Desktop app**

1. Launch Reasonix and open **Settings → Models & providers**.
2. Click **+ Add provider**.
3. Choose **Recommended preset → DeepSeek Official**.
4. Enter the DeepSeek API Key, add the provider, and set DeepSeek V4 Flash or Pro as the default model.

The CLI and desktop app share the global configuration and credentials. Their default locations are:

- macOS / Linux: `~/.reasonix/config.toml` and `~/.reasonix/.env`
- Windows: `%APPDATA%\reasonix\config.toml` and `%APPDATA%\reasonix\.env`

#### 4. First run

**Terminal CLI/TUI**

Enter your project directory and start Reasonix:

```sh
cd /path/to/my-project
reasonix
```

Use `npx --yes reasonix` for the no-install form. The historical `npx reasonix code` command is still accepted as a compatibility alias, but new documentation and scripts should invoke `reasonix` directly.

**Desktop app**

1. In the project area, select **Use existing folder** and open your code directory, or choose **New blank project**.
2. Click **New session**.
3. Describe the task in the composer and send it. Reasonix can inspect the project, propose edits, and request tools; approve file writes or commands when prompted by the desktop app.

#### 5. Choose a model and reasoning effort

Reasonix uses **DeepSeek V4 Flash** by default for everyday iteration. Switch to **DeepSeek V4 Pro** when you need stronger reasoning. Both are configured with a 1-million-token context window.

| Model | Model ID | Supported reasoning effort |
| --- | --- | --- |
| DeepSeek V4 Flash | `deepseek-v4-flash` | `low`, `high`, `max` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `high`, `max` |

In the terminal TUI, use:

```text
/model
/effort max
/help
```

- `/model` opens the model picker; it also accepts a model name for direct switching.
- `/effort max` changes the current session to `max` reasoning effort.
- `/help` lists the slash commands supported by the installed version.

You can also select the model and effort at startup:

```sh
reasonix --model deepseek/deepseek-v4-pro --effort max
```

In the desktop app, use the model and reasoning-effort selectors next to the composer. New sessions use the model saved under **Settings → Models & providers → Default model**.

#### 6. Troubleshooting

- **Missing API Key**: rerun `reasonix setup` in the terminal, or check the DeepSeek Official provider under **Settings → Models & providers** in the desktop app.
- **`reasonix` is not found**: restart the terminal and verify that npm's global executable directory is on `PATH`, or use `npx --yes reasonix`.
- **DeepSeek models are missing in the desktop app**: confirm that the DeepSeek Official provider was added, then refresh the model list or create a new session.
- **Project-level configuration is needed**: run `reasonix setup --local` in the project root. It writes `./reasonix.toml`; the API Key remains only in the global `.env`.

<div align="center">
<img src="https://raw.githubusercontent.com/esengine/reasonix/main/docs/logo.svg" width="640" alt="Reasonix" />
</div>
