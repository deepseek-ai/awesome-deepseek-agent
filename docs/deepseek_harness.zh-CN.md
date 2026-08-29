[English](./deepseek_harness.md) | [简体中文](./deepseek_harness.zh-CN.md) · [← Back](../README.md)

# 接入 DeepSeek Harness

DeepSeek Harness 是 DeepSeek 自研的、基于 Cordis 插件框架的 Agent harness：每一项能力都是通过 `cordis.yml` profile 组合起来的插件，模型经由这些插件扩展的工具接缝运行。它可以在终端无头运行、作为 Web UI 使用，也可以作为 ACP 自动化服务器，并从 npm 或 GitHub 安装社区插件。

#### 1. 安装 Node.js 与 pnpm

- 安装 [Node.js](https://nodejs.org/en/download/) 22.19+（或 24+）。
- 安装 [pnpm](https://pnpm.io/installation) 11。

#### 2. 获取 DeepSeek API Key

从 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 获取 API Key，然后导出：

```
export DEEPSEEK_API_KEY=sk-...
```

Windows PowerShell：`$env:DEEPSEEK_API_KEY = "sk-..."`。

#### 3. 运行 harness

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm dsh web                                  # Web UI 位于 http://127.0.0.1:3080
pnpm dsh --profile headless "你的任务"          # 无头运行
```

DeepSeek Harness 搭配 DeepSeek-V4 系列模型使用，支持最高 **100 万 token** 上下文；**DeepSeek-V4-Pro** 还支持 **max** 推理强度——详见 [Thinking Mode 文档](https://api-docs.deepseek.com/guides/thinking_mode)。

#### 4. 安装插件

插件是声明了 `dsh.bundle` manifest 的 npm 包，安装到指定 profile：

```
dsh plugin --profile web add dsh-auto-review
```

社区注册表见 [awesome-dsh-plugin.com](https://awesome-dsh-plugin.com) 与 [deepseek1024.com](https://deepseek1024.com) 商店，官方文档见 [deepseek.com/harness](https://www.deepseek.com/harness)。
