[English](./projv.md) | [简体中文](./projv.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 proJV

proJV 是一款为 DeepSeek 而生的纯原生 C++20 终端 agent：约 3.4 MB 的单文件，没有任何运行时需要安装，每一行代码都由它自己写成，而且技能、角色、工具、主题全都是文件 —— 刻意不做 MCP 层，也没有插件注册表。它直接对接 `api.deepseek.com`，支持 DeepSeek-V4-Pro 与 DeepSeek-V4-Flash，可用完整的 100 万 token 上下文，本地、SSH、tmux 里表现一致。

- **GitHub：** <https://github.com/MilesKHuang/proJV>

#### 1. 安装 proJV

从 [Releases 页面](https://github.com/MilesKHuang/proJV/releases) 下载对应平台的压缩包：

- Windows：`proJV-0.6.3-windows-x64.zip`
- Linux：`proJV-0.6.3-linux-x64.tar.gz`

```sh
# 或从源码构建（需要 CMake 3.16+ 和 C++20 编译器）
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

解压到任意目录。你会得到 `proJV_tui`（Windows 上是 `.exe`）、`projv_files/`、两份 README 和许可证。**可执行文件必须和 `projv_files/` 放在一起 —— 这两样就是一次完整安装。** 其余依赖（FTXUI、SQLiteCpp、nlohmann/json、toml++、loguru）全部随源码内置，不需要 vcpkg、conan、npm 或 pip。

压缩包明显大于二进制，是因为 `projv_files/` 里还带着 TUI 渲染用的中文字库、主题和示例技能。

- Windows：二进制没有代码签名，SmartScreen 可能提示 —— 点「更多信息」→「仍要运行」。
- Linux：发布包面向常规 glibc 桌面；若自己编译，只需额外装 `sudo apt-get install -y libcurl4-openssl-dev`（Debian/Ubuntu）。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。proJV 首次启动会弹配置窗让你粘贴；之后按 `F2` 随时可以重新打开。Key 保存在可执行文件旁边的 `projv_files/config.toml` 里 —— 打包产物刻意不包含该文件，所以你的 Key 和聊天记录不会被一起分发。

#### 3. 把 proJV 指向你的项目

```sh
cd /path/to/my-project
./proJV_tui          # Windows: proJV_tui.exe
```

`workspace_path` 是文件工具唯一能碰的目录树，**留空表示「可执行文件所在目录」**。所以要让 agent 改你的代码，先在配置窗（`F2`）里把它设成项目路径；保存后工具会立刻按新的根目录重新注册。

#### 4. 第一条消息

输入需求按 `Enter` 发送。多步任务会实时显示在对话里，模型做规划时还会出现在 TODO 面板（`F9`）。`/help` 列出对话内命令。内置两个示例技能：`/monica <目录>` 用十个 worker 并发整理一个仓库，`/bigbang <主题>` 走三方角色辩论、最后产出一份执行文档。

#### 5. 快捷键

| 按键 | 操作 |
|-----|------|
| `Enter` | 发送 prompt |
| `Esc` | 中断当前回合；空闲时退出 |
| `F1` | 关于 |
| `F2` | 配置（API Key、模型、工作区） |
| `F3` | 新对话 |
| `F5` | 打开历史会话 |
| `F6` / `F7` | 切换主题 / 主题编辑器 |
| `F8` | 切换思考链显示（摘要 ↔ 完整思考） |
| `F9` | 打开 / 关闭 TODO 面板 |
| `F10` | 切换模型（列表从 API 拉取） |
| `Tab` | 切换角色（内置提示词在 `projv_files/prompts/`） |
| `PgUp` / `PgDn` | 滚动对话 |
| `Ctrl+C` | 退出（会话会先落盘） |

#### 6. 配置

`projv_files/config.toml` 位于二进制旁边，第一次保存配置时创建。

| 键 | 含义 |
|----|------|
| `api_key` | DeepSeek API Key |
| `model` | `deepseek-v4-flash`（默认）或 `deepseek-v4-pro` |
| `base_url` | API 基址，默认 `https://api.deepseek.com` |
| `max_tokens` | 单次回复预算，默认 `65536` |
| `temperature` | 默认 `0.0`；官方文档注明思考模式下该项不生效 |
| `reasoning_effort` | 思考强度：`none` / `low` / `high` / `max`，默认 `max` |
| `workspace_path` | 文件工具唯一可操作的目录树；留空 = 可执行文件所在目录 |
| `context_window` | `0` = 自动（用满 V4 上下文） |
| `theme` | 当前主题名 |
| `python_path` | `projv_files/pytool/` 里 Python 工具的解释器；留空 = `PATH` 里的 `python` |
| `cpp_compiler_path`、`clang_format_path` | 可选，用于构建任务与 `format_file` |
| `[model_prices]` | 模型名前缀 → 每 1M token 的输入/输出价格，用于成本估算 |

#### 7. 思考模式与推理强度

思考默认开启 —— proJV 按官方文档的方式打开它，并同时发送 `reasoning_effort`，开箱就是最深的 `max` 级。官方默认强度是 `high`，所以这里的 `max` 是一次有意的上调，不是硬性要求：

| `reasoning_effort` | proJV 实际发送 |
|---|---|
| `max` / `high` / `low` | 发对应强度的 `reasoning_effort`；`F8` 可看思考链 |
| `none` | 发 `thinking: {"type": "disabled"}` 且不发强度字段（官方定义的「关闭思考」写法） |
| 其它值 | 记一条日志后忽略，回落到官方默认的 `high` |

官方文档里的别名（`minimal` → `low`、`medium`/`xhigh` → `high`、`ultra` → `max`）同样接受。思考内容会完整保留并在每次请求里回传，因此开着思考也能正常调用工具。

#### 8. 完整的 100 万 token 上下文

DeepSeek V4 支持 100 万 token 上下文，proJV 会用满它：`context_window = 0`（默认）对两个 V4 模型都会解析成 **1,048,576 token**，再扣除回复预算。长会话在上下文压力升高时会自动压缩 —— 用一段摘要替换最早的若干条消息 —— `/compress` 也可以随时手动触发同一套逻辑。状态栏会显示当前压力。

#### 9. `AGENTS.md`

把 `AGENTS.md` 放在工作区根目录，proJV 会在每个新会话里注入它，包在 `[AGENTS.MD] ... [END AGENTS.MD]` 之间，紧跟在目录树之后。这里适合放构建命令、项目约定这类模型无法从代码推断的东西。每个会话最多读 16 KiB；改完文件要等下一次新对话（`F3`）或 `/clear` 之后才生效。

#### 10. 技能、角色、工具、主题 —— 全是文件

| 什么 | 放在哪 | 怎么用 |
|---|---|---|
| 技能 | `projv_files/skills/<name>/`（`config.json`、每个 agent 一个 `.md`、`tools/*.json`） | `/skill list`，然后 `/<name> <主题>`；`skill_maker` 能自动写新的 |
| 角色 | `projv_files/prompts/*.md` | `Tab` 循环切换 |
| 额外工具 | `projv_files/pytool/<name>/`（Python） | 启动时自动加载；需要 `python_path` |
| 主题 | `projv_files/theme/*.json` | `F6` 切换，`F7` 可视化编辑并实时预览 |

#### 11. 图片

在 Flash 模型下可以用 `@路径` 附加图片（给目录会自动展开，每条消息最多 8 张），也可以让 agent 自己取图：它调用 `view_image(paths=[...])`，当前回合结束，图片在下一轮以一条标着 `(auto)` 的 user 消息送达。`deepseek-v4-pro` 不接受图片，proJV 会直接不附加，而不是让你吃一个 400。

#### 12. 定价

以下数字是官方 [价格页](https://api-docs.deepseek.com/quick_start/pricing) 的快照 —— 引用前请再核对一次：

| 模型 | 输入 / 百万 token | 输出 / 百万 token | 缓存命中 / 百万 token |
|------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

状态栏的成本估算读的是 `config.toml` 里的 `[model_prices]` 表，价格变了记得同步更新。
