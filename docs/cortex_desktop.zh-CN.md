[English](./cortex_desktop.md) | [简体中文](./cortex_desktop.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Cortex Desktop

Cortex Desktop 是一台会听、会说、会动手的本地 AI 工作站。它不是又一个聊天框：开口跟它说，它听得懂也答得上；让它替你点鼠标、敲键盘操作本机应用；一个人忙不过来时派一队子代理并行干。最后交到你手上的是能直接用的 PPT、研究报告和文档——全程跑在你自己的 Mac 上。

模型你自己接。内置目录收录了 37 家供应商、1000 多个模型，DeepSeek 就在其中，接入只需粘贴一个 API Key——无需代理、无需自定义端点、无需手工登记模型。

- **官网：** <https://rambocode.github.io/cortex-work-release/zh/>
- **下载：** <https://github.com/rambocode/cortex-work-release/releases/latest>

#### 1. 安装 Cortex Desktop

Cortex Desktop 免费下载。在 [Releases 页面](https://github.com/rambocode/cortex-work-release/releases/latest)获取 macOS 安装包：

- Apple 芯片：`Cortex-<版本号>-arm64.dmg`
- Intel 芯片：`Cortex-<版本号>-x64.dmg`

打开 `.dmg`，把 **Cortex** 拖入「应用程序」即可。安装包已签名并通过 Apple 公证，无需绕过 Gatekeeper。安装后应用会从同一发布源自动更新。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)创建 API Key，并立即复制保存——平台只会完整展示一次。

#### 3. 在设置中填入 DeepSeek API Key

1. 从左侧栏打开**设置**，进入**模型**分区。
2. 切换到 **API Key** 标签页，这里列出所有使用 API Key 认证的供应商，DeepSeek 就在其中。
3. 找到 **DeepSeek**，点击**配置**。
4. 把 Key 粘贴进 **API Key** 输入框，点击**保存**。密钥进系统钥匙串：配置文件里只留一个引用名，明文不落盘；真正的密钥在发请求那一刻才解出来。保存后不再回显明文。
5. 可选：点击**测试连接**，离开页面前先验证 Key 是否可用。

**Base URL 覆盖**保持留空即可。Cortex 默认使用 DeepSeek 官方端点 `https://api.deepseek.com`，走 OpenAI 兼容协议。只有当你需要把 DeepSeek 流量导向自建网关时才填写这一项。

如果你更习惯用环境变量配置，该供应商同样会读取环境变量 `DEEPSEEK_API_KEY`。

#### 4. 选择 DeepSeek V4 模型

模型选择入口在输入框上方的胶囊按钮上，它同时显示当前的 Agent、模型与推理强度。

1. 点击输入区的胶囊按钮。
2. 在**模型**一栏中选择：
   - **deepseek-v4-pro** —— 编程、长链路规划与 Agent 工作流。
   - **deepseek-v4-flash** —— 追求低延迟的日常对话。
3. 直接发送消息即可。选择在新建会话或下一次发送时生效。

模型能力是自动识别的，不是替你猜的。两个 DeepSeek V4 模型在内置目录中都登记了 **100 万 token 上下文窗口**与 384,000 token 的最大输出，因此长会话、大仓库场景无需你另行设置上下文长度。Cortex 也不会偷偷换模型——界面上显示的模型，就是实际会跑的模型。

如果输入区提示**未配置供应商**，说明还没有接入任何供应商，请回到第 3 步。

#### 5. 把推理强度调到最高

DeepSeek V4 实际只支持 `high` 与 `max` 两档推理强度。Cortex 从模型目录读取这一约束，会把更低的档位（`极简` / `低` / `中`）自动抬到 `高`，所以不会出现把 DeepSeek V4 跑在不受支持档位上的情况。

1. 点击同一个输入区胶囊按钮。
2. 在**推理**一栏中选择**思考·最高**。

编程、重构与多步 Agent 任务建议用**最高**档；轻量对话用**思考·高**即可。推理内容会以增量方式实时渲染在会话里，模型思考过程可见。

#### 常见问题

- **`401` / 鉴权失败：** Key 粘错了输入框，或已在平台侧被吊销。重新进入**设置 → 模型 → API Key → DeepSeek → 配置**，先点**清除密钥**，再重新粘贴。已配置的供应商 API Key 框显示为空属于正常现象——它表示「留空则不修改已保存的密钥」，而不是没有密钥。
- **模型选择器里找不到 DeepSeek 模型：** 必须先在 API Key 标签页保存 DeepSeek 的密钥；没有凭据的供应商不会出现在输入区的模型列表中。
- **只有走代理时请求失败：** 检查 **Base URL 覆盖**，它必须是包含协议头的完整 URL，且指向兼容 DeepSeek 的 OpenAI 风格端点。点击**清除覆盖**可回退到官方端点。
- **选了更低档位但推理强度仍显示「高」：** 这是刻意设计。DeepSeek V4 不支持更低档位，Cortex 会将其抬到 `high`，而不是把不受支持的值发给接口。
