# FCD (FUA CODE) — DeepSeek 智能体指南

FCD 是 FUA STUDIO 打造的免费（闭源）终端与桌面 AI 编码代理。它提供流式 CLI（`fcd.exe`）、液态玻璃 Qt 桌面（`fcd-desktop.exe`）、Linux 二进制与安卓应用——全部共用同一套代理内核。本指南介绍 FCD 的安装、接入 DeepSeek 模型、以及首次任务，包括多智能体 **FUA Workflow（FWF）** 模式。

## 功能特性

- 流式 CLI + Qt 液态玻璃桌面（Windows / Linux / Android）
- 内置工具：文件读写编辑、glob、grep、shell 命令；MCP 服务器预设
- **审批 Agent**：每次工具调用在执行前由独立判定模型做风险评估（APPROVE / DENY / 询问用户）
- **FUA Workflow（FWF）**：2–6 个内置智能体并行工作（领头 / 计划者 / 执行者），支持群聊与私信
- 每周用量额度、套餐兑换码、会话持久化、上下文自动压缩

## 安装

### Windows

1. 从 FCD GitHub Releases 页面下载 `FCD-Setup.exe` 并运行。安装器会部署 `fcd.exe`（CLI）、`fcd.ico` 与开始菜单 / 桌面快捷方式。
2. 可选下载 `fcd-desktop.exe`（单文件 Qt 桌面版）获得图形界面体验。

### Linux

下载 `fcd.elf`，赋予执行权限后运行：

```bash
chmod +x fcd.elf
./fcd.elf
```

### Android

安装 `FCD-0.0.1.apk`（无需 root）。安卓版本提供相同的对话循环与移动端友好的工具集。

## 配置 — DeepSeek 模型

FCD 使用 OpenAI 兼容的 `chat/completions` 协议，DeepSeek 的服务端点为 `https://api.deepseek.com/v1`。

1. 启动 `fcd`，用你的 API Key 添加 DeepSeek 端点（在 <https://platform.deepseek.com/api_keys> 创建）：

   ```
   /add https://api.deepseek.com/v1 deepseek-v4-pro <你的API_KEY>
   ```

2. 切换默认模型（支持编号 / 名称）：

   ```
   /models deepseek-v4-pro
   ```

3. 追求更快更省的回合可使用 flash 档：

   ```
   /add https://api.deepseek.com/v1 deepseek-v4-flash <你的API_KEY>
   /models deepseek-v4-flash
   ```

### 启用 1M 上下文窗口

DeepSeek v4 系列模型提供 **100 万 token 上下文窗口**。FCD 在 `data/config.json` 中按模型保存上下文上限；为你添加的模型条目设置 `max_context_tokens` 为 1,000,000：

```json
{
  "models": [{
    "id": "…",
    "model": "deepseek-v4-pro",
    "max_context_tokens": 1000000,
    "max_output_tokens": 384000
  }]
}
```

FCD 会在对话接近配置预算时自动压缩历史，超大型代码库也能在单会话内处理。

### Max Thinking / 推理强度

DeepSeek v4 支持最高推理档位。在 FCD 中开启思考并推到 `max`：

```
/think on
/think-effort max
```

FCD 会将其映射为 DeepSeek 请求中的 OpenAI 兼容参数 `reasoning_effort: max`。不要把关闭思考当作 API 报错的变通方案——v4 模型下 `max` 档稳定且代码质量最佳。

> 本文不列价格；做预算前请以 DeepSeek 官方定价页为准。

## 首次运行

在项目目录下启动 `fcd`，试一个真实编码任务：

```
> 找出 src 下所有 TODO 并汇总成表格
> 把 utils/time.py 重构成 dataclass 并保持 API 兼容，跑通测试
```

FCD 以 Markdown 流式输出模型回答，展示每次工具调用，并支持 `/adm <M|auto|ALL>` 审批模式：

- `auto`（默认）：**审批 Agent** 在每次操作执行前独立做风险自审。只读操作直接放行；有风险或越界的动作会**请求你的指示**（`y/N`）——判定模型只看工具名与参数摘要、绝不接触文件内容，文件内的提示词注入无法绕过审批门。
- `M`：所有工具调用手动确认。
- `ALL`：全自动。

其他常用命令：`/usage`（额度进度条）、`/redeem <码>`（套餐兑换码）、`/mcp`（MCP 预设）、`/clear`（重置上下文）。

## FUA Workflow（FWF）— 多智能体模式

FWF 让多个内置智能体组队：1 个**领头**、1 个**计划者**、其余为**执行者**（共 2–6 个）。

```
/fwf on                          # 默认 3 个内置免费模型
/fwf on deepseek-v4-pro deepseek-v4-flash deepseek-v4-pro --judge deepseek-v4-flash
/fwf off
```

- **计划者**提出 `PLAN: [步骤1]|[步骤2]|…`，**领头**审核（`PLAN-REVIEW: APPROVE / REVISE`），再用 `TASK: [i] …` 分配任务；执行者**并行**执行并汇报；领头最后发出 `FINAL: …`。
- 直接输入即可对全员广播（大群），用 `@2 你的问题` 私信某位成员。
- 用量按 **N 倍速度**消耗（每个智能体独立计时）；FWF 启动**前**会弹确认，并提示提示词注入风险——FWF 中不建议引入外部 skills / MCP 工具。
- 每位成员的工具调用仍先过独立**审批 Agent**。

## 资源

- [GitHub 仓库](https://github.com/FUA-Studio/FCD) — 发布版、下载与公告
- 程序内文档：`/help`、`/mcp`、`/fwf` 状态输出
