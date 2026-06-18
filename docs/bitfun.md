[English](./bitfun.md) | [简体中文](./bitfun.zh-CN.md) · [← Back](../README.md)

# Integrate with BitFun

[BitFun](https://github.com/GCWing/BitFun) is a desktop-grade Agent runtime and a ready-to-use suite of desktop Agent applications. It includes Code, Cowork, Computer Use, and Personal Assistant agents, with MCP, LSP, memory, Skills, context compression, and remote control built in.

BitFun is a good fit for DeepSeek V4 because its runtime is designed for long-running local sessions and cache-friendly agent loops. In a 731-trial SWE-Bench-Pro run, BitFun recorded a weighted KV cache hit rate of **98.67%** across **1.56B cached input tokens**; **83.1%** of trials reached at least **98%** cache hit rate, and **51.8%** reached at least **99%**.

#### 1. Install BitFun

Download the latest desktop installer from the [BitFun Releases](https://github.com/GCWing/BitFun/releases) page.

If you prefer to build from source:

```sh
git clone https://github.com/GCWing/BitFun.git
cd BitFun
pnpm install
pnpm run desktop:dev
```

#### 2. Get a DeepSeek API Key

Create an API key in the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then keep it ready for the BitFun model configuration.

#### 3. Add a DeepSeek V4 model

Open BitFun and go to **Settings → Model Configuration**. The quickest path is:

1. Click the **DeepSeek** template.
2. Paste your DeepSeek API key.
3. Click the one-click validation button next to the configuration.
4. Save the configuration after validation passes.

The DeepSeek template fills the official API URL and OpenAI-compatible request format for you. BitFun supports DeepSeek V4's **1M context window**, **384K max output**, and **max** reasoning effort; these values can be reviewed or adjusted in the model's advanced settings.

For lower-cost iteration, add `deepseek-v4-flash` as a **fast model**. It is useful for exploration, quick repository scanning, and lightweight agent turns, while `deepseek-v4-pro` remains the best default for complex coding and reasoning tasks.

#### 4. Select the model for an Agent

Choose the DeepSeek model in BitFun's model selector, then start with the Agent that matches your workflow:

| Agent | Best for |
|-------|----------|
| Code Agent | Repository exploration, code edits, terminal commands, Git work, debugging, and review |
| Cowork Agent | PDF, DOCX, XLSX, PPTX, and knowledge-work tasks |
| Computer Use | Browser and desktop-app operation through screen, mouse, and keyboard control |
| Personal Assistant | Long-running assistance, memory-backed tasks, scheduling, and remote entry points |

#### 5. Verify the setup

Use the one-click validation button beside the model configuration. If it passes, start a Code Agent session in a project directory and ask it to inspect the repository or run a small test command.

BitFun should stream the answer and preserve the session locally. You can type `/usage` during a session to inspect recorded runtime and token usage details.

#### Troubleshooting

- Authentication errors: check that the API key is copied from the DeepSeek Platform and has not expired or been revoked.
- Model not found: use `deepseek-v4-pro` or `deepseek-v4-flash`.
- Context looks too small: review the model's advanced settings and confirm that Context Window Size is set to `1000000`.
- Thinking is missing: review the advanced settings and confirm that reasoning mode is enabled with Reasoning Effort set to `max`.

#### Resources

- [BitFun GitHub](https://github.com/GCWing/BitFun)
- [BitFun Website](https://openbitfun.com/)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
