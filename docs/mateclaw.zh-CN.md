[English](./mateclaw.md) | [简体中文](./mateclaw.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 MateClaw

<img src="./assets/mateclaw_preview.png" width="1024" border="1" />

> **大多数 AI 工具，会在它依赖的供应商挂掉那一刻一起死。大多数，会在你关掉浏览器标签那一刻把你忘掉。大多数，给你一个对话框，就当作产品。**

MateClaw 是一个开源的个人 AI 操作系统。一个 JAR。Apache 2.0 协议。底层是 Spring Boot 3.5 + Spring AI Alibaba。同一个大脑，会出现在 **Web 控制台**、**桌面端**、**网页嵌入小部件**、**Java 插件 SDK**，以及 **8 个 IM 渠道** —— 钉钉、飞书、企业微信、微信、Telegram、Discord、QQ、Slack。同一份记忆，同一套 Skills，同一组工具，不同的入口。

DeepSeek V4 直接接入到所有这些能力里 —— V4 Pro 跑重推理，V4 Flash 跑高吞吐对话，两者的 thinking-mode 推理内容都会与答案一起流式输出，并在整段对话中完整保留。

#### 为什么需要这一层

某家大型 LLM 供应商一旦下线几个小时，每一个把 AI 战略压在单一供应商上的团队，都只能盯着红色的报错卡片。AI 正在变成基础设施。基础设施不能绑死在一家供应商上。

在 MateClaw 里，你把 DeepSeek、DashScope、OpenAI、Anthropic、Gemini、Kimi、Ollama、LM Studio、MLX 拖进一条优先级调用链。主用供应商返回 401 或者超时，下一家立即续上，用户看到的回答不会断。一个健康追踪器（`vip.mate.llm.failover.ProviderHealthTracker`）会把出错的供应商放进冷却窗口，避免每一轮都浪费几秒。

你不用写重试脚本。你拖。

#### 完整能力

- **Agent 运行时** —— **ReAct** 用于迭代式推理，**Plan-and-Execute** 用于多步任务。基于 Spring AI Alibaba 的 StateGraph 实现：reasoning / action / observation / planning / step-execution 各自一个节点，节点之间用条件边串起来。动态上下文裁剪、智能截断、过期流清理 —— 这些不起眼的事情让长对话真正能用。
- **LLM Wiki** —— 上传 PDF、Markdown、网页。Wiki 引擎会把这些原料消化成带 `[[Wiki 链接]]` 的页面，每一句话都有可点击回到原文片段的引用。仓库和图书馆的差别。
- **记忆生命周期** —— 对话后抽取、定时整合、做梦式整理（重新阅读当天）。配合每个 Workspace 下的 `AGENTS.md` / `SOUL.md` / `PROFILE.md` / `MEMORY.md` 文件。不用你亲自照看的记忆系统。
- **Skills + MCP + Tool Guard** —— ClawHub 市场的 `SKILL.md` 包，stdio / SSE / Streamable HTTP 三种 MCP 接入，ACP 端点也会注册成 Skill 卡片。叠加一层带 RBAC 与审批流的 Tool Guard，对高风险工具调用先审批再执行。能力需要边界。
- **多模态生产** —— TTS、STT、图像、音乐、视频、腾讯混元 3D。统一的异步流水线，进度通过 SSE 实时推送。
- **企业基础能力** —— JWT 认证。按 Agent / 按模型 / 按工具的 RBAC。完整审计日志。Flyway 自愈式迁移。

#### 安装

三种方式，挑不让你叹气的那种。

**桌面端 —— 无需 Java：**

直接到 [GitHub Releases](https://github.com/matevip/mateclaw/releases) 下载。内置 JRE 21，双击运行。支持 Mac / Windows / Linux。

**Docker —— 接近生产部署：**

```bash
git clone https://github.com/matevip/mateclaw.git
cd mateclaw
cp .env.example .env
docker compose up -d
```

控制台地址 `http://localhost:18080`。默认账号 `admin` / `admin123` —— 上来先改密码。

**源码 —— 给开发者：**

```bash
git clone https://github.com/matevip/mateclaw.git
cd mateclaw/mateclaw-server
mvn spring-boot:run
```

控制台地址 `http://localhost:18088`。

#### 添加 DeepSeek

进入管理控制台：

1. **Settings → Model Providers** → 找到 **DeepSeek** → 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) → 启用。把 DeepSeek 拖到调用链顶部即设为主用，或者放在某家之后作为兜底。
2. **Settings → Models** —— 两个内置条目已经在那儿：**DeepSeek V4 Pro**（`deepseek-v4-pro`）和 **DeepSeek V4 Flash**（`deepseek-v4-flash`）。1M 上下文。thinking-mode 推理。
3. **Agents** → 编辑任意一个 Agent → 把模型设成 V4 Pro（重推理）或 V4 Flash（快响应）→ 保存。

到这一步，配置就完了。推理内容会与答案一起流式输出，并在整段对话中保留，不会用完即丢。

#### 开始使用

- **Web / 桌面端** —— 进入控制台，选择 Agent，开聊。流式走 SSE；工具调用和推理过程实时渲染。
- **IM 渠道** —— 在 **Channels** 下，为 8 个支持平台中的任意一个挂上 webhook。同一个 Agent，记忆共享，Skills 共享。
- **Wiki** —— 在 **Wiki** 下创建知识库，上传原料，让消化器自动生成结构化页面。Agent 检索时会带上引用。
- **Skills** —— 在 **Skills → Marketplace** 安装或上传 Skill 包。Agent 运行时直接加载，不用重启。受 Tool Guard 约束。
- **网页嵌入** —— `mateclaw-webchat` 是一个只需一行 `<script>` 的小部件，可以挂到任何网站上，对外暴露指定的 Agent。

#### 注意事项

- 生产部署请通过 `mysql` Spring profile 切到 MySQL。DeepSeek API Key 放进密钥管理系统，不要留在 `.env` 里。
- 文档：<https://claw.mate.vip/docs>
- 源码：<https://github.com/matevip/mateclaw>
- 桌面端下载：<https://github.com/matevip/mateclaw/releases>

---

重点不在渠道列表。重点是 —— 另一头的 AI 记得你、跑你的工具、按你的规则推理，不在别人家的云上。把 DeepSeek V4 接进去，你就拥有了一个既快又愿意思考的引擎。

同一个大脑，五种入口。这就是核心思想。
