[English](./deepx-code.md) | [简体中文](./deepx-code.zh-CN.md) · [← Back](../README.md)

# Integrate with deepx-code

[deepx-code](https://github.com/itmisx/deepx-code) is a DeepSeek-native coding agent that runs in the terminal. Written in Go — small, fast, and cross-platform — it leans on automatic context compaction and zero-token local keyword routing to cut cost on long sessions. It also bundles a built-in code graph for symbol-level navigation (cutting read/glob/grep token waste) and local image OCR (PaddleOCR PP-OCRv5) for offline screenshot reading, and integrates with MCP servers and Claude-ecosystem skills.

#### 1. Install deepx-code

macOS / Linux — installs a prebuilt binary to `~/.local/bin/deepx`:

```
curl -fsSL https://raw.githubusercontent.com/itmisx/deepx-code/main/scripts/install.sh | bash
```

Windows (PowerShell):

```
irm https://raw.githubusercontent.com/itmisx/deepx-code/main/scripts/install.ps1 | iex
```

Upgrade any time with `deepx upgrade`.

#### 2. Get a DeepSeek API Key

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys). The first run of deepx-code opens a built-in setup wizard that asks for it and persists it to `~/.deepx/model.yaml` — no environment variable needed. The default config points both roles at `api.deepseek.com` using **DeepSeek-V4-Flash** / **DeepSeek-V4-Pro** with a 1M-token context window.

#### 3. Enter the project directory and run `deepx` to get started.

```
cd /path/to/my-project
deepx
```

By default deepx-code uses **DeepSeek-V4-Flash** for cost-efficient iteration and automatically escalates to **DeepSeek-V4-Pro** for complex, multi-step work. Inside the TUI: `/plan` (read-only planning), `/auto` (full autonomy), `/review` (confirm writes and commands), `/compact` (compact the session to save context), `/lang` (switch zh/en). Run `/help` for the full slash-command reference.

Drop an image path into the chat (e.g. an error screenshot or a UI mockup) and deepx-code reads the text from it with built-in OCR — local inference, no multimodal API needed. On first use it downloads the ONNX runtime and the PaddleOCR model (~37MB); after that it runs offline and responds in seconds.
