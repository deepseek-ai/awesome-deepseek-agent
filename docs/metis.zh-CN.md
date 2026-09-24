[English](./metis.md) | [简体中文](./metis.zh-CN.md) | [← 返回](../README.zh-CN.md)

# 在 Metis 中接入 DeepSeek

[Metis](https://github.com/Wholiver/metis) 是开源、终端优先的编程 Agent，提供项目记忆、仓库搜索、验证工具、交互式 TUI、print/JSON 模式、RPC 和 SDK。

> Metis 是独立的第三方项目，本指南不是 DeepSeek 官方文档。

## 1. 安装 Metis

Metis 需要 Node.js 22.19 或更高版本。

```bash
npm install -g @wholiver_hu/metis@rc
```

## 2. 创建 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，然后设置给 Metis：

```bash
export DEEPSEEK_API_KEY="your-deepseek-api-key"
```

如需持久保存，请将该命令加入 shell 配置文件。也可以在交互模式中通过 `/login` 保存 API Key。

## 3. 使用 DeepSeek V4 Pro 启动 Metis

在项目目录中，以最高推理强度启动交互式会话：

```bash
cd /path/to/project
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

`xhigh` 会映射为 DeepSeek V4 Pro 的 `max` 推理强度。Metis 内置了 `deepseek-v4-pro` 和 `deepseek-v4-flash` 的 DeepSeek API 地址及推理内容处理配置。

两个模型都已配置 DeepSeek V4 的 100 万 token 上下文窗口和最高 384,000 token 输出，无需额外配置自定义端点或模型定义。

## 4. 按任务选择模型

复杂实现和调试工作使用 V4 Pro 与最高推理强度：

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

需要更低成本、更快迭代时使用 V4 Flash。它同样支持 100 万 token 上下文窗口，并可通过 `xhigh` 使用 `max` 推理：

```bash
metis --provider deepseek --model deepseek-v4-flash --thinking xhigh
```

进入交互模式后，可使用 `/model` 查看和切换模型；也可在终端运行 `metis --list-models deepseek`。

## 5. 运行第一个任务

在仓库中启动 Metis，然后用自然语言描述任务：

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh
```

```text
审查认证流程，找出缺失的错误处理，实现最小且安全的修复，并运行相关测试。
```

Metis 会在修改文件前检查项目指令和代码，随后记录结果并运行可用验证命令。非交互自动化可使用 `--print` 传入提示词：

```bash
metis --provider deepseek --model deepseek-v4-pro --thinking xhigh --print \
  "在不修改文件的前提下，总结此仓库的测试配置。"
```

## 资源

- [Metis 仓库](https://github.com/Wholiver/metis)
- [Metis 文档](https://github.com/Wholiver/metis/tree/main/docs)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
