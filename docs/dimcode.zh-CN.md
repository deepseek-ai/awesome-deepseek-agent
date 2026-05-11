[English](./dimcode.md) | [简体中文](./dimcode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DimCode

[DimCode](https://dimcode.dev/) 是一个多模型 AI 编程 Agent，提供桌面端和终端 TUI，支持会话、供应商连接、工具权限管理、MCP 与 ACP 编辑器集成。

#### 1. 安装 DimCode CLI

- 安装 [Node.js](https://nodejs.org/zh-cn/download/)。
- 在命令行界面，执行以下命令安装 DimCode CLI：

```
npm install -g dimcode@latest
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```
dim --version
```

#### 2. 运行 DimCode

进入项目目录并执行 `dim`：

```
cd /path/to/my-project
dim
```

#### 3. 连接 DeepSeek 供应商

- 在命令栏输入 `/connect`，打开 **Connect Provider** 面板。

<div align="center">
<img src="./assets/dimcode/step1.png" width="1024" border="1" />
</div>

- 在供应商列表中选择 **DeepSeek**。

<div align="center">
<img src="./assets/dimcode/step2.png" width="1024" border="1" />
</div>

- 填入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)，然后应用供应商配置。

<div align="center">
<img src="./assets/dimcode/step3.png" width="1024" border="1" />
</div>

#### 4. 选择 DeepSeek 模型

- 输入 `/models` 打开模型选择器。
- 搜索 `deep`，选择一个可用的 DeepSeek 模型：
  - DeepSeek Chat
  - DeepSeek Reasoner
  - DeepSeek V4 Flash
  - DeepSeek V4 Pro

<div align="center">
<img src="./assets/dimcode/step4.png" width="1024" border="1" />
</div>

#### 5. 设置思考强度

- 使用 DeepSeek 思考模型时，在 DimCode 的 thinking effort 面板中选择 **High** 或 **Max**。

<div align="center">
<img src="./assets/dimcode/step5.png" width="1024" border="1" />
</div>
