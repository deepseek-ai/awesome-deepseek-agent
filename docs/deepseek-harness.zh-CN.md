[English](./deepseek-harness.md) | [简体中文](./deepseek-harness.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）是 DeepSeek 的开源 agent harness——「一切皆插件」，由 [Cordis](https://github.com/cordiverse/cordis) 驱动。它以终端 CLI 或本地 Web UI 运行，开箱即用 DeepSeek V4 Pro / Flash。本指南介绍安装、配置与首次运行。

#### 1. 安装依赖

- [Node.js](https://nodejs.org/en/download/) 18+。

直接用 npm 运行 dsh（无需全局安装）：

```shell
npx @deepseek-ai/dsh web
```

首次运行会下载包，然后启动 Web UI，默认地址 `http://127.0.0.1:3080`。

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并复制。

#### 3. 配置 DeepSeek V4

dsh 通过环境变量读取模型后端。把下面几行写入 shell 配置（`~/.zshrc` / `~/.bashrc`）：

```shell
export DEEPSEEK_API_KEY="sk-你的DeepSeek-API-Key"
export DEEPSEEK_DEFAULT_MODEL="deepseek-v4-pro"
```

dsh 默认走 DeepSeek 官方 API，无需设置 base URL。DeepSeek V4 Pro / Flash 支持最高 **100 万 token** 的上下文，V4 Pro 还支持多档推理强度（`max` 与 `high`）——建议保持 `max` 以获得最佳编码体验。

#### 4. 运行 dsh

```shell
source ~/.zshrc
npx @deepseek-ai/dsh web
```

在浏览器打开 `http://127.0.0.1:3080`。

#### 5. 首次运行

新建会话，给一个能验证模型的任务：

```text
用一句话介绍你自己，并告诉我你现在的模型 ID。
```

如果回复带 `deepseek-v4-pro`，说明路由成功。

#### 可选：第三方 OpenAI 兼容端点

dsh 是 OpenAI 兼容的，可以指向任意 OpenAI 格式端点——例如带免费 DeepSeek V4 档的提供商：

```shell
export DEEPSEEK_API_KEY="sk-teamo-你的Key"
export DEEPSEEK_BASE_URL="https://api.teamorouter.com/v1"
export DEEPSEEK_DEFAULT_MODEL="deepseek-v4-pro-free"
```

这样 dsh 就指向 [TeamoRouter](https://teamorouter.com/docs/install-deepseek-harness)，它提供 `deepseek-v4-pro-free` / `deepseek-v4-flash-free`，各 200 次/天（无需绑卡）。
