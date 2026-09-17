# Raidho

[Raidho](https://github.com/vitaliyfedotovpro-art/raidho) 是一个**用一个模型规划、
用另一个模型执行**的编码智能体，并带有可在多次运行之间保留事实的持久化记忆。它不绑定
特定服务商，使用你自己的 API 密钥运行——非常适合 DeepSeek：把 `deepseek-v4-pro`
放在推理端，把更便宜的 `deepseek-v4-flash` 放在执行端，这样高 token 消耗的工具循环
在快速模型上运行，而规划则使用强模型。

## 安装

需要 Python ≥ 3.11。

```bash
git clone https://github.com/vitaliyfedotovpro-art/raidho
cd raidho
pip install -e '.[openai-compat]'   # DeepSeek / 兼容 OpenAI 的后端
pip install -e '.[embed]'           # 可选：语义记忆召回
```

或使用引导式安装脚本，它会实时校验你的密钥并运行一次冒烟测试：

```bash
bash install.sh
```

## 为 DeepSeek 配置

单一服务商——全部在 DeepSeek 上运行：

```bash
export CODER_PROVIDER=deepseek
export CODER_MODEL=deepseek-v4-flash      # 执行模型
export DEEPSEEK_API_KEY=sk-...
```

分离模式（Raidho 的核心）——用 `deepseek-v4-pro` 推理，用 `deepseek-v4-flash` 执行：

```bash
export CODER_PROVIDER=deepseek            # 执行（code 模式，工具循环）
export CODER_MODEL=deepseek-v4-flash
export CODER_REASON_PROVIDER=deepseek     # 推理（text 模式）
export CODER_REASON_MODEL=deepseek-v4-pro
export DEEPSEEK_API_KEY=sk-...
```

DeepSeek V4 模型支持 100 万 token 的上下文窗口，因此长文件和多步工具循环无需手动截断
即可容纳。端点（`https://api.deepseek.com/chat/completions`）会自动使用；DeepSeek
无需覆盖 base-URL。

## 首次运行

无界面模式——运行单个任务后退出：

```bash
coder "create a FastAPI hello-world app and run it"
```

交互式 REPL：

```bash
coder
```

在 REPL 中：

- `/code` — 智能体编码（工具循环，在 `CODER_MODEL` 上执行）
- `/text` — 推理对话（若设置了 `CODER_REASON_MODEL` 则在其上运行）
- `/council <question>` — 两个服务商辩论，由中立环节提炼共识（一致点、遗留分歧、建议）
- `/ctx` — 切换 context-first 模式
- `/learn` — 切换对重复只读工具循环的自动蒸馏
- `/quit` — 退出

## 记忆

Raidho 记住 `(主语, 关系, 宾语)` 形式的事实，并在每一轮把相关事实召回到提示词中。
新事实通过 `remember` 工具保存，议会结论会自动蒸馏为事实。记忆按项目写入
`<workdir>/.raidho/memory`，下次运行时自动重新加载——今天得出的决定明天会重新浮现，
仅在相关时召回，且支持跨语言。它采用向量符号架构（VSA），而非 RAG；使用它无需了解
其内部实现。REPL 在启动时会打印加载了多少条事实。
