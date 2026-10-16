[English](./deer_flow.md) | [简体中文](./deer_flow.zh-CN.md) · [← Back](../README.md)

# Integrate with DeerFlow

[DeerFlow](https://github.com/bytedance/deer-flow) is an open-source super agent harness created by ByteDance that orchestrates sub-agents, memory, and sandboxed code execution, powered by extensible skills.

DeerFlow provides first-class support for DeepSeek through its built-in `PatchedChatDeepSeek` provider, handling DeepSeek's `reasoning_content` thinking stream seamlessly.

- **GitHub:** <https://github.com/bytedance/deer-flow>
- **Official Site:** <https://deerflow.tech>

---

## 1. Get a DeepSeek API Key

1. Log in to the [DeepSeek Platform](https://platform.deepseek.com/).
2. Navigate to **API Keys** and generate an API key.
3. Save the key for configuration.

---

## 2. Install DeerFlow

Clone the DeerFlow repository:

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
```

Copy the example configuration file:

```bash
cp config.example.yaml config.yaml
```

Set your DeepSeek API key in your environment or in a `.env` file:

```bash
echo "DEEPSEEK_API_KEY=sk-your-deepseek-api-key" >> .env
```

---

## 3. Configure DeepSeek in `config.yaml`

Edit `config.yaml` to declare the DeepSeek-V4 models under the `models` section and set the default model:

```yaml
# ============================================================================
# LLM Models Configuration
# ============================================================================
default_model: deepseek-v4-pro

models:
  # DeepSeek-V4-Pro with Thinking Mode
  - name: deepseek-v4-pro
    display_name: DeepSeek-V4-Pro (Thinking)
    use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
    model: deepseek-v4-pro
    api_key: $DEEPSEEK_API_KEY
    timeout: 600.0
    max_retries: 2
    max_tokens: 8192
    supports_thinking: true
    supports_vision: false
    when_thinking_enabled:
      extra_body:
        thinking:
          type: enabled
    when_thinking_disabled:
      extra_body:
        thinking:
          type: disabled

  # DeepSeek-V4-Flash for fast subagent tasks
  - name: deepseek-v4-flash
    display_name: DeepSeek-V4-Flash
    use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
    model: deepseek-v4-flash
    api_key: $DEEPSEEK_API_KEY
    timeout: 300.0
    max_retries: 2
    max_tokens: 8192
    supports_thinking: false
    supports_vision: false
```

### Key Capabilities

- **1M Context Window**: DeepSeek-V4 models support up to 1,000,000 tokens of context, enabling deep codebase exploration and multi-step agent reasoning in DeerFlow.
- **Thinking Mode**: Setting `supports_thinking: true` and configuring `thinking: { type: "enabled" }` enables deep reasoning with `reasoning_content` replayed accurately across turns.
- **Sub-Agents Routing**: You can assign `deepseek-v4-flash` to lighter subagent roles in `subagents.default_model` to reduce latency and cost while keeping `deepseek-v4-pro` as the lead agent.

---

## 4. Launch DeerFlow

### Option A: Using Docker (Recommended)

```bash
docker compose up -d
```

### Option B: Local Development

Ensure Python 3.12+ and Node.js 22+ are installed:

```bash
make dev
```

Open `http://localhost:2026` in your browser to access the DeerFlow interface and start interacting with your DeepSeek-powered super agent!
