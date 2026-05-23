[English](./qwen_code.md) | [简体中文](./qwen_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Qwen Code

Qwen Code是一款开源的终端 AI 智能体,它能帮助你理解大型代码库、自动化繁琐工作，加速交付

#### 1. 安装Qwen Code

- Linux / macOS
```
curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh | bash
```

- Windows（以管理员身份运行）
```
powershell -Command "Invoke-WebRequest 'https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat' -OutFile (Join-Path $env:TEMP 'install-qwen.bat'); & (Join-Path $env:TEMP 'install-qwen.bat')"
```

建议安装完成后重启终端，以确保环境变量生效。

#### 2. 获取 Deepseek API Key

- 前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key。
- 复制 Key（以 `sk-` 开头）

#### 3. 在 Qwen Code 中配置API Key

- 使用以下命令打开 Qwen Code
```
cd your-project
qwen
```

- 输入`/auth`以配置身份验证
- 在“选择认证方式”界面中，选择`API Key Bring your own API key`选项
- 随后选择`Custom API Key For other OpenAI / Anthropic / Gemini-compatible providers`
- 随后，接下来的三个选项中，您有两个都可以使用：

    - 如您选择`OpenAI-compatible`，则在选中后的“Base URL”界面输入以下url
    ```
    https://api.deepseek.com
    ```
    - 如您选择`Anthropic-compatible`，则在则在选中后的“Base URL”界面输入以下url
    ```
    https://api.deepseek.com/anthropic
    ```
- 在“API Key”页面，输入上面获得的API Key（以`sk-`开头）

- 随后进入“Model IDs”页面，可以输入以下model id，以逗号分隔：
```
deepseek-v4-flash,deepseek-v4-pro
```
- 在接下来的“Advanced Config”页面，您可以根据您的需求启用“Enable thinking（启用思考）”和“Enable modality（启用多模态）”

- 最后进入“Review”页面，你可以简单检视由前面的设置生成的`settings.json`，如无误可以直接回车确认

#### 4. 全部设置完后，即可直接使用

#### 5. Visual Studio Code 插件

该 VS Code 扩展（Beta 版）通过直接集成到 IDE 中的原生图形界面，让你实时查看 Qwen 的代码更改，从而更便捷地访问和与 Qwen Code 交互。你可以在vscode插件市场搜索`Qwen Code Companion`，或点击[该链接](https://marketplace.visualstudio.com/items?itemName=qwenlm.qwen-code-vscode-ide-companion)插件该插件