[English](./deepagent_studio.md) | [简体中文](./deepagent_studio.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepAgent Studio

DeepAgent Studio is an open-source, DeepSeek-native agent runtime with a Tauri
desktop IDE. Its Rust runtime provides durable sessions, tool-use approvals,
MCP, skills, sub-agents, context engineering, and replayable event storage.

- **GitHub:** <https://github.com/eighteendreamer/DeepAgent-Studio>

#### 1. Install DeepAgent Studio

DeepAgent Studio is currently run from source. Install the Rust toolchain
specified by the repository, plus Node.js and pnpm. Install the platform
prerequisites required by Tauri before continuing.

```sh
git clone https://github.com/eighteendreamer/DeepAgent-Studio.git
cd DeepAgent-Studio/apps/desktop
pnpm install
pnpm tauri dev
```

The command builds the desktop shell and opens the app.

#### 2. Connect your DeepSeek account

Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
When the onboarding screen opens, paste the key and select **Connect**.

DeepAgent Studio validates the key by discovering models from DeepSeek before
accepting it. The key is stored in the operating system keychain rather than
the application's SQLite database.

#### 3. Use DeepSeek-V4-Pro with maximum reasoning

After model discovery, DeepAgent Studio automatically selects:

| Role | Model |
| --- | --- |
| Chat and tool use | `deepseek-v4-flash` |
| Reasoning | `deepseek-v4-pro` |

Both DeepSeek V4 models use the full **1M-token context window** in the runtime
(with a 384K-token maximum output budget). Open the model/thinking control in
the composer, choose **DeepSeek-V4-Pro**, and set the thinking level to
**Deep** for complex coding tasks. This sends DeepSeek `reasoning_effort=max`.

| Thinking level | DeepSeek behavior |
| --- | --- |
| Simple | Thinking disabled |
| Medium | Thinking enabled with `reasoning_effort=high` |
| Deep | Thinking enabled with `reasoning_effort=max` |

#### 4. Start your first coding session

1. Add a local folder from the project sidebar.
2. Start a new chat in that project.
3. Ask DeepAgent Studio to inspect or change the project, for example:

   ```text
   Inspect this project, explain its architecture, and propose the smallest safe change for the issue I describe next.
   ```

4. Review and approve tool calls when prompted. The default approval policy
   keeps side-effectful work under your control.

#### Optional: run the headless runtime demonstration

From the repository root, the following command runs the scripted end-to-end
runtime demonstration:

```sh
cargo run -p deepagent-cli
```
