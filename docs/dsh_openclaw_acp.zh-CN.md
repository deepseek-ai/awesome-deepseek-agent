[English](./dsh_openclaw_acp.md) | [简体中文](./dsh_openclaw_acp.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 从 OpenClaw 和微信调用 DeepSeek Harness

[`dsh-openclaw-acp`](https://github.com/BeAChanger/dsh-openclaw-acp) 是一个原生 DeepSeek Harness 组合包，通过官方 Agent Client Protocol（ACP）传输暴露 Harness profile。OpenClaw 官方 ACPX 插件可以把该 profile 注册为外部 Agent，因此 OpenClaw 已配置的任何渠道——包括微信——都能调用它。

本集成把三类责任明确分开：

- DeepSeek Harness 负责 Agent、DeepSeek 模型、工具、工作区沙箱与会话日志。
- OpenClaw ACPX 负责 ACP 进程、调度与对话路由。
- OpenClaw 渠道插件负责微信认证、发送者身份与消息投递。

本组合包不会读取或转发微信凭据与发送者标识；这些渠道信息仍由 OpenClaw 负责。

## 1. 安装 DeepSeek Harness 与组合包

前置条件：

- pnpm 10，以及 OpenClaw 支持的 Node.js 版本；稳定版 OpenClaw `2026.7.1-2` 要求 Node.js 22.22.3+、24.15.0+ 或 25.9.0+
- 一个 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- OpenClaw `2026.7.1-2` 或更高版本，并已配置渠道；微信渠道可参考腾讯 [`openclaw-weixin`](https://github.com/Tencent/openclaw-weixin)

安装当前已验证的 Harness 版本与组合包：

```bash
npm install -g pnpm@10.28.2 @deepseek-ai/dsh@0.1.0-rc.6
dsh plugin --profile openclaw add https://github.com/BeAChanger/dsh-openclaw-acp/releases/download/v0.1.3/dsh-openclaw-acp-0.1.3.tgz
dsh --profile openclaw --dump-config
```

该命令使用预构建的 release 产物（SHA-256：`51ab3d78a7505448b5827b84a79081ae9fd11a5553949eafa3a317b5ee4763fd`），安装时不会执行仓库构建脚本。Release 同时提供校验文件。

配置输出中应同时出现 `id: openclaw-acp` 和 `name: dsh-openclaw-acp`。

让 OpenClaw Gateway 进程可以读取 API Key：

```bash
export DEEPSEEK_API_KEY="your-api-key"
```

PowerShell：

```powershell
$env:DEEPSEEK_API_KEY = "your-api-key"
```

如果 OpenClaw 作为系统服务运行，应在服务环境中配置变量，不能只在交互式终端中临时设置。

## 2. 在 OpenClaw 注册 Harness

安装并启用 OpenClaw 官方 ACP runtime：

```bash
openclaw plugins install @openclaw/acpx@2026.7.1
openclaw config set plugins.entries.acpx.enabled true
```

如需接入微信，安装本组合已验证的腾讯渠道版本。最后一条命令会显示二维码，必须由运营方确认授权：

```bash
openclaw plugins install @tencent-weixin/openclaw-weixin@2.4.6
openclaw config set plugins.entries.openclaw-weixin.enabled true
openclaw channels login --channel openclaw-weixin
```

把以下设置加入 OpenClaw 配置：

```json5
{
  acp: {
    enabled: true,
    backend: "acpx",
    defaultAgent: "deepseek-harness",
    allowedAgents: ["deepseek-harness"]
  },
  plugins: {
    entries: {
      acpx: {
        enabled: true,
        config: {
          agents: {
            "deepseek-harness": {
              command: "dsh",
              args: ["--profile", "openclaw"]
            }
          }
        }
      },
      "openclaw-weixin": {
        enabled: true
      }
    }
  }
}
```

修改插件配置后重启 Gateway。

## 3. 首次运行

先在 OpenClaw 对话中验证 runtime，再交付真实任务：

```text
/acp doctor
/acp spawn deepseek-harness --cwd /工作区绝对路径
```

使用微信渠道时，在连接到同一个 Gateway 的微信会话中发送相同命令。消息链路是：

```text
微信 -> OpenClaw 渠道 -> ACPX -> dsh --profile openclaw -> DeepSeek Harness
```

多个微信号同时登录时，建议按账号、渠道和发送者隔离私聊会话：

```bash
openclaw config set session.dmScope per-account-channel-peer
```

如果渠道声明了当前对话绑定能力，可以加 `--bind here`，让后续消息继续进入同一个 ACP 会话。如果渠道没有该能力，就使用不绑定的一次性命令；OpenClaw 会把完成结果回传给父对话。

## DeepSeek V4 配置

组合包使用已验证的 `deepseek-official` Harness 适配器，并配置：

- 模型：`deepseek-v4-flash`
- thinking：启用
- 推理强度：`max`
- 上下文窗口：1,000,000 token
- 输出上限：384,000 token

任务需要更强模型时，可在 Gateway 环境中选择 DeepSeek V4 Pro：

```bash
export DSH_OPENCLAW_MODEL=deepseek-v4-pro
```

Harness 会原样传递模型名；`deepseek-v4-flash` 和 `deepseek-v4-pro` 共用 1M 上下文与最大推理强度 profile。

## 安全边界与当前协议限制

- OpenClaw 沙箱不会包裹外部 ACP 进程。DeepSeek Harness 通过自己的 `DSH_PERMISSION_MODE` 执行边界；普通部署保留默认 `workspace-write`。
- ACPX 默认只批准读取。写文件或执行 shell 的任务可能在运维者选择非交互权限策略前失败。只有在独立操作系统账号和受限工作区中才使用 `approve-all`；它不适合作为共享 Gateway 的默认值。
- 暂时不要为此 Agent 启用 OpenClaw ACPX 的 MCP 工具桥。Harness ACP `0.1.0-rc.6` 会拒绝非空 `mcpServers`。
- Harness ACP 当前只支持新会话，不声明加载、恢复、fork 或会话列表能力。
- ACP 只返回已提交的 assistant 文本，不转发实时推理或工具事件。
- 持久对话绑定取决于渠道适配器；不支持绑定时仍可使用一次性父对话回传。

## 验证证据

组合包仓库包含单元、打包和真实协议检查。冒烟测试会把打包产物安装进隔离 profile，并两次完成 `initialize` 与 `session/new`：先直接启动已发布的 `dsh` CLI 并验证纯 JSON-RPC stdout，再通过 OpenClaw 官方 ACPX 插件所使用的已发布 `acpx@0.11.2` runtime，以自定义 Agent 注册方式拉起该 profile：

```bash
git clone https://github.com/BeAChanger/dsh-openclaw-acp.git
cd dsh-openclaw-acp
pnpm install
pnpm test
pnpm run test:acp
pnpm audit --prod --audit-level high --registry https://registry.npmjs.org
```

协议冒烟不会发起模型请求；只有首次通过 OpenClaw 发送真实提示词时才需要有效 API Key。另一个隔离的 OpenClaw `2026.7.1-2` 状态目录中，`@openclaw/acpx@2026.7.1` 与 `@tencent-weixin/openclaw-weixin@2.4.6` 均以启用状态成功加载，所有必需依赖完整；包含自定义 Agent、微信渠道和多账号会话隔离的组合配置通过了 `openclaw config validate`。扫码登录与真实消息投递仍需由运营方完成。

## 参考资料

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness 插件打包](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.zh.md)
- [OpenClaw ACP Agent](https://github.com/openclaw/openclaw/blob/main/docs/tools/acp-agents.md)
- [OpenClaw ACPX 配置](https://github.com/openclaw/openclaw/blob/main/docs/tools/acp-agents-setup.md)
- [腾讯 OpenClaw 微信渠道](https://github.com/Tencent/openclaw-weixin)
