[English](./dassi.md) | [简体中文](./dassi.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Dassi

Dassi 是一款运行在 Chrome 侧边栏中的 AI Agent，支持浏览器自动化、写作和分析，并内置 DeepSeek 供应商，可使用你自己的 API Key。

- **官网：** <https://dassi.ai/>
- **文档：** <https://docs.dassi.ai/>

#### 1. 安装 Dassi

1. 从 [Chrome 应用商店安装 Dassi](https://chromewebstore.google.com/detail/dassi-ai-agent-for-chrome/bjcngahpcjeililljmfegmlanlpgibdi)。
2. 固定扩展，点击工具栏中的 Dassi 图标打开侧边栏，然后登录 Dassi。
3. 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，确保账户已开通 API 访问且余额充足。

使用自有密钥需要处于有效的 Dassi 试用期，或订阅包含 BYOK 的套餐。Dassi 服务与 DeepSeek API 用量分别计费，当前条款请参阅 [Dassi 套餐](https://dassi.ai/pricing/)。

#### 2. 连接 DeepSeek

1. 从侧边栏菜单打开 **设置（Settings）**，选择 **模型（Models）**。
2. 展开 **API keys**，在 **其他供应商（Other providers）** 中找到 **DeepSeek**。
3. 点击 **API Key**，粘贴 DeepSeek 密钥，再点击 **保存（Save）**。
4. 等待连接成功提示。内置供应商使用 `https://api.deepseek.com`，无需填写自定义地址或编辑配置文件。
5. 执行浏览器任务时，在模型选择器中选择**支持视觉的 Flash 条目**。在仍使用旧名称的 Dassi 模型目录中，该条目为 `deepseek-v4-flash-vision-exp`，目前由 DeepSeek 当前 Flash 模型提供服务。纯文本任务也可选择 **DeepSeek V4 Pro**（`deepseek-v4-pro`）。确认选择后再发送下一条消息。

#### 3. 选择模型并了解限制

- **DeepSeek V4 Pro**（`deepseek-v4-pro`）是新建 DeepSeek 连接的默认模型，适合文本、代码和推理任务。
- **当前 DeepSeek Flash**（`deepseek-flash`，V4.1 Flash）同时支持文本和**视觉输入**，能够读取截图、分析图像。请参阅 [DeepSeek 视觉能力指南](https://api-docs.deepseek.com/guides/vision/)。部分 Dassi 版本仍显示旧 ID `deepseek-v4-flash` 或 `deepseek-v4-flash-vision-exp`；DeepSeek 仍接受这些别名，并由当前 Flash 提供服务，详见 [最新模型说明](https://api-docs.deepseek.com/quick_start/pricing/)。
- DeepSeek V4 支持 **100 万 token 上下文**。Dassi 根据模型目录确定上下文限制，供应商卡片中没有单独的上下文窗口设置项。
- **Dassi 中的视觉能力：** 需要基于截图操作浏览器时，请选择 Dassi 标记为支持视觉的 Flash 条目。旧版 Dassi 模型目录可能仍将 `deepseek-v4-flash` 标记为纯文本，这是目录的限制，并非当前 Flash 不支持视觉。必要时更新扩展并检查模型选择器。V4 Pro 仍为纯文本模型。
- **深度思考：** Dassi 主 Agent 启用思考并使用 `high` 推理强度。DeepSeek API 支持 `reasoning_effort: "max"`，但 Dassi 目前没有面向用户的推理强度选择器或请求体编辑器来启用它。本指南不宣称 Dassi 已支持 `max`。API 可用的推理等级请参阅 [DeepSeek 深度思考文档](https://api-docs.deepseek.com/guides/thinking_mode/)。

#### 4. 运行第一个任务

选中**支持视觉的 Flash 条目**，打开一篇公开文章，然后发送：

```text
阅读当前页面，用五条要点概括主要内容。
附上页面标题和网址，不要修改网站上的任何内容。
```

确认 Dassi 读取页面并返回包含来源网址的摘要。更多任务请参阅 [Dassi 浏览器自动化指南](https://docs.dassi.ai/guides/browser-automation/)。

如需使用 **DeepSeek V4 Pro** 进行纯文本连接测试，可发送：

```text
编写一个 JavaScript 函数，根据对象的 id 去重，并保留原始顺序。
请附上一个包含重复 ID 的使用示例。
```

确认 Dassi 返回函数和示例。这个任务可以检查连接，无需输入截图，也不会修改网站内容。

写作和分析时，可将相关文本粘贴到对话中。

#### 5. 常见问题

- **密钥被拒绝：** 确认复制的是 DeepSeek API Key，账户已开通 API 访问且余额充足。请在供应商设置中输入密钥，不要发到聊天中。
- **已连接，但仍在使用其他模型：** 保存供应商密钥和切换当前模型是两个步骤，需要明确选中 DeepSeek 模型。
- **出现纯文本提示：** 该提示指模型的截图支持能力。可先用纯文本任务验证连接；需要视觉浏览器操作时，请切换到支持视觉的模型。
- **找不到模型：** 更新扩展后重新查看模型选择器。可选条目取决于 Dassi 的模型目录。
