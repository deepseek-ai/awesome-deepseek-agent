[English](./deepseeker_code.md) | [简体中文](./deepseeker_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeeker-Code

DeepSeeker-Code 是一个由 DeepSeek 驱动的本地优先 AI 编码助手。自研 agentic 引擎配三种等价入口——VS Code 插件、终端 CLI（React Ink）、本地 HTTP 服务——共享同一套工具链、审批网关与会话存储。它通过 OpenAI 兼容 API 直连 `api.deepseek.com`，支持 DeepSeek V4 模型全量 100 万 token 上下文窗口，推理力度最高可用 `max` 档。

- **GitHub：** <https://github.com/xknk/deepseeker-code>

#### 1. 安装 DeepSeeker-Code

**终端 CLI**（npm）：

```sh
npm install -g deepseeker-code
```

**VS Code 插件**：从 [Releases](https://github.com/xknk/deepseeker-code/releases) 下载 `.vsix` 安装：

```sh
code --install-extension deepseeker-code-<version>.vsix
```

插件自包含——引擎已内联，无需另装 CLI。两个入口共享 `~/.deepseeker-code/` 下的会话与配置，CLI 里开的会话可以在 VS Code 里接着聊。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，然后：

- **CLI**：设置为环境变量：

  ```sh
  export DEEP_SEEK_API_KEY=sk-***
  ```

- **VS Code 插件**：在设置里填 `deepseekerCode.apiKey`。

#### 3. 配置模型（可选）

```sh
export DEEP_SEEK_MODEL=deepseek-v4-pro      # 默认 deepseek-flash
export DEEP_SEEK_AUX_MODEL=deepseek-flash   # 轻量任务（如摘要）
export DEEP_SEEK_REASONING_EFFORT=max       # "high"（默认）或 "max"；low/medium 已废弃，会映射为 high
export DEEP_SEEK_THINKING=0                 # 关闭思考模式（默认开启）
```

DeepSeek V4 模型提供 100 万 token 上下文窗口；DeepSeeker-Code 的自动上下文压缩针对 DeepSeek-V4 调优，长会话压缩后细节不丢——被归档的消息与超长工具结果可经内置 `recall` 工具按需取回。

#### 4. 首次运行

```sh
cd /path/to/your-project
deepseeker-code
```

VS Code 中：命令面板执行 `DeepSeeker-Code: Open Chat`（或按 `Ctrl+Esc`）。

开箱即得的能力：

- **审批网关**：只读工具免审执行；文件修改与危险操作需明确审批，「总是允许」会持久化为 glob 权限规则。
- **两阶段计划模式**：先只读调研，再提交实施方案供你审批，批准后才开始写代码。
- **每次修改都有 diff**：CLI 红绿内联、VS Code 左右对比、或原生 `vscode.diff` 编辑器。
- **MCP / Hooks / Skills / 子 Agent**：四套扩展机制，含经 MCP 接入外部工具。

#### 使用建议

1. 保持审批网关开启，glob 放行规则只授予可信路径。
2. 非平凡任务先走计划模式——agent 动手前先对齐方案。
