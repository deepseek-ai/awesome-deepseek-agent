[English](./deepclaude.md) | [简体中文](./deepclaude.zh-CN.md) · [← Back](../README.md)

# 接入 deepclaude

deepclaude 是一个轻量启动器，让 [Claude Code](https://github.com/anthropics/claude-code) 的自主 agent 循环跑在 **DeepSeek V4 Pro**（或任意 Anthropic 兼容后端）上，而非 Anthropic——同样的体验，成本只是零头。它只是一个 shell/PowerShell 脚本加一个本地代理，无需单独维护运行时。

- **GitHub:** <https://github.com/aattaran/deepclaude>

#### 1. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 注册、充值，复制你的 API Key。

#### 2. 设置环境变量

**macOS / Linux:**

```bash
echo 'export DEEPSEEK_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**

```powershell
setx DEEPSEEK_API_KEY "sk-your-key-here"
```

#### 3. 安装 deepclaude

克隆仓库并把启动器放到 `PATH`：

```sh
git clone https://github.com/aattaran/deepclaude.git
cd deepclaude
```

**macOS / Linux:**

```bash
chmod +x deepclaude.sh
sudo ln -s "$(pwd)/deepclaude.sh" /usr/local/bin/deepclaude
```

**Windows (PowerShell):**

```powershell
# 把脚本复制到已在 PATH 中的目录，或把仓库目录加入 PATH
Copy-Item deepclaude.ps1 "$env:USERPROFILE\.local\bin\deepclaude.ps1"
```

#### 4. 首次运行

在任意项目目录下：

```sh
deepclaude
```

这会启动经 DeepSeek V4 Pro 路由的 Claude Code。其他常用参数：

```sh
deepclaude --status        # 查看可用后端与密钥
deepclaude --backend or    # 使用 OpenRouter（最便宜）
deepclaude --backend fw    # 使用 Fireworks AI（最快）
deepclaude --backend anthropic  # 正常 Claude Code（需要 Opus 时）
deepclaude --cost          # 显示价格对比
deepclaude --benchmark     # 跨供应商延迟测试
```

deepclaude 还提供一个 OpenAI 兼容代理（`/v1/chat/completions`），让其他工具也能通过同一个 Key 访问 DeepSeek V4 Pro——详见仓库 README。
