[English](./rekall.md) | [简体中文](./rekall.zh-CN.md) · [← Back](../README.md)

# 集成 Rekall

Rekall 不是一个编程代理。它是底层——一个透明的 HTTP 代理，拦截代理向 DeepSeek 发出的请求，去除框架噪声，并将剩余内容压缩为密集的中文（约 100:1 压缩率）。模型自然地解压中文。你在不增加系统提示膨胀的情况下获得持久的身份记忆。

- **GitHub:** <https://github.com/rekall-labs/ren>
- **SIGNATURE:** 260 个中文字符——压缩后的身份。阅读它以理解该方法。

#### 1. Rekall 的作用

在你的代理（Hermes、Claude Code、OpenCode 等）和 DeepSeek API 之间，Rekall：

| 阶段 | 操作 | 原因 |
|-------|--------|------|
| **分类** | 三分桶：静态（身份、规则）、动态（对话）、工具调用（原样保留） | 含图片 URL 的工具调用必须原样通过 |
| **剥离** | 14 条正则规则去除品牌 XML、RLHF 指令、技能目录、记忆块 | 对回访用户来说这些是噪声 |
| **压缩** | qwen2.5:0.5b 以 temp=0 压缩前 4K 字符 → 约 150 字符中文 | 0.5B 模型无法添油加醋——纯粹压缩 |
| **重建** | 静态规则 + 中文上下文 + 保留工具调用 + 英文用户消息 | 模型看到干净的信号 |
| **转发** | 发送至 `api.deepseek.com/v1/chat/completions` | 透明代理——代理不知道它的存在 |

#### 2. 安装

**依赖：**

```bash
# 安装压缩模型
ollama pull qwen2.5:0.5b

# Python 代理
pip install httpx uvicorn starlette
```

**启动代理：**

```bash
python3 prompt_proxy_v2.py --port 8787 --preamp --api-key "$DEEPSEEK_API_KEY"
```

或通过启动脚本：

```bash
bash start_preamp.sh
```

**配置你的代理：**

```yaml
model:
  provider: deepseek
  base_url: http://localhost:8787/v1
  default: deepseek-v4-pro
```

你的代理向 `localhost:8787` 发送请求，而不是直接发送到 `api.deepseek.com`。Rekall 处理并转发。代理永远不会知道代理的存在。

#### 3. 体验变化

| 方面 | 直接使用 DeepSeek | 通过 Rekall |
|--------|----------------|------------|
| **个性** | 热情、恭敬、RLHF 锚定 | 直接、任务聚焦、用户调优 |
| **记忆** | 仅会话 | 持久的压缩身份 |
| **上下文用量** | 系统提示约 50K tokens | 约 500 字符中文（~100:1） |
| **工具调用** | 在系统提示上下文中 | 原样通过 |
| **拒绝** | "我无法帮助" | 模型根据用户历史评估请求 |
| **降级** | — | Ollama 不可用时仅正则剥离 |

#### 4. 架构说明

**三分桶** 是在实践中发现的，后来与 DeepSeek 的 Engram 研究独立对齐：
- **静态**（身份、规则）→ 对应 Engram 的条件内存（O(1) 查找）
- **动态**（对话）→ 对应动态计算（注意力层）
- **工具调用**原样保留 → 对应 Engram 的上下文感知门控绕过

**为什么用 0.5B？** 更大的模型会解释、添油加醋、"帮助"。0.5B 模型只能保留或丢弃——二元的。这是压缩器所需的性质——不是智能，只是保真度。

**为什么用中文？** 信息密度约为英文的 3 倍。任何能读中文的模型（DeepSeek、Qwen 等）在推理时都能自然解压，零额外成本。这不是语言选择，是编码选择。

#### 5. 配置

详见 [`docs/config.md`](https://github.com/rekall-labs/ren/blob/main/docs/config.md)：

- 直连模式——无代理，直接连接 DeepSeek API
- 预放模式——通过 `:8787` 端的 Rekall 路由
- 使用 `/profile use` 热切换

#### 6. 故障排除

| 症状 | 可能原因 | 修复 |
|---------|-------------|-----|
| `Connection refused :8787` | 代理未运行 | 启动代理 |
| `本地预放失败 (5xx)` | Ollama 未运行 | `ollama serve` |
| 视觉调用失败 | 预放在压缩工具消息 | 升级到 v2——已修复 |
| 模型忘记身份 | 压缩器丢失意图 | 调整 `num_predict` 或检查正则剥离规则 |
