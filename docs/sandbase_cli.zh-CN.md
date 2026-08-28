[English](./sandbase_cli.md) | [← 返回](../README.zh-CN.md)

# 使用 SandBase CLI 接入 DeepSeek

SandBase CLI 是 Apache-2.0 开源命令行工具和本地 MCP 桥接器，让支持 MCP 的客户端通过一次认证连接发现并调用托管的 AI 模型与 API，其中包括 DeepSeek 模型。

#### 1. 安装

```bash
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz catalog --json
```

该只读命令会输出已验证的客户端目录。macOS 或 Linux 也可使用：

```bash
brew install sandbaseai/tap/sandbaseai-cli
```

#### 2. 连接客户端

```bash
npx -y https://github.com/sandbaseai/cli/releases/download/v0.1.17/sandbaseai-cli-0.1.17.tgz connect
```

按浏览器 OAuth 提示完成认证，然后重启所选客户端。凭据不会放入命令行参数或 URL。

#### 3. 首次运行 DeepSeek

让已连接的客户端使用 DeepSeek V4 模型（例如 `deepseek-v4-pro`）完成编程或推理任务。模型可用性与价格由实时目录返回。DeepSeek V4 支持最高 100 万 Token 上下文；客户端提供该设置时请调整上下文上限。

只读诊断命令：

```bash
sandbase doctor --json
```

客户端、校验和、回滚行为与完整 MCP 工具列表请参阅 [SandBase CLI README](https://github.com/sandbaseai/cli)。

