[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Hermes

Hermes 是 Nous Research 打造的开源自我进化 AI Agent。它内置学习闭环：能够从经验中生成技能，在使用过程中持续优化，沉淀知识，并在跨会话中逐步构建你偏好的动态模型。

#### 1. 安装 Hermes

##### 快速安装

通过一行安装命令，你可以在两分钟内快速启动 Hermes Agent。

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

唯一前置依赖是 Git，其余内容安装脚本会自动处理。

更多安装说明请参考 [Hermes 安装文档](https://hermes-agent.nousresearch.com/docs/getting-started/installation)。

#### 2. 运行并配置

重新加载 shell 后，开始配置 Hermes：

- 执行 `hermes setup` 命令
- 选择 Quick Setup
- 当提示选择模型提供商时，选择 **DeepSeek**
- 输入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Base URL 填写 `https://api.deepseek.com`
- 选择 `deepseek-v4-pro` 模型
- 继续完成其余配置选项

#### 3. 思考模式与常见错误

##### 关于思考模式

DeepSeek 模型默认开启思考模式（Thinking Mode）。在工具调用场景下，模型会生成 `reasoning_content`（思维链内容），且根据 [DeepSeek 思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)，工具调用后的 `reasoning_content` 必须随对话历史回传给 API。

Hermes 的 `display.show_reasoning` 默认值为 `false`，会从对话历史中移除 `reasoning_content`，可能导致 HTTP 400 错误。

##### 400 错误处理

如果运行时出现以下错误：

```
HTTP 400: The `reasoning_content` in the thinking mode must be passed back to the API.
```

这说明 `reasoning_content` 未正确回传。以下为两种处理方案：

**方案一：关闭思考模式（推荐）**

编辑 `~/.hermes/config.yaml`，在 `model` 配置中添加：

```yaml
model:
  default: deepseek-v4-pro
  provider: custom
  base_url: https://api.deepseek.com
  api_mode: chat_completions
  api_key: <your-deepseek-api-key>
  extra_body:
    thinking:
      type: disabled
```

此方案下，DeepSeek 不再生成 `reasoning_content`，不会触发回传冲突，同时节省上下文消耗。

**方案二：保留思考模式**

若需要保留推理过程，需启用 `show_reasoning` 确保 `reasoning_content` 在对话历史中正确回传：

```yaml
model:
  default: deepseek-v4-pro
  provider: custom
  base_url: https://api.deepseek.com
  api_mode: chat_completions
  api_key: <your-deepseek-api-key>
  extra_body:
    thinking:
      type: enabled

display:
  show_reasoning: true
```

此方案下，Hermes 会保留并回传 `reasoning_content`，但终端会展示推理过程，上下文消耗也会增加。

修改配置文件后重启 Hermes 生效。
