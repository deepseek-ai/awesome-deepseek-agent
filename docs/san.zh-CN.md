[English](./san.md) | [简体中文](./san.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 San

San 是开源的终端 Agent 运行时 —— 单个 Go 原生二进制，不依赖 Node.js 或 Python。DeepSeek 是**内置供应商**：V4 模型 ID、100 万 token 上下文、推理强度与每轮费用都已经接好，你只需要准备一个 API Key。

- **GitHub：** <https://github.com/genai-io/san>
- **文档：** <https://genai-io.github.io/san/>

#### 1. 安装 San

Homebrew（macOS / Linux）：

```bash
brew tap genai-io/san
brew install san
```

安装脚本（macOS / Linux）：

```bash
curl -fsSL https://raw.githubusercontent.com/genai-io/san/main/install.sh | bash
```

Windows（PowerShell）：

```powershell
irm https://raw.githubusercontent.com/genai-io/san/main/install.ps1 | iex
```

或使用 Go 1.25.8+：

```bash
go install github.com/genai-io/san/cmd/san@latest
```

验证安装：

```bash
san version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制 API Key。

#### 3. 接入 DeepSeek

**方式 A —— 在应用内配置。** 启动 San 并打开模型选择器：

```bash
san
```

```
/models
```

选择 **DeepSeek**，按提示粘贴 API Key，San 会保存下来供后续会话使用。

**方式 B —— 环境变量。** San 启动时会读取 `DEEPSEEK_API_KEY`：

```bash
export DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

```powershell
$env:DEEPSEEK_API_KEY="<你的 DeepSeek API Key>"
```

如果你通过网关或代理访问，再设置 `DEEPSEEK_BASE_URL`，默认值为 `https://api.deepseek.com`。

#### 4. 选择模型

再次运行 `/models`，选择：

- `deepseek-v4-pro` —— 编程能力最强
- `deepseek-v4-flash` —— 更快、更便宜

两者都已内置 V4 的完整规格：**100 万 token 上下文**、最高 **384K 输出 token**，无需再手动填写上下文窗口配置。状态栏里的会话费用按 DeepSeek 官方价格计算，含缓存命中价。

#### 5. 调高思考强度

DeepSeek V4 默认开启思考，默认强度为 `high`。San 提供完整的强度阶梯 —— `off · low · high · xhigh · max`，可以直接指定：

```
/think max
```

也可以用 `Ctrl+T` 在这些档位之间循环切换。做高难度编程任务时建议保持 **`max`**；`xhigh` 同样可用，DeepSeek 会将其映射为 `high`。只有 `off` 会关闭思考模式。

到这里就完成了 —— 在任意项目目录执行 `san`，即可基于 DeepSeek V4 开始编程。

> **提示：** `/context` 可以按类别查看 100 万上下文窗口被什么占满，`/models` 可在会话中途切换模型且不丢失对话。
