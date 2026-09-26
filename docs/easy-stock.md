[English](./easy-stock.md) | [简体中文](./easy-stock.zh-CN.md) · [← Back](../README.md)

# Integrate with easy-stock

easy-stock is a local-first desktop workbench for the China A-share market. It unifies a market overview, theme radar, limit-up ladder and sentiment-cycle analysis, AI stock reports, portfolio inspection, and automated collection of post-market commentary — with an AI copilot (the Hermes runtime) that runs on your own API keys, and all research memory kept on your machine.

- **GitHub:** <https://github.com/jundizhou/easy-stock>
- **Releases:** <https://github.com/jundizhou/easy-stock/releases/latest>

> The app UI is currently Chinese-first (it targets the China A-share market). The steps below include the exact Chinese labels to look for.

#### 1. Install easy-stock

Download the installer for your platform from the [releases page](https://github.com/jundizhou/easy-stock/releases/latest) — Windows and macOS builds are provided. No Node.js, Go, or Python required.

#### 2. Configure the DeepSeek provider

Open **系统设置 → Hermes 模型运行时** (System Settings → Hermes Model Runtime) and click **新增配置** (Add Configuration):

1. Select **DeepSeek** from the provider list. The base URL is preset to `https://api.deepseek.com`, the protocol to `Chat Completions`, and the default model to `deepseek-v4-pro`.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the API Key field.
3. To switch models, click **获取模型** (Fetch Models) and pick **`deepseek-v4-pro`** for the strongest reasoning, or **`deepseek-v4-flash`** for faster, cheaper runs. If the list is unavailable, choose **手动输入其他模型…** (enter model manually) and type the model name.
4. Click **保存并测试连接** (Save and Test Connection). Seeing **「Hermes 模型连接可用」** (Hermes model connection available) means the configuration works.

Notes:

- DeepSeek V4 models support up to **1 million tokens** of context. easy-stock passes full research context (quotes, theme structure, analysis history) to the model, which suits long review and consensus tasks.
- `deepseek-v4-pro` runs with deep thinking enabled by default on DeepSeek's API side — easy-stock uses the standard Chat Completions protocol, so this applies out of the box without extra configuration.

#### 3. First run: analyze a stock

1. Search a stock by name or code in the top search bar and open its page.
2. Go to **个股 AI 分析** (AI Stock Analysis) and generate a report. easy-stock classifies the stock's likely path (sentiment ladder, trend capacity, trend growth, range-bound watch, or weak/risk), and produces an evidence-linked report with confirmation and invalidation conditions.
3. Try **大 V 复盘日记 → 今日观点共识** (Review Diary → Today's Consensus) after market close to distill cross-author consensus and disagreements from collected commentary.

#### 4. Going further

- **Automated commentary collection.** Under **系统设置 → 大 V 复盘自动化** (System Settings → Review Automation), log in to Xueqiu or TaoGuba through the built-in browser; easy-stock then syncs new articles from your subscribed authors on a schedule.
- **Portfolio inspection.** Add up to 10 holdings with weights, pick a trading style, and get a portfolio health report with concentration and correlation risks.
- **Local research memory.** Articles, analysis records, and AI sessions are stored on your machine; your API key never leaves your computer.
- **Other providers.** The same settings panel also supports OpenAI-compatible endpoints (Kimi/Moonshot, Qwen, GLM, and more) and Anthropic — you can keep multiple configurations and switch between them.
