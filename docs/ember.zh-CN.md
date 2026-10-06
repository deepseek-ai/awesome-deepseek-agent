[English](./ember.md) | [简体中文](./ember.zh-CN.md) · [← Back](../README.md)

# 接入 Ember

Ember 是一个"文本优先"的终端编程 Agent，用 C++20 写成：Windows 二进制自带一切，
Linux 二进制只依赖系统的 `libcurl.so.4`。它提供 Windows 与 Linux 版本，可以把多个
服务商的模型分组成模型组，支持思考强度控制，并能通过 MCP 服务器、插件可执行文件和
子代理扩展能力。

源码与预编译二进制：<https://github.com/yyfdfsyyf-source/ember>

#### 1. 安装 Ember

**Windows** —— 从
[release 页面](https://github.com/yyfdfsyyf-source/ember/releases/latest)下载
[`Ember-0.10.1-win64.zip`](https://github.com/yyfdfsyyf-source/ember/releases/download/v0.10.1/Ember-0.10.1-win64.zip)
（同一份字节也提交在仓库的
[`releases/`](https://github.com/yyfdfsyyf-source/ember/tree/main/releases) 目录里），
解压后运行 `agent.exe`。

**Linux** —— 下载
[`ember-0.10.1-linux-x86_64.tar.gz`](https://github.com/yyfdfsyyf-source/ember/releases/download/v0.10.1/ember-0.10.1-linux-x86_64.tar.gz)，然后：

```bash
tar -xzf ember-0.10.1-linux-x86_64.tar.gz
cd ember-0.10.1-linux-x86_64
./ember --version
```

Linux 二进制动态链接到系统的 `libcurl.so.4`，并要求 glibc 2.30 及以上；包内附带的
`verify.sh` 会在你运行任何东西之前把这两项检查一遍。

**从源码构建**（Windows 只要一个 `g++`；CMake + Ninja 两个平台都能配）：

```powershell
.\build.ps1        # Windows -> out/agent.exe，同时编出测试二进制
```

```bash
cmake -B build -G Ninja && cmake --build build && ctest --test-dir build
./build-linux.sh   # 发布用的 Linux 二进制就是它产的：out-linux/dynamic/ember
```

装好之后用 `agent.exe --version` / `./ember --version` 确认版本。

#### 2. 配置 DeepSeek

Ember 从工作目录读取 `settings.json`（可用 `--config PATH` 指定别的路径）。
优先级为：内置默认值 < `AGENT_*` 环境变量 < `settings.json` < 命令行参数。

```json
{
  "model": "deepseek-v4-pro",
  "thinking": "max",
  "providers": [
    {
      "name": "deepseek",
      "base_url": "https://api.deepseek.com/v1",
      "api_key_env": "DEEPSEEK_API_KEY"
    }
  ],
  "groups": [
    { "name": "ds", "provider": "deepseek", "models": ["deepseek-v4-pro", "deepseek-v4-flash"] }
  ]
}
```

- `api_key_env` 填的是**环境变量名**，密钥因此不用写进文件。用
  `setx DEEPSEEK_API_KEY <key>`（Windows）或 `export DEEPSEEK_API_KEY=<key>`
  （Linux）设置；也可以改用 `"api_key"` 直接内联。
- 一个**模型组**把一批模型绑到某个服务商上。`/model` 按分组列出模型，
  `/model <编号|名称>` 会一步把模型**连同**它的 base URL 和密钥一起切换。
  不属于任何组的模型使用顶层的 `base_url`/`api_key`。
- DeepSeek 原生就说 effort 这套写法（`"reasoning_effort"`），而它正是 Ember 的
  默认 `thinking_style`，所以接 DeepSeek 不需要另外设置 `thinking_style`。

API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

#### 3. 运行并选择模型

```bash
cd /path/to/your/repo
ember            # Windows 上运行 agent.exe
```

- `/model` 列出所有已配置的模型；`/model deepseek-v4-flash` 切换过去。
- `/think` 显示当前思考档位，`/think max`（或 `high`、`low`、`none`）即时改。
  界面上边框会显示 `[think:max]`（档位是 `auto` 时不额外显示，因为 `auto` 根本不
  发送该字段）。启动时用 `--thinking NAME` 或 `AGENT_THINKING`。
- `/settings` 打开内置编辑器改同样的键，`/help` 列出全部命令。

DeepSeek 定义了 `low`、`high`、`max` 三档。Ember 把你选的档位原样作为
`reasoning_effort` 发出去，所以 `/think max` 就是 DeepSeek 的 `max`。

#### 上下文窗口

DeepSeek V4 支持最长 100 万 token 的上下文。Ember 没有按模型设置的
`context_window` 字段，而是用**预算（budget）**来管理会话：

- `"budget"`（或 `--budget N`）：触发"把会话最老的一段摘要压缩"的 token 预算。
  默认 `6000`，适合短平快的定点修改；如果你想让 Ember 在压缩前保留更长的原始
  历史，把它调高（例如 `200000`）。填 `0` 则完全关闭压缩。
- `"prune_before_send"`（默认 `true`）：每次请求前丢弃冗余的工具输出。
- `--tool-cap N`：单个工具结果的字节上限（默认 4096，`0` 表示不限）。

因为压缩是按预算触发、而不是把上下文长度钉死在某个值，只要 `budget` 低于 100 万，
Ember 就自然留在 DeepSeek 的 1M 上限之内。

#### 更进一步

Ember 的工具集包含 shell 执行、带结构化补丁的文件编辑、通过 CDP 的无头浏览器
自动化、Windows 上基于 UI Automation 的桌面自动化、并行子代理，以及 PTC 批量
工具执行。MCP 服务器与插件可执行文件会注册成额外工具；会话按文件持久化，
`/sessions` 可以回到之前的对话继续。
