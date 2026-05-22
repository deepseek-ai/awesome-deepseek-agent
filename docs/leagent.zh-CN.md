[English](./leagent.md) | [简体中文](./leagent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 LeAgent

LeAgent 是一个可自部署的本地优先平台，用于构建由大语言模型驱动的办公自动化 —— 对话式 AI、可视化工作流以及 100+ 工具集于一身。DeepSeek 是目前验证最充分的供应商，推荐首次使用时选用。

#### 1. 安装 LeAgent

**前置条件：** git、uv、Node.js 20+

克隆仓库并通过启动脚本运行：

```
git clone https://github.com/vixues/LeAgent.git
cd LeAgent
./start.sh
```

后端将在 7860 端口启动，前端将在 5173 端口启动。

也可以使用 Docker 部署：

```
cd LeAgent/deploy
cp .env.example .env
docker compose up -d --build
```

或者使用一键安装脚本：

```
curl -fsSL https://vixues.com.cn/install.sh | bash
```

#### 2. 配置 DeepSeek 作为模型供应商

1. 打开 LeAgent Web UI，地址为 `http://localhost:5173`。
2. 进入 **设置 → 模型供应商**。
3. 在供应商列表中选择 **DeepSeek**。
4. 输入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
5. 选择模型 —— `deepseek-v4-pro` 质量最佳，`deepseek-v4-flash` 响应更快。
6. 将**上下文窗口**设置为 `1000000`（DeepSeek V4 支持最高 100 万 token 上下文）。
7. 开启**思考模式**，并将推理强度设为 `max` 以获得 `deepseek-v4-pro` 的最佳效果。
8. 保存配置。

#### 3. 开始使用

- **对话：** 打开 Chat 页面，开始由 DeepSeek 驱动的多轮对话。
- **工作流：** 使用可视化 ReactFlow 编辑器，构建拖拽式自动化工作流，以 DeepSeek 作为推理引擎。
- **工具：** 探索 100+ 内置工具（文档、网页、数据、代码执行、数据库等），Agent 可在对话过程中调用这些工具。

更多信息请参阅 [LeAgent 文档](https://github.com/vixues/LeAgent)。
