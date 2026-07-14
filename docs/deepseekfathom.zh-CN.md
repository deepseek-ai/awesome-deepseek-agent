[English](./deepseekfathom.md) | [简体中文](./deepseekfathom.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 集成 DeepSeekFathom

DeepSeekFathom 是一款开源的 DeepSeek 原生编程 Agent，同时提供 Windows 桌面端和跨平台 CLI。它内置本地编程工具、会话恢复、权限与思考控制，并支持 MCP、插件、Hooks 和 Agent Skills。

- **GitHub：** <https://github.com/ffffff233/DeepSeekFathom>

#### 1. 安装 DeepSeekFathom

**Windows 桌面端：** 从 GitHub Release 下载并运行安装程序：

- [DeepSeekFathom-0.1.17-Setup.exe](https://github.com/ffffff233/DeepSeekFathom/releases/download/desktop-v0.1.17/DeepSeekFathom-0.1.17-Setup.exe)

安装程序按当前用户安装，并在桌面和开始菜单中添加 DeepSeekFathom；这种方式不需要预先安装 Python。

**CLI：** 先安装 Python 3.11 或更高版本，再安装对应的正式标签：

```sh
# Windows PowerShell 或命令提示符
py -3 -m pip install --upgrade https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz

# Linux 或 macOS
python3 -m pip install --upgrade https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz
```

验证 CLI 是否安装成功：

```sh
deepseekfathom version
```

#### 2. 配置 DeepSeek API

从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key，然后保存官方接口地址和当前模型：

```sh
deepseekfathom config set --base-url https://api.deepseek.com --api-key sk-... --model deepseek-v4-pro
deepseekfathom doctor --live
```

需要更快响应时可以改用 `deepseek-v4-flash`。在桌面端中，打开**设置**，选择 DeepSeek 服务商，然后填写相同的 Base URL、API Key 和模型。

DeepSeekFathom 会按 DeepSeek V4 模型的 **1,000,000 token（100 万 token）上下文窗口**进行预算。五档公开思考等级会映射到 DeepSeek 原生的 `reasoning_effort`：

| DeepSeekFathom 等级 | 上游 `reasoning_effort` |
|---|---|
| `fast` | `low` |
| `balanced` | `medium` |
| `deep` | `high` |
| `ultra` | `xhigh` |
| `max` | `max` |

`max` 使用 `deepseek-v4-pro` 的真实上游能力：DeepSeekFathom 会把 `reasoning_effort: "max"` 原样发送给 DeepSeek。

#### 3. 进入项目目录并首次启动

```sh
cd /path/to/my-project
deepseekfathom start --mode agent --think max
```

输入 `/` 可以打开命令面板；使用 `/model`、`/think` 和 `/mode` 切换当前模型、思考等级和权限模式。对话会自动保存，可以通过 `deepseekfathom sessions list` 查看，并用 `deepseekfathom sessions resume <SESSION_ID>` 恢复。

通过 Python 安装启动桌面端时，先安装桌面依赖再运行：

```sh
python3 -m pip install --upgrade "deepseekfathom[desktop] @ https://github.com/ffffff233/DeepSeekFathom/archive/refs/tags/v0.1.109.tar.gz"
deepseekfathom-desktop
```

使用 Windows 安装程序的用户，可以直接从桌面或开始菜单启动 **DeepSeekFathom**。
