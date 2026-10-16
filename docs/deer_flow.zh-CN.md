[English](./deer_flow.md) | [简体中文](./deer_flow.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeerFlow

[DeerFlow](https://github.com/bytedance/deer-flow) 是字节跳动开源的超级智能体运行框架（Super Agent Harness），具备多子 Agent 协同编排、长短期记忆管理、安全沙箱代码执行以及可扩展 Skill 生态等核心能力。

DeerFlow 原生内置 `PatchedChatDeepSeek` 模型驱动，完美兼容 DeepSeek 的 `reasoning_content` 思考过程流式回放。

- **GitHub 仓库：** <https://github.com/bytedance/deer-flow>
- **官方网站：** <https://deerflow.tech>

---

## 1. 获取 DeepSeek API Key

1. 登录 [DeepSeek 开放平台](https://platform.deepseek.com/)。
2. 进入 **API Keys** 页面，创建并复制 API Key。

---

## 2. 安装与准备 DeerFlow

克隆 DeerFlow 仓库：

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
```

从示例配置文件复制生成配置文件：

```bash
cp config.example.yaml config.yaml
```

配置环境变量（可在当前 shell 环境导出或写入 `.env` 文件）：

```bash
echo "DEEPSEEK_API_KEY=sk-your-deepseek-api-key" >> .env
```

---

## 3. 在 `config.yaml` 中配置 DeepSeek

编辑 `config.yaml` 文件，在 `models` 节点下声明 DeepSeek-V4 系列模型，并指定默认主模型：

```yaml
# ============================================================================
# LLM 模型配置
# ============================================================================
default_model: deepseek-v4-pro

models:
  # 支持深度思考的 DeepSeek-V4-Pro
  - name: deepseek-v4-pro
    display_name: DeepSeek-V4-Pro (Thinking)
    use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
    model: deepseek-v4-pro
    api_key: $DEEPSEEK_API_KEY
    timeout: 600.0
    max_retries: 2
    max_tokens: 8192
    supports_thinking: true
    supports_vision: false
    when_thinking_enabled:
      extra_body:
        thinking:
          type: enabled
    when_thinking_disabled:
      extra_body:
        thinking:
          type: disabled

  # 面向轻量子任务的 DeepSeek-V4-Flash
  - name: deepseek-v4-flash
    display_name: DeepSeek-V4-Flash
    use: deerflow.models.patched_deepseek:PatchedChatDeepSeek
    model: deepseek-v4-flash
    api_key: $DEEPSEEK_API_KEY
    timeout: 300.0
    max_retries: 2
    max_tokens: 8192
    supports_thinking: false
    supports_vision: false
```

### 关键能力说明

- **100 万 Token 超大上下文**：DeepSeek-V4 系列模型支持高达 1,000,000 tokens 上下文窗口，在 DeerFlow 处理海量文件检索、复杂代码重构与多轮长任务交互时游刃有余。
- **深度思考模式（Thinking Mode）**：通过开启 `supports_thinking: true` 并传入 `thinking: { type: "enabled" }`，框架能稳定接收并解析模型的思考链过程。
- **子 Agent 智能分流**：可将 `deepseek-v4-flash` 配置为 `subagents.default_model`，在保持主 Agent 深度推理的同时显著优化端到端延迟与 Token 成本。

---

## 4. 启动与使用

### 方式 A：Docker 快速启动（推荐）

```bash
docker compose up -d
```

### 方式 B：本地开发环境启动

确保系统已安装 Python 3.12+ 与 Node.js 22+：

```bash
make dev
```

启动完成后，在浏览器访问 `http://localhost:2026` 即可开始使用由 DeepSeek 驱动的超级智能体！
