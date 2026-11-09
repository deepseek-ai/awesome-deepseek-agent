[English](./vaf.md) | [简体中文](./vaf.zh-CN.md) · [← Back](../README.md)

# Integrate with VAF

VAF (Veyllo Agentic Framework) is an open-source agent framework and harness with persistent memory and tools for web, code and files. It runs as a desktop app, a headless server or a terminal app on Windows, macOS and Linux, and can also be embedded as a Python library. DeepSeek is one of its built-in providers: no base URL or custom endpoint needs to be configured.

#### 1. Install VAF

Requirements: Git and a container runtime. The installer sets up the container engine, Python and Node for you.

###### Linux / macOS

```bash
git clone https://github.com/Veyllo-Labs/VAF.git && cd VAF
chmod +x install.sh && ./install.sh
```

When the installer asks for the profile, choose **Lean (API)**: it downloads no local chat, speech-to-text or text-to-speech model, so the chat runs on DeepSeek only.

###### Windows

```powershell
git clone https://github.com/Veyllo-Labs/VAF.git
cd VAF
.\install.bat
```

For more installation options, see the [VAF installation guide](https://github.com/Veyllo-Labs/VAF/blob/main/docs/setup/INSTALLATION_GUIDE.md).

#### 2. Configure DeepSeek

##### In the web UI

Start the desktop app with `vaf tray` (web UI at `http://localhost:3000`) and sign in. Then:

- **Settings → General → API Keys**: enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys) in the DeepSeek field.
- **Settings → AI & Model**: choose **DeepSeek** as the provider and pick the model: `deepseek-v4-pro` or `deepseek-flash`. `deepseek-auto` uses `deepseek-flash` for the chat and `deepseek-v4-pro` for background runs, workflows and context compression.
- **Settings → AI & Model → DeepSeek thinking effort**: choose **Max**. The default, Standard, sends no effort, so DeepSeek uses its own default (`high`).
- Save with **Save Changes**.

##### In the terminal

Start the terminal chat with `vaf run`, type `/settings`, choose **AI Provider → DeepSeek**, enter your API key and pick the model. Set the thinking effort with:

```bash
vaf models config deepseek_reasoning_effort max
```

Accepted values are `low`, `high` and `max`; an empty value restores DeepSeek's default. Any other value is refused.

#### 3. Context window

VAF treats every DeepSeek model as a 1M-token context window. By default it compresses the conversation history once it passes 45,000 tokens, because every reply resends the whole history and DeepSeek bills each token. To let the history grow towards the full 1M window, move **Settings → AI & Model → Context effort** to its last step, or run:

```bash
vaf models config context_compress_tokens 0
```

(`0` means: compress only when the model's window fills up.)

#### 4. Get started

Open the web UI with `vaf tray`, or chat in the terminal:

```bash
vaf run
```

A one-shot prompt to check the setup:

```bash
vaf prompt "Hello"
```

#### Use VAF as a Python library

```bash
pip install --pre vaf
```

```python
import os

from vaf import Agent

agent = Agent(config={
    "provider": "deepseek",
    "api_key_deepseek": os.environ["DEEPSEEK_API_KEY"],
    "api_model_deepseek": "deepseek-v4-pro",
    "deepseek_reasoning_effort": "max",
})
print(agent.run("In one short sentence, what is DeepSeek?"))
```

#### Notes

- DeepSeek models do not read images in VAF. To work with images, choose a vision provider under **Settings → AI & Model → Vision provider**.
- VAF passes DeepSeek's `reasoning_content` back on tool-calling turns, as DeepSeek's thinking mode requires, so thinking stays on during tool use.
