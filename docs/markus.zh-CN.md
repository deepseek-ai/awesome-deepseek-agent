[English](./markus.md) | [简体中文](./markus.zh-CN.md) · [← Back](../README.md)

# 接入 Markus

[Markus](https://www.markus.global/) 是一个开源的 AI 数字员工平台，提供完整的 Web GUI，让您在浏览器中就能创建、管理和部署 AI Agent。所有操作都在图形界面中完成。

DeepSeek 是 Markus 的内置 Provider — 只需配置 API Key 即可直接使用，无需手动添加。

#### 1. 安装与启动

确保已安装 [Node.js](https://nodejs.org/) 和 [pnpm](https://pnpm.io/installation)，然后运行：

```bash
# 先设置 DeepSeek API Key
export DEEPSEEK_API_KEY=your-api-key-here

# 克隆并启动 Markus
git clone https://github.com/markus-global/markus.git
cd markus
pnpm install
pnpm dev
```

浏览器会自动打开管理后台，地址为 `http://localhost:8056`。

**配置 DeepSeek — 两种方式**：

- **启动前设置环境变量**（自动检测）：`export DEEPSEEK_API_KEY=your-key` — 启动时自动加载。
- **在 GUI 中配置**（无需环境变量）：进入 **设置 → LLM Providers**，找到 DeepSeek，填写 API Key 即可，GUI 会持久保存。

也可以全局安装：

```bash
npm install -g @markus-global/cli
markus start
```

然后在浏览器中通过 **设置 → LLM Providers** 配置 DeepSeek API Key，无需环境变量。

#### 2. 为 Agent 选择 DeepSeek

在 Markus GUI 中，创建 Agent 并使用 DeepSeek 只需几步：

1. 在左侧导航栏进入 **Agent → 创建 Agent**
2. 为 Agent 起个名称（如"DeepSeek 助手"）
3. 在 **模型 Provider** 中选择 **DeepSeek**
4. 选择一个模型 — `deepseek-v4-flash`（快速）或 `deepseek-v4-pro`（更强）
5. 点击保存，Agent 即刻就绪

您也可以随时在 **设置 → LLM Providers** 中管理 DeepSeek 配置 — Provider 已预置，只需填写或更新 API Key。

#### 3. 还能做什么？

在 Markus 管理后台中，您还可以：

- **编排多 Agent 团队** — 为不同 Agent 分配不同的 DeepSeek 模型，各司其职
- **创建结构化任务** — 将工作分解为子任务，配合审核工作流
- **添加技能** — 为 Agent 安装 Web 搜索、浏览器自动化、代码分析等能力
- **配置治理规则** — 设置审批层级、任务上限和审核分配

所有操作都在浏览器中完成。无需手动配置 Provider，无需 CLI 脚本。设置好 `DEEPSEEK_API_KEY` 即可开始。

更多信息请访问 [Markus GitHub 仓库](https://github.com/markus-global/markus)。
