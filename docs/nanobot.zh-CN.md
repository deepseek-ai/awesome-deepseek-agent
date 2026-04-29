[English](./nanobot.md) | [简体中文](./nanobot.zh-CN.md)

# 接入 nanobot

nanobot 是一个轻量级AI智能体，支持接入常用聊天工具。

#### 1. 安装 nanobot

- 安装 [uv](https://github.com/astral-sh/uv)
- 执行下面的命令安装 nanobot:

```
uv tool install nanobot-ai
```

- 注意：在 Windows 操作系统下，请将用户根目录下的 `.local/bin` 目录添加到环境变量中：

```powershell
$env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
```

- 或者通过 `uv` 更新终端：

```powershell
uv tool update-shell
```

- 完成安装后，执行下面的命令，如果显示版本号则安装成功:

```
nanobot --version
```

#### 2. 配置 nanobot 的配置文件

运行下面的命令初始化 nanobot 配置文件：

```
nanobot onboard
```

不同操作系统生成的配置文件路径如下：

- **Windows**: `$env:USERPROFILE\.nanobot\config.json`
- **Linux / MacOS**: `~/.nanobot/config.json`

编辑配置文件 `config.json`，修改下面的配置项:

```json
{
    "agents": {
        "defaults": {
            "model": "deepseek-v4-pro",
            "provider": "deepseek",
        }
    },
    "providers": {
        "deepseek": {
            "apiKey": "<你的 DeepSeek API Key>",
            "apiBase": "https://api.deepseek.com/v1",
        },
    },
}
```

#### 3. 开始使用

在终端中运行：

```
nanobot agent
```
