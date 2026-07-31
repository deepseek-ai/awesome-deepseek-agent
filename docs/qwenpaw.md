[English](./qwenpaw.md) | [简体中文](./qwenpaw.zh-CN.md) · [← Back](../README.md)

# Integrate with QwenPaw

QwenPaw is an open-source personal AI assistant built by the AgentScope team. It provides a web console and terminal UI, connects to chat platforms, and can be extended with skills, memory, and MCP tools. DeepSeek is available as a built-in model provider.

- **GitHub:** <https://github.com/agentscope-ai/QwenPaw>
- **Docs:** <https://qwenpaw.agentscope.io/docs/>

#### 1. Install QwenPaw

QwenPaw requires Python 3.11–3.13. Install QwenPaw v2.0.1 or later, initialize it, and start the web console:

```bash
python -m pip install --upgrade "qwenpaw>=2.0.1"
qwenpaw init --defaults
qwenpaw app
```

Open <http://127.0.0.1:8088/> in your browser.

> QwenPaw also offers script, Docker, and desktop-app installation methods. See the [QwenPaw Quick Start](https://qwenpaw.agentscope.io/docs/quickstart/) if you prefer one of those options.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and copy it.

#### 3. Configure the DeepSeek Provider

In the QwenPaw console:

1. Go to **Settings → Models**.
2. Open the built-in **DeepSeek** provider's settings, enter your API key, save it, and click **Test Connection**.
3. Open the provider's model list and test `deepseek-v4-pro` or `deepseek-v4-flash`.
4. Open the selected model's configuration and set:
   - **Max Tokens:** `384000`
   - **Max Context Length:** `1000000`
   - **Relay Reasoning:** enabled
5. In the model's generation-parameters JSON box, enter:

```json
{
  "reasoning_effort": "max",
  "extra_body": {
    "thinking": {
      "type": "enabled"
    }
  }
}
```

Save the model settings. Select the configured model under **Settings → Models → Default LLM**, or use the model selector in the upper-right corner of **Chat** to select it for the current conversation.

DeepSeek V4 Pro and Flash support a 1-million-token context window and up to 384,000 output tokens. Thinking mode is enabled by default, but the explicit configuration above ensures that QwenPaw requests the highest available reasoning effort.

#### 4. First Run

Start a new chat and send a prompt that exercises a tool call, for example:

```text
Use the current-time tool to tell me the local time, then explain which tool you used.
```

You can also use the same configured agent from QwenPaw's terminal UI:

```bash
qwenpaw
```

#### Troubleshooting

- **401 or 403 response:** Verify the API key and make sure your DeepSeek account has available credit.
- **Model is missing:** Upgrade with `python -m pip install --upgrade qwenpaw`. DeepSeek V4 Pro and Flash are built in to QwenPaw v2.0.1.
- **400 error mentioning `reasoning_content`:** Upgrade to QwenPaw v2.0.1 or later. Current versions preserve the reasoning content required by DeepSeek during multi-turn tool calls; do not disable thinking mode as a workaround.

For current model behavior and limits, see the [DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/) and [Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/) documentation.
