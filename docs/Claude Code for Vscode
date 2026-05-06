# 如何将 DeepSeek V4 Flash/Pro 接入 Claude Code for VS Code

本指南将指导你通过简单的配置，让 VS Code 中的 Claude Code 插件调用 DeepSeek 的模型（`deepseek-v4-pro` 或 `deepseek-v4-flash`），享受更低成本、更强性能的编码辅助体验。

## 前置条件

- 已安装 [Visual Studio Code](https://code.visualstudio.com/)
- 已在 VS Code 扩展市场搜索安装 **Claude Code** 插件
- 已注册 [DeepSeek 开放平台](https://platform.deepseek.com) 并获取 API Key

## 配置步骤

### 1. 打开 VS Code 设置

使用快捷键 `Ctrl + ,`（macOS 使用 `Cmd + ,`）打开设置界面，在搜索框中输入 `claude code`，找到相关设置项，点击 **Edit in settings.json** 打开配置文件。

### 2. 粘贴 JSON 配置

将以下完整的 JSON 配置复制并粘贴到你的 `settings.json` 文件中（注意不要覆盖已有的其他配置）。**请务必将 `ANTHROPIC_AUTH_TOKEN` 的值替换为你自己的 DeepSeek API Key**。

```json
{
  "claudeCode.selectedModel": "deepseek-v4-pro",
  "claudeCode.environmentVariables": [
    {
      "name": "ANTHROPIC_BASE_URL",
      "value": "https://api.deepseek.com/anthropic"
    },
    {
      "name": "ANTHROPIC_AUTH_TOKEN",
      "value": "sk-xxx"   // ⚠️ 替换为你的真实 API Key
    },
    {
      "name": "ANTHROPIC_MODEL",
      "value": "deepseek-v4-pro[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_OPUS_MODEL",
      "value": "deepseek-v4-pro[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_SONNET_MODEL",
      "value": "deepseek-v4-flash[1m]"
    },
    {
      "name": "ANTHROPIC_DEFAULT_HAIKU_MODEL",
      "value": "deepseek-v4-pro"
    },
    {
      "name": "CLAUDE_CODE_SUBAGENT_MODEL",
      "value": "deepseek-v4-flash"
    },
    {
      "name": "API_TIMEOUT_MS",
      "value": "600000"
    },
    {
      "name": "CLAUDE_CODE_EFFORT_LEVEL",
      "value": "max"
    },
    {
      "name": "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC",
      "value": "1"
    }
  ],
  "claudeCode.preferredLocation": "panel",
  "claudeCode.disableLoginPrompt": true
}
```

### 3. 重启并使配置生效

保存 `settings.json` 后，**完全退出并重启 VS Code**（或执行窗口重载：`Ctrl + Shift + P` → `Developer: Reload Window`），确保所有环境变量正确加载。

### 4. 验证模型接入

重新打开 Claude Code 面板（通常位于侧边栏或底部面板），在对话框中输入 `/model`，如果你看到 `deepseek-v4-pro` 或 `deepseek-v4-flash` 出现在模型列表中，即代表配置成功。你可以尝试一个简单的代码生成任务（例如“用 Python 写一个快速排序函数”）来测试其可用性。

## 配置项详解

| 环境变量 / 设置项 | 说明 |
| :--- | :--- |
| `ANTHROPIC_BASE_URL` | 指向 DeepSeek 兼容 Anthropic 的 API 端点，**固定为** `https://api.deepseek.com/anthropic` |
| `ANTHROPIC_AUTH_TOKEN` | 你的 DeepSeek API Key，请在[开放平台](https://platform.deepseek.com)生成 |
| `ANTHROPIC_MODEL` | 主对话模型，建议使用 `deepseek-v4-pro[1m]`（`[1m]` 表示启用 100 万 token 上下文） |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | 对应 Claude Opus 级别的模型，设为 `deepseek-v4-pro[1m]` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | 对应 Claude Sonnet 级别，设为 `deepseek-v4-flash[1m]`（快速且长上下文） |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | 对应 Claude Haiku 级别，设为 `deepseek-v4-pro`（也可用 flash） |
| `CLAUDE_CODE_SUBAGENT_MODEL` | 子代理任务使用的模型，快速任务推荐 `deepseek-v4-flash` |
| `API_TIMEOUT_MS` | 请求超时时间（毫秒），处理复杂任务时 600000（10 分钟）可有效避免中断 |
| `CLAUDE_CODE_EFFORT_LEVEL` | 努力程度/推理深度，`max` 会尝试更深入的推理（耗时更长） |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | 设 `1` 禁用非必要遥测，保护隐私 |
| `claudeCode.preferredLocation` | 界面位置，`panel` 为底部面板，也可设为 `sidebar` |
| `claudeCode.disableLoginPrompt` | 设为 `true` 以跳过原始登录提示，直接使用自定义 API Key |
