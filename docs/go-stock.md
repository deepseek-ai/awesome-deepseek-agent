[English](./go-stock.md) | [简体中文](./go-stock.zh-CN.md) · [← Back](../README.md)
# Integrate with go-stock
[go-stock](https://github.com/ArvinLovegood/go-stock) is an open-source desktop stock-analysis tool built with Wails and Naive UI. It embeds a full AI agent available in three modes (React / Plan-Execute / DeepAgents) with 150+ built-in financial data tools, covering A-share / HK / US quotes, fund-flow tracking, Dragon-Tiger lists, limit-up ladders, knowledge bases, and scheduled market review reports.
- **GitHub:** <https://github.com/ArvinLovegood/go-stock>
#### 1. Install go-stock
Download the latest build for your platform from the [go-stock releases page](https://github.com/ArvinLovegood/go-stock/releases):
- Windows (`go-stock-windows-amd64.exe`, portable — no installation required)
- macOS (`go-stock-darwin-universal`, Intel and Apple Silicon)
You can also build from source with Go 1.27+, Node.js and the Wails CLI:
```bash
wails build
```
#### 2. Configure the DeepSeek Model Service
Launch go-stock and open the **AI Model Service** (AI模型服务) page from the left navigation.
1. Click **+ Add AI Config** (+ 添加AI配置). In the **API Endpoint** (接口地址) field, pick the **DeepSeek (https://api.deepseek.com)** preset from the dropdown — the base URL is filled in automatically.
2. Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) into the **Token (apiKey)** field.
3. Set **Model Name** to **`deepseek-v4-pro`** (or **`deepseek-v4-flash`**). You can click the field to fetch the live model list from the API, or type the name manually.
4. Leave **Context Window** at `0` (auto). go-stock maintains a built-in model-parameter table that recognizes `deepseek-v4-*` models and automatically applies the full **1 million token** context window and 384K max output — no manual configuration required.
5. Click **Save Config** (保存配置) at the top of the page.
DeepSeek V4 models run with thinking mode enabled by default, so reasoning works out of the box with no extra configuration. (go-stock does not currently expose a `reasoning_effort` selector; thinking follows the API default.)
#### 3. Start Analyzing
Open the floating AI assistant from the toolbar and pick an agent mode:
- **Quick (React)** — fastest loop, recommended with the latest DeepSeek models.
- **Planning (Plan-Execute)** — plans first, then executes each step.
- **DeepAgents** — built-in task planning and sub-agent delegation for complex multi-step analysis.
Then just ask in natural language, e.g. *"Analyze the fundamentals and capital flow of CATL and give me an operation plan for tomorrow."* The agent autonomously calls its built-in data tools (quotes, financials, fund flow, Dragon-Tiger lists, limit-up ladder, sector rotation, etc.) and returns a grounded report with sources.
#### 4. Going Further
Once DeepSeek V4 is configured, you can use it across the rest of go-stock:
- **Scheduled reports.** Enable the daily review (18:00) and morning-strategy (09:00) cron tasks to have DeepSeek generate market reviews and pre-market plans automatically, with optional Feishu / DingTalk push.
- **Knowledge base & long-term memory.** Build a local knowledge base over your research notes; the agent's long-term memory keeps context across sessions (add an embedding model config for vector retrieval).
- **MCP servers.** Extend the agent with external MCP tools from the MCP Server manager.
- **Vision.** Add another config with model name `deepseek-v4-flash-vision-exp` and turn on the **Vision** switch to analyze K-line screenshots and other images directly in the chat.
> ⚠️ go-stock is for learning and research only. AI-generated analysis is not investment advice — invest at your own risk.
