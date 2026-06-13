[English](./langdriver.md) | [简体中文](./langdriver.zh-CN.md) · [← Back](../README.md)

# 集成 LangDriver

LangDriver 是一个极简的 ReAct Agent——约 500 行 Ruby。它将 ReAct 循环与 macOS Seatbelt 硬沙箱结合，支持 MCP 协议、声明式 Skill 安装、持久记忆与异步压缩。开箱即用，针对 DeepSeek 调优。

- **GitHub:** <https://github.com/kevin0x5/langdriver>

#### 1. 安装 LangDriver

需要 **macOS** 和 **Ruby 3.0+**（使用 Ruby 3 自带的 Reline）。

```sh
git clone https://github.com/kevin0x5/langdriver && cd langdriver
```

#### 2. 配置 LangDriver

设置 DeepSeek API key：

```sh
export DEEPSEEK_API_KEY=sk-xxx
```

默认 `langdriver.yaml` 已针对 DeepSeek 调优：

```yaml
runtime:
  model: deepseek-v4-pro                # 或 deepseek-v4-flash（更便宜更快）
  compact_model: deepseek-v4-flash      # 异步压缩用
  api_base: https://api.deepseek.com
  api_key_env: DEEPSEEK_API_KEY
  max_steps: 50
  extra:
    max_tokens: 384000                  # DeepSeek v4 单次最大输出
    reasoning_effort: max               # 复杂 Agent 任务建议 max
    thinking: { type: enabled }         # 开启思维链（DeepSeek-V3.2+ 支持思考模式下的工具调用）
```

从 [DeepSeek 平台](https://platform.deepseek.com/api_keys) 获取 API Key。

> **注意：** DeepSeek v4 原生支持 1M 上下文，无需额外开关。`runtime.extra` 配置块会原样透传到 chat/completions 请求体。

**主要配置文件：**

| 文件 | 作用 |
|---|---|
| `profile.md` | 助手的人格 / 语气（system prompt） |
| `tools.yaml` | 全局安全天花板——能读写什么、能否联网 |
| `skills.yaml` | 每个 Skill 的开关 / 信任级别 / 优先级 |
| `mcp.yaml` | MCP server 连接信息 |
| `hooks.yaml` | `after_user_prompt` / `after_tool_use` 提醒文本 |

#### 3. 运行 LangDriver

```sh
ruby langdriver.rb
```

进入 REPL 后：

```
> 读 sample.txt 用一句话总结
```

模型自己调 `read` 拿到文件内容，再调 `final_answer`。**没有写死流程，没有提示词模板，每一步都是模型自己决定的。**

#### REPL 常用命令

| 命令 | 功能 |
|---|---|
| `/exit` | 退出 |
| `/clear` | 清空当前会话（记忆保留） |
| `/memory` | 查看持久记忆 |
| `/remember <fact>` | 追加一条事实到长期记忆 |
| `/todos` | 查看任务清单 |
| `/skill list` | 列出已安装的 Skill |
| `/skill install <url> <name>` | 安装社区 Skill（克隆后入 Seatbelt 沙箱） |
| `/mcp` | 列出 MCP 提供的工具 |

#### 安全模型

通过 `skill install` 安装的社区 Skill 运行在 **macOS Seatbelt 沙箱** 内，含动态生成的 deny-by-default 安全策略。三层权限求交（Skill 声明 × 本地覆盖 × 全局天花板）和 core/external 信任分级，确保不可信脚本无法越权读写或联网。

