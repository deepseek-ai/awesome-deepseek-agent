[English](./prosophor.md) | [简体中文](./prosophor.zh-CN.md) · [← Back](../README.md)

# Integrate with Prosophor

Prosophor is a plugin-based proactive AI agent CLI with full multi-model support. It connects to DeepSeek via both Anthropic-compatible and OpenAI-compatible APIs.

#### 1. Install Prosophor

- Install build dependencies: CMake 3.20+, C++17 compiler, SDL2, libcurl.

```
# Ubuntu / Debian
sudo apt install cmake g++ libsdl2-dev libcurl4-openssl-dev

# macOS
brew install cmake sdl2 curl
```

- Clone and build:

```
git clone https://github.com/Swair/prosophor.git
cd prosophor
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

- After building, verify the binary:

```
./prosophor --version
```

#### 2. Configure DeepSeek

Prosophor uses `config/.prosophor/settings.json` for provider configuration. Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Edit `config/.prosophor/settings.json`:

```json
{
  "default_role": "default",
  "log_level": "info",
  "providers": {
    "anthropic": [
      {
        "api_key": "<your DeepSeek API Key>",
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

> **Model naming convention**: Use `deepseek-v4-pro[1m]` for the 1M-context model and `deepseek-v4-flash` for the fast model. The `[1m]` suffix is required.

You can also use the OpenAI-compatible endpoint as an alternative:

```json
{
  "providers": {
    "openai": [
      {
        "api_key": "<your DeepSeek API Key>",
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

> **Important**: The `base_url` must include the full path (e.g., `/anthropic/v1/messages` or `/chat/completions`).

#### 3. Run Prosophor

```
cd /path/to/your/project
/path/to/prosophor/build/prosophor
```

Prosophor starts in interactive CLI mode. Type `/help` to see available commands, or just start chatting with DeepSeek.

<div align="center">
</div>
