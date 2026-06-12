[English](./bitfun.md) | [简体中文](./bitfun.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 BitFun

[BitFun](https://github.com/GCWing/BitFun) 是桌面级 Agent Runtime，也是一套开箱即用的桌面 Agent 应用。它内置 Code、Cowork、Computer Use、Personal Assistant 等 Agent，并提供 MCP、LSP、记忆、Skills、上下文压缩和远程控制能力。

BitFun 很适合接入 DeepSeek V4：它的运行时面向长时间本地会话和 cache-friendly 的 Agent 循环设计。在一次 731 条 trial 的 SWE-Bench-Pro 评测中，BitFun 记录了 **98.67%** 的加权 KV cache 命中率，覆盖 **15.6 亿 cached input tokens**；其中 **83.1%** 的 trial 命中率不低于 **98%**，**51.8%** 不低于 **99%**。

#### 1. 安装 BitFun

从 [BitFun Releases](https://github.com/GCWing/BitFun/releases) 页面下载最新版桌面安装包。

如果你希望从源码运行：

```sh
git clone https://github.com/GCWing/BitFun.git
cd BitFun
pnpm install
pnpm run desktop:dev
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，稍后填入 BitFun 的模型配置。

#### 3. 添加 DeepSeek V4 模型

打开 BitFun，进入 **设置 → 模型配置**。最简单的路径是：

1. 点击 **DeepSeek** 模板。
2. 粘贴你的 DeepSeek API Key。
3. 点击配置项旁边的一键校验按钮。
4. 校验通过后保存配置。

DeepSeek 模板会自动填好官方 API 地址和 OpenAI 兼容请求格式。BitFun 支持 DeepSeek V4 的 **100 万 token 上下文窗口**、**384K 最大输出**和 **max** 推理强度；这些值可以在模型的高级设置中查看或调整。

如果想降低日常迭代成本，可以把 `deepseek-v4-flash` 配置为**快速模型**。它适合 explore、快速扫仓库、轻量 Agent 回合等任务；复杂编码与深度推理任务仍建议默认使用 `deepseek-v4-pro`。

#### 4. 为 Agent 选择模型

在 BitFun 的模型选择器中选择 DeepSeek 模型，然后根据任务选择对应 Agent：

| Agent | 适合场景 |
|-------|----------|
| Code Agent | 仓库探索、代码修改、终端命令、Git、调试和代码审查 |
| Cowork Agent | PDF、DOCX、XLSX、PPTX 与知识工作流 |
| Computer Use | 通过屏幕、鼠标和键盘操作浏览器或桌面应用 |
| Personal Assistant | 长时间助理任务、记忆、日程调度和远程入口 |

#### 5. 验证配置

点击模型配置项旁边的一键校验按钮即可验证配置。校验通过后，在项目目录中启动一个 Code Agent 会话，让它检查仓库或运行一条简单测试命令。

如果模型配置正确，BitFun 会流式返回回答，并将会话保存在本地。会话中也可以输入 `/usage` 查看已记录的运行时与 token 使用情况。

#### 常见问题

- 认证失败：确认 API Key 来自 DeepSeek 开放平台，且没有过期或被撤销。
- 找不到模型：请使用 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- 上下文窗口过小：检查模型高级设置，确认 Context Window Size 已设置为 `1000000`。
- 没有思考过程：检查高级设置，确认已开启 Reasoning Mode，并将 Reasoning Effort 设置为 `max`。

#### 相关资源

- [BitFun GitHub](https://github.com/GCWing/BitFun)
- [BitFun 官网](https://openbitfun.com/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
