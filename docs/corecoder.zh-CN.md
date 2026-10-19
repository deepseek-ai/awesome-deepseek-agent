[English](./corecoder.md) | [简体中文](./corecoder.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 CoreCoder

[CoreCoder](https://github.com/he-yufeng/CoreCoder) 是一个极简、可整读的 coding agent 引擎：约 1.3k 行引擎代码、总共约 2.8k 行纯 Python，一个下午就能读完，然后 fork 成你自己的。它能读写文件、执行 shell、派生子 agent、三档压缩上下文，并且任何会改动你磁盘的工具调用都会先停下来等你确认。

#### 1. 安装 CoreCoder

需要 Python 3.10 或更高版本。

```bash
pip install corecoder
```

如果你打算边读边改（本项目更推荐的方式），从源码安装：

```bash
git clone https://github.com/he-yufeng/CoreCoder
cd CoreCoder
pip install -e .
```

#### 2. 配置 DeepSeek

CoreCoder 原生讲 OpenAI 兼容 API，DeepSeek 开箱即用。导出三个环境变量（或写进项目根目录的 `.env` 文件，启动时自动加载）：

```bash
export OPENAI_API_KEY=sk-...        # 从 https://platform.deepseek.com/api_keys 获取
export OPENAI_BASE_URL=https://api.deepseek.com
export CORECODER_MODEL=deepseek-v4-pro
```

也可以用 `DEEPSEEK_API_KEY` 代替 `OPENAI_API_KEY`，效果相同。

DeepSeek V4 支持最长 1M tokens 的上下文。CoreCoder 的上下文预算默认 128k（超出后走三档压缩）；要吃满整个窗口：

```bash
export CORECODER_MAX_CONTEXT=1000000
export CORECODER_MAX_TOKENS=384000
```

思考链在 CoreCoder 里是一等公民：DeepSeek `reasoning_content` 字段里的思维链会在模型工作时以暗色流式显示，并且永远不会被回塞进对话历史发给 API。CoreCoder 目前不发送 `reasoning_effort` 参数，因此使用服务商默认的思考强度。

#### 3. 开始使用

在你的项目目录里运行：

```bash
corecoder
```

先来一个只读任务，比如 `读一下 main.py 并解释入口逻辑`，再试一个会改代码的：`给 CLI 加一个 --version 选项`。任何会写文件或执行命令的工具调用都会先暂停等你批准。一次性脚本场景用 `corecoder -p "..."`，此时默认拒绝变更类工具，除非显式加 `--yes`。

跑起来之后，仓内还有一个八篇的源码精读系列带你逐行拆引擎（[中文](https://github.com/he-yufeng/CoreCoder/blob/main/article/00-index.md) / [English](https://github.com/he-yufeng/CoreCoder/blob/main/article/00-index_EN.md)），其中第三篇讲的正是上面配置所走的 provider 层。
