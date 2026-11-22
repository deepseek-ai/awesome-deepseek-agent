[English](./codeaf.md) | [简体中文](./codeaf.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 codeaf

codeaf 是 AgentField 推出的开源（Apache 2.0）软件工厂。你在终端里描述要做的事，它就能在任意模型上运行编程任务，可以同时运行多个，每个任务都在自己的仓库副本和独立分支上进行。DeepSeek 官方 API 是它的内置供应商之一。

#### 1. 安装 codeaf

- macOS 和 Linux：

```bash
curl -fsSL https://agentfield.ai/get/codeaf | bash
```

- Windows：从 [Releases 页面](https://github.com/Agent-Field/CodeAF/releases) 下载 `codeaf-windows-amd64.exe`（或 `-arm64.exe`）。

- 检查安装结果，若显示版本号则安装成功：

```bash
codeaf --version
```

#### 2. 连接 DeepSeek

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后执行：

```bash
codeaf connect deepseek
```

在 `key:` 提示处粘贴 Key。codeaf 会先用 `GET /models` 校验 Key，再保存，并显示 `deepseek is connected` 以及找到的模型数量。也可以在脚本中连接：

```bash
echo "$DEEPSEEK_API_KEY" | codeaf connect deepseek
```

也可以在会话中通过 `/connect` → **DeepSeek** 连接。codeaf 直接调用 `https://api.deepseek.com/v1`（OpenAI 兼容接口），中间不经过任何代理或路由。

#### 3. 选择模型和思考强度

在项目目录中以 DeepSeek-V4-Pro 和最高思考强度启动 codeaf：

```bash
cd /path/to/my-project
codeaf chat --model deepseek/deepseek-v4-pro --reasoning max
```

- 模型：`deepseek/deepseek-v4-pro` 或 `deepseek/deepseek-v4-flash`。前缀 `deepseek/` 是已连接供应商的名称，可运行 `codeaf connect` 查看。如果你是在会话中通过 `/connect` 连接的，供应商可能显示为 `deepseek-direct`，此时请使用 `deepseek-direct/deepseek-v4-pro`。
- 在会话中，`/model` 可切换模型并保存选择。
- **思考强度：** 命令行使用 `--reasoning low|high|max`，会话中使用 `/effort max`，或在 `/settings` 的 thinking 一行设置。codeaf 会发送 DeepSeek 自己的 `reasoning_effort` 字段（`low`、`high` 或 `max`）。未设置时使用 DeepSeek 的默认值（`high`）。
- **1M 上下文：** DeepSeek V4 模型最多支持 100 万 token 上下文。codeaf 会从 DeepSeek 的模型列表读取每个模型的上下文窗口，无需额外配置。

#### 4. 第一次运行

像对同事说话一样描述需求，例如：

```text
给注册接口加上输入校验，另外修一下 utils 里不稳定的日期测试。
```

每个代码任务都在自己的仓库副本中运行，并落在自己的分支上，因此两个任务不会同时修改同一批文件。对于需要无人值守完成的大型、需求明确的改动，可在会话中使用 `/senior-dev <需求>`，或在 shell 中执行 `codeaf senior-dev "<需求>"`（macOS 和 Linux）。
