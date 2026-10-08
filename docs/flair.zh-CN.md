[English](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/docs/flair.md) | [简体中文](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/docs/flair.zh-CN.md) · [← 返回](https://github.com/deepseek-ai/awesome-deepseek-agent/blob/main/README.md)

# 集成 flair

flair 是一个开源、以 DeepSeek 为先的智能体 AI 助手，具备两大能力——高级**编程**与通用**桌面自动化**——可运行于 Linux、macOS 和 Windows。它使用兼容 OpenAI 的协议，并以 DeepSeek V4 作为主要提供方。

- **GitHub:** <https://github.com/NAST0R/flair>

#### 1. 安装 flair

需要 Python ≥ 3.10。

```
git clone https://github.com/NAST0R/flair.git
cd flair
pip install -e .
# 可选扩展（更详细的内存/CPU 信息、跨平台剪贴板），供通用智能体使用：
pip install -e ".[extras]"
```

#### 2. 为 DeepSeek 配置 flair

flair 从 `.env` 文件加载配置。复制模板并填入你的 DeepSeek 密钥：

```
cp .env.example .env
```

然后编辑 `.env`，将 DeepSeek 设为当前提供方：

```
FLAIR_PROVIDER=deepseek

DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-flash       # 快速主力模型（非思考）
DEEPSEEK_THINK_MODEL=deepseek-v4-pro   # 用于 --think 的推理模型

FLAIR_ROOT=.                           # 编程智能体被限制的工作根目录
FLAIR_AUTO_APPROVE=false               # 执行破坏性操作前需确认
```

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API 密钥。

**配置项：**

| 变量 | 说明 |
| --- | --- |
| `FLAIR_PROVIDER` | 当前提供方——设为 `deepseek` |
| `DEEPSEEK_API_KEY` | 你的 DeepSeek API 密钥 |
| `DEEPSEEK_MODEL` | 快速、非思考模型（默认 `deepseek-v4-flash`） |
| `DEEPSEEK_THINK_MODEL` | 用于 `--think` 步骤的推理模型（默认 `deepseek-v4-pro`） |
| `FLAIR_ROOT` | 编程智能体被限制的工作根目录 |
| `FLAIR_AUTO_APPROVE` | 跳过破坏性操作的确认提示（默认 `false`） |

> **思考模式与 1M 上下文。** 在 DeepSeek **V4** 上，思考模式通过*参数*开启，而非使用单独的模型名。flair 仅在 `--think` 步骤自动启用它，并使用 `deepseek-v4-pro`（真正的推理模型）；快速工具循环则保持在 `deepseek-v4-flash`。两个 V4 模型都提供 **100 万 token** 的上下文窗口——flair 直接依据 API 返回的 `prompt_tokens` 精确测量上下文，并在接近阈值（默认为窗口的 75%）时自动压缩历史，从而保持前缀缓存有效。

> **成本跟踪。** flair 依据每个模型的价格表（可通过 `FLAIR_PRICE_*` 覆盖）估算每轮成本，并可用 `--max-cost <usd>` 设置硬性上限。请在 [DeepSeek 价格页面](https://api-docs.deepseek.com/quick_start/pricing) 查看当前费率。

#### 3. 运行 flair

```
flair                                  # 交互式 REPL，在编程与通用之间自动路由
flair -p "open youtube for me"         # 单次任务
flair --think -p "refactor the parsing module to reduce complexity"   # 首步使用推理模型
flair --root ~/projects/my-repo        # 让编程智能体指向某个项目
flair --yes -p "run the tests and fix the errors"                     # 不需确认
```

**常用 REPL 命令：**

| 命令 | 作用 |
| --- | --- |
| `/code <task>` | 强制使用编程智能体 |
| `/do <task>` | 强制使用通用智能体 |
| `/think <task>` | 首步使用思考模型 |
| `/provider [name]` | 查看或在运行时切换提供方（`deepseek` / `openai`） |
| `/model <name>` | 运行时切换快速模型 |
| `/think-model <name>` | 运行时切换思考模型 |
| `/cost` | 会话 token / 成本汇总 |
| `/compact` | 立即压缩当前智能体的上下文 |
| `exit` | 退出 |

大功告成——flair 现在已经在 DeepSeek V4 上运行了。
