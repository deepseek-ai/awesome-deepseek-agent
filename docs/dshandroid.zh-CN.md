[English](./dshandroid.md) | [简体中文](./dshandroid.zh-CN.md) · [← Back](../README.md)

# 接入 DShAndroid

[DShAndroid](https://github.com/kekejiang114514/deepseek-harness-android) 是一个把 DeepSeek 直接跑在手机上的安卓 Agent 客户端 —— 不用 Termux、不用 root、不用电脑。它是纯 Java 应用，直接构建在 Android 平台 API 之上：Agent 循环、工具调用和界面都在设备本地运行，还能通过无障碍服务操作手机自身的屏幕。

- **GitHub：** <https://github.com/kekejiang114514/deepseek-harness-android>

只聊天的话，除联网外不需要任何权限。其余能力都是可选的，且逐项授权。

#### 1. 安装 DShAndroid

到 [Releases 页面](https://github.com/kekejiang114514/deepseek-harness-android/releases/latest) 下载最新的 `DeepSeekHarness-*.apk` 并打开，按系统提示允许「安装未知应用」。

- Android 6.0（API 23）及以上。屏幕手势派发需要 Android 7.0+ —— 更低版本会退化为节点级点击，在部分自绘控件上会失败。
- 应用不含内置运行时，也没有任何第三方依赖，装完即可打开。
- 权限全部可选：**无障碍**（读屏、点击、输入）、**悬浮窗**（状态胶囊）、**通知**。全部拒绝也依然是一个完整的聊天客户端。

#### 2. 配置 DeepSeek

打开 **设置 → 端点与密钥**。

1. **Base URL** 保持默认 `https://api.deepseek.com`（OpenAI 兼容端点；只有想走 Anthropic 报文格式时才需要加 `/anthropic`）。
2. 把 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘进密钥栏并保存。
3. 模型列表是保存后从端点的 `/models` 实时读取的，所以当前目录会原样出现 —— 选择器里没有硬编码任何模型名。编程与推理选 **`deepseek-v4-pro`**；想要更低延迟、且需要图片输入时选 **`deepseek-flash`**。

两个模型在 DeepSeek 一侧都支持 **100 万 token** 上下文与最高 **384K** 输出。DShAndroid 不发送上下文窗口参数，而是主动把历史压小 —— 见第 3 步。

**推理强度**

DeepSeek V4 默认开启思考模式、默认强度为 `high`，DShAndroid 会把返回的 `reasoning_content` 流式渲染成答案上方的可折叠块，能看着模型思考，之后折叠起来。

聊天标题下方有一个 `模型 · 强度 ▾` 弹层，共六档：`off / low / medium / high / xhigh / max`。档位会作为 `reasoning_effort` 真正发给接口，弹层上显示的就是实际发出去的取值 —— `max` 就是 `reasoning_effort: "max"`，`off` 则是关闭思考模式（`thinking: {"type": "disabled"}`）。

接口只接受 `low`、`high`、`max` 三档，所以六档会收敛到这三个值，映射与官方文档一致：`low → low`，`medium/high/xhigh → high`，`max → max`。输出上限也随档位提高（`4096` 到 `65536` tokens，远低于 384K 的上限），因为思考链本身也计入 `max_tokens`。

如果要用工具调用，有一点需要知道：请求里一旦带了 `tools`，之前 assistant 轮次的 `reasoning_content` 就必须在后续每次请求中都回传，否则接口会返回 `400`。DShAndroid 会把它存在历史里并自动回传。

#### 3. 首次运行

发一条消息即可。发之前有几点值得知道：

- **上下文会自己压缩。** 历史估算超过约 24k tokens 时，应用先把过大的工具结果截断，再把较早的轮次折叠成滚动摘要。聊天里会出现灰色提示行，例如 `↻ folded 5 turns 24.1k → 13.8k tokens`，过程是可见的。这也是这里很少需要用到 100 万上下文的原因：长会话被维持在很小的规模，而不是一路涨满窗口。如果服务端仍以超长拒绝请求，应用会强力压缩并重试一次，而不是把原始报错甩给你。
- **工具调用以卡片呈现。** 文件读取、命令执行、网页抓取各自是一张可展开的卡片；Agent 循环没有步数上限，同一步内的只读工具会并发执行。
- **文件访问有边界。** 在设置里选 **workspace**（只能碰应用自己的工作区）或 **device**（整个共享存储），工具会遵守这条边界。
- **它会问你问题。** 需要决策时模型调用 `ui.ask`，聊天里出现 2–6 个选项的卡片，答案回到同一轮对话里。

#### 4. 可选能力

- **屏幕操作。** 在 **设置 → 无障碍** 里启用服务（应用会直接深链到系统里它自己的那一页 —— Android 不允许应用自我授权）。之后模型就能读屏（`a11y.screen` 输出紧凑大纲，`a11y.dump` 输出完整节点树）、点击、滑动、输入、等待文字出现，以及启动应用。动作会降级而不是失败：点文本节点会向上找到最近的可点击祖先，输入会向上找到最近的可编辑控件。
- **悬浮胶囊。** 一轮对话运行时，悬浮窗显示 Agent 在做什么 —— 状态、当前工具、耗时，以及暂停按钮。应用在前台时它不出现。
- **插件。** 两类插件共用 `/sdcard/DShAndroid/plugins/`。声明式 `plugin.json` 不写代码就能接任何 HTTP API；为 DeepSeek Harness 写的工具插件（`import { defineTool } from '@deepseek-ai/dsh-tools'`）可以直接跑。
- **暂停与续写。** 回复流式输出时，发送按钮变成暂停按钮；暂停会保留已写出的部分并告知模型被打断，继续时从半句接着写，而不是重新生成。

#### 5. 常见问题

| 现象 | 含义 |
| --- | --- |
| 保存后模型列表为空 | 密钥或 Base URL 不对，或该端点不提供 `/models`。手动填模型 id 即可。 |
| `401` / `invalid api key` | 密钥粘贴时带了空白字符，或它属于另一个账号。 |
| 屏幕类工具不执行 | 无障碍未启用，或被系统关掉了。**系统在强制停止某个包时，会把该包的无障碍记录一并删除**（从最近任务里关闭应用、或「一键清理」都会触发），所以彻底关闭过应用之后需要重新开启一次。 |
| 报错重试后仍在重复同一个工具调用 | Agent 会把连续相同的工具结果标记为「卡住」并提示模型；直接要求它换一种做法。 |

---

*本指南按 DShAndroid 1.4.1（versionCode 88）核对。模型名、上下文窗口与输出上限以 2026 年 11 月的 [DeepSeek 模型与价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 页面为准。*
