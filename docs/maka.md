[English](./maka.md) | [简体中文](./maka.zh-CN.md) · [← Back](../README.md)

# Integrate with Maka

[Maka](https://github.com/maka-agent/maka-agent) is an open-source, local-first AI agent workspace for desktop and terminal. It combines persistent project sessions with file and shell tools, Skills, and multiple model connections.

- **GitHub:** <https://github.com/maka-agent/maka-agent>
- **Releases:** <https://github.com/maka-agent/maka-agent/releases/latest>

#### 1. Install Maka

The current public binary supports Apple Silicon macOS. Download `Maka-<version>-mac-arm64.dmg` and its `.sha256` file from the [latest release](https://github.com/maka-agent/maka-agent/releases/latest).

Optionally verify the download before opening it:

```shell
shasum -a 256 -c Maka-<version>-mac-arm64.dmg.sha256
```

Open the DMG, drag **Maka** to **Applications**, and launch it from Finder.

#### 2. Get a DeepSeek API Key

Open the [DeepSeek API Keys page](https://platform.deepseek.com/api_keys), create an API key, and copy it. Maka stores model credentials locally; the key is not written into project files.

#### 3. Add the DeepSeek Connection

1. Open **Settings → Models** in Maka.
2. Select the **API** tab, find **DeepSeek**, and open its provider card.
3. Paste the API key and click **Save provider**. Maka uses the official `https://api.deepseek.com` endpoint and fetches the live model catalog automatically.
4. Open the newly created DeepSeek connection. Under **Model management**, enable `deepseek-v4-flash` and `deepseek-v4-pro`. If the models are not visible yet, click **Update model catalog**.
5. Set **DeepSeek V4 Flash** (`deepseek-v4-flash`) as this connection's default model, click **Test connection**, and then click **Set as default connection**.

Maka's built-in metadata configures both DeepSeek V4 models with a **1,000,000-token context window** and up to **384,000 output tokens**, so no manual context-window field is required.

#### 4. Select Maximum Reasoning

Create a new task and select **DeepSeek V4 Flash** from the model picker beside the composer. Open the model picker's **Thinking level** menu and choose **Maximum**.

For `deepseek-v4-flash`, Maka maps this selection to `reasoning_effort: "max"`. You can switch to **DeepSeek V4 Pro** from the same model picker when you want to use the Pro model.

#### 5. Run a First Agent Task

Open a disposable project folder and send a small tool-using task, for example:

```text
Create a file named deepseek-maka-smoke.txt containing exactly:
DeepSeek V4 works in Maka
Then read the file back and report the result.
```

Review any tool permission prompt before approving it. A successful run should create the file, read it back, and return the same text.

#### Troubleshooting

- **The V4 models are missing:** open the connection and click **Update model catalog**. Confirm that the model IDs are exactly `deepseek-v4-flash` and `deepseek-v4-pro`.
- **Maximum is not shown:** select `deepseek-v4-flash` in the current task, then reopen **Thinking level** in the model picker.
- **Authentication fails:** create a new API key on the DeepSeek Platform and update the connection's model key.
- **The provider returns a balance error:** check the account balance and billing status on the DeepSeek Platform.
- **The app cannot be installed:** the current public build is for Apple Silicon macOS; Intel macOS, Windows, and Linux packages are not available yet.

#### Related Resources

- [Maka repository](https://github.com/maka-agent/maka-agent)
- [Maka releases](https://github.com/maka-agent/maka-agent/releases/latest)
- [DeepSeek API documentation](https://api-docs.deepseek.com/)
- [DeepSeek thinking mode](https://api-docs.deepseek.com/guides/thinking_mode)
