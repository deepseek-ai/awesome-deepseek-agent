[English](./deepseek_harness_android.md) | [简体中文](./deepseek_harness_android.zh-CN.md) · [← Back](../README.md)

# DeepSeek Harness for Android

[DeepSeek Harness for Android](https://github.com/guzhou079-arch/deepseek-harness-android) 把 DeepSeek Harness 的 Agent 运行时打包成一个可直接安装的安卓 APK —— 不用 Termux、不用 root、不用电脑。终端、文件读写与命令执行都在 App 内运行，随包 21 款技能，甚至能在手机上自行编译、打包、签名出 APK。

#### 1. 安装

要求：Android 7.0（API 24）及以上 —— 截图与虚拟屏等能力需要 Android 11+；首次启动后应用数据约 0.6 GB；需要联网（模型在远端）。

1. 到 [Releases](https://github.com/guzhou079-arch/deepseek-harness-android/releases) 下载最新的 `DeepSeekHarness-vX.Y-dist.apk`；每个 Release 都列出该 APK 的 SHA-256，可自行核对。
2. 点开 APK，按系统提示允许「安装未知应用」。
3. 打开 App：首次启动会解压内置运行时（几百 MB，视机型约 1–3 分钟）。
4. 按需授予权限 —— 无障碍（读屏、点击、截图）、通知、悬浮窗。只聊天的话，除联网外不需要任何权限。

#### 2. 配置 DeepSeek

App 以 `provider: deepseek-official` 注册 DeepSeek 官方通道，并组合两种鉴权插件之一：API Key，或 DeepSeek 账号登录。

**方式 A —— API Key（推荐）**

1. 到 [platform.deepseek.com](https://platform.deepseek.com/) 创建一个 Key。
2. 在 App 里打开设置页的「模型 / 账户」卡片，把 Key 粘进去。

Key 以凭据引用形式保存（`dsh-llm-deepseek` 适配器的 `apiKeyEnv: DEEPSEEK_API_KEY`），按请求解析；报错只会指出引用名，不会回显 Key 本身。

**方式 B —— 账号登录**

在同一张卡片里用 DeepSeek 账号登录，走账号版通道。

**模型**

| 模型 | 输入 | 上下文窗口 |
| --- | --- | --- |
| `deepseek-flash` | 文本 + 图片 | 1,000,000 tokens |
| `deepseek-v4-pro` | 文本 | 1,000,000 tokens |

以上是适配器默认广告的目录项；模型 id 会原样透传到线上，所以新发布的 DeepSeek 模型无需重新注册即可使用。默认 base URL 为 `https://api.deepseek.com/anthropic`，可用 `baseURL` 或 `$DEEPSEEK_BASE_URL` 覆盖（走网关时有用）。默认单次输出上限 256,000 tokens，上下文回退值 1,000,000。

**推理强度**

提供 `off`、`low`、`high`、`max`。其中 `low`/`high`/`max` 会开启思考并以 `output_config.effort` 下发；`off` 则下发 `thinking.type: disabled`。在模型选择器里选，或在通道配置里设 `reasoningEffort`。

#### 3. 首次运行

- 发一条消息，Agent 会流式作答；shell 命令、文件读取、网页抓取都会以工具卡片呈现，可逐条查看。
- 想用手机自动化，就开启无障碍服务；可选再启动 Shizuku，App 用它拿特权 shell。自动化可以把应用跑在**虚拟屏**上，不会占用你正在用的屏幕。
- 可选：**设置 → 自建环境** 会下载约 190 MB 的工具链（proot + Alpine + OpenJDK 17），让 App 能在手机上编译、打包、签名 APK。

#### 4. 常见问题

| 现象 | 含义 |
| --- | --- |
| `MISSING_CREDENTIAL` | 该通道没有配置 API Key —— 按第 2 步添加。 |
| `INVALID_CREDENTIAL` / `AUTH` | Key 不对或已吊销；报错会指出需要修的那个凭据引用。 |
| `CONTEXT_WINDOW_EXCEEDED` | 会话超出模型上下文；新建会话或让压缩机制介入。 |
| `RATE_LIMIT` / `QUOTA` | 服务端限流 / 额度问题 —— 稍后重试或检查 DeepSeek 账号余额。 |
| 首次启动转圈好几分钟 | 正在解压运行时。反复失败可在 App 内控制台重试。 |
| 更新时报 `INSTALL_FAILED_UPDATE_INCOMPATIBLE` | 已装的是别的签名的同名包。先在 App 内导出备份，**不要**直接卸载（会清空应用私有数据）。 |
