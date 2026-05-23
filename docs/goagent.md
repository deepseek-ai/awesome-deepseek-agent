[English](./goagent.md) | [简体中文](./goagent.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with GoAgent

[GoAgent](https://github.com/wimi321/GoAgent) is an open-source Go / Weiqi / Baduk agent. It combines KataGo analysis, board evidence, local knowledge, student profiles, and LLM tool use so the teacher can explain moves from evidence instead of guessing.

GoAgent can use DeepSeek through its OpenAI-compatible LLM provider. For current-move reviews that attach board screenshots, use a DeepSeek-compatible endpoint or proxy that supports image input. If your endpoint is text-only, DeepSeek is still useful for SGF, KataGo, knowledge-base, and tool-grounded teaching tasks.

#### 1. Install GoAgent

Download the latest desktop release from [GoAgent Releases](https://github.com/wimi321/GoAgent/releases).

To run from source:

```
git clone https://github.com/wimi321/GoAgent.git
cd GoAgent
pnpm install
pnpm dev
```

#### 2. Get a DeepSeek API Key

Create an API key in the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Configure DeepSeek in GoAgent

Open **Settings** in GoAgent and configure the LLM provider:

- **Base URL**: `https://api.deepseek.com`
- **API Key**: your DeepSeek API key
- **Model**: `deepseek-v4-pro` or `deepseek-v4-flash`

If GoAgent shows a model refresh or connection test button, use it after saving the credentials.

For long game reviews, prefer DeepSeek V4's 1M context mode when your endpoint exposes it. If your compatible proxy supports `reasoning_effort`, use `max` with `deepseek-v4-pro` for deeper reviews, and use `high` or the provider default for faster interactive teaching.

#### 4. Start a Teaching Session

In GoAgent:

1. Import an SGF file or load a game from the game library.
2. Make sure KataGo is configured and the win-rate graph has analysis data.
3. Ask the teacher to analyze the current move, a move range, or the full game.

Example prompts:

```
Analyze the current move using KataGo evidence and local knowledge.
Find the three most important turning points in this game.
Review moves 80-120 and explain what the student should train next.
```

GoAgent's teacher can call tools for game records, KataGo analysis, trace packets, board images, knowledge retrieval, and student profiles. The final answer should be grounded in tool results rather than unsupported claims.

#### 5. Notes

- Do not send private games to an external model provider unless you are comfortable with that provider's data policy.
- Use `deepseek-v4-flash` for lower-latency chat and `deepseek-v4-pro` for deeper reviews.
- For image-based board reading, make sure the selected OpenAI-compatible endpoint accepts image messages.
