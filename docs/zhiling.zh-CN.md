[English](./zhiling.md) | [简体中文](./zhiling.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入知令

[知令](https://zhiling.plus) 是一款面向科研与工程场景的智能体桌面软件，支持多模型接入、自定义模型配置（BYOK），以及六种工作模式——Agent、Plan、Research、Debug、Ask、超级任务。支持多任务并行、子任务派发调度，以及定时任务和条件触发任务等自动化调度能力，适合处理长时大任务。

知令**内置了 DeepSeek V4 模型**——安装后即可直接选用 `deepseek-v4-pro` 或 `deepseek-v4-flash`，无需额外配置。对于高级用户，知令还支持通过 OpenAI 兼容接口添加自定义模型（BYOK），使用自己的 API Key 独立计费。

#### 1. 安装知令

- 从 [zhiling.plus](https://zhiling.plus) 下载对应平台的安装包。
- 运行安装程序，按提示完成安装。
- 启动知令，注册或登录，打开一个项目文件夹。

#### 2. 方式一：使用内置 DeepSeek 模型（推荐）

知令预置了 DeepSeek-V4-Pro 和 DeepSeek-V4-Flash，不需要 API Key，无需手动配置。

- 在知令中打开项目。
- 在智能体面板中，点击模型选择下拉框。
- 选择 **DeepSeek V4 Pro** 或 **DeepSeek V4 Flash**。

![知令模型选择器展示 DeepSeek 选项](./assets/zhiling_model_selector.png "知令模型选择器，展示 DeepSeek V4 Pro 和 V4 Flash")

配置完成——现在就可以在知令中与 DeepSeek 协作。使用量计入知令套餐额度。

#### 3. 方式二：BYOK 自定义配置

如果你希望使用自己的 DeepSeek API Key，可以通过知令的设置界面添加自定义模型条目。此方式独立于套餐计费，直接从你的 DeepSeek 账户扣费。

首先，前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

然后，在知令中：

- 进入 **设置** → **模型**。

![知令设置 → 模型中的 BYOK 条目列表](./assets/zhiling_byok_list.png "知令设置 → 模型页面，展示自定义模型条目列表和添加按钮")

- 点击 **添加自定义条目**（或对应版本的等效按钮）。
- 按下方表格填写配置字段：

| 字段 | 值 | 说明 |
|------|-----|------|
| 显示名称 | `DeepSeek V4 Pro` 或 `DeepSeek V4 Flash` | 自定义显示名称，会出现在模型选择器中 |
| API Base URL | `https://api.deepseek.com` | **不要**追加 `/v1` 后缀，知令会自动拼接路径 |
| 模型 ID | `deepseek-v4-pro` 或 `deepseek-v4-flash` | 必须严格匹配 |
| API Key | `sk-xxxx...xxxx` | 从 DeepSeek 开放平台获取的密钥 |
| Temperature | `0.6`（可选） | 控制输出随机性，默认为 0.6 |

![知令 BYOK 配置表单，展示 DeepSeek 字段填写示例](./assets/zhiling_byok_config.png "知令 BYOK 配置对话框，展示 DeepSeek 字段填写示例")

- 保存条目。自定义模型将出现在模型选择器中，与内置模型并列显示。
- **注意 API Key 安全**：密钥保存在本机。请勿在共享或公共设备上保存。

#### 4. 使用知令与 DeepSeek

- 在智能体面板中，确认模型下拉框中已选择 DeepSeek 模型。
- 根据任务类型选择合适的工作模式（Agent、Plan、Research、Debug、Ask、超级任务）。
- 输入问题或提示，回车发送。知令会实时流式展示 DeepSeek 的回复。
- 使用 `deepseek-v4-pro` 时，知令会自动启用深度思考模式——你将看到模型的推理过程与最终答案同时展示。

![使用 DeepSeek 模型在知令中对话的效果](./assets/zhiling_chat_example.png "知令智能体面板使用 DeepSeek V4 Pro，展示流式回复与推理过程")

> **100 万 Token 上下文窗口**：DeepSeek V4 系列模型支持高达 **100 万 token** 的上下文窗口。知令作为客户端不做额外限制，你可以充分利用 DeepSeek V4 的完整上下文能力。

> **思考模式**：知令智能识别模型厂商，自动适配思考模式参数。选择 `deepseek-v4-pro` 后，推理强度默认为 `max`，提供最佳的编程与分析体验。你可以在智能体设置中调整推理强度级别（`high` / `max`）。

#### 可选：验证配置

对于 BYOK 配置，可以用 `curl` 测试 API Key 和模型名称是否有效：

```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <你的 API Key>" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

如果请求成功，说明 API Key 和模型名称均可正常使用。

#### 常见问题

- **模型选择器中没有 DeepSeek 选项**：请确认知令已更新到最新版本。内置 DeepSeek 模型从 1.0 版本开始提供。
- **认证失败 / 401（仅 BYOK）**：检查你的 API Key 是否正确且未过期。可前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 验证。
- **模型未找到 / 404（仅 BYOK）**：确认模型 ID 是否严格写为 `deepseek-v4-pro` 或 `deepseek-v4-flash`——没有拼写错误，没有多余空格。
- **BYOK 条目没有出现在选择器中**：返回设置 → 模型，确认条目已保存。可能需要重启知令使更改生效。
- **响应缓慢或超时**：检查网络连接。DeepSeek API 偶有高负载，通常重试即可解决。
- **API Base URL 报错**：确认填写的是 `https://api.deepseek.com`，末尾不要带 `/v1`。知令内部会自动拼接路径——自行添加 `/v1` 会导致重复路径（如 `/v1/v1/chat/completions`）。
