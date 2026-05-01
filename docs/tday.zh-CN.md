[English](./tday.md) | [简体中文](./tday.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Tday

[Tday](https://github.com/unbug/tday) 是一个桌面启动器，通过浏览器式标签页同时运行多种编程 Agent（Pi、Claude Code、Codex、OpenCode 等），并提供统一的供应商配置、本地推理服务自动发现、跨 Agent 的长期记忆与 Token 用量分析。DeepSeek 是 Tday 内置的一等供应商。

<p align="center">
  <a href="https://x.com/i/status/2049935301808935356">
    <img alt="Tday 演示" src="https://github.com/user-attachments/assets/5d7ac6d9-cf0a-4eb3-b865-71ffbd11806b" width="800" />
  </a>
</p>

#### 1. 安装 Tday

从 [Tday Releases](https://github.com/unbug/tday/releases/latest) 页面下载对应平台的最新版本：

- **macOS** —— `Tday-<version>-mac-arm64.dmg`（Apple Silicon）或 `Tday-<version>-mac-x64.dmg`（Intel）
- **Windows** —— `Tday-<version>-win-x64.exe`
- **Linux** —— `Tday-<version>-linux-x86_64.AppImage` 或 `Tday-<version>-linux-x64.tar.gz`

也可以从源码构建：

```bash
git clone https://github.com/unbug/tday.git
cd tday
pnpm install
pnpm build:core   # 构建 Rust tday-core 二进制
pnpm dev          # 启动桌面应用
```

> **源码构建依赖：** Node.js ≥ 20、pnpm ≥ 9、Rust ≥ 1.78。

Tday 内置了 `pi`、`claude-code`、`codex`、`opencode` 适配器。请通过 `npm i -g` 全局安装你计划使用的 Agent，例如：

```bash
npm install -g @mariozechner/pi-coding-agent
npm install -g @anthropic-ai/claude-code
npm install -g @openai/codex
npm install -g opencode-ai
```

#### 2. 配置 DeepSeek 供应商

请前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

**方式 A —— 使用 Settings UI（推荐）**

1. 启动 Tday。
2. 进入 **Settings → Providers**，点击 **+ Add provider**。
3. 在供应商选择器中选择 **DeepSeek**。
4. 填写：
   - **Base URL**：`https://api.deepseek.com`（DeepSeek 的 OpenAI 兼容端点，无需追加 `/v1`）
   - **API Key**：粘贴你的 DeepSeek API Key
   - **Model**：在最新模型下拉列表中选择（如 `deepseek-v4-pro` 或 `deepseek-v4-flash`），也可手动输入模型 ID
5. （可选）开启 **Use this provider/model for all agents**，让所有启动的 Agent 共享同一份 DeepSeek 配置。
6. 保存。

**方式 B —— 直接编辑 `~/.tday/providers.json`**

```json
{
  "providers": {
    "deepseek": {
      "vendor": "deepseek",
      "baseUrl": "https://api.deepseek.com",
      "apiKey": "<your DeepSeek API Key>",
      "models": [
        { "id": "deepseek-v4-pro",   "name": "DeepSeek V4 Pro" },
        { "id": "deepseek-v4-flash", "name": "DeepSeek V4 Flash" }
      ]
    }
  },
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro"
}
```

修改文件后重启 Tday 即可生效。

#### 3. 打开标签页开始编码

1. 按 **Cmd+T**（macOS）/ **Ctrl+T**（Windows / Linux）新建一个 Agent 标签页，或点击标签栏的 **+** 按钮。
2. 从下拉菜单中选择要使用的 Agent —— **Pi**、**Claude Code**、**Codex** 或 **OpenCode**。
3. 设置该标签页的工作目录（浏览或粘贴路径，按 **Enter** 提交）。
4. Tday 会在真实 PTY 中启动 Agent，并通过环境变量与对应的 CLI 参数注入 DeepSeek 配置，让 Agent 使用 DeepSeek 而不是它自带的默认供应商。
5. 进入 Agent 后，可随时通过 `/model`（或所选 Agent 提供的快捷方式）切换模型 —— 选择 `deepseek-v4-pro` 获得最强推理能力，或选择 `deepseek-v4-flash` 获得更快更省的响应。

> **小贴士：** 你可以同时打开多个标签页，例如在 `~/projects/api` 中运行 Pi，在 `~/projects/web` 中运行 Claude Code，它们共享同一份 DeepSeek Key 和模型配置。标签页与工作目录在应用重启后会自动恢复。

更多内容（架构、路线图、本地推理自动发现、Token 用量分析、长期记忆等）请查阅 [Tday README](https://github.com/unbug/tday#readme)。
