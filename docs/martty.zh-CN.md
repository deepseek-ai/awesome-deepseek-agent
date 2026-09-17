[English](./martty.md) | [简体中文](./martty.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Martty

Martty 是一款采用 Rust 和 ratatui 编写的开源终端原生 ACP 客户端。它默认启动 DeepSeek Harness，并在可扩展 TUI 中呈现流式推理、工具调用、子代理、Plan、图片和持久会话。

- **GitHub：** <https://github.com/openma-ai/Martty>
- **网站：** <https://martty.sh>

#### 1. 安装 Martty

Martty 需要 Node.js 18 或更高版本。安装已发布的 npm 包：

```sh
npm install --global martty
martty --version
```

如果只想预览界面，不使用 API Key 或 Agent Runtime：

```sh
martty --demo
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key，然后将其提供给启动 Martty 的进程：

```sh
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

Martty 也支持在运行界面中通过 `/auth` 使用 ACP 认证。凭据由 Agent Runtime 管理，不会写入对话。

#### 3. 进入项目并启动 Martty

```sh
cd /path/to/my-project
martty --model deepseek-v4-pro
```

未指定 `--model` 时，默认的 DeepSeek Harness 集成会使用 `deepseek-v4-flash`。进入 Martty 后：

1. 输入 `/model`，在 `deepseek-v4-pro` 与 `deepseek-v4-flash` 之间切换。
2. 输入 `/effort max`，让 DeepSeek-V4-Pro 使用最高推理强度。
3. 发送编程任务，例如：`检查这个仓库，并为失败的测试提出最小且安全的修复方案。`

DeepSeek-V4-Pro 与 DeepSeek-V4-Flash 支持 **100 万 token 上下文窗口**以及最高 **38.4 万输出 token**。Martty 会读取 DeepSeek Harness 实时公布的模型与会话能力，因此客户端不需要另行设置上下文窗口。参见[当前模型信息](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)与[思考模式文档](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode)。

#### 常用命令

| 命令 | 操作 |
|---|---|
| `/model` | 选择当前 Agent 公布的模型 |
| `/effort` | 选择推理强度（`off`、`high` 或 `max`） |
| `/permission` | 选择会话权限模式 |
| `/new` | 创建新的持久会话 |
| `/resume` | 恢复以前的会话 |
| `/image <path>` | 向下一条 prompt 添加本地图片 |
| `/ui deepseek` | 切换到内置 DeepSeek UI 预设 |
| `/auth` | 通过 ACP 完成认证 |

模型回合运行时，`Enter` 会排队 follow-up，`Ctrl+X` 会立即 steer 当前回合，`Esc` 会中断回合并保留草稿。

#### 可选：作为 DeepSeek Harness Profile 管理

如果已经安装 DeepSeek Harness，可以把 Martty 作为 Profile Plugin 管理：

```sh
npm install --global @deepseek-ai/dsh
dsh plugin --profile martty add martty@latest
dsh --profile martty
```

这种方式由 DeepSeek Harness 管理 Profile、插件和升级，Martty 继续作为终端客户端。
