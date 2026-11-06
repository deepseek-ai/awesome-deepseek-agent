[English](./jiuwenswarm.md) | [简体中文](./jiuwenswarm.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 JiuwenSwarm

JiuwenSwarm 是一个开源（Apache-2.0）的多智能体工作台，基于 [openJiuwen](https://openjiuwen.com/en/) 构建。在集群模式下，**Leader** Agent 会将复杂任务拆解为多个阶段，并组建一支由专业 **Teammates** 构成的团队；Skills 可被复用，可通过 Swarm Skills Hub 共享，并依据执行反馈持续改进。同一个 Agent 可从浏览器、终端 TUI，或你已在使用的聊天应用（飞书、钉钉、企业微信、微信和小艺；Telegram、Discord、Slack 和 WhatsApp）访问。它支持 OpenAI 兼容的模型提供商，包括 DeepSeek。

#### 1. 安装 JiuwenSwarm

##### 前置要求

- `workswarm` PyPI 包要求 Python 3.11–3.13（`>=3.11,<3.14`）；从源码安装还支持 3.14。
- Node.js 18+ 仅用于源码安装（构建前端），20+ 用于浏览器自动化；普通聊天不需要它。

##### pip 安装

```bash
# 创建并激活虚拟环境
python -m venv jiuwenswarm-env
source jiuwenswarm-env/bin/activate   # Windows 下为：jiuwenswarm-env\Scripts\activate

# 安装 JiuwenSwarm（PyPI 包名：workswarm）
pip install workswarm

# 首次初始化
jiuwenswarm-init

# 启动服务
jiuwenswarm-start
```

> PyPI 包名为 `workswarm`（由 `jiuwenswarm` 更名而来）；CLI 命令（`jiuwenswarm-init`、`jiuwenswarm-start`，以及 `jiuwenswarm chat` 子命令）和 `~/.jiuwenswarm` 数据目录保留 JiuwenSwarm 这一名称。

##### 桌面应用

官方也为 Windows 10/11 和 macOS 11+（仅 Apple Silicon）提供预编译安装包；HarmonyOS PC 请从官网 <https://openjiuwen.com/en/jiuwenswarm> 安装。安装后从桌面启动即可，无需执行上面的 `jiuwenswarm-*` 命令。

#### 2. 配置 DeepSeek

1. 启动 JiuwenSwarm 并打开 Web UI（默认 <http://localhost:5173>）。
2. 在左侧边栏打开「**设置**」→「**模型**」（旧版本为「**更多**」→「**配置信息**」）。
3. 添加或编辑默认模型。先选择「**模型提供商**」，再填写：

| 字段 | 值 |
| --- | --- |
| 模型提供商 | `DeepSeek`（内置预设；仅当你的版本没有 DeepSeek 预设时，才选择「**自定义**」或 `OpenAI`） |
| 模型名称 | `deepseek-v4-pro`（最适合复杂的多智能体与编程任务）或 `deepseek-v4-flash`（更快、更便宜） |
| API Key | 你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| API URL | `https://api.deepseek.com` —— 仅在「**自定义**」时显示；DeepSeek 预设已使用该地址。**不要**追加 `/chat/completions` |

4. 将该条目标记为「**主模型**」（默认模型），点击 **测试** 验证连接，然后确认对话框并保存。保存会热加载配置；少数改动会触发服务重启。

> 开箱即用时，JiuwenSwarm 使用 256K 上下文窗口和提供商的默认推理强度。DeepSeek V4 支持 1M 上下文和 `max` 推理强度 —— 请在下一步中启用这两项。

#### 3. 启用 1M 上下文与 max 推理强度

DeepSeek V4 模型最高支持 **100 万 token** 的上下文和 **`max`** 推理强度。JiuwenSwarm 不会根据模型名称推断这两项，因此请在 `~/.jiuwenswarm/config/config.yaml` 中显式设置（该文件在首次启动时创建；Windows 下为 `%USERPROFILE%\.jiuwenswarm\config\config.yaml`）。

在标记为 `is_default: true` 的模型条目中添加这些键，并将上下文引擎的预算提高到相同的值：

```yaml
models:
  defaults:
    - model_id: mdl_default_primary   # 保留你文件中已有的 model_id
      model_client_config:
        api_base: https://api.deepseek.com
        api_key: sk-your-deepseek-api-key
        model_name: deepseek-v4-pro
        client_provider: DeepSeek
      model_config_obj:
        temperature: 0.95
        reasoning_level: max        # DeepSeek V4 提供 off / low / high / max
        context_window: 1000000     # 1M tokens（256K 为内置默认值）
      is_default: true
react:
  context_engine_config:
    context_window_tokens: 1000000
```

- `reasoning_level: max` 会作为推理强度 `max` 发送给 DeepSeek V4；`off`、`low` 和 `high` 是其他受支持的级别。在「**设置 → 模型 → 编辑模型**」的对话框中，同一设置以 **推理** 的形式提供，因此你也可以在那里选择 `max`，而不必编辑 YAML。
- `model_config_obj.context_window` 向模型层声明该模型的真实上下文窗口，而 `react.context_engine_config.context_window_tokens` 则是 JiuwenSwarm 上下文压缩引擎使用的预算（未设置时会回退为 256K，且优先于单模型的值）。两者都应设置，这样 1M 窗口才会同时用于模型层和上下文压缩；压缩会在达到预算的 80% 时启动。

> 如果 `jiuwenswarm-init` 在文件中留下了 `${API_BASE}` / `${API_KEY}` / `${MODEL_NAME}` 占位符，请将它们替换为字面值，或导出与之匹配的 `API_BASE`、`API_KEY`、`MODEL_NAME` 和 `MODEL_PROVIDER` 环境变量。从 Web UI 保存的配置会以字面值写入。

保存文件 —— JiuwenSwarm 会监视该文件并自动重新加载。如果某项改动未生效，请重启服务。

#### 4. 开始第一次对话

- **Web UI**：打开 Web UI（默认 <http://localhost:5173>）并进入 **聊天**。在聊天输入区选择执行模式：
  - **Agent 模式** —— 由单个 Agent 负责规划与执行；适合日常问答和代码生成。
  - **集群模式** —— 由 Leader Agent 拆解任务并协调专业 Teammates；适合大型、多步骤的工作。
- **终端 TUI**：`jiuwenswarm chat "..."` 用于一次性提示词，`jiuwenswarm chat` 用于交互式会话。使用 `/mode` 切换子模式（`agent.plan`、`agent.fast`、`code.normal`、`code.team`、`team`），使用 `/model` 切换模型。
- **聊天应用**：在 Web UI 的频道设置中启用频道（或在 `config.yaml` 中设置 `enabled: true` 并填入对应平台的凭据），即可从飞书、钉钉、企业微信、微信、小艺、Telegram、Discord、Slack 或 WhatsApp 与同一个 Agent 对话。在群聊中，请 @ 提及机器人。

集群模式的示例提示词：

```text
对新能源汽车行业进行深入研究，并生成一份分析报告。
```

#### 5. 故障排查

- **模型测试失败**：检查 API Key 是否有效、base URL 是否可达，并确保 `api_base` 不带 `/chat/completions` 后缀；模型名称和提供商必须与端点匹配。
- **Web UI 无法访问**：检查服务横幅（`http://localhost:5173`；如果端口被占用，启动器会选择下一组空闲端口并将其打印出来）以及 `~/.jiuwenswarm/logs/` 中的错误。
- **改动被忽略**：从 Web UI 再次保存，或使用 `jiuwenswarm-start` 重启；检查 YAML 缩进。
- **1M 上下文或 max 推理强度未生效**：确认这些键位于标记为 `is_default: true` 的条目上，然后检查 `~/.jiuwenswarm/logs/` 中的配置错误。
- **上下文窗口仍为 256K**：无效的 `context_window` / `context_window_tokens` 值会被静默忽略 —— 请使用诸如 `1000000` 的正整数。
- **远程访问**：运行 `FRONTEND_HOST=0.0.0.0 jiuwenswarm-start` 暴露 Web UI，然后从另一台机器打开 `http://<server-ip>:5173`。

上游参考：[安装指南](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/InstallGuide.md) · [配置](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/Configuration.md) · [常见问题](https://github.com/openJiuwen-ai/jiuwenswarm/blob/develop/docs/en/FAQ.md)
