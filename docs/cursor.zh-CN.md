[English](./cursor.md) | [简体中文](./cursor.zh-CN.md) · [↩ 返回](../README.zh-CN.md)

# 接入 Cursor

Cursor 原生并不能正确处理 DeepSeek 思维链模式下的工具调用，因此更推荐在 DeepSeek API 前面加一层兼容代理。一个现成可用的参考实现是 [deepseek-cursor-proxy](https://github.com/yxlao/deepseek-cursor-proxy)。

#### 1. 准备 ngrok

Cursor 的自定义模型通常需要公网 HTTPS 地址，不能直接填 `localhost`，最省事的方式是使用 [ngrok](https://ngrok.com/)。

- 先注册一个 ngrok 账号。
- 再安装 ngrok。
- 最后配置一次 authtoken。

推荐按下面顺序操作。

**步骤 1：安装 ngrok**

Windows 更推荐直接去官方下载页下载压缩包，而不是用命令行安装器：

1. 打开 [ngrok Windows 下载页](https://ngrok.com/download/windows)。
2. 点击 `Download`，下载 Windows 的 zip 压缩包。
3. 解压后把 `ngrok.exe` 放到一个固定目录，比如 `D:\\tools\\ngrok\\`。

macOS 可以直接用 Homebrew：

```bash
brew install ngrok
```

如果你已经在用 Cloudflare Tunnel 等其他隧道服务，也可以直接替代 ngrok。

**步骤 2：配置 authtoken**

打开 [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) 复制自己的 authtoken，然后执行一次配置命令即可。

Windows 示例：

```bash
cd D:\tools\ngrok
.\ngrok.exe config add-authtoken <你的-ngrok-token>
```

macOS 或已加入 PATH 的环境可以直接执行：

```bash
ngrok config add-authtoken <你的-ngrok-token>
```

**步骤 3：可选的联通性测试**

如果你想先确认 ngrok 本身能正常工作，可以临时做一次 HTTP 联通测试：

```bash
# 终端 1：随便起一个本地 8080 测试服务
python -m http.server 8080

# 终端 2：把 8080 暴露到公网
ngrok http 8080
```

看到 ngrok 输出 `https://xxxx.ngrok-free.app` 或类似公网地址后，浏览器打开它，能看到目录列表或 `python -m http.server` 的默认页面，就说明 ngrok 没问题。

这一步只是测试 ngrok 是否可用，不是正式给 Cursor 用的代理地址。测试完成后记得把这两个进程都关掉，尤其是 `ngrok http 8080` 要按 `Ctrl+C` 退出。后面的 `deepseek-cursor-proxy` 会自动启动它自己的本地端口，并在启用 ngrok 时自动拉起对应的隧道；如果你把测试用的 8080 隧道一直开着，后面很容易把地址填错。

#### 2. 克隆并启动代理

如果你本机已经有 `uv` 环境，推荐优先直接用 `uv` 运行，步骤最省事：

```bash
git clone https://github.com/yxlao/deepseek-cursor-proxy.git
cd deepseek-cursor-proxy
uv run deepseek-cursor-proxy
```

如果你还没有 `uv`，也可以先安装到 Python 环境中再启动：

```bash
git clone https://github.com/yxlao/deepseek-cursor-proxy.git
cd deepseek-cursor-proxy
pip install -e .
deepseek-cursor-proxy
```

首次运行后，代理会自动创建：

- `~/.deepseek-cursor-proxy/config.yaml`
- `~/.deepseek-cursor-proxy/reasoning_content.sqlite3`

如果启用了 ngrok，启动日志里会打印一个可供 Cursor 使用的 HTTPS 公网地址。后面在 Cursor 里填写 Base URL 时，要以 `deepseek-cursor-proxy` 启动后打印出来的地址为准，不要继续使用上一步 `ngrok http 8080` 测试时生成的地址。

#### 3. 在 Cursor 中添加自定义模型

打开 Cursor 设置，新增一个兼容 OpenAI 的自定义模型：

- 模型名：`deepseek-v4-pro` 或 `deepseek-v4-flash`
- API Key：你的 DeepSeek API Key
- Base URL：你的隧道地址，并在末尾加上 `/v1`

例如：

```text
https://example.ngrok-free.dev/v1
```

代理会沿用 Cursor 传来的模型名，所以你可以直接在 Cursor 里切换 `deepseek-v4-pro` 和 `deepseek-v4-flash`。

#### 4. 在 Cursor 中开始使用

在 Cursor 中选中刚添加的 DeepSeek 模型后，就可以像平时一样使用聊天或 Agent 模式。

这个代理最关键的作用，是为 DeepSeek 思维链工具调用补回 Cursor 没有传回的 `reasoning_content` 字段，避免 400 报错。同时它也能把思考过程显示到 Cursor 里，并补上一些工具调用兼容性处理。

#### 可选启动参数

参考代理里比较常用的参数有：

```bash
# 不在 Cursor 里显示 thinking 内容
deepseek-cursor-proxy --no-display-reasoning

# 输出更详细的请求日志
deepseek-cursor-proxy --verbose

# 指定本地端口
deepseek-cursor-proxy --port 9000

# 不启用 ngrok，仅本地运行
deepseek-cursor-proxy --no-ngrok
```

<div align="center">
<img src="https://raw.githubusercontent.com/yxlao/deepseek-cursor-proxy/main/assets/cursor_config.png" width='900' border='1' />
</div>
