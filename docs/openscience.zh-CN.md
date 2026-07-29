[English](./aipoch_open_science.md) | [简体中文](./aipoch_open_science.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 AIPOCH Open Science 中接入 DeepSeek

AIPOCH Open Science 是一款面向科学研究的开源桌面 AI 工作台，在同一应用内提供持久化项目、沙箱化 Agent Runtime、Python/R Notebook、Skills、Connectors、文件处理和多模型服务。

- **GitHub：** <https://github.com/aipoch/open-science>
- **最新版本：** <https://github.com/aipoch/open-science/releases/latest>

本文基于 **Open Science v0.7.3** 核对。

#### 1. 安装 AIPOCH Open Science

从 GitHub 最新 Release 下载对应安装包：

- Apple Silicon macOS：`open-science-0.7.3-mac-arm64.dmg`
- Intel macOS：`open-science-0.7.3-mac-x64.dmg`
- Windows 10/11 x64：`open-science-0.7.3-win-x64-setup.exe`

<img width="1009" height="709" alt="aipoch_open_science_release" src="https://github.com/user-attachments/assets/dc6a8f53-fd9e-4a6e-8a8c-5348e7f9167e" />

首次启动时，Open Science 会检查系统兼容性、应用存储权限、安全凭据存储和安装网络。处理所有未显示为 **Ready** 的项目，然后点击 **Continue**。

<img width="1266" height="953" alt="aipoch_open_science_environment" src="https://github.com/user-attachments/assets/e91c18d7-d297-4ba2-941d-009956951ecf" />

下一步选择一个 Agent Runtime。只需要安装实际准备使用的 Runtime。点击 **Install**，等待自动检测完成；目标 Runtime 显示为 **Active** 后继续。

<img width="1266" height="953" alt="aipoch_open_science_agent_runtime" src="https://github.com/user-attachments/assets/b1c6a5ea-8936-4974-8625-746bb2527147" />

#### 2. 配置内置 DeepSeek 服务

先到 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

首次启动时，可以直接在 **Model provider** 步骤填写相同配置。下面使用 **Settings → Model** 演示，是因为完成 Onboarding 后仍可从这里重复添加或修改服务。

在项目主页点击右上角的齿轮图标。

<img width="1280" height="848" alt="aipoch_open_science_settings" src="https://github.com/user-attachments/assets/ed3fd6f3-c64c-48aa-afde-db9c0e2cf959" />

打开 **Model**，滚动到 Provider 列表底部，点击 **Add provider**。

<img width="1280" height="848" alt="aipoch_open_science_add_provider" src="https://github.com/user-attachments/assets/f1f6bf2f-2390-4ee7-931c-2bcadbcdc1b5" />

将 **Provider type** 设为 **DeepSeek**。连接 DeepSeek 官方 API 时使用内置服务，不要选择 **Custom Gateway**。

<img width="1690" height="1139" alt="aipoch_open_science_select_deepseek" src="https://github.com/user-attachments/assets/d77b2dbb-b3cc-4c91-ab55-a94ce11600bb" />

将 API Key 粘贴到 **API Key**，然后点击 **Save**。不要把接口地址填入 API Key 字段。DeepSeek 配置页会显示三个受支持的 V4 模型 ID：

<img width="1690" height="1139" alt="aipoch_open_science_supported_models" src="https://github.com/user-attachments/assets/772d649b-0c14-4589-bd8b-c7cf4df19b43" />

| 模型 | 推荐用途 | 上下文窗口 |
| --- | --- | --- |
| `deepseek-v4-pro` | 编程、科研和复杂 Agent 任务 | 1,000,000 token |
| `deepseek-v4-pro[1m]` | Anthropic 兼容执行路径的显式长上下文别名 | 1,000,000 token |
| `deepseek-v4-flash` | 交互速度优先和低延迟任务 | 1,000,000 token |

请严格使用上表中的当前 V4 模型 ID，不要替换成旧版 DeepSeek 模型 ID。

保存后，Open Science 会测试该 Provider。DeepSeek Provider 卡片显示绿色状态图标，表示连接检查已通过。随后选择需要的 DeepSeek 模型作为 Active model；下图使用 `deepseek-v4-pro[1m]`。

<img width="1280" height="848" alt="aipoch_open_science_active_deepseek" src="https://github.com/user-attachments/assets/29481b57-1e42-4ca9-af61-af4fe998539c" />

使用 `deepseek-v4-pro` 时，将 **Reasoning effort** 设为 **Max**，以获得最高推理强度。既可以在 Model 设置页配置默认值，也可以从消息输入区为当前会话单独切换。

<img width="583" height="207" alt="aipoch_open_science_reasoning_effort" src="https://github.com/user-attachments/assets/11d3232e-c518-4b2b-b45d-91f7a7d2c368" />

使用内置服务时，Open Science 会自动提供接口地址。v0.7.3 定义的地址为：

- Anthropic 兼容接口：`https://api.deepseek.com/anthropic`
- OpenAI 兼容 Base URL：`https://api.deepseek.com/v1`

正常配置时不需要手动修改这两个地址。

> **Max 不是装饰性界面选项。** Open Science v0.7.3 会把 `max` 选择规范化为 `reasoningEffort: "max"`，同时启用 thinking。在 OpenAI 兼容请求路径中，桥接层会把它序列化到实际请求体的 `reasoning_effort: "max"`。

聊天界面的上下文指示器会按完整模型窗口显示用量。例如 `71k / 1M tokens (7%)` 可以直接确认当前上限为 100 万 token：

<img width="355" height="136" alt="aipoch_open_science_context_1m" src="https://github.com/user-attachments/assets/b81dea52-ea8b-430e-b5b8-5675ac86cd67" />

#### 3. 完成首次启动配置

新安装会在 Model provider 之后继续完成以下步骤；如果应用已经显示项目主页，可以跳过本节。

**Notebook runtime** 为可选步骤。可以启用检测到的 Python/R 解释器、安装应用托管环境，也可以暂时关闭，之后在 **Settings → Runtimes** 中配置。

为项目、运行产物、Notebook 和运行环境选择 **Data location**，然后点击 **Finish**。Open Science 开始管理该目录后，如需迁移，请使用 **Settings → Storage → Change location**，不要直接在文件管理器中移动。

#### 4. 创建项目并运行 DeepSeek

1. 点击 **New project**。
2. 输入项目名称，并按需填写描述。
3. 点击 **Create project**。
4. 在输入框上方的模型选择器中，确认当前模型是 `deepseek-v4-pro`、`deepseek-v4-pro[1m]` 或 `deepseek-v4-flash`。
5. 输入提示词并发送。

<img width="1084" height="681" alt="aipoch_open_science_deepseek_project" src="https://github.com/user-attachments/assets/dcd9c394-9b8c-49df-a725-237bcd6e4f91" />

首次验证建议使用一个容易检查的小任务：

```text
请先回复当前模型名称，然后列出 AI Agent 可以帮助复现科学论文的三种方式。
```

能够正常收到回复，说明该项目已经可以调用 DeepSeek。使用 `deepseek-v4-pro` 执行编程或复杂科研任务时，可将 **Reasoning effort** 保持为 **Max**。

#### 常见问题

- **401 / 身份验证失败：** 确认 **API Key** 中填写的是真实有效的 DeepSeek API Key。
- **未找到模型 / 404：** 模型名必须严格使用 `deepseek-v4-pro`、`deepseek-v4-pro[1m]` 或 `deepseek-v4-flash`。
- **修改接口地址后连接失败：** 重新选择内置 **DeepSeek** 服务，并保留应用自动生成的地址。
- **项目里看不到模型：** 打开 **Settings → Model**，重新测试模型服务，并把 DeepSeek 模型设为当前模型。
- **推理强度不符合预期：** 确认模型为 `deepseek-v4-pro`、Reasoning effort 已开启，并选中了 **Max**。
