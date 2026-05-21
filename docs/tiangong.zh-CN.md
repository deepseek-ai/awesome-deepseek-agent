[English](./tiangong.md) | [简体中文](./tiangong.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入天工（Tiangong）

天工是一个基于 Rust 和 Tauri + React 构建的开源个人 AI 智能体平台，支持桌面 GUI、CLI 和 HTTP/WS Server 三种运行模式。支持多智能体协作、MCP 工具接入、本地 Skill、长期记忆和多媒体生成。DeepSeek 是推荐的模型供应商之一。

- **GitHub：** <https://github.com/silent-rs/silent-Tiangong>

#### 1. 安装天工

从 [GitHub Releases](https://github.com/silent-rs/silent-Tiangong/releases) 下载对应平台的安装包：

- **macOS：** 下载 `.dmg`，打开后将「天工」拖入「应用程序」目录。
- **Windows：** 下载 `.msi` 或 `.exe`，按安装向导完成安装。
- **Linux：** 下载 `.AppImage`、`.deb` 或 `.rpm`，按发行版习惯安装或直接运行。

macOS 首次打开如提示应用已损坏：

```sh
xattr -cr /Applications/天工.app
```

可选：创建命令行软链接：

```sh
ln -s /Applications/天工.app/Contents/MacOS/天工 /usr/local/bin/tiangong
```

验证安装：

```sh
tiangong --help
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 在桌面端配置 DeepSeek

启动天工，点击侧边栏 **设置 → 模型**。

**添加 DeepSeek 供应商：**

在供应商表单中填入 DeepSeek 的连接信息：

<img src="./assets/tiangong_set_provider.png" width="600" alt="在天工设置中添加 DeepSeek 供应商" />

- **名称：** `deepseek`
- **Base URL：** `https://api.deepseek.com/v1`
- **API Key：** 你的 DeepSeek API Key（也支持 `${DEEPSEEK_API_KEY}` 环境变量语法）
- **协议：** `openai_compatible`

**配置模型路由：**

添加模型并分配到对应的能力路由：

<img src="./assets/tiangong_set_routing.png" width="600" alt="在天工设置中配置模型路由" />

- 添加 `deepseek-v4-pro`，路由到 **Chat** 能力。
- 添加 `deepseek-v4-flash`，路由到 **Lite** 能力。

DeepSeek V4 模型支持 **100 万 token 上下文窗口**（天工已内置配置）。

#### 4. 启动和使用

**桌面 GUI** — 从应用程序中启动，或运行：

```sh
tiangong
```

**CLI 模式** — 在终端中运行：

```sh
tiangong cli
```

**Server 模式** — 启动 HTTP/WebSocket 服务器，供远程调用：

```sh
tiangong server        # 前台运行
tiangong server -d     # 守护进程
tiangong server stop   # 停止守护进程
```

#### 核心能力

| 能力 | 说明 |
|---|---|
| **多智能体协作** | 主 Agent 可创建 PM、Developer、Tester、Researcher 等 Sub Agent，通过消息和文件锁协作 |
| **本地工具** | 文件读写、命令执行、代码搜索、补丁应用、网页抓取等 |
| **MCP** | 通过 `~/.tiangong/mcp.json` 接入外部 MCP 工具服务器 |
| **Skill** | 通过 `~/.tiangong/skills.json` 安装和管理本地 Skill |
| **长期记忆** | 基于 SQLite + Tantivy + 向量索引的跨会话回忆，保存项目事实、偏好和决策 |
| **多媒体生成** | 图片、视频、语音识别、语音合成等能力路由 |
| **权限治理** | 桌面会话支持监督模式和信任模式切换；Server 模式使用受控的远程角色边界 |

#### 配置文件

所有配置存储在 `~/.tiangong/` 目录下：

| 文件 | 用途 |
|---|---|
| `app.json` | 应用主配置（会话、UI 状态） |
| `models.json` | 模型供应商、模型和路由配置 |
| `skills.json` | Skill 配置 |
| `mcp.json` | MCP 服务器配置 |
| `sessions/` | 会话持久化 |
| `memory/` | 长期记忆数据 |
| `logs/` | 运行日志 |
| `media/` | 生成或归档的媒体文件 |
