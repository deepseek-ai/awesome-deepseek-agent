[English](./adal.md) | [简体中文](./adal.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 AdaL

AdaL 是一款开源的 AI 编程 Agent 命令行工具，面向终端软件工程场景，并提供 SDK 与云端 Agent 托管选项。

#### 1. 安装 AdaL

**macOS、Linux、WSL：**

```
curl -fsSL https://adal.sylph.ai/install.sh | bash
```

**Windows PowerShell：**

```
irm https://adal.sylph.ai/install/windows | iex
```

**Windows CMD：**

```
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://adal.sylph.ai/install/windows | iex"
```

验证安装：

```
adal --version
```

#### 2. 运行与配置

- 在项目目录中启动 AdaL：

```
cd /path/to/my-project
adal
```

- 将当前模型切换为 DeepSeek-V4-Pro：

```
/model deepseek-deepseek-v4-pro
```

更快、更低成本的 DeepSeek-V4-Flash 也可通过 `deepseek-deepseek-v4-flash` 使用。

AdaL 通过其自有的托管代理路由 DeepSeek 请求，费用从 AdaL 的额度/订阅中扣除——目前尚不支持针对 DeepSeek 的自带密钥（BYOAK）方式（AdaL 的 BYOAK 目前仅支持 Anthropic、OpenAI 和 Google）。

AdaL 的模型注册表已自动为两款模型设置了接近 100 万 token 上限的输入上下文窗口（V4-Pro 为 936K，V4-Flash 为 984K），无需手动配置。由于 DeepSeek-V4 在 AdaL 的 Provider 抽象层中未声明单次请求的推理强度（reasoning effort）参数，AdaL 目前未针对 DeepSeek 暴露独立的推理强度开关。

#### 3. 非交互 / Headless 模式

DeepSeek 模型同样适用于 AdaL 的 headless 模式，方便脚本化与 CI 场景：

```
adal -q "Refactor this function for readability" -m deepseek-deepseek-v4-pro
```
