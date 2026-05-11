[English](./qwen_code.md) | [简体中文](./qwen_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Qwen Code

Qwen Code 是阿里巴巴通义千问团队开发的开源 AI 终端助手。DeepSeek 已经作为**内置第三方提供商**集成在 Qwen Code 中——你只需要带上自己的 API Key 即可使用。

- **GitHub:** <https://github.com/QwenLM/qwen-code>
- **文档:** <https://qwenlm.github.io/qwen-code-docs/zh/users/overview/>

#### 1. 安装 Qwen Code

- 安装 [Node.js](https://nodejs.org/zh-cn/download/) 20 或更高版本。
- 安装 Qwen Code：

```bash
npm install -g @qwen-code/qwen-code@latest
```

或通过快速安装脚本：

```bash
bash -c "$(curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.sh)"
```

或 Homebrew：

```bash
brew install qwen-code
```

- 验证：

```bash
qwen --version
```

#### 2. 获取 DeepSeek API Key

前往 [DeepSeek Platform](https://platform.deepseek.com/api_keys)，创建并复制 API Key。

#### 3. 通过 /auth 配置 DeepSeek

启动 Qwen Code，然后运行 `/auth` 命令：

```bash
qwen
```

进入交互会话后：

```
/auth
```

将出现认证菜单，按以下步骤操作：

1. 选择 **Third-party Providers**
2. 选择 **DeepSeek API Key**
3. **步骤 1/2** — 粘贴你的 DeepSeek API Key，回车
4. **步骤 2/2** — 确认模型 ID：`deepseek-v4-pro, deepseek-v4-flash`（可自行修改），回车

确认后将显示：`Successfully configured DeepSeek API Key`。

#### 4. 切换到 DeepSeek 模型

运行 `/model` 命令，选择 `deepseek-v4-pro` 或 `deepseek-v4-flash`：

```
/model
```

大功告成。Qwen Code 将使用 DeepSeek V4 模型进行编码。

> **提示：** 随时使用 `/model` 切换模型，使用 `/auth` 重新配置 API Key。