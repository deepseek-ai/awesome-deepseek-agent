[English](./kun.md) | [简体中文](./kun.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Kun

[Kun](https://github.com/KunAgent/Kun) 是一款开源 AI Agent 工作空间，它将需求澄清、设计稿、实施计划和 Agent 编码整合到同一条 GUI 工作流中。Kun 内置同名本地运行时（`kun serve`），并默认使用 DeepSeek 作为文本与推理主模型。

- **GitHub：** <https://github.com/KunAgent/Kun>

#### 1. 安装 Kun

从 [GitHub Releases](https://github.com/KunAgent/Kun/releases) 下载对应平台的安装包，或从源码运行：

```sh
git clone https://github.com/KunAgent/Kun.git
cd Kun
npm install
npm run dev
```

环境要求：

- [Node.js](https://nodejs.org/en/download/) 20+
- DeepSeek API Key

> **注意：** 首次启动 Kun 时，在设置向导中选择 **DeepSeek** 作为模型供应商并填入 API Key。

#### 2. 为 DeepSeek 配置 Kun 运行时

Kun 的本地运行时会直接请求 DeepSeek API。最简单的启动方式是使用 `kun serve`：

```sh
mkdir -p ~/.deepseekgui/kun
kun serve \
  --data-dir ~/.deepseekgui/kun \
  --api-key "$DEEPSEEK_API_KEY" \
  --base-url https://api.deepseek.com/beta \
  --model deepseek-v4-pro
```

也可以通过环境变量设置 API Key：

```sh
export DEEPSEEK_API_KEY="sk-..."
export KUN_MODEL="deepseek-v4-pro"
kun serve --data-dir ~/.deepseekgui/kun
```

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取你的 API Key。

**常用 CLI 参数：**

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--api-key` | DeepSeek 兼容 API Key | 空 |
| `--base-url` | DeepSeek 兼容 API 地址 | `https://api.deepseek.com/beta` |
| `--model` | 默认模型 id | `deepseek-v4-pro` |
| `--data-dir` | 运行时数据目录 | 必填 |
| `--approval-policy` | 工具审批模式：`auto`、`on-request`、`never` 等 | `auto` |
| `--sandbox-mode` | 文件沙箱：`read-only`、`workspace-write`、`danger-full-access` | `workspace-write` |

#### 3. 使用 DeepSeek V4 模型

Kun 内置了 DeepSeek V4 的模型画像。两个模型都默认配置 **100 万 token** 上下文窗口，并在输入 token 接近 98 万时触发上下文压缩：

| 模型 | 适用场景 |
|------|----------|
| `deepseek-v4-pro` | 复杂推理、规划、代码审查（默认） |
| `deepseek-v4-flash` | 速度更快、成本更低的任务与快速澄清 |

切换默认模型的方式：

- 给 `kun serve` 传入 `--model deepseek-v4-flash`，或
- 设置环境变量 `KUN_MODEL`，或
- 编辑 `~/.deepseekgui/kun/config.json`：

```json
{
  "serve": {
    "model": "deepseek-v4-pro",
    "baseUrl": "https://api.deepseek.com/beta",
    "apiKey": "sk-..."
  }
}
```

#### 4. 在终端中使用 Kun

除了 GUI，Kun 也可以作为独立的 Agent CLI 使用：

```sh
# 单次任务
kun run --data-dir ~/.deepseekgui/kun --workspace "$PWD" "summarize this repo"

# 交互式 REPL
kun chat --data-dir ~/.deepseekgui/kun --workspace "$PWD"

# 列出可用工具
kun exec --data-dir ~/.deepseekgui/kun --workspace "$PWD" --list-tools
```

#### 5. 在 GUI 中开始编码

1. 启动 Kun，在 **Code** 模式中绑定本地项目文件夹。
2. 新建会话并输入问题或指令。
3. Kun 会读取项目上下文、执行工具，并在文件变更前展示内联 diff。

> **提示：** Kun 直接将请求转发给 DeepSeek API，因此 `deepseek-v4-pro` 的深度思考/推理内容可以开箱即用，无需在 Kun CLI 层面额外设置 reasoning-effort 参数。
