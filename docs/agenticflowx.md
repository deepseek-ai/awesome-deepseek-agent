[English](./agenticflowx.md) | [简体中文](./agenticflowx.zh-CN.md) · [← Back](../README.md)

# Integrate with AgenticFlowX

[AgenticFlowX](https://github.com/AgenticFlowX/agenticflowx) (AFX) is a spec-driven AI coding extension for VS Code. Use it as a normal chat-first coding assistant, or switch to **Spec mode** for a planning-first workflow with requirements, design, tasks, and a traceable journal kept in your repo. DeepSeek ships as a **built-in provider**, so you can run the whole workflow on DeepSeek-V4 with nothing more than an API key.

- **GitHub:** <https://github.com/AgenticFlowX/agenticflowx>
- **Website:** <https://agenticflowx.github.io>

#### 1. Install the extension

Search for **AgenticFlowX** in the Extensions view and install it from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=AgenticFlowX.agenticflowx) or [Open VSX](https://open-vsx.org/extension/agenticflowx/agenticflowx) (requires VS Code `1.105+`).

<div align="center">
<img src="./assets/agenticflowx_marketplace.png" width="600" border="1" />
</div>

Once installed, click the **AgenticFlowX** icon in the activity bar to open the chat panel.

<div align="center">
<img src="./assets/agenticflowx_activity_bar.png" width="600" border="1" />
</div>

#### 2. Add your DeepSeek API key

DeepSeek is a built-in provider — no custom endpoint, base URL, or config file required.

1. In the AFX chat panel, open **Settings → Models → Built-in**.
2. Under **API key providers**, find the **DeepSeek** card and expand it.
3. Get an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), paste it into the key field, and click **Save setup**. The key is stored in VS Code SecretStorage — never logged or echoed.
4. Set **Default model** to **DeepSeek V4 Pro** (`deepseek-v4-pro`). **DeepSeek V4 Flash** (`deepseek-v4-flash`) is also available for faster, lower-cost turns.

<div align="center">
<img src="./assets/agenticflowx_deepseek_provider.png" width="600" border="1" />
</div>

DeepSeek runs on AFX's bundled API Providers runtime, so there is no separate CLI to install.

#### 3. Pick DeepSeek and start coding

Open the model picker in the chat composer and select **DeepSeek V4 Pro** (or **DeepSeek V4 Flash**) — each entry shows its `1M` context window and per-MTok pricing. The displayed pricing comes from AFX's bundled model metadata; for the latest official rates, check the [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing). Then ask a question, attach context with `@path/to/file` mentions, or right-click a selection in the editor and choose **AgenticFlowX → Send Selection**.

<div align="center">
<img src="./assets/agenticflowx_model_picker.png" width="600" border="1" />
</div>

#### 4. Reasoning effort and 1M context

DeepSeek V4 supports up to **1 million tokens** of context — shown as `1M` next to each DeepSeek model in the picker — so the full window is available out of the box.

For the deepest reasoning on hard coding tasks, set **Thinking level** to **Extra High** (or **High** for shorter turns). You can change it per turn from the top of the composer model picker, or set a workspace default in **Settings → Runtimes → Thinking level**.
