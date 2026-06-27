# 接入 Orcana

[English](./orcana.md) · [← 返回](../README.zh-CN.md)

Orcana 是一个 DeepSeek-native 的终端 Coding Agent runtime，面向长时间运行的软件工程任务。

它的核心方向是 constraint-first coding workflow：任务识别、计划门控、任务包、受控工具调用、补丁事务、证据化完成，以及用于编码会话的交互式 TUI。

- GitHub: https://github.com/Leo-Ayh-Oday/deepseek-orcana

## 1. 安装 Orcana

Orcana 需要 Node.js 18+ 或 Bun。

通过 npm 安装：

```bash
npm install -g deepseek-orcana
```

或者从源码安装：

```bash
git clone https://github.com/Leo-Ayh-Oday/deepseek-orcana.git
cd deepseek-orcana
bun install
bun run build
```

验证安装：

```bash
orcana --version
```

## 2. 获取 DeepSeek API Key

前往 DeepSeek Platform 获取 API Key：

```
https://platform.deepseek.com
```

Orcana 通过环境变量或本地配置文件使用 DeepSeek。

## 3. 配置 DeepSeek

### 方式一：环境变量

Linux / macOS：

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export DEEPSEEK_MODEL_OVERRIDE="deepseek-v4-pro"
```

Windows PowerShell：

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:DEEPSEEK_MODEL_OVERRIDE="deepseek-v4-pro"
```

### 方式二：配置文件

复制配置模板并编辑：

```bash
mkdir -p ~/.deepseek-code
cp settings.example.json ~/.deepseek-code/settings.json
```

配置文件采用嵌套结构：

```json
{
  "provider": {
    "baseUrl": "https://api.deepseek.com/anthropic",
    "apiKey": "${DEEPSEEK_API_KEY}",
    "modelOverride": "deepseek-v4-pro",
    "costMode": "normal",
    "idleTimeoutMs": 60000
  },
  "loop": {
    "maxSteps": 100,
    "autoContinue": false
  },
  "memory": {
    "compactionEnabled": true
  },
  "sandbox": {
    "enabled": true
  }
}
```

Orcana 的 ModelRouter 使用 `deepseek-v4-pro` 进行计划、编码、修复和审查，使用 `deepseek-v4-flash` 进行快速任务识别、轻量判断和辅助调用。复杂编码任务默认使用 max reasoning effort。

DeepSeek V4 支持 1M token 上下文窗口 — Orcana 自动追踪上下文预算，524K 警告，629K 阻止。

## 4. 在项目中启动 Orcana

进入你的项目目录：

```bash
cd /path/to/your-project
```

启动交互式 TUI：

```bash
orcana
```

非交互式一次性 prompt：

```bash
orcana "分析这个项目结构，找到主要入口文件"
```

其他命令：

```bash
orcana --cli "修复 src/utils.ts 里的类型错误"   # CLI 模式
orcana list                                       # 列出所有会话
orcana last                                       # 恢复最近会话
```

## 5. 第一个编码任务

建议先从小型、可验证的任务开始：

```
在这个 TypeScript 项目里找一个简单的类型错误，解释根因，修复它，并运行相关的验证命令。
```

对于更复杂的任务，Orcana 会先计划再修改：

```
重构 TUI 的输入组件，使长文本粘贴不阻塞渲染。
先检查相关文件，产出计划，然后实现最小安全变更并验证。
```

## 6. Orcana 如何使用 DeepSeek

Orcana 围绕 DeepSeek-native coding workflow 设计：

- 使用 `deepseek-v4-pro` 进行计划、编码、修复和审查。
- 使用 `deepseek-v4-flash` 进行快速任务识别、轻量判断和辅助调用（6 个独立 Flash 角色）。
- 复杂工程任务默认使用 max reasoning effort。
- 缓存感知的 prompt 布局：稳定前缀（系统规则 + 工具 schema + 项目宪法）一次性计算，全会话复用。
- 支持 FIM 风格的局部代码编辑（基于 Anthropic 兼容端点），受 PatchTransaction 保护。
- thinking token 跨上下文压缩周期保留。
- 支持长上下文任务执行和上下文预算追踪。

## 7. 核心特性

### 计划和任务控制

Orcana 使用 planning gate 和 TaskPacket 来减少盲目编辑。复杂任务在实现前必须先产出计划、范围、完成标准和验证要求。

### 补丁事务

代码编辑被记录为 patch transaction：`read → record baseHash → propose → check scope → apply → verify → commit / rollback`。文件修改保持范围可控、可审计，验证失败时可回滚。

### Ripple 引擎 2.0

在任何文件写入前，Ripple 引擎追踪变更如何传播到整个代码库。7 层：API Diff → 语义引用 → 用法分类 → 验证映射 → 义务门控。在所有受影响的调用方处理完之前阻止写入。212 tests，8.5/10。

### 证据化完成

Orcana 记录 typecheck、test、build 或 manual inspection 等验证证据。没有必要证据时，Agent 被阻止声称任务完成。Final Truthfulness Gate 将完成文本与 EvidenceLedger 交叉校验。

### 面向长任务的 TUI

交互式 TUI 面向包含计划、工具调用、代码编辑、验证和修复循环的编码任务。展示当前 mode、计划节点、任务包、工具流、补丁状态、证据状态和 gate block 原因。

### 工具风险分级

工具按风险分五级：Risk 0（只读，自动放行）、Risk 2（文件写入，策略判定）、Risk 4–5（git mutation、外部效应 — 需用户确认，禁止 session allow）。

## 8. 推荐使用场景

适合使用 Orcana 的场景：

- TypeScript / JavaScript 仓库理解。
- 带验证的 bug 修复。
- TUI / CLI 功能迭代。
- 需要计划和受控编辑的重构任务。
- DeepSeek-native Coding Agent 实验。

建议先从小型、可验证任务开始，再尝试大范围多文件任务。

## 9. 已知限制

Orcana 仍是实验性的 Coding Agent runtime。一些运行时能力仍在演进中：lifecycle hooks、长任务记忆、端到端 replay、完整 rewind 工作流。

对于高风险操作，请在接受结果前检查计划、改动和验证输出。除非你完全理解工具权限和回滚行为，否则不要在生产仓库中使用自动批准模式。

当前版本：v0.2.1。目标：v1.0（10 Phase / 32 PR 组 / 17 条可验证验收标准）。

## 10. 故障排查

### 找不到 API Key

检查 `DEEPSEEK_API_KEY` 是否存在：

```bash
echo $DEEPSEEK_API_KEY
```

Windows PowerShell：

```powershell
echo $env:DEEPSEEK_API_KEY
```

### 模型名错误

请使用当前 DeepSeek V4 模型名：

```
deepseek-v4-pro
deepseek-v4-flash
```

避免使用旧模型名，例如 `deepseek-chat`、`deepseek-reasoner` 或 `deepseek-coder`。

### 上下文窗口没有配置

DeepSeek V4 支持 1M token 上下文窗口。Orcana 通过 ContextEpoch 自动管理 — 无需手动配置。

### 推理强度太低

复杂编码任务默认使用 max reasoning effort。可在 `~/.deepseek-code/settings.json` 中确认。

### 命令找不到

可用命令：`orcana`、`deepseek-orcana`、`deepseek-code`、`deepseek`。如果 `orcana` 找不到，尝试 `npx deepseek-orcana`。
