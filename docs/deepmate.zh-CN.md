[English](./deepmate.md) | [简体中文](./deepmate.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 将 DeepSeek 接入 Deepmate

[Deepmate](https://github.com/kevin0x5/deepmate) 是面向长期项目工作的本地优先 Agent 工作台，提供成本感知的上下文管理、受治理的 Skill、MCP 与工具调用、任务恢复和自进化能力，并针对 DeepSeek V4 进行了专门优化。

## 1. 安装 Deepmate

Deepmate 需要 Python 3.11 或更高版本。

```bash
python3 -m pip install --upgrade deepmate
```

检查安装结果与本地环境：

```bash
deepmate --doctor
```

## 2. 配置 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/) 创建 API Key。请通过环境变量保存，不要写入项目文件。

macOS 或 Linux：

```bash
export DEEPSEEK_API_KEY="<your-api-key>"
```

PowerShell：

```powershell
$env:DEEPSEEK_API_KEY = "<your-api-key>"
```

Deepmate 会在运行时读取该变量，自动生成的配置中只保存环境变量引用。

## 3. 在项目中启动 Deepmate

进入需要处理的项目目录并启动：

```bash
cd /path/to/your/project
deepmate
```

首次启动时，Deepmate 会创建本地配置。默认的 DeepSeek 配置为：

- 日常任务使用 `deepseek-v4-flash`；
- 需要更强模型时使用 `deepseek-v4-pro`；
- 上下文窗口为 1,000,000 token。

在终端界面中输入任务即可开始。Deepmate 可以规划和执行长任务、创建检查点、恢复中断的工作，并对受治理的工具操作发起审批。

## 4. 使用 DeepSeek V4 Pro 与最高推理强度

对于复杂的一次性任务，可以选择 V4 Pro 并启用最高推理强度：

```bash
deepmate \
  --model deepseek-v4-pro \
  --thinking enabled \
  --reasoning-effort max \
  "检查这个项目，并给出安全的迁移方案。"
```

启动交互界面时也可以使用相同的模型与推理选项。任务模式命令、配置说明和故障排查请参阅 [Deepmate 文档](https://github.com/kevin0x5/deepmate#readme)。
