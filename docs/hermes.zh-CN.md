[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Hermes 智能体

Hermes 是由 [Nous Research](https://nousresearch.com) 打造的开源自我进化 AI 智能体。它内置学习闭环：能够从经验中生成技能，在使用过程中持续优化，沉淀知识，并在跨会话中逐步构建你偏好的动态模型。

Hermes 通过多个提供商后端支持 DeepSeek V4 Pro 和 V4 Flash 作为主力模型，让你在最大化能力和成本效率之间灵活选择。

> **DeepSeek V4 系列是 Hermes 的推荐主力模型。** 它们在推理能力、上下文长度（100万token）和成本之间提供了最佳平衡，非常适合智能体工作流。

---

#### 1. 安装 Hermes

##### 快速安装

通过一行安装命令，你可以在两分钟内快速启动 Hermes Agent。

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

唯一前置依赖是 Git，其余内容安装脚本会自动处理。

更多安装说明请参考 [Hermes 安装文档](https://hermes-agent.nousresearch.com/docs/getting-started/installation)。

#### 2. 配置 DeepSeek 作为提供商

##### 方式 A：快速设置（自动配置）

重新加载 shell 后，开始配置 Hermes：

- 执行 `hermes setup` 命令
- 选择 **Quick Setup** 选项
- 当提示选择模型提供商时，选择 **DeepSeek**
- 输入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Base URL 填写 `https://api.deepseek.com`
- 选择 `deepseek-v4-pro`（推荐用于复杂推理）或 `deepseek-v4-flash`（更快、成本更低）
- 继续完成其余配置选项

##### 方式 B：手动配置（高级）

如需精细控制，直接编辑 `~/.hermes/config.yaml`：

```yaml
model:
  default: deepseek-v4-pro
  provider: deepseek

providers:
  deepseek:
    api_key: ${DEEPSEEK_API_KEY}     # 通过环境变量或直接填入
    base_url: https://api.deepseek.com
    type: openai_compatible
```

要启用 100 万 token 上下文窗口，在模型名后添加 `[1m]` 后缀：

```yaml
model:
  default: deepseek-v4-pro[1m]           # 启用 100 万上下文
```

##### 方式 C：OpenCode Go 提供商（推荐用于编程）

如需在终端中通过 DeepSeek 进行原生编程，可将 Hermes 配置为使用 [OpenCode Go](https://github.com/opencode-ai/opencode) 提供商。[GenTech Labs](https://github.com/ProtoJay4789/genTech-agent-kit) 在生产环境中即采用此方案——以 DeepSeek V4 Flash 为主力模型 24/7 全天候运行。

```bash
# 安装 OpenCode Go
curl -fsSL https://opencode.ai/install.sh | bash
```

然后配置 Hermes：

```yaml
model:
  default: deepseek-v4-flash
  provider: opencode-go

providers:
  opencode-go:
    api_key: ${DEEPSEEK_API_KEY}
    base_url: https://api.deepseek.com
    type: openai_compatible
```

#### 3. 多配置文件模型路由

一个强大的模式是运行两个 Hermes 配置来实现成本优化的模型路由——使用 V4 Flash 进行草稿和快速迭代，使用 V4 Pro 进行深度分析：

```bash
# 创建第二个配置
hermes profile create deepseek-pro
```

为每个配置设置不同的模型：

| 配置 | 模型 | 用途 |
|---------|-------|----------|
| `default` | `deepseek-v4-flash` | 日常任务、草稿、快速迭代 |
| `deepseek-pro` | `deepseek-v4-pro[1m]` | 代码审计、复杂推理、100 万上下文 |

随时切换配置：

```bash
hermes profile switch deepseek-pro
```

#### 4. 思考 / 推理深度设置

DeepSeek V4 Pro 支持可配置的推理级别。对于 Claude Code 兼容的端点，设置：

```bash
export CLAUDE_CODE_EFFORT_LEVEL=max
```

对于 OpenAI 兼容的提供商，在支持的请求参数中包含 `reasoning_effort`。Hermes 默认自动处理推理内容的回传——无需手动配置。

#### 5. 验证设置

```bash
# 查看当前模型和提供商
hermes status

# 发送测试提示
hermes run "我现在使用的是哪个 DeepSeek 模型？"
```

预期输出：

```
Model: deepseek-v4-flash (opencode-go)
Provider: opencode-go
```

#### 6. 生产环境部署

搭配 DeepSeek V4 模型的 Hermes 可以 24/7 全天候自主运行，具备：

- **定时任务** — 自动化日常任务（每日简报、研究扫描、投资组合监控）
- **多通道网关** — 同时运行 Telegram、Discord、CLI 等多个通信渠道
- **技能自学习** — Hermes 从经验中自动编写新技能并持久化
- **跨会话记忆** — 通过内置的 Honcho 记忆系统实现

参考案例：[GenTech Labs](https://github.com/ProtoJay4789/genTech-agent-kit) 以 DeepSeek V4 Flash 作为主力生产模型，在单台 VPS 上运行 30+ 个定时任务、4 个通信渠道、200+ 个技能，实现全天候稳定运行。

#### 7. 故障排除

| 问题 | 解决方法 |
|---------|---------|
| `Model not found` 错误 | 确保模型名使用 V4 格式：`deepseek-v4-pro` 或 `deepseek-v4-flash`（不要使用已弃用的 `deepseek-chat`）|
| 上下文窗口错误 | 使用 `[1m]` 后缀：`deepseek-v4-pro[1m]` |
| 频率限制 | 在 config.yaml 中添加备用提供商，自动在限流时重试 |
| 推理内容回传问题 | 升级 Hermes 到最新版本——此问题已自动处理 |

---

#### 参考资源

- [Hermes 官方文档](https://hermes-agent.nousresearch.com/docs)
- [DeepSeek 平台](https://platform.deepseek.com/) — 获取 API Key
- [DeepSeek API 文档](https://api-docs.deepseek.com/) — API 参考
- [Hermes GitHub 仓库](https://github.com/NousResearch/hermes-agent)
- [OpenCode Go](https://github.com/opencode-ai/opencode) — 替代提供商后端
