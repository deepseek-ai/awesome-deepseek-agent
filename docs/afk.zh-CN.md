[English](./afk.md) | [简体中文](./afk.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AFK

AFK 是一个基于浏览器的编程 Agent 平台。你只需要在自己的机器上安装 daemon，将它连接到 AFK 账号，然后就可以在浏览器中使用 DeepSeek 模型运行编程会话。

#### 1. 创建 AFK 账号

在浏览器中打开 AFK：

<https://afk.mooglest.com>

创建账号或登录。

#### 2. 安装并连接 AFK Daemon

在 AFK 中，根据你的操作系统按照 daemon 设置说明进行安装。

daemon 会运行在你的机器上，并让 AFK 访问你选择的项目目录。连接成功后，它会出现在 AFK 浏览器界面中。

#### 3. 获取 DeepSeek API Key

前往 [DeepSeek Platform](https://platform.deepseek.com/api_keys)，创建并复制 API Key。

#### 4. 在 AFK 中配置 DeepSeek

在 AFK 浏览器界面中：

1. 打开 **Account → LLM**
2. 点击 **Add connection**
3. 选择 **DeepSeek**
4. 粘贴你的 DeepSeek API Key
5. 保存连接
6. 可选：点击 **Test** 验证连接是否可用

AFK 的 DeepSeek 连接会自动使用默认的 DeepSeek API 端点。只有在使用自定义代理或网关时，才需要设置 Base URL。

#### 5. 启动编程会话

创建一个新的 AFK 会话：

1. 点击 **New session**
2. 选择已连接的 daemon
3. 选择你的项目目录
4. 选择 DeepSeek 连接
5. 选择或手动输入模型：
   - `deepseek-v4-pro`
   - `deepseek-v4-flash`
6. 输入编程任务并启动会话

示例任务：

```text
Inspect this repository, find the failing tests, fix the underlying issue, and summarize what changed.
```

AFK 会通过你已连接的 daemon 运行 Agent，将进度实时流式展示到浏览器，并在该会话中使用你选择的 DeepSeek 模型。

#### 说明

- DeepSeek V4 模型支持最高 **100 万 token** 上下文。
- 如果模型列表中没有显示最新的 DeepSeek 模型，可以手动输入 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- AFK 会在每个会话启动时选择模型，因此你可以在新会话中切换 DeepSeek 或其他提供商。
- AFK 支持持久会话、浏览器可见的执行进度、通过 `AGENTS.md` 配置项目指令、子 Agent、Skills、MCP 工具以及工作区隔离。

#### 故障排查

- `401` 或认证错误：检查 **Account → LLM** 中的 DeepSeek API Key。
- `402` 或支付错误：检查你的 DeepSeek Platform 余额。
- 没有可用 daemon：确认 AFK daemon 已安装、正在运行，并已连接到你的账号。
- 看不到项目目录：确认 daemon 安装或配置时允许访问该目录。
- 模型未列出：手动输入 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
