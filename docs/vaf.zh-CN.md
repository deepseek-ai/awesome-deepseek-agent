[English](./vaf.md) | [简体中文](./vaf.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 VAF

VAF（Veyllo Agentic Framework）是一个开源的 Agent 框架与运行环境，带有持久记忆，以及用于网页、代码和文件的工具。它可以在 Windows、macOS 和 Linux 上以桌面应用、无界面服务器或终端应用的形式运行，也可以作为 Python 库嵌入到你自己的程序中。DeepSeek 是 VAF 的内置服务商之一，无需配置 Base URL 或自定义端点。

#### 1. 安装 VAF

前置依赖：Git 和容器运行时。安装脚本会自动为你配置容器引擎、Python 和 Node。

###### Linux / macOS

```bash
git clone https://github.com/Veyllo-Labs/VAF.git && cd VAF
chmod +x install.sh && ./install.sh
```

当安装脚本询问安装配置（profile）时，选择 **Lean (API)**：它不会下载本地的对话、语音识别或语音合成模型，对话完全通过 DeepSeek 进行。

###### Windows

```powershell
git clone https://github.com/Veyllo-Labs/VAF.git
cd VAF
.\install.bat
```

更多安装方式请参考 [VAF 安装指南](https://github.com/Veyllo-Labs/VAF/blob/main/docs/setup/INSTALLATION_GUIDE.md)。

#### 2. 配置 DeepSeek

##### 在 Web 界面中配置

使用 `vaf tray` 启动桌面应用（Web 界面地址为 `http://localhost:3000`）并登录，然后：

- **设置 → 常规 → API Key**：在 DeepSeek Key 一栏填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- **设置 → AI 与模型**：服务商选择 **DeepSeek**，并选择模型：`deepseek-v4-pro` 或 `deepseek-flash`。`deepseek-auto` 会在对话中使用 `deepseek-flash`，在后台任务、工作流和上下文压缩中使用 `deepseek-v4-pro`。
- **设置 → AI 与模型 → DeepSeek 思考强度**：选择 **最高**。默认值“标准（DeepSeek 默认）”不会发送思考强度参数，此时 DeepSeek 使用自身的默认值（`high`）。
- 点击 **保存更改**。

##### 在终端中配置

使用 `vaf run` 启动终端对话，输入 `/settings`，选择 **AI Provider → DeepSeek**，填入 API Key 并选择模型。思考强度通过以下命令设置：

```bash
vaf models config deepseek_reasoning_effort max
```

可选值为 `low`、`high` 和 `max`；留空则恢复 DeepSeek 的默认值。其他值会被拒绝。

#### 3. 上下文窗口

VAF 将所有 DeepSeek 模型视为 1M Token 的上下文窗口。默认情况下，对话历史超过 45,000 Token 后 VAF 就会对其进行压缩，因为每次回复都会重新发送完整历史，而 DeepSeek 会对每个 Token 计费。如果希望历史一直增长到完整的 1M 窗口，请把 **设置 → AI 与模型 → 上下文投入** 调到最后一档，或运行：

```bash
vaf models config context_compress_tokens 0
```

（`0` 表示：只有在模型窗口快满时才压缩。）

#### 4. 开始使用

使用 `vaf tray` 打开 Web 界面，或在终端中对话：

```bash
vaf run
```

用一次性提示检查配置是否正常：

```bash
vaf prompt "Hello"
```

#### 作为 Python 库使用

```bash
pip install --pre vaf
```

```python
import os

from vaf import Agent

agent = Agent(config={
    "provider": "deepseek",
    "api_key_deepseek": os.environ["DEEPSEEK_API_KEY"],
    "api_model_deepseek": "deepseek-v4-pro",
    "deepseek_reasoning_effort": "max",
})
print(agent.run("In one short sentence, what is DeepSeek?"))
```

#### 说明

- 在 VAF 中，DeepSeek 模型不读取图片。如需处理图片，请在 **设置 → AI 与模型 → 视觉服务商** 中选择一个视觉服务商。
- 按照 DeepSeek 思考模式的要求，VAF 会在工具调用轮次中回传 `reasoning_content`，因此在使用工具时思考模式也保持开启。
