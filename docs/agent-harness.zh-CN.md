# 集成 Jig

[English](./awesome-deepseek-agent-guide.md) | [简体中文](./awesome-deepseek-agent-guide.zh-CN.md) · [← Back](../README.md)

Jig 是一个 Python 多 Agent 编排框架，内置 12 个预设角色、4 层记忆架构和硬约束 Harness 层。针对 DeepSeek V4 API 做了缓存优先前缀哈希、Flash 优先成本路由和自动 Tool-Call Repair 优化。

#### 1. 前置条件

- Python 3.10+
- 从 [DeepSeek 平台](https://platform.deepseek.com/api_keys) 获取 API Key

#### 2. 安装

```bash
# 克隆仓库
git clone https://github.com/luyi14-bits/agent-harness.git
cd agent-harness

# 安装依赖
pip install pydantic>=2.0 pydantic-settings>=2.0 pyyaml>=6.0
```

#### 3. 配置

设置环境变量：

```bash
# Linux / macOS
export DEEPSEEK_API_KEY="sk-your-key-here"

# Windows
set DEEPSEEK_API_KEY=sk-your-key-here
```

或在项目根目录创建 `.env` 文件：

```
DEEPSEEK_API_KEY=sk-your-key-here
```

#### 4. 首次运行

```bash
# 启动交互式群聊模式
python run.py
```

输入 `help` 查看可用命令，或直接输入自然语言请求如 `"帮我写一个登录功能的 PRD"`。

#### 5. 挂载自定义 Skill

```bash
python run.py --attach my-custom-skill
```

---

## DeepSeek 专有优化

Jig 为 DeepSeek V4 API 专门优化：

### 缓存优先前缀哈希

使用 SHA-256 前缀哈希最大化 DeepSeek 的上下文缓存打折（缓存命中仅需 2% 费用）。不可变上下文前缀会冻结到 session 结束时，前缀不变时缓存命中率接近 100%。

### Flash 优先成本路由

所有 Agent 默认使用 `deepseek-v4-flash`。短查询（<100 token）保持 Flash；复杂任务自动升级到 `deepseek-v4-pro`。Token 预算防止成本失控。

### 推理力度控制

```python
from jig.adapters.deepseek_adapter import DeepSeekAdapter
adapter = DeepSeekAdapter(reasoning_effort="high")  # low / medium / high
```

### 自动 Tool-Call Repair

DeepSeek V4 的 FC 返回偶尔有格式错误（末尾逗号、未引号 key、代码块包裹）。Jig 用 4 层修复链自动处理，全部失败时优雅降级到纯文本模式。

### 100 万 Token 上下文

Jig 完整支持 DeepSeek V4 的 100 万 token 上下文窗口。

### 硬约束 Harness 层

与纯 prompt 框架不同，Jig 通过 3 层 ToolGuard（白名单/黑名单/调用前钩子）在工具执行前拦截，5 阶段 LOOP SOP 门禁自动降级。

---

## 定价参考

| 模型 | 输入 / M tokens | 输出 / M tokens | 缓存命中 / M tokens |
|-------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |
