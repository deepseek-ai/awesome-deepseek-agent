[English](./continue.md) | [简体中文](./continue.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Continue

Continue 是一个开源的 AI 编程助手，支持 VS Code 和 JetBrains，提供可自定义的模型供应商和 Agent 工作流。

#### 1. 安装 Continue

- **VS Code：** 打开扩展视图（`Ctrl+Shift+X`），搜索 `Continue`，安装 Continue Dot 开发的扩展。
- **JetBrains：** 打开 Settings → Plugins → Marketplace，搜索 `Continue` 并安装。

#### 2. 获取 DeepSeek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建一个 API Key。
- 复制该 key（以 `sk-` 开头）。

#### 3. 打开 Continue 配置文件

Continue 的 YAML 配置文件位于：

- **VS Code：** `~/.continue/config.json` 或 `~/.continue/config.yaml`
- **JetBrains：** `~/.continue/config.json` 或 `~/.continue/config.yaml`

你也可以在 VS Code 中通过点击 Continue 侧边栏的齿轮图标，选择 **Open Config** 来打开配置文件。

#### 4. 添加 DeepSeek 模型配置

将以下配置粘贴到你的 `~/.continue/config.yaml` 中：

```yaml
models:
  - name: DeepSeek · V4 Pro (Thinking None)
    provider: deepseek
    model: deepseek-v4-pro
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        thinking:
          type: disabled

  - name: DeepSeek · V4 Pro (Thinking High)
    provider: deepseek
    model: deepseek-v4-pro
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        reasoning_effort: high
        thinking:
          type: enabled

  - name: DeepSeek · V4 Pro (Thinking Max)
    provider: deepseek
    model: deepseek-v4-pro
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        reasoning_effort: max
        thinking:
          type: enabled

  - name: DeepSeek · V4 Flash (Thinking None)
    provider: deepseek
    model: deepseek-v4-flash
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        thinking:
          type: disabled

  - name: DeepSeek · V4 Flash (Thinking High)
    provider: deepseek
    model: deepseek-v4-flash
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        reasoning_effort: high
        thinking:
          type: enabled

  - name: DeepSeek · V4 Flash (Thinking Max)
    provider: deepseek
    model: deepseek-v4-flash
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use
    requestOptions:
      extraBodyProperties:
        reasoning_effort: max
        thinking:
          type: enabled
```

> **关于 `${{ secrets.DEEPSEEK_API_KEY }}`：** Continue 支持使用 `${{ secrets.VAR_NAME }}` 语法引用密钥。当 Continue 遇到该语法时，会按以下顺序查找密钥来源：
> 1. **工作区 `.env` 文件** — `<workspace-root>/.env`
> 2. **工作区 Continue `.env` 文件** — `<workspace-root>/.continue/.env`
> 3. **全局 `.env` 文件** — `~/.continue/.env`
> 4. **进程环境变量** — 系统环境变量（仅 [Continue CLI](https://docs.continue.dev/cli/configuration) 有效）
>
> 在上述任一位置创建 `.env` 文件，写入 `DEEPSEEK_API_KEY=sk-your-key`（不要加引号）。添加或更改密钥后请重启 IDE。
>
> **重要提示：** VS Code 和 JetBrains 扩展无法读取通过 `export` 设置的终端环境变量，必须使用 `.env` 文件。
>
> 你也可以直接将 `${{ secrets.DEEPSEEK_API_KEY }}` 替换为你的 API Key 字符串。

> **提示：** 你不需要包含全部 6 个配置。只选取你实际使用的模型名称和思考模式即可——例如一个 V4 Pro 和一个 V4 Flash 配置就足以开始使用。

#### 5. 使用模型

- 打开 VS Code 中的 Continue 侧边栏（或 JetBrains 中的 Continue 工具窗口）。
- 点击聊天面板底部的模型选择器，选择已配置的 DeepSeek 模型之一。
- 开始使用 Continue 的 Agent 功能——以上所有配置均启用了 `tool_use`。

<div align="center">
<img src="./assets/continue_vscode_models.png" width="720" border="1" />
</div>

#### 可选：1M 上下文窗口

DeepSeek V4 模型支持最多 **100 万 tokens** 的上下文。默认情况下 Continue 会从供应商读取上下文窗口限制。如果需要手动调整，可以在模型配置中添加 `contextLength` 字段：

```yaml
  - name: DeepSeek · V4 Pro (Thinking Max)
    provider: deepseek
    model: deepseek-v4-pro
    apiKey: ${{ secrets.DEEPSEEK_API_KEY }}
    contextLength: 1000000
    ...
```

#### 可选：思考强度级别

DeepSeek V4 Pro 通过 `extraBodyProperties` 配置三种思考模式：

| 模式 | `thinking.type` | `reasoning_effort` | 适用场景 |
|------|----------------|-------------------|----------|
| **Thinking None** | `disabled` | （省略） | 简单任务、快速响应、低成本 |
| **Thinking High** | `enabled` | `high` | 复杂编码，适度的推理深度 |
| **Thinking Max** | `enabled` | `max` | 深度推理、架构设计、最困难的任务 |

DeepSeek V4 Flash 支持相同的思考级别以保持一致性。

> **注意：** `reasoning_effort: max` 能提供最佳的编程体验，推荐用于深度架构工作。当你需要更快的响应时，可以切换到 `high` 或 `disabled`。
