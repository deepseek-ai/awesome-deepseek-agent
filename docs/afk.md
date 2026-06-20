[English](./afk.md) | [简体中文](./afk.zh-CN.md) · [← Back](../README.md)

# Integrate with AFK

AFK is a browser-based coding agent platform. Install the daemon on your machine, connect it to your AFK account, and run coding sessions from the browser using DeepSeek models.

#### 1. Create an AFK Account

Open AFK in your browser:

<https://afk.mooglest.com>

Create an account or sign in.

#### 2. Install and Connect the AFK Daemon

In AFK, follow the daemon setup instructions for your operating system.

The daemon runs on your machine and gives AFK access to the project directories you choose. After it connects, it will appear in the AFK browser UI.

#### 3. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 4. Configure DeepSeek in AFK

In the AFK browser UI:

1. Open **Account → LLM**
2. Click **Add connection**
3. Select **DeepSeek**
4. Paste your DeepSeek API key
5. Save the connection
6. Optionally click **Test** to verify the connection

AFK's DeepSeek connection uses the default DeepSeek API endpoint automatically. Only set a Base URL if you use a custom proxy or gateway.

#### 5. Start a Coding Session

Create a new AFK session:

1. Click **New session**
2. Select a connected daemon
3. Choose your project directory
4. Select the DeepSeek connection
5. Select or manually enter a model:
   - `deepseek-v4-pro`
   - `deepseek-v4-flash`
6. Enter a coding task and start the session

Example task:

```text
Inspect this repository, find the failing tests, fix the underlying issue, and summarize what changed.
```

AFK will run the agent through your connected daemon, stream progress to the browser, and use the selected DeepSeek model for the session.

#### Notes

- DeepSeek V4 models support up to **1 million tokens** of context.
- If the model list does not show the latest DeepSeek models, manually enter `deepseek-v4-pro` or `deepseek-v4-flash`.
- AFK chooses the model per session, so you can switch between DeepSeek and other providers when starting new sessions.
- AFK supports persistent sessions, browser-visible progress, project instructions through `AGENTS.md`, sub-agents, skills, MCP tools, and workspace isolation.

#### Troubleshooting

- `401` or authentication errors: check your DeepSeek API key in **Account → LLM**.
- `402` or payment errors: check your DeepSeek Platform balance.
- No daemon available: make sure the AFK daemon is installed, running, and connected to your account.
- Project directory not visible: make sure the daemon was installed or configured with access to that directory.
- Model not listed: manually enter `deepseek-v4-pro` or `deepseek-v4-flash`.
