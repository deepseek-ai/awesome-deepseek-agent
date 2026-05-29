[English](./tg_helper.md) | [简体中文](./tg_helper.zh-CN.md) · [← Back](../README.md)

# Integrate with TG HELPER

TG HELPER is a desktop-level AI agent for Windows with **70+ built-in tools** covering file management, browser automation, IoT control, QQ Bot integration, embedded development (Arduino), and more. It supports both cloud models (OpenAI-compatible format) and local models (Ollama), and features a plugin ecosystem, multi-personality system, and proactive intelligence.

TG HELPER v0.2.5+ **natively supports DeepSeek V4 models** with Thinking Mode (`reasoning_effort` control), 1M context window configuration, and automatic parameter injection across all AI call paths.

#### 1. Install TG HELPER

```bash
git clone https://github.com/JXW666NB/TG-HELPER.git
cd TG-HELPER
pip install -r requirements.txt
playwright install chromium
```

#### 2. Configure DeepSeek in TG HELPER

Launch TG HELPER and open the **API Settings** tab:

```bash
python "TG HELPER.py"
```

On first launch, a setup wizard will guide you through configuration. For existing installations, navigate to **Settings → API Settings** (or the gear icon in the sidebar).

Fill in the following under **Main AI Configuration**:

| Field | Value |
|---|---|
| **API Key** | Your [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| **Base URL** | `https://api.deepseek.com/v1` |
| **Model Name** | `deepseek-v4-pro` or `deepseek-v4-flash` |

> ⚠️ Do NOT use `deepseek-chat` or `deepseek-reasoner` — these model names are **deprecated** as of July 2026. TG HELPER uses the current model naming.

Click **💾 Save API Settings**. The `deepseek` keyword in the model name is detected automatically.

##### Enabling DeepSeek Thinking Mode

After saving with a DeepSeek model name, a **🧠 DeepSeek Exclusive Configuration** section will appear in the API Settings page:

- **Enable Deep Thinking (Thinking Mode)**: Check this to activate DeepSeek V4's chain-of-thought reasoning. The model will output reasoning content (`reasoning_content`) before the final answer, significantly improving accuracy on complex tasks. When enabled, `reasoning_effort` and `thinking: {type: "enabled"}` are automatically passed to all API calls.
- **Reasoning Effort**: Choose from a dropdown:
  - `high` — recommended for most tasks
  - `max` — strongest reasoning for complex agent workflows (automatically applied by default for agent-class workloads)
- **Context Window**: Select from 16K up to **1M tokens** (DeepSeek V4 supports up to 1,000,000 tokens of context). This maps to the `max_tokens` parameter.

TG HELPER automatically injects these parameters across **all 8 AI call paths** including:
- Main agent conversation loop
- Multimodal image/video analysis
- Arduino code generation
- AI video generation (HTML+CSS animation rendering)
- AI image generation
- Plugin AI translator
- Web content summarization

No manual code changes are required — everything is configured through the GUI.

#### 3. Get Started

Type your request in the chat input at the bottom and press **Enter** to start interacting with TG HELPER powered by DeepSeek V4. Press **Shift+Enter** for line breaks.

Some things you can try:

- `"Help me organize the files on my desktop by type"`
- `"Browse to amazon.com and find the best-selling USB-C cables under $10"`
- `"Generate a 30-second animated video about a cute cat jumping with a balloon"`
- `"Turn on the living room lights via IoT"` (requires MQTT device setup)

TG HELPER will use its 70+ tools to execute your requests. Dangerous operations (file deletion, mouse/keyboard control, code execution) require explicit confirmation before proceeding. Refer to the [Security Mechanisms](https://github.com/JXW666NB/TG-HELPER#%EF%B8%8F-security-mechanisms) section for details.
