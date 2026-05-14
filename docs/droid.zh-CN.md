[English](./droid.md) | [简体中文](./droid.zh-CN.md) · [← Back](../README.zh-CN.md)

# 集成 Droid

Droid 是一款运行在终端中的 AI 原生软件开发 Agent。

#### 1. 安装 Droid

```bash
# macOS / Linux
curl -fsSL https://app.factory.ai/cli | sh

# Homebrew
brew install --cask droid

# Windows
irm https://app.factory.ai/cli/windows | iex

# npm
npm install -g droid
```

#### 2. 配置 DeepSeek 为自定义模型

打开 `~/.factory/settings.json`，先删除内置的程序再添加如下：

```json
{
  "customModels": [
    {
      "model": "deepseek-v4-pro",
      "id": "custom:deepseek-v4-pro-0",
      "index": 0,
      "baseUrl": "https://api.deepseek.com/anthropic",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "displayName": "deepseek-v4-pro",
      "noImageSupport": true,
      "provider": "anthropic"
    },
    {
      "model": "deepseek-v4-flash",
      "id": "custom:deepseek-v4-flash-1",
      "index": 1,
      "baseUrl": "https://api.deepseek.com/anthropic",
      "apiKey": "${DEEPSEEK_API_KEY}",
      "displayName": "deepseek-v4-flash",
      "noImageSupport": true,
      "provider": "anthropic"
    }
  ]
}
```

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 3. 登录 Droid

终端输入 `droid` 打开，根据提示在浏览器中登录 Factory，使用 Google 账号登录。

#### 4. 设置中文界面（可选）

若界面不是中文，设置用户环境变量：

```bash
# macOS / Linux
export LANG=zh_CN

# Windows
$env:LANG="zh_CN"
```

再次终端输入 `droid` 打开即可使用中文界面。

#### 5. 可选设置

**设置推理强度：** 在 `~/.factory/settings.json` 中添加 `reasoningEffort` 字段（默认 `none`）：

```json
{
  "reasoningEffort": "high"
}
```

可选值：
- `none` — 不推理，响应最快
- `low` — 低推理，简单任务适用
- `medium` — 中等推理，日常任务推荐
- `high` — 高推理，复杂任务效果最佳

**其他设置：** 在 Droid 中输入 `/settings` 打开设置面板：

- Default compaction token limit — 设置上下文窗口大小
- 偏好设置：
  - 云端会话同步 — 建议关闭
  - 在主视图中显示思考过程 — 建议打开
  - 显示上下文窗口使用率 — 建议打开
- 其他设置根据个人需要调整
