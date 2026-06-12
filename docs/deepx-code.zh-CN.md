[English](./deepx-code.md) | [简体中文](./deepx-code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 deepx-code

[deepx-code](https://github.com/itmisx/deepx-code) 是一款以 DeepSeek 为原生后端、运行在终端里的编程 Agent。用 Go 开发，小巧快速、全平台覆盖；通过自动上下文压缩与零 token 的本地关键词路由，大幅降低长会话的 token 成本。还内置代码图谱做符号级导航（减少 read/glob/grep 的 token 浪费），以及本地图片 OCR（PaddleOCR PP-OCRv5）做离线截图识别，并接入 MCP 与 Claude 生态的 skill。

#### 1. 安装 deepx-code

macOS / Linux —— 安装预编译二进制到 `~/.local/bin/deepx`：

```
curl -fsSL https://raw.githubusercontent.com/itmisx/deepx-code/main/scripts/install.sh | bash
```

Windows（PowerShell）：

```
irm https://raw.githubusercontent.com/itmisx/deepx-code/main/scripts/install.ps1 | iex
```

随时用 `deepx upgrade` 升级。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。deepx-code 首次启动会弹出内置向导询问 Key，并持久化到 `~/.deepx/model.yaml` —— 无需配置环境变量。默认配置将两个角色都指向 `api.deepseek.com`，使用 **DeepSeek-V4-Flash** / **DeepSeek-V4-Pro**，上下文窗口 100 万 token。

#### 3. 进入项目目录，执行 `deepx` 即可开始使用。

```
cd /path/to/my-project
deepx
```

deepx-code 默认使用 **DeepSeek-V4-Flash** 跑日常迭代以控制成本，遇到复杂多步任务自动升级到 **DeepSeek-V4-Pro**。TUI 内：`/plan`（只读规划）、`/auto`（全自动）、`/review`（写操作与命令需确认）、`/compact`（压缩会话以节省上下文）、`/lang`（中英切换）。输入 `/help` 查看完整 slash 命令参考。

把图片路径丢进对话（比如报错截图或 UI 稿），deepx-code 会用内置 OCR 读出其中文字 —— 本地推理，不依赖多模态 API。首次使用会下载 ONNX runtime 与 PaddleOCR 模型（约 37MB），之后离线运行、秒级响应。
