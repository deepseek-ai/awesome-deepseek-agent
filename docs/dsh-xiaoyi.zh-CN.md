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
| **小艺开放平台凭证** | 一个 OpenClaw 模式的智能体，给你 `AK` / `SK` / `agentId`。见下面「小艺凭证怎么拿」 |

> 前两项是跑 DSH 本身用的；最后一项才是让手机能连上来的关键。

### 小艺凭证怎么拿

**这三样是华为发的，插件造不出来。** 得你自己去申请：

1. 注册**华为开发者账号**并完成**实名认证**——<https://developer.huawei.com/consumer/cn/register/>
2. 登录**小艺开放平台**，创建一个智能体——<https://developer.huawei.com/consumer/cn/hag/hagindex.html#/>
   创建时**必须选「OpenClaw 模式」**，别的模式跟本插件不兼容。
3. 在智能体详情页取三样东西：
   - `agentId`——在 **AgentCard** 模块里；
   - `AK` / `SK`——左侧**「凭证管理」→「新建凭证」**。**SK 只显示一次**，当场复制存好。
4. 把你自己的华为账号加进智能体的**「测试管理」→「测试白名单」**。上架之前只有白名单里的账号能访问，大约几分钟后生效。
5. 这个模式的官方文档——<https://developer.huawei.com/consumer/cn/doc/doccenter-celia/openclaw-0000002518410344>

> 菜单名、入口位置、审核流程**全部由华为决定，随时可能变**。上面哪一步跟你看的对不上，请以华为官方文档为准，别以本文为准。

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
  "cwd": "C:\\Users\\<你>\\Desktop",
  "publicBaseUrl": "",
  "imageHost": ""
}
```

也可以启动后让会话里的 agent 调 `xiaoyi_set` 工具直接改。

插件会用 WebSocket 连到华为云，用 `AK`/`SK` 鉴权，每 30 秒发一次心跳。

## 第 4 步 —— 第一次对话

1. 冷启动 DSH 宿主
2. 调 `xiaoyi_status` 工具看通道状态 —— 应该是 `ready: true` 且 `connected: true`
3. 在手机上对小艺说句话
4. 消息被投进一条名为 `xiaoyi-listen-*` 的 DSH 会话，agent 作答，回复发回小艺那条对话

---

## 两个方向分别能传什么

规划用法之前先看这个。

| 方向 | 支持情况 |
| --- | --- |
| **手机 → DSH**（你发给小艺的） | **文字、语音（转成文字）、图片/文件都可以。** 附件会下载到 `~/.dsh/xiaoyi/media/`，再把本地路径交给 agent |
| **DSH → 手机**（小艺回给你的） | **文字可以**——回复正文，以及 `xiaoyi_send` 推的短消息。**图片/文件推回手机不可靠**：协议只接受公网 https URL，而且小艺客户端不保证把文件渲染出来 |

一句话：**入站方向才是靠得住的。**

## 安全须知

- **凭证只在你本机。** 存在 `~/.dsh/xiaoyi/state.json`，插件不会把它上传到任何地方。因为是明文，**别提交进 Git、别放进同步盘**。
- **入站附件有 SSRF 防护。** 附件的 `uri` 来自外部消息，属于不可信输入：只允许 `http/https`；重定向的**每一跳都在发请求之前**先检查；主机要过两道关 —— 结构检查 + **它实际解析到什么地址**（所以 `127.0.0.1.nip.io` 会和 `127.0.0.1` 一样被拒）。环回、私网、链路本地、唯一本地、多播、站点本地、IPv4-mapped、NAT64、6to4、Teredo 全拦，含 `169.254.169.254` 这类云元数据地址。
- **下载有体积闸门**：单文件 50 MB，流式读取，对方少报 `Content-Length` 也打不爆内存。
- **插件自己的 HTTP 路由没有鉴权。** 不要把 DSH 端口裸奔到公网；要走隧道的话，用带鉴权的方案。

---

## 使用建议

- **思考强度** —— 难题用 `max`；日常快问快答 `high` 通常就够，而且明显更省
- **长上下文** —— DeepSeek V4 支持 100 万 token，可以把大文件、长日志直接丢给会话
- **会话复用** —— 插件重启后会续用同一条 `xiaoyi-listen-*` 会话，对话历史始终在一处
- **收图** —— 小艺发来的图片会下载到本地并交给 agent，agent 可直接读图
- **往外发文件** —— 协议只接受公网 https 地址，而且客户端会不会渲染出来不在插件控制范围内。要么起一条隧道并在 `publicBaseUrl` 里填上，要么显式选择第三方图床 —— 但请把这个方向当实验性功能

## 排错

| 现象 | 检查 |
| --- | --- |
| `xiaoyi_status` 报 `ready: false` | AK / SK / agentId 有缺项 |
| 一直连不上 | `wsUrl` 是否正确；本机能否访问 `hag.cloud.huawei.com:443` |
| 反复重连 | 看 `~/.dsh/xiaoyi/xiaoyi.log` 里有没有「连接假死」 |
| 小艺那边没回复 | 确认 DSH 宿主日志里插件加载成功，并查看 `~/.dsh/xiaoyi/xiaoyi.log` |
| 发回去的图收不到 | 属于预期 —— 这个方向本来就不可靠，见「两个方向分别能传什么」 |
| 手机连不上 | **跑 DSH 的那台电脑必须开着并且在线**，这是前提 |

## 相关链接

- 插件仓库：<https://github.com/HangZhouXi/dsh-xiaoyi>
- DeepSeek 开放平台：<https://platform.deepseek.com/>
- DeepSeek API 文档：<https://api-docs.deepseek.com/>
- DSH：<https://deepseek.com/harness>
- 小艺开放平台（OpenClaw 模式）：<https://developer.huawei.com/consumer/cn/doc/doccenter-celia/openclaw-0000002518410344>
