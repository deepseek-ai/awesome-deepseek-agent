[English](./qoder.md) | [简体中文](./qoder.zh-CN.md) · [← Back](../README.md)

# Integrate with Qoder

Qoder is an AI coding agent platform built by the Qoder team. It has DeepSeek as a **built-in first-party model** — select it directly from the model list on paid plans, or bring your own DeepSeek API key when BYOK is enabled on your account.

Qoder offers multiple product forms:

- **QoderWork** — a desktop agentic assistant for everyone
- **Qoder CLI** — an agentic AI coding tool built for command-line developers
- **Qoder** — an autonomous development desktop built for real software development

Qoder CLI and Qoder Desktop support DeepSeek-V4-Pro and DeepSeek-V4-Flash with up to **1M context window** and **max thinking effort**. DeepSeek built-in selection is currently only available on **QoderWork CN**.

- **Website:** [https://qoder.com](https://qoder.com)
- **Docs:** [https://docs.qoder.com](https://docs.qoder.com)

---

## Install

### QoderWork (CN)

Download from the QoderWork CN site [https://qoder.com.cn/qoderwork](https://qoder.com.cn/qoderwork) and run the installer for your platform. Built-in DeepSeek model selection is currently only available in this CN release.

### Qoder CLI

**macOS / Linux:**

```bash
curl -fsSL https://qoder.com/install | bash
```

**Windows PowerShell:**

```bash
irm https://qoder.com/install.ps1 | iex
```

**Windows CMD:**

```bash
curl -fsSL https://qoder.com/install.cmd -o install.cmd && install.cmd
```

Verify:

```bash
qodercli --version
```

### Qoder Desktop

Download from [https://qoder.com/download](https://qoder.com/download) and run the installer for your platform (macOS 10.15+, Windows 10+, Linux .deb/.rpm).

---

## Sign In

Launch Qoder and sign in. In CLI:

```bash
qodercli
```

Inside the interactive session:

```
/login
```

Follow the prompts to complete authentication via browser or personal access token.

In Desktop, follow the built-in sign-in flow on first launch.

---

## Use DeepSeek as a Built-in Model (Paid Plans)

DeepSeek-V4-Pro and DeepSeek-V4-Flash are available as built-in models on paid plans (Pro, Pro+, Ultra, Teams) — no API key required.

### In QoderWork (CN only)

In the QoderWork CN release, open the model selector in the task input box and pick `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash`. The selected model is summarized below the input with its context window and credit usage.

![QoderWork CN — DeepSeek-V4-Pro selected in the task model selector](./assets/qoderwork_chat_deepseek.png "QoderWork CN home screen with DeepSeek-V4-Pro selected")

### In CLI

Run the `/model` command and switch to the **New Models** tab:

```
/model
```

Select `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash` and press Enter.

![Qoder CLI with DeepSeek-V4-Pro selected](./assets/qoder_cli_deepseek_v4_pro.png "DeepSeek-V4-Pro selected with max thinking effort")

### In Desktop

Click the model selector dropdown in the AI Chat input box, switch to the **New Models** tab, and pick `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash`. Picking a model also exposes a side panel where you can adjust the **context window** (200K / 400K / 1M) and toggle **thinking** with `high` / `max` depth for that model.

![Qoder Desktop — DeepSeek-V4-Pro with context and thinking options](./assets/qoder_ide_chat_deepseek_params.png "DeepSeek-V4-Pro selection with context window and thinking effort side panel")

### Model Details

| Model | Credit Usage | Description |
|-------|-------------|-------------|
| DeepSeek-V4-Pro | 0.5x | Excels at complex reasoning, code generation, and engineering tasks |
| DeepSeek-V4-Flash | 0.1x | Fast reasoning and low cost with balanced capabilities |

Both models support up to **1M context window** and **max thinking effort**.

---

## Use DeepSeek with Your Own API Key (BYOK)

DeepSeek is a built-in BYOK provider — once BYOK is enabled on your account, you can plug in your own DeepSeek API key without any custom-endpoint configuration. Get one from the [DeepSeek Platform](https://platform.deepseek.com/api_keys) first.

### In CLI

1. Run `/model` and switch to the **Custom** tab. Highlight `[+] Add custom model...` and press Enter.

   ![Qoder CLI — Custom tab, Add custom model entry](./assets/qoder_cli_byok_custom_empty.png "Qoder CLI Custom tab with Add custom model entry highlighted")

2. **Step 1 — Provider:** select `DeepSeek` from the provider list.

   ![Qoder CLI BYOK wizard — select DeepSeek provider](./assets/qoder_cli_byok_provider_deepseek.png "Select DeepSeek as the BYOK provider")

3. **Step 2 — Model:** pick `DeepSeek-V4-Pro` or `DeepSeek-V4-Flash` (under the *Pay As You Go* group).

   ![Qoder CLI BYOK wizard — select DeepSeek model](./assets/qoder_cli_byok_select_model.png "Pick DeepSeek-V4-Pro or DeepSeek-V4-Flash")

4. **Step 3 — Credentials:** paste your DeepSeek API key and press Enter. The CLI validates it server-side before saving.

   ![Qoder CLI BYOK wizard — enter API key](./assets/qoder_cli_byok_api_key.png "Enter DeepSeek API key in the credentials step")

5. The new entry appears under the **Custom** tab. Press Enter to activate it; press `d` to delete.

   ![Qoder CLI — Custom tab with DeepSeek-V4-Pro added](./assets/qoder_cli_byok_added.png "BYOK DeepSeek-V4-Pro listed under Custom tab")

6. After activation, the active model line at the bottom of the screen switches to `DeepSeek-V4-Pro (DeepSeek)` and traffic now goes through your own key.

   ![Qoder CLI — DeepSeek-V4-Pro active via BYOK](./assets/qoder_cli_byok_active.png "Status line showing DeepSeek-V4-Pro (DeepSeek) as the active model")

### In Desktop

1. Open **Settings → Models**. If you have no BYOK entries yet, you'll see *No custom models yet*.

   ![Qoder Desktop — Settings, Models tab empty](./assets/qoder_ide_settings_models_empty.png "Qoder Desktop Settings Models tab with no custom models")

2. Click **+ Add**. In the dialog, choose `DeepSeek` as the provider, leave Type as `Pay As You Go`, select one or more models (e.g. *DeepSeek-V4-Pro*, *DeepSeek-V4-Flash*) and paste your API key.

   ![Qoder Desktop — Add Models dialog with DeepSeek + API key](./assets/qoder_ide_byok_add_models_dialog.png "Add Models dialog: provider DeepSeek, 2 models selected, API key entered")

3. After clicking **Add**, both models appear in the Models list with a toggle for enable/disable.

   ![Qoder Desktop — Models list after adding DeepSeek BYOK](./assets/qoder_ide_settings_models_added.png "Settings Models list now contains DeepSeek-V4-Pro and DeepSeek-V4-Flash")

4. Back in the chat input, open the model selector and switch to the **Custom** tab — your BYOK DeepSeek models are listed there. Click one to use it.

   ![Qoder Desktop — Chat model selector, Custom tab with DeepSeek BYOK](./assets/qoder_ide_chat_custom_tab.png "Chat model selector Custom tab listing the BYOK DeepSeek models")

> **Note on BYOK access:** BYOK availability is account-controlled. The DeepSeek provider is part of the built-in BYOK list, so it does not require the higher "custom URL" permission used for arbitrary OpenAI-compatible endpoints. If "Add custom model" is missing in the CLI or "+ Add" is missing in Desktop, check your plan or workspace settings.

---

## Configure Model Parameters

DeepSeek V4 models support configurable parameters:

**Context Window:**

| Option | Description |
|--------|-------------|
| 200K | Standard, sufficient for most tasks |
| 400K | Extended for larger codebases |
| 1M | Maximum for large-scale projects |

**Thinking Effort:**

| Option | Description |
|--------|-------------|
| low | Minimal reasoning, fastest response |
| medium | Moderate reasoning depth |
| high | Deep reasoning for complex tasks |
| xhigh | Deep analysis for high-difficulty problems |
| max | Maximum reasoning depth |

### CLI Commands

```bash
# Select model at startup
qodercli --model deepseek-v4-pro
qodercli --model deepseek-v4-flash

# Adjust parameters
qodercli --reasoning-effort max --context-window 1000000
```

Or use slash commands in the interactive session:

```
/model
/effort max
/context-window
```

> **Tip:** Use `/model` to switch between models at any time. Your selection is automatically persisted across sessions.
