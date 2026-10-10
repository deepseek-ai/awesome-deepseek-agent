# DeepSeek Harness (DSH) + 华为小艺

把**华为小艺**接到跑在你自己电脑上的 **DeepSeek Harness（DSH）** 会话，于是你在手机上就能用上 **DeepSeek-V4-Pro / DeepSeek-V4-Flash**。

本文走一遍：安装 → 配置 → 第一次成功对话。

---

## 你能得到什么

小艺变成你本机 DSH 会话的一个入口 —— **同一个会话、同一套工具、同一份工作目录和文件**。没有第二个 agent，也没有把你项目传到云上。

```
华为小艺（手机）  →  华为云 OpenClaw 通道  →  你电脑上的 DSH  →  DeepSeek-V4
```

接好之后，你可以在任何地方对小艺说话、打字或发图，回复会回到小艺那条对话里。

## 前置条件

| 需要什么 | 说明 |
| --- | --- |
| **DSH（DeepSeek Harness）** | 在将要跑 agent 的那台机器上装好并能用 |
| **Node.js ≥ 20** | 插件用了内置的 `fetch` / `FormData` / `Blob` |
| **DeepSeek API Key** | 在 [DeepSeek 开放平台](https://platform.deepseek.com/) 申请 |
| **小艺开放平台凭证** | 一个 OpenClaw 模式的智能体，给你 `AK` / `SK` / `agentId`。需要在华为小艺开放平台申请开通 |

> 前两项是跑 DSH 本身用的；最后一项才是让手机能连上来的关键。

---

## 第 1 步 —— 装好并配置 DSH

装好 DSH，用你的 API Key 指向 DeepSeek。先在**本机**确认它自己能正常对话。

模型选当前的 DeepSeek V4 型号：

- `deepseek-v4-pro` —— 能力最强
- `deepseek-v4-flash` —— 最快最省

DeepSeek V4 支持最高 **100 万 token 上下文**，其中 `deepseek-v4-pro` 支持多档思考强度（`max` 和 `high`）。难题就把思考强度调高。

## 第 2 步 —— 装 `dsh-xiaoyi` 插件

插件开源（MIT）：<https://github.com/HangZhouXi/dsh-xiaoyi>

```bash
dsh plugin --profile web add git+https://github.com/HangZhouXi/dsh-xiaoyi
dsh plugin --profile web install
```

然后**冷启动 DSH 宿主**。宿主端插件不吃热重载，**必须冷启动**才生效。

## 第 3 步 —— 填小艺凭证

新建或编辑 `~/.dsh/xiaoyi/state.json`：

```json
{
  "enabled": true,
  "ak": "你的 AK",
  "sk": "你的 SK",
  "agentId": "OpenClaw 模式智能体的 agentId",
  "wsUrl": "wss://hag.cloud.huawei.com/openclaw/v1/ws/link",
  "sessionId": "",
  "cwd": "C:\\Users\\<你>\\Desktop"
}
```

也可以启动后让会话里的 agent 调 `xiaoyi_set` 工具直接改。

插件会用 WebSocket 连到华为云，用 `AK`/`SK` 鉴权，每 30 秒发一次心跳。

## 第 4 步 —— 第一次对话

1. 冷启动 DSH 宿主
2. 调 `xiaoyi_status` 工具看通道状态 —— 应该是 `ready: true` 且 `connected: true`
3. 在手机上对小艺说句话
4. 消息被投进一条名为 `xiaoyi-listen-*` 的 DSH 会话，agent 作答，回复发回小艺那条对话

## 使用建议

- **思考强度** —— 难题用 `max`；日常快问快答 `high` 通常就够，而且明显更省
- **长上下文** —— DeepSeek V4 支持 100 万 token，可以把大文件、长日志直接丢给会话
- **会话复用** —— 插件重启后会续用同一条 `xiaoyi-listen-*` 会话，对话历史始终在一处
- **收图** —— 小艺发来的图片会下载到本地并交给 agent，agent 可直接读图
- **往外发文件** —— 小艺协议只接受公网 https 地址。要么起一条隧道并在 `publicBaseUrl` 里填上，要么显式选择第三方图床

## 排错

| 现象 | 检查 |
| --- | --- |
| `xiaoyi_status` 报 `ready: false` | AK / SK / agentId 有缺项 |
| 一直连不上 | `wsUrl` 是否正确；本机能否访问 `hag.cloud.huawei.com:443` |
| 反复重连 | 看 `~/.dsh/xiaoyi/xiaoyi.log` 里有没有「连接假死」 |
| 小艺那边没回复 | 确认 DSH 宿主日志里插件加载成功，并查看 `~/.dsh/xiaoyi/xiaoyi.log` |
| 手机连不上 | **跑 DSH 的那台电脑必须开着并且在线**，这是前提 |

## 相关链接

- 插件仓库：<https://github.com/HangZhouXi/dsh-xiaoyi>
- DeepSeek 开放平台：<https://platform.deepseek.com/>
- DeepSeek API 文档：<https://api-docs.deepseek.com/>
- DSH：<https://deepseek.com/harness>
