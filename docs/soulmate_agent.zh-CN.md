[English](./soulmate_agent.md) | [简体中文](./soulmate_agent.zh-CN.md) · [← 返回](../README.md)

# 接入 Soulmate Agent

Soulmate Agent 是本地优先的 AI 桌面 Agent（Python 核心 + Electron 外壳），支持 Windows / macOS。会话、记忆与 API Key 都留在用户自己的机器上，也不锁定单一模型厂商。

#### 1. 安装 Soulmate Agent

从 [Releases](https://github.com/weixin97676414/soulmate-agent/releases/latest) 下载 Windows 安装包：

```
Soulmate-Agent-Setup-1.0.1.exe
```

macOS 由项目支持，按 [仓库 README](https://github.com/weixin97676414/soulmate-agent) 的构建步骤运行（核心需要 Python 3.13+，桌面端需要 Node.js 20+）。

#### 2. 配置 DeepSeek

1. 从左侧图标栏进入 **模型**。
2. 选择 **深度求索（DeepSeek）**，它是预置服务商之一。
3. **接口地址 Base URL** 填 `https://api.deepseek.com/v1`。
4. 在 [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys) 创建 API Key，粘贴到 **API Key**。密钥用系统钥匙串加密保存（Windows 上为 DPAPI），不明文落盘。
5. 选择模型名：
   - `deepseek-flash` —— DeepSeek-V4.1-Flash，支持工具调用与图像理解
   - `deepseek-v4-pro` —— DeepSeek-V4-Pro，支持工具调用，不支持图像理解
6. **上下文窗口（tokens）** 填 `1048576`。
7. 保持 **支持工具调用** 开启；**支持图片输入** 只对 `deepseek-flash` 开启。
8. 打开 **支持思考强度**，再选择 **能力档位**。三个档位与 DeepSeek 的推理强度对应如下：

| 能力档位 | `reasoning_effort` |
| --- | --- |
| 便宜快速 | `low` |
| 标准 | `high` |
| 最强 | `max` |

9. 点 **保存并测试连通性**。应用会真实发一次请求并返回延迟。

![DeepSeek 服务商与模型选择](assets/soulmate-agent-deepseek-provider.png)

![DeepSeek 能力档位与价格设置](assets/soulmate-agent-deepseek-settings.png)

#### 3. 首次运行

新建一个对话，给它一个需要动手的任务，例如：「打开这个网页，把正文里的价格整理成表格」。工具卡片会显示每次调用的状态与耗时，所有桌面操作都会先向你确认再执行。

#### 说明

- DeepSeek V4 支持 1M 上下文（1,048,576 tokens），输出上限 384K。
- 思考模式默认开启，`reasoning_effort` 取 `low`、`high`、`max`。
- `deepseek-flash` 是 Flash 当前的模型名。旧名 `deepseek-v4-flash` 接口仍接受，但对应模型已下线，请求由 DeepSeek-V4.1-Flash 提供服务并按 Flash 价格计费。
- 价格按百万 token 计费，并区分峰谷：空闲时段为高峰价的一半。高峰时段为北京时间周一至周五 09:00–12:00、14:00–18:00（不含中国法定节假日）。
- 截图的窗口标题是 **Buddy Manager**。它是内置搭子之一，窗口标题会跟随当前在用的搭子名称变化。

#### 可选：价格设置

在 **价格设置** 里填入单价（人民币 / 百万 token），应用的「用量与费用」页才会显示真实金额。下列数值已与 [官方定价页](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) 核对：

`deepseek-flash`

| | 输入（缓存命中） | 输入（缓存未命中） | 输出 |
| --- | --- | --- | --- |
| 空闲时段 | 0.02 | 1 | 4 |
| 高峰时段 | 0.04 | 2 | 8 |

`deepseek-v4-pro`

| | 输入（缓存命中） | 输入（缓存未命中） | 输出 |
| --- | --- | --- | --- |
| 空闲时段 | 0.15 | 4.5 | 13.5 |
| 高峰时段 | 0.30 | 9.0 | 27.0 |
