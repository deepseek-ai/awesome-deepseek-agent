[English](./sol_next.md) | [简体中文](./sol_next.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Sol Next 中接入 DeepSeek

[Sol Next](https://github.com/chongyangzhang92-hub/Sol-Next) 是一款独立研发、Apache-2.0 开源的 Android 10–16/17 与鸿蒙多模态 AI 手机操作系统级智能体，内置纯 Rust 16KB 原生内核、Display 0 1:1 零漂移后台虚拟屏、全球 20 国语言按手机系统语言自动切换、关 Wi-Fi 无线调试持续在线以及零依赖 stdio MCP Server。

Sol Next 开箱即免费内置加密封装的 `deepseek-v4-flash`，同时也完整支持在设置中填入自有 DeepSeek API Key，切换至 `deepseek-v4-pro` 或 `deepseek-v4-flash`，充分发挥 DeepSeek V4 的 **1M（100 万 Token）超长上下文窗口**与 `max` / `high` 推理深度能力。

#### 1. 安装 Sol Next

前往 [GitHub Releases](https://github.com/chongyangzhang92-hub/Sol-Next/releases/tag/v9.0.4-public) 下载最新版 `v9.0.4-public` APK（主流手机推荐 `ARM64` 版本，国内用户也可通过仓库主页提供的直连镜像下载），或使用内置零依赖 CLI 一键校验并安装：

```bash
python3 scripts/sol-cli.py install --abi arm64 --mirror china --verify-sha256 --grant-permissions
```

#### 2. 配置自有 DeepSeek V4 API Key（BYOK）

安装后即可直接体验默认内置的 `deepseek-v4-flash`。如需接入自己的 DeepSeek 账号并使用 `deepseek-v4-pro`（支持 1M 上下文与 `max` 推理深度）：

1. 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
2. 在手机上打开 **Sol Next**，进入 **设置 › 模型 API 配置（BYOK）**。
3. 填入兼容 OpenAI 协议的 DeepSeek 接口参数：
   - **API Base URL**：`https://api.deepseek.com/v1`
   - **模型 ID**：`deepseek-v4-pro`（适合复杂跨 App 长链路规划，兼容 `max` 推理深度）或 `deepseek-v4-flash`（适合高频日常极速操控）
   - **API Key**：填入你的 DeepSeek API Key（`sk-...`）
4. DeepSeek V4 系列支持最高 **100 万 Token（1M）上下文窗口**，且 `deepseek-v4-pro` 支持 `reasoning_effort`（`max` / `high`）思考深度，能够让 Sol Next 在多步跨应用操作中完整保留屏幕状态与上下文记忆，显著提升长任务成功率。

#### 3. 快速上手（语音 / 文字 / MCP）

- **手机端语音与文字**：点击「晨曦轨道」声波球说话或在底部输入框直接下达自然语言指令，Sol Next 将在 1:1 后台虚拟屏中静默执行，涉及付款或微信敏感操作时默认弹窗确认。
- **通过 MCP 接入 Claude Code / Cursor / Codex**：
  ```json
  {
    "mcpServers": {
      "sol-next": {
        "command": "python3",
        "args": ["/path/to/Sol-Next/mcp/sol_mcp_server.py"]
      }
    }
  }
  ```

更多 20 国语言文档与 SHA-256 校验信息请查看 [Sol Next 仓库主页](https://github.com/chongyangzhang92-hub/Sol-Next) 与 [项目官网](https://chongyangzhang92-hub.github.io/Sol-Next/)。
