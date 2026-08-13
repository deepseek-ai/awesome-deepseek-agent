[English](./xenon.md) | [简体中文](./xenon.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Xenon

[Xenon](https://github.com/xianyu-sheng/Xenon) 是一个开源终端 AI 编程 Agent，支持 DeepSeek V4 模型发现、可配置推理强度、原生工具调用、缓存与费用观测、工具权限控制、MCP 服务、八种执行引擎以及透明的用户治理记忆。

## SWE-bench 官方评测

在 **SWE-bench_Lite 官方 harness**（30 实例 × 5 引擎、单次尝试、最便宜模型档）上，Xenon 达到 **40.0% 实例级 / 45.8% 单元级**，评测报告（采样种子、评分方法、成本核算、无补丁归因）全部入库可复现。同模型 A/B（v0.8.0 → v0.8.2，DeepSeek V4 Flash）将框架增益隔离为 **实例级 +6.7pp / 单元级 +11.0pp**。

## 1. 安装

安装 Python 3.10 或更高版本，然后安装已验证的 v0.8.2 版本：

```bash
pip install -U "git+https://github.com/xianyu-sheng/Xenon.git@v0.8.2"
xenon --version
```

如需参与开发，可克隆仓库后使用 `-e ".[dev]"` 安装。

## 2. 配置 DeepSeek

启动 Xenon 并打开交互式配置向导：

```text
> /setup
```

选择 **DeepSeek**，输入从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取的 API Key，再选择 `deepseek-v4-pro` 和/或 `deepseek-v4-flash`。Xenon 会通过供应商的 `/models` API 获取当前模型列表，并将所选模型加入故障转移池。

也可以直接编辑 `~/.xenon/credentials.yaml`：

```yaml
deepseek: "sk-xxxxxxxxxxxxxxxx"
```

Xenon 内置的 V4 模型条目采用 100 万 Token 上下文窗口。上下文管理器会在达到配置上限前预警并压缩长对话。

### 推理强度

`deepseek-v4-pro` 默认使用 `reasoning_effort=max`。可针对单个模型修改：

```text
> /set_model ds-pro deepseek/deepseek-v4-pro reasoning_effort=high
```

允许值为 `low`、`medium`、`high` 和 `max`。该配置会保存到模型注册表，并用于普通请求、流式请求和原生工具请求。当 API 要求强制指定 `tool_choice` 时，由于两者不兼容，Xenon 仅对该次请求关闭思考模式。

## 3. 运行

```bash
cd /path/to/project
xenon
```

常用命令和快捷键：

```text
/models        查看已注册模型
/model         交互式选择一个已注册模型
/pool          查看故障转移池和模型健康状态
/mode react    切换到 ReAct 执行引擎
/cost          查看 Token 缓存用量和预估费用
/cache lanes   查看按模型隔离的追加式提示词轨道
/memory status 查看记忆作用域、路径与容量阈值
Shift+Tab      循环切换执行模式
Ctrl+O         展开或折叠执行详情
```

Xenon 会在多轮工具调用中保留 DeepSeek 原生的 `reasoning_content`、`tool_calls` 和 `tool_call_id` 消息。文件及命令工具在执行前会经过权限策略检查。v0.8.2 还会为工具执行写入有界且隐私安全的恢复点，包括并行 Plan-Execute 步骤；会话中断后可以恢复，而不会重放有状态操作。

## 缓存与费用观测

状态栏、`/cost` 视图和退出摘要基于 API 返回的 `usage` 字段，在本地计算缓存命中率与预估费用。v0.8.2 新增 Cache Rails：每个模型维护独立的追加式提示词轨道，切换模型后再次返回时不会重建该模型的稳定前缀。`/cache lanes` 提供不含提示词原文的轨道诊断，真实命中率仍以厂商 `usage` 为准；观测和缓存亲和均不会额外调用模型。详细设计与真实供应商验收见 [DeepSeek 缓存指南](https://github.com/xianyu-sheng/Xenon/blob/v0.8.2/docs/deepseek-guide.md)。

## 用户治理记忆

Xenon v0.8.2 提供会话、项目本地、项目共享和用户全局四个隔离的记忆作用域。
用户明确说“记住这个项目使用 Python 3.12”时，Xenon 会立即保存，并回显记忆
ID、作用域和准确的本地路径。若 Xenon 自己发现可能值得长期复用的信息，它只会
展示候选内容、原因、作用域与保存位置；未经用户确认不会持久化。

记忆受 token 阈值约束，可用 `/memory inspect` 检查、用 `/memory doctor` 诊断。
潜在冲突只提示而不静默覆盖，`/memory replace` 与 `/memory rollback` 保证变更可逆。
存储和授权模型详见[记忆系统规范](https://github.com/xianyu-sheng/Xenon/blob/v0.8.2/docs/MEMORY_SYSTEM_SPEC.md)。

## 视觉桥接器（可选）

按 `Ctrl+Alt+V` 可附加图片。当模型池中已配置的供应商支持视觉输入时，Xenon 会让该模型描述图片，再将文字描述交给 DeepSeek 推理。此功能复用已有供应商凭证，并不表示 DeepSeek 模型本身具备多模态能力。
