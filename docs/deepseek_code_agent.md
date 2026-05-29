[English](./deepseek_code_agent.md) | [简体中文](./deepseek_code_agent.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Code Agent

Use DeepSeek V4 models in the browser: edit files, run commands, browse the workspace, collaborate with multiple AI agents, attach reference material, and switch models on the fly.

**Repository:** [github.com/diky87688973/deepseek-code-agent](https://github.com/diky87688973/deepseek-code-agent)

### Highlights

- Local browser workflow: set keys and paths in `config.ini`—no full IDE extension stack to wire up.
- Multiple session tabs in one window; switch to the `/immersive` multi-column layout when you need several threads side by side.
- Tool steps stay in the side panel beside the transcript so you can see what ran without hunting through raw logs.
- Knowledge base: configure the folder once, tick files per session—no need to paste long documents into the input each time.
- `/plan` and `/execute` work with the Todo panel: review the plan before acting, or walk the checklist step by step.
- Light and dark themes, plus a context-usage strip next to the input so longer threads stay readable at a glance.
- Switch DeepSeek models in the UI (available models depend on your deployment).

### DeepSeek V4 Configuration

The agent connects to DeepSeek through an OpenAI-compatible API. Configure these in `config.ini`:

| Setting | Value | Notes |
|---------|-------|-------|
| Models | `deepseek-v4-pro`, `deepseek-v4-flash` | Switchable in the UI in real time |
| API Base | `https://api.deepseek.com` | OpenAI-compatible endpoint |
| Context Window | 1M tokens | Set via `model_context_tokens_json` |
| Reasoning Effort | `max` / `high` | Set `reasoning_effort` in `[misc]` section |
| KV Cache | Enabled by default | Leverages DeepSeek prefix caching to reduce costs |

The default model is `deepseek-v4-flash` for fast everyday responses. Switch to `deepseek-v4-pro` in the UI when you need deeper reasoning — no restart required.

---

### When it fits

- You want a web UI instead of tying everything to a heavy IDE plugin.
- You mostly work on one machine and prefer chat plus file-side helpers over a terminal-only loop.
- You keep several conversations open at once, or want a wider layout to follow multiple threads in parallel.

---

### Capabilities

| Item | Notes |
|------|------|
| Chat & tabs | Several conversations in one window |
| Tools | File, search, Git, command-style actions; progress in the side panel |
| Knowledge base | Point at a text folder; tick files per session |
| `@` paths | Picker or typed paths |
| Modes | `/plan` for a plan first; `/execute` to follow the checklist |
| Layout | `/` by default; multi-column at `/immersive` |
| Theme | Light or dark |
| Context strip | Usage overview next to the input |

On Windows, run `start.bat`; while the app runs, the install directory is protected read-only.

---

### Token Cost

Estimated token costs are fetched automatically from [DeepSeek's pricing page](https://api-docs.deepseek.com/quick_start/pricing) and displayed in the UI. The agent updates rates from the official page on startup, so you always see the latest figures.

---

![Main layout](./assets/deepseek_code_agent_ui.png)

*Main layout*

#### 1. Install

Python 3.8 or newer.

```bash
git clone https://github.com/diky87688973/deepseek-code-agent.git
cd deepseek-code-agent
pip install -r requirements.txt
```

#### 2. Configure

Edit **`config.ini`** in the repository root: API endpoint and key, listen port, workspace path, data directory, knowledge-base path, and any other fields—follow the **comments inside the file** for the rest.

API keys: [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Run

- **Windows:** run `start.bat`
- **Linux / macOS:** `chmod +x start.sh && ./start.sh`
- **Manual:** `python main_tray.py`

Open `http://127.0.0.1:8801` or `http://127.0.0.1:8801/immersive` in the browser. Host and port must match `config.ini`.

---

#### 4. Knowledge base

![Knowledge base panel](./assets/deepseek_code_agent_kb.png)

*Knowledge base panel*

After you set the knowledge-base directory in `config.ini`, tick files in the panel.

---

#### 5. Theme, immersive layout, context overview

![Light theme](./assets/deepseek_code_agent_theme_light.png)

*Light theme*

![Multi-column layout](./assets/deepseek_code_agent_immersive_tabs.png)

*Multi-column layout*

![Context overview](./assets/deepseek_code_agent_context_view.png)

*Context overview*

---

#### Quick actions

| Input / control | Effect |
|-----------------|--------|
| `/plan` | Plan first; defer writes to disk |
| `/execute` | Run against the current checklist |
| `@…` | Reference a file |
| File button | Insert `@` paths |
| Knowledge panel | Tick reference files |
| Theme | Light or dark |
| Classic ↔ immersive | Toggle in the header |

---

#### Example prompts

> Read `test.txt` on the desktop  
> Show recent Git history for this repository  
> List files in the current directory
