[English](./deepagent_studio.md) | [简体中文](./deepagent_studio.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepAgent Studio

DeepAgent Studio 是一个开源的 DeepSeek 原生 Agent 运行时平台，并提供基于 Tauri 的桌面 IDE。其 Rust 运行时提供持久化会话、工具调用审批、MCP、Skills、子 Agent、上下文工程与可回放的事件存储。

- **GitHub：** <https://github.com/eighteendreamer/DeepAgent-Studio>

#### 1. 安装 DeepAgent Studio

DeepAgent Studio 当前从源码运行。请安装仓库锁定的 Rust 工具链、Node.js 和 pnpm，并在继续前安装对应操作系统的 Tauri 前置依赖。

```sh
git clone https://github.com/eighteendreamer/DeepAgent-Studio.git
cd DeepAgent-Studio/apps/desktop
pnpm install
pnpm tauri dev
```

该命令会构建桌面壳并打开应用。

#### 2. 连接 DeepSeek 账户

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。首次启动时，在引导页粘贴 API Key 并点击“连接”。

DeepAgent Studio 会先通过 DeepSeek 的模型发现接口校验 API Key，再接受该配置。Key 保存到操作系统钥匙串，而不会写入应用的 SQLite 数据库。

#### 3. 使用 DeepSeek-V4-Pro 与最高推理强度

模型发现完成后，DeepAgent Studio 会自动选择：

| 角色 | 模型 |
| --- | --- |
| 聊天与工具调用 | `deepseek-v4-flash` |
| 推理 | `deepseek-v4-pro` |

运行时会为这两个 DeepSeek V4 模型启用完整的 **100 万 token 上下文窗口**（最高 38.4 万 token 输出预算）。对于复杂编程任务，请在输入框的模型/思考控件中选择 **DeepSeek-V4-Pro**，并将思考档位设为 **Deep**；这会向 DeepSeek 发送 `reasoning_effort=max`。

| 思考档位 | DeepSeek 行为 |
| --- | --- |
| Simple | 关闭思考 |
| Medium | 开启思考，使用 `reasoning_effort=high` |
| Deep | 开启思考，使用 `reasoning_effort=max` |

#### 4. 开始第一个编码会话

1. 从项目侧边栏添加本地文件夹。
2. 在该项目中创建新会话。
3. 让 DeepAgent Studio 检查或修改项目，例如：

   ```text
   检查这个项目，说明它的架构；然后为我接下来描述的问题提出最小且安全的修改方案。
   ```

4. 出现提示时审核并批准工具调用。默认审批策略会让具有副作用的操作保持在你的控制之下。

#### 可选：运行无头运行时演示

在仓库根目录执行以下命令，可运行脚本化的端到端运行时演示：

```sh
cargo run -p deepagent-cli
```
