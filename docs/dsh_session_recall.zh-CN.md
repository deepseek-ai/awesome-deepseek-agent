[English](./dsh_session_recall.md) | [简体中文](./dsh_session_recall.zh-CN.md) · [← Back](../README.md)

# 集成 dsh-session-recall

dsh-session-recall 是 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH，DeepSeek 官方 Agent 运行时）的开源插件。它给 agent 提供一个 `recall` 工具，可以全文检索自己过往的会话原文："上周修的那个 bug"、"简历选的什么字体"。官方 `@deepseek-ai/dsh-session-query` 服务刻意不提供模型可调用的工具和调用方授权；本插件通过可信的 `ctx.sessionQuery` 缝补齐这两点——默认把每次调用限定在调用方 agent 的项目目录内——并把 Harness 默认关闭的 FTS 索引改为持久化落盘。

#### 1. 前置条件：已安装 DeepSeek Harness

这是一个 DSH out-of-tree 插件，需要先有 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 环境。不需要额外 API key——检索走 DSH 自己的查询引擎，沿用 Harness 已配置的任意 provider。

#### 2. 把插件装进 profile

```
dsh plugin --profile web add dsh-session-recall
```

包声明了 `dsh.bundle`，会自动加入 profile 的插件层栈。它的 bundle patch 还会开启 FTS 索引（`openAt: first-search`）并指向 `<DSH_HOME>/session-recall/` 下的持久化数据库，替换官方默认的内存索引。之后重启 `dsh web` 进程，让新安装的层生效。

#### 3. 直接问过去的事

正常对话即可：

> "上周简历模板的字体是怎么改的？"

当用户提到之前做过的事、或早期上下文被压缩掉时，模型会自己调用 `recall`。每条命中返回该会话最强匹配事件的摘要——标题、日期、会话 id——并在 Web UI 里渲染成原生搜索卡片。模型按需使用的变体：

- `all_projects: true` —— 搜索所有项目目录的会话，而不只是当前项目
- `session_id` —— 只搜某一个会话内的事件
- `limit` / `cursor` —— 翻页
