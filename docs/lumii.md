[English](./lumii.md) | [简体中文](./lumii.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with LUMII

[LUMII (ZERA AI OS)](https://zeraneo.com/) is a Windows AI agent desktop assistant with chat, workspaces, and tools. Its native DeepSeek provider accepts your own DeepSeek API key and uses the OpenAI-compatible Chat Completions endpoint at `https://api.deepseek.com`.

> Draft validation status — 2026-10-08: the settings, model choices, and Maximum reasoning option were inspected in a local LUMII 1.2.6 installation; the provider mapping was checked in source. A successful live conversation and multi-turn tool run are still pending because the available DeepSeek account returned HTTP 402. The public download also has different package identities from the inspected installation, so its walkthrough remains to be repeated. The examples below are verification steps, not recorded successful runs.

## 1. Install and prepare your account

1. Download the Windows installer from the [official LUMII download page](https://zeraneo.com/download). This guide covers Windows 10/11 x64.
2. Run the installer, allow the required components to finish installing, and open LUMII. Complete the app's account sign-in if prompted.
3. If the first-login model wizard appears, you can select **Skip for now** and configure DeepSeek through Settings as described below.
4. Obtain a key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) and confirm that its account has available API balance. The LUMII account and the DeepSeek API account are separate; LUMII sign-in does not provide DeepSeek API credit. Consult [official pricing](https://api-docs.deepseek.com/quick_start/pricing/) for current charges.

## 2. Connect the native DeepSeek provider

The screenshots use the Chinese interface. English control names are given in the steps, with the corresponding Chinese labels where useful.

1. Open the account menu at the bottom left, then **Settings → Model providers** (`设置 → 模型提供商`).
2. Scroll to **Connect with an API key or token** (`使用 API 密钥或令牌连接`). In **Provider**, select **DeepSeek API key**.
3. Enter your key in **API key or token**, then select **Save configuration** (`保存配置`). If a credential is already stored, the card displays **Configured** instead of the key; use **Reconfigure** (`重新配置`) only when replacing it.
4. Select **Sync models** (`同步模型`) on the DeepSeek card. A saved credential or a visible model list alone does not prove a billable model call succeeds.
5. Inspect **Current connection**. For a native Pro connection, the reference is `deepseek/deepseek-v4-pro`.

![DeepSeek API-key provider card with a stored credential; the key is not displayed](./assets/lumii-deepseek-api-key.png)

![LUMII Settings navigation and the native DeepSeek current connection](./assets/lumii-deepseek-provider.png)

The native provider supplies its endpoint and model metadata; this route does not require a custom-provider JSON file or a manually entered context limit.

## 3. Choose a model and Maximum reasoning

The current [official model catalog](https://api-docs.deepseek.com/quick_start/pricing/) lists the following model IDs. Both have **1M context**. LUMII's native catalog includes the context metadata; an application's usable input budget can be lower after system instructions and tool definitions are included.

| API model ID | LUMII display label | Input |
| --- | --- | --- |
| `deepseek-flash` | DeepSeek-V4.1-Flash / DeepSeek V4.1 Flash | Text and images |
| `deepseek-v4-pro` | DeepSeek-V4-Pro / DeepSeek V4 Pro | Text |

Use `deepseek-flash` for Flash; the official API currently treats the older V4 Flash names as aliases. Choose the **DeepSeek** provider, since similarly named models can also be offered by other providers.

![Native DeepSeek model choices in Settings](./assets/lumii-deepseek-models.png)

1. Select **New task** (`新任务`) and the intended Agent.
2. Click the model name or **Reasoning** control at the bottom of the composer to open **Model settings** (`模型设置`). Choose **DeepSeek V4 Pro** or **DeepSeek V4.1 Flash**.
3. Under **Reasoning capability** (`推理能力`), select **Maximum** (`最高`). This is LUMII's `max` level. The source adapter maps it to `reasoning_effort: "max"` with thinking enabled, matching the [DeepSeek thinking API](https://api-docs.deepseek.com/guides/thinking_mode/).
4. Close the dialog and confirm the model and reasoning labels in the composer before sending. Selections apply immediately to the conversation; **Inherited: High** means the current inherited level is High, not Maximum.

![Blank LUMII task using DeepSeek V4 Pro with inherited High reasoning](./assets/lumii-deepseek-new-task.png)

![DeepSeek Model settings showing the available Maximum button; High is currently selected](./assets/lumii-deepseek-thinking.png)

LUMII also maps Low/Minimal to `low`, Medium/High to `high`, and Extra high/Maximum to `max` for its native DeepSeek adapter. The **Thinking speed** control is separate; the inspected DeepSeek model does not expose a speed override.

## 4. First conversation

These requests consume DeepSeek API balance. Once balance is available, keep the selected DeepSeek model and Maximum reasoning, then send:

> What is 17 × 23? Reply with only the result.

The expected result is `391`. In the same conversation, send:

> Add 9 to the previous result. Reply with only the new result.

The expected result is `400`. Check that the model selection stays on DeepSeek and the responses finish without a billing, authentication, or provider error. Expected answers are not evidence that these requests have already passed validation.

## 5. Verify multi-turn tools with thinking enabled

Choose a small test workspace from the folder control below the composer. Use a text editor to create `deepseek-demo.txt` in that folder with this content:

```text
item: demo
quantity: 12
unit_price: 3
```

With Maximum reasoning selected, send:

> Use the file-reading tool to read deepseek-demo.txt in the current workspace. Report quantity × unit_price. Only read files; do not edit them or send anything externally.

Then, in the same conversation:

> Read deepseek-demo.txt again using the file-reading tool. Confirm the item name and the total from the previous turn. Only read files.

Check for an actual file-reading tool record in both turns and final answers with total `36` and item `demo`. If a tool is unavailable, resolve workspace/tool access before treating this check as passed. A plain text answer without the tool records does not verify multi-turn tool use.

DeepSeek requires prior assistant `reasoning_content` to be returned on later requests that carry tools. LUMII's native provider declares this compatibility requirement; successful execution of this two-turn check is still pending. See [the official thinking-mode tool-call requirements](https://api-docs.deepseek.com/guides/thinking_mode/#tool-calls).

## 6. Troubleshooting

Use the error details to distinguish failures. The provider's [official error reference](https://api-docs.deepseek.com/quick_start/error_codes/) explains the HTTP codes.

| Symptom | Next step |
| --- | --- |
| `401` | Check the DeepSeek key and which Agent/provider credential is selected. |
| `402` / `Insufficient Balance` | Check the DeepSeek API account's balance before retrying. |
| `429` | Reduce concurrent requests and wait before retrying. |
| `503` | Retry later when the provider recovers. |
| `400` mentioning `reasoning_content` | Check the LUMII version and report the error details through its help/support entry. Keep thinking enabled when verifying the fix. |
| DeepSeek is missing from the picker | Confirm **DeepSeek API key** is configured for the intended Agent, sync that provider, and reopen the model picker. Record any sync failure. |
| A conversation has a different model | Choose DeepSeek in that conversation's **Model settings**; changing an Agent default does not verify the model used by an existing conversation. |

Before reporting a problem, retain the app version, selected provider/model, operation, and error code. Omit API keys and private workspace contents.
