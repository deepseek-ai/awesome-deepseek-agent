[English](./workbuddy.md) | [简体中文](./workbuddy.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 WorkBuddy/CodeBuddy

WorkBuddy/CodeBuddy 是 AI Agent 与编程助手工具。它支持通过本地模型配置文件添加自定义模型，可以使用 OpenAI 兼容的 Chat Completions API 接入 DeepSeek V4。

#### 1. 安装 WorkBuddy/CodeBuddy

- 安装并登录 WorkBuddy/CodeBuddy。
- 至少打开一次项目目录，让应用创建本地配置目录。
- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

#### 2. 配置本地模型

创建或编辑用户级配置文件：

```
C:\Users\<你的用户名>\.codebuddy\models.json
```

如果只想让配置对某个项目生效，也可以创建项目级配置文件：

```
<你的项目>\.codebuddy\models.json
```

写入以下配置，并将 `<your DeepSeek API Key>` 替换成你的真实 API Key：

```json
{
  "models": [
    {
      "id": "deepseek-v4-pro",
      "name": "DeepSeek V4 Pro",
      "vendor": "DeepSeek",
      "url": "https://api.deepseek.com/v1/chat/completions",
      "apiKey": "<your DeepSeek API Key>",
      "maxInputTokens": 128000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false,
      "relatedModels": {
        "lite": "deepseek-v4-flash",
        "reasoning": "deepseek-v4-pro"
      }
    },
    {
      "id": "deepseek-v4-flash",
      "name": "DeepSeek V4 Flash",
      "vendor": "DeepSeek",
      "url": "https://api.deepseek.com/v1/chat/completions",
      "apiKey": "<your DeepSeek API Key>",
      "maxInputTokens": 128000,
      "maxOutputTokens": 8192,
      "supportsToolCall": true,
      "supportsImages": false
    }
  ],
  "availableModels": [
    "deepseek-v4-pro",
    "deepseek-v4-flash"
  ]
}
```

请将 `models.json` 保存为 UTF-8 无 BOM。部分桌面版本在读取带 UTF-8 BOM 文件头的 JSON 时，可能会读取本地模型配置失败。

#### 3. 重启并选择模型

完全退出 WorkBuddy/CodeBuddy 后重新打开。

在模型选择器中选择：

```
DeepSeek V4 Pro
DeepSeek V4 Flash
```

#### 4. 可选：验证 API Key

Windows 用户可以在 PowerShell 中验证 API Key：

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"

curl https://api.deepseek.com/v1/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"stream":false}'
```

如果请求成功，说明 API Key 和模型名都可用。

#### 常见问题

- `Authentication Fails` 或 `401`：检查 `apiKey` 是否为真实 DeepSeek API Key。不要把接口 URL 填到 API Key 字段。
- `未找到模型` 或 `404`：检查模型 id 是否严格写成 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- `读取本地模型配置失败`：检查 `models.json` 是否是合法 JSON，并保存为 UTF-8 无 BOM。
- 模型选择器中不显示：完全重启 WorkBuddy/CodeBuddy，并确认文件放在 `.codebuddy\models.json`。
- UI 中直接显示 `${DEEPSEEK_API_KEY}`：桌面端可能不会展开 `models.json` 中的环境变量，请在本地配置文件中写入真实 API Key。
