[English](./cline_cli.md) | [简体中文](./cline_cli.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Cline CLI

Cline CLI 是 Cline 的命令行版本。它是一个 AI 编程助手，可以在终端中读取和编辑文件、执行 Shell 命令，并帮助你处理项目任务。

#### 1. 安装 Cline CLI

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 20+。
- 在命令行界面，执行以下命令安装 Cline CLI：

```
npm install -g cline
```

- 安装结束后，执行以下命令，若显示版本号则安装成功：

```
cline version
```

#### 2. 启动认证向导

执行 Cline 认证向导：

```
cline auth
```

进入欢迎界面后，选择 **Use your own API key**。

这个选项在 Cline 文档中也叫 **Bring your own API key**。它表示 Cline 会直接使用你自己的 DeepSeek API Key，由 DeepSeek 负责请求计费和速率限制。

#### 3. 选择 DeepSeek 供应商

在供应商选择界面中，选择 **DeepSeek**。

如果你更偏向脚本化配置，Cline 中 DeepSeek 的 provider id 是 `deepseek`。

#### 4. 输入 DeepSeek API Key

根据提示粘贴你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。

请妥善保管这个 Key。API Key 是一种凭证，作用类似程序访问 DeepSeek 的密码，Cline 会用它代表你调用 DeepSeek 模型。

#### 5. 选择模型

选择一个可用的 DeepSeek 模型：

- `deepseek-chat` — 适合通用编程和对话任务。
- `deepseek-reasoner` — 适合需要更强推理和分步分析的任务。

模型选择完成后，认证配置就结束了。

#### 6. 启动 Cline

```
cd /path/to/my-project
cline
```

#### 可选：使用命令参数配置 DeepSeek

上面的认证向导是配置 DeepSeek 最直接的方式。如果要在脚本中配置，也可以跳过向导，直接传入 DeepSeek 供应商、API Key 和模型：

```
cline auth -p deepseek -k <your DeepSeek API Key> -m deepseek-chat
```

如果想使用推理模型，可以把 `deepseek-chat` 换成 `deepseek-reasoner`。
