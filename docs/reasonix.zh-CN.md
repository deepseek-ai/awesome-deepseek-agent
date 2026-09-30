[English](./reasonix.md) | [简体中文](./reasonix.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Reasonix

Reasonix 是一款以 DeepSeek 为原生后端的跨平台编程 Agent。设计围绕 DeepSeek API 展开 —— Cache-First 循环、Flash 优先的成本控制、工具调用自动修复 —— 直接对接 `api.deepseek.com`，不需要额外的协议转换代理。它同时提供终端 CLI/TUI 和桌面端，内置 DeepSeek V4 Flash 与 DeepSeek V4 Pro，并支持 100 万 token 上下文和 `max` 推理强度。

- [Reasonix GitHub 仓库](https://github.com/esengine/DeepSeek-Reasonix)
- [Reasonix 桌面端下载](https://reasonix.io/?download=desktop#start)

#### 1. 安装 Reasonix

选择终端版或桌面版即可；桌面版不依赖 Node.js，也不要求先安装 CLI。

**终端 CLI/TUI**

使用 npm 安装时需要 [Node.js](https://nodejs.org/en/download/) 18 或更高版本：

```sh
npm install -g reasonix
```

macOS 也可以通过 Homebrew 安装原生版本：

```sh
brew install esengine/reasonix/reasonix
```

不想全局安装时，也可以在后续命令中把 `reasonix` 替换成 `npx --yes reasonix`。Windows 用户若需要 Git 操作、Git Bash 或 POSIX hooks，建议安装 [Git for Windows](https://git-scm.com/download/win)，但它不是 Reasonix 的强制运行依赖。

**桌面端**

从[官方下载页](https://reasonix.io/?download=desktop#start)选择对应安装包：

| 系统 | 安装包 |
| --- | --- |
| macOS | 通用 `.dmg` 或 `.zip`，支持 Apple Silicon 和 Intel |
| Windows | 签名安装程序 `.exe` 或便携版 `.zip`，支持 x64 和 ARM64 |
| Linux | `.deb` 或 `.tar.gz`，支持 x64 |

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)创建 API Key。终端版和桌面版会将 Key 写入 Reasonix 管理的全局凭据文件，不需要手动设置系统环境变量。

#### 3. 配置 DeepSeek

**终端 CLI/TUI**

运行配置向导，添加 DeepSeek 官方服务、填写 API Key，并选择默认模型：

```sh
reasonix setup
```

如果使用免安装方式，请运行：

```sh
npx --yes reasonix setup
```

**桌面端**

1. 启动 Reasonix，打开 **设置 → 模型与模型服务**。
2. 点击 **+ 添加模型服务**。
3. 依次选择 **推荐预设 → DeepSeek 官方**。
4. 填入 DeepSeek API Key，添加服务，并把 DeepSeek V4 Flash 或 Pro 设为默认模型。

CLI 与桌面端共用全局配置和凭据。默认位置如下：

- macOS / Linux：`~/.reasonix/config.toml` 与 `~/.reasonix/.env`
- Windows：`%APPDATA%\reasonix\config.toml` 与 `%APPDATA%\reasonix\.env`

#### 4. 首次运行

**终端 CLI/TUI**

进入项目目录后启动 Reasonix：

```sh
cd /path/to/my-project
reasonix
```

免安装方式对应为 `npx --yes reasonix`。历史命令 `npx reasonix code` 目前仍作为兼容别名保留，但新文档和脚本应直接使用 `reasonix`。

**桌面端**

1. 在项目区选择 **使用现有文件夹**，打开你的代码目录；也可以选择 **新建空白项目**。
2. 点击 **新建会话**。
3. 在输入框中描述任务并发送。模型可以读取项目、生成修改并请求执行工具；涉及写文件或运行命令时，按桌面端提示确认权限。

#### 5. 选择模型与推理强度

Reasonix 默认使用 **DeepSeek V4 Flash** 进行日常迭代。需要更强推理时，可以切换到 **DeepSeek V4 Pro**；两者都配置为 100 万 token 上下文。

| 模型 | 模型 ID | 支持的推理强度 |
| --- | --- | --- |
| DeepSeek V4 Flash | `deepseek-v4-flash` | `low`、`high`、`max` |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `high`、`max` |

在终端 TUI 中：

```text
/model
/effort max
/help
```

- `/model` 打开模型选择器，也可以接模型名直接切换。
- `/effort max` 把当前会话的推理强度切换为 `max`。
- `/help` 查看当前版本支持的完整 slash 命令。

也可以在启动时指定模型和推理强度：

```sh
reasonix --model deepseek/deepseek-v4-pro --effort max
```

桌面端可以直接使用输入框附近的模型选择器和推理强度选择器；新建会话默认使用 **设置 → 模型与模型服务 → 默认模型** 中保存的模型。

#### 6. 常见问题

- **提示缺少 API Key**：终端重新运行 `reasonix setup`；桌面端回到 **设置 → 模型与模型服务**，检查 DeepSeek 官方服务的 Key。
- **终端找不到 `reasonix`**：重启终端并检查 npm 全局可执行目录是否在 `PATH` 中，或改用 `npx --yes reasonix`。
- **桌面端看不到 DeepSeek 模型**：确认已经添加 DeepSeek 官方服务，然后刷新模型列表或新建会话。
- **需要项目级配置**：在项目根目录运行 `reasonix setup --local`，配置会写入 `./reasonix.toml`；API Key 仍只保存在全局 `.env` 中。

<div align="center">
<img src="https://raw.githubusercontent.com/esengine/reasonix/main/docs/logo.svg" width="640" alt="Reasonix" />
</div>
