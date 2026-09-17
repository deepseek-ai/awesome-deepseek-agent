[English](./gritcode.md) | [简体中文](./gritcode.zh-CN.md) · [← Back](../README.md)

# Integrate with Gritcode

Gritcode is an open-source, native desktop AI coding agent for macOS and Linux. It is written in C++ with wxWidgets (no Electron), so the whole app is about 10 MB. Next to the agent chat it keeps the essentials: a project file tree, an editor with syntax highlighting, and saved sessions per project folder.

- **GitHub:** <https://github.com/lszl84/gritcode>
- **Website:** <https://gritcode.ai>

#### 1. Install Gritcode

Download the latest build from the [Gritcode releases page](https://github.com/lszl84/gritcode/releases/latest):

- macOS (`.dmg` — Apple Silicon, macOS 14 or later; signed and notarized)
- Linux (`.deb` — built on Ubuntu 24.04)

On Debian / Ubuntu, install the package with apt:

```bash
sudo apt install ./gritcode-*-Linux.deb
```

#### 2. Configure DeepSeek

Click the gear button in the toolbar to open **Settings**.

1. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **API key** field under **DeepSeek**. The key is stored in your system keyring.
2. Set **Reasoning effort** to **Max** for the strongest reasoning on coding tasks. (**High** is DeepSeek's default and is faster.)
3. Click **OK**.

<div align="center">
<img src="./assets/gritcode_settings.png" width="560" border="1" />
</div>

Gritcode talks to DeepSeek's OpenAI-compatible endpoint (`https://api.deepseek.com`) directly — no proxy or config file needed. Once a key is set, it loads the available models live from the `/models` endpoint, so new DeepSeek models show up without an app update.

#### 3. Start Coding

1. Open the session dropdown in the toolbar, choose **New Session…**, and pick your project folder.
2. In the model dropdown next to it, choose **DeepSeek V4 Pro** (`deepseek-v4-pro`) or **DeepSeek Flash** (`deepseek-flash`, i.e. DeepSeek V4.1 Flash).
3. Type a task and click **Send**.

<div align="center">
<img src="./assets/gritcode_session.png" width="480" border="1" />
</div>

DeepSeek V4 runs with thinking mode enabled, and Gritcode is built around it:

- The full **1 million token** context window is used out of the box — nothing to configure.
- Every request carries `reasoning_effort` (`high` or `max`, from Settings). At **Max**, Gritcode raises the output limit to 384K tokens so long reasoning isn't cut off.
- `reasoning_content` is passed back in the conversation history across tool calls, as DeepSeek's [thinking mode](https://api-docs.deepseek.com/guides/thinking_mode) requires.
- The model's reasoning appears in a collapsed **Thinking** block — expand it to watch the reasoning stream in.

#### 4. Going Further

- **Free models without a key.** The **OpenCode Free** entry in the model dropdown uses the free OpenCode Zen tier — handy for trying Gritcode before adding a DeepSeek key.
- **Sessions per folder.** Each project folder keeps its own session history; switch projects from the session dropdown.
- **Grit History.** With **Enable Grit History tools** turned on in Settings, the agent can search your past sessions across projects.
