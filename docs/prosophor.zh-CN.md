[English](./prosophor.md) | [简体中文](./prosophor.zh-CN.md) · [← Back](../README.md)

# 接入 Prosophor

Prosophor 是基于插件化主动触发架构的 AI Agent CLI，支持通过 Anthropic 兼容和 OpenAI 兼容两种 API 接入 DeepSeek 模型。

#### 1. 安装 Prosophor

- 安装构建依赖：CMake 3.20+、C++17 编译器、SDL2、libcurl。

```
# Ubuntu / Debian
sudo apt install cmake g++ libsdl2-dev libcurl4-openssl-dev

# macOS
brew install cmake sdl2 curl
```

- 克隆并构建：

```
git clone https://github.com/Swair/prosophor.git
cd prosophor
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

- 构建完成后，验证可执行文件：

```
./prosophor --version
```

#### 2. 配置 DeepSeek

Prosophor 使用 `config/.prosophor/settings.json` 进行 Provider 配置。从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。

编辑 `config/.prosophor/settings.json`：

```json
{
  "default_role": "default",
  "log_level": "info",
  "providers": {
    "anthropic": [
      {
        "api_key": "<你的 DeepSeek API Key>",
        "base_url": "https://api.deepseek.com/anthropic/v1/messages",
        "timeout": 60,
        "agents": {
          "default": {
            "model": "deepseek-v4-pro[1m]",
            "temperature": 0.7,
            "max_tokens": 8192,
            "context_window": 128000,
            "thinking": false
          },
          "fast": {
            "model": "deepseek-v4-flash",
            "temperature": 0.1,
            "max_tokens": 1024,
            "context_window": 128000,
            "thinking": true
          }
        }
      }
    ]
  }
}
```

> **模型命名约定**：1M 上下文模型使用 `deepseek-v4-pro[1m]`，快速模型使用 `deepseek-v4-flash`。`[1m]` 后缀不可省略。

也可以使用 OpenAI 兼容端点作为替代方案：

```json
{
  "providers": {
    "openai": [
      {
        "api_key": "<你的 DeepSeek API Key>",
        "base_url": "https://api.deepseek.com/chat/completions",
        "timeout": 60,
        "agents": {
          "default": {
            "model": "deepseek-v4-pro",
            "temperature": 0.7,
            "max_tokens": 8192,
            "context_window": 128000,
            "thinking": false
          }
        }
      }
    ]
  }
}
```

> **注意**：`base_url` 必须包含完整路径（例如 `/anthropic/v1/messages` 或 `/chat/completions`）。

#### 3. 运行 Prosophor

```
cd /path/to/your/project
/path/to/prosophor/build/prosophor
```

Prosophor 将以交互式 CLI 模式启动。输入 `/help` 查看可用命令，或直接与 DeepSeek 对话。

<div align="center">
</div>
