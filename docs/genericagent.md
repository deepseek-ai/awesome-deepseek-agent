[English](./genericagent.md) | [简体中文](./genericagent.zh-CN.md) · [← Back](../README.md)

# Integrate with GenericAgent

> **Physical-level omnipotent executor. Any task you need done — from file operations, script execution, browser control to system-level intervention — I'm at your service. Describe your goal.**

**GenericAgent (GA)** is a minimal, self-evolving autonomous agent framework — the entire core is only ~3,000 lines of seed code with a ~100-line Agent loop, yet it features a complete **hierarchical memory system (L0-L4)**, **9 atomic tools** (browser / terminal / filesystem / keyboard+mouse / screen vision / mobile ADB, etc.), and a unique **self-evolution capability**: every task automatically crystallizes into a reusable Skill, getting stronger with use.

GA is fully open-source and free — you only need your own LLM API Key to get started.

> 📖 Project: [github.com/lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent)
> 📄 Technical Report: arXiv 2604.17091

---

#### 1. Install GenericAgent

**Method 1: One-line install (recommended)**

The one-line command sets up an isolated Python runtime, downloads the complete project, and installs dependencies.

Linux / macOS:
```bash
GLOBAL=1 bash -c "$(curl -fsSL http://fudankw.cn:9000/files/ga_install.sh)"
```

Windows PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -c "$env:GLOBAL=1; irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

After installation, launch the desktop app from `frontends/GenericAgent.exe`.

**Method 2: Developer install**

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"
cp mykey_template.py mykey.py      # Fill in your API Key next
python launch.pyw
```

---

#### 2. Configure DeepSeek V4

Copy `mykey_template.py` to `mykey.py` and configure DeepSeek V4. GA calls DeepSeek via the OpenAI-compatible protocol — configuration is straightforward:

```python
native_oai_deepseek_config = {
    "name": "DeepSeek Flash",
    "apikey": "sk-<your DeepSeek API Key>",
    "apibase": "https://api.deepseek.com",
    "model": "deepseek-v4-flash",            # Everyday lightweight tasks
    "reasoning_effort": "medium",
}

native_oai_deepseek_pro_config = {
    "name": "DeepSeek Pro",
    "apikey": "sk-<your DeepSeek API Key>",
    "apibase": "https://api.deepseek.com",
    "model": "deepseek-v4-pro",              # Complex reasoning tasks
    "reasoning_effort": "max",               # Maximum reasoning effort
}
```

> 💡 **Tips**:
> - DeepSeek V4 supports a **1M context window** — GA is fully compatible.
> - `reasoning_effort` supports `none / minimal / low / medium / high / max`.
> - At runtime, type `/session.reasoning_effort=high` in the GA terminal to switch reasoning levels on the fly.

---

#### 3. First Run

Once GA starts, you'll enter an interactive REPL environment. Try your first DeepSeek V4 task:

```
GA > Write a Python script that counts the total lines of all Python files in the current directory.
```

GA will automatically invoke atomic tools (filesystem, terminal) to complete the task. Afterward, it automatically **crystallizes** this operation into a Skill that can be reused for similar future tasks.

You can also launch the desktop UI:
```bash
python launch.pyw
```

Or start the Streamlit web interface:
```bash
streamlit run frontends/ui_app.py
```

---

#### 4. Learn More

| Feature | Description |
|------|------|
| 🧬 **Self-Evolving** | Every task crystallizes into a Skill — no preloaded skill library needed |
| 🧠 **Hierarchical Memory** | L0-META → L1-Insight → L2-Facts → L3-SOP → L4-Raw, auto short/long-term management |
| ⚡ **9 Atomic Tools** | Browser / Terminal / Files / Keyboard+Mouse / Vision / OCR / Mobile(ADB) / Voice / Scheduler |
| 🔌 **Multi-Model** | DeepSeek / Claude / GPT / Gemini / Kimi / MiniMax — one framework, all models |
| 🤖 **Bootstrapped** | The entire repo — from git init to all code — was built by GA itself |
| 🪶 **Ultra Token-Efficient** | <30K context window, 1/10 to 1/30 of comparable agents |
| 💰 **100% Free & Open Source** | MIT license, zero fees — just bring your own API Key |

---

#### FAQ

**Q: Is DeepSeek required?**
A: No. GA supports multiple model protocols. You can add or switch models in `mykey.py` at any time. DeepSeek V4 is recommended for its excellent cost-effectiveness, and GA is fully tuned for it.

**Q: How do I update to the latest version?**
A: Run `git pull` in the GA project directory, then let GA read the changelog itself.

**Q: Compatibility issues?**
A: Make sure you're using **Python 3.11 or 3.12** (3.14 is incompatible). Run `python --version` to check.
