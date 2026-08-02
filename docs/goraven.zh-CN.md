[English](./goraven.md) | [简体中文](./goraven.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GoRaven

GoRaven 是一个开源、可自部署的团队 Agent 平台。团队里每个人都有自己的独立 Agent 工作空间 —— Agent 在里面读文件、写代码、跑命令、调接口、查知识库并交付成果。支持 DeepSeek、OpenAI、Claude、Qwen、GLM 或任何兼容 API。

- **GitHub：** <https://github.com/8treenet/goraven>
- **官网：** <https://goraven.dev>
- **在线体验：** <https://preview.goraven.dev>

#### 1. 部署 GoRaven

```bash
docker pull 8treenet/goraven:latest

docker run -d --restart=always --name goraven-agent \
  -p 8000:8000 \
  8treenet/goraven:latest
```

如需持久化数据，挂载一个数据卷：

```bash
docker run -d --restart=always --name goraven-agent \
  -p 8000:8000 \
  -v /opt/goraven:/goraven/data \
  8treenet/goraven:latest
```

打开 <http://localhost:8000>，按照初始化向导创建管理员账号。然后前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。

#### 2. 添加 DeepSeek 模型

进入管理后台的 **模型** 页面，点击 **新增模型**：

1. 模型服务商选择 **DeepSeek**，**Base URL** 会自动填入 `https://api.deepseek.com/v1`。
2. 将 DeepSeek API Key 粘贴到 **API Key**。
3. 在 **模型** 一栏填写 `deepseek-v4-pro` —— 也可以点击下拉框拉取 DeepSeek 推荐模型列表。
4. 将 **上下文长度（K Tokens）** 设置为 `1000` —— DeepSeek V4 系列支持 100 万 token 上下文窗口。
5. 可选：开启 **默认模型** 标签，新对话将默认选中该模型。

用同样的步骤再添加 `deepseek-v4-flash`，用于低延迟、低成本的日常任务，并开启 **快模型** 标签。保存时会自动校验连通性。

#### 3. 开始 Agent 会话

打开一个项目或新建对话，点击顶部模型标签即可在 DeepSeek V4 Pro 与 V4 Flash 之间切换。编码、长程规划、多步骤 Agent 任务建议使用 V4 Pro。直接布置任务即可 —— Agent 会自己读写文件、执行 Shell 命令、调用 MCP 工具。

#### 4. 管控访问与配额

作为管理员，在 **模型** 页面点击模型对应的 **成员**，可以控制哪些用户和团队可用该模型，并设置配额防止过度使用。

#### 常见问题

- `401` 或鉴权失败：检查 API Key 与 Base URL 是否正确（`https://api.deepseek.com/v1`）。
- 模型无响应：确认模型名是准确的 `deepseek-v4-pro` 或 `deepseek-v4-flash`。旧版 V3 模型名称已废弃，不再对应当前模型。
- 需要走代理：填写可选的 **代理 URL** 字段，例如 `http://127.0.0.1:7890`。
- 自定义容器时区：在 `docker run` 命令中追加 `-e TZ=Asia/Shanghai`。
