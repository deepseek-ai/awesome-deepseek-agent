# 接入 SolonCode

SolonCode 是一个基于 Java 实现的开源编码智能体，以终端命令行方式运行，帮助开发者完成代码编写、项目分析、重构建议、测试生成、文档编写等全流程研发任务。

## 从零安装 SolonCode

### 1. 系统要求

- **Java 8+**（支持 Java 8 到 Java 26 运行环境，需提前安装）
- 支持 macOS、Linux、Windows

### 2. 安装 SolonCode

**Mac / Linux 用户：**

```bash
curl -fsSL https://solon.noear.org/soloncode/setup.sh | bash
```

**Windows 用户（PowerShell）：**

```powershell
irm https://solon.noear.org/soloncode/setup.ps1 | iex
```

安装完成后，执行以下命令，若显示版本号则安装成功：

```bash
soloncode --version
```

### 3. 配置 DeepSeek 模型

安装完成后，需修改配置文件 `~/.soloncode/config.yml`。API Key 在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取。

打开 `~/.soloncode/config.yml`，找到 `models` 配置项，填入 DeepSeek 的 API 信息：

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<你的 DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
      contextLength: 1_000_000
```

> **说明：**
> - `apiUrl` 可以是完整的接口地址（也可以是 OpenAI baseUrl）。

### 4. 启动使用

配置完成后，进入你的项目目录，执行 `soloncode` 命令即可开始使用：

```bash
cd /path/to/my-project
soloncode

# 或者 web 交互方式
soloncode web 0
```

## 从现有安装中切换到 DeepSeek

如果你已经安装了 SolonCode 并使用了其他模型（如 OpenAI、通义千问等），只需修改 `~/.soloncode/config.yml` 中的 `models` 配置项即可切换到 DeepSeek：

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<你的 DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
      contextLength: 1_000_000
```

修改后重新启动 SolonCode 即可生效。

## 多模型混合配置

SolonCode 支持同时配置多个模型，第一个为默认模型，运行后也可自由切换模型：

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<你的 DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
      contextLength: 1_000_000
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<你的 DeepSeek API Key>"
      model: "deepseek-v4-pro"
      timeout: "180s"
      contextLength: 1_000_000
```

