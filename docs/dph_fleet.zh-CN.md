[English](./dph_fleet.md) | [简体中文](./dph_fleet.zh-CN.md) · [← Back](../README.zh-CN.md)

# dph-fleet 接入 DeepSeek

[dph-fleet](https://github.com/polaris-smart/dph-fleet) 是 DeepSeek Harness（dsh）的开源插件，把你的多台设备变成一个舰队：任何跑在 dsh 会话里的智能体都能直接使用它注册的工具——同网设备发现（mDNS）、密钥配对（WiFi 式输入一个 key）、SSH 跨网直连执行命令、文件传输。纯插件挂载，零核心改动、运行时零 npm 依赖，卸载不留痕迹。

- **GitHub:** <https://github.com/polaris-smart/dph-fleet>

#### 1. 安装 dsh（DeepSeek Harness）

dph-fleet 运行在 dsh 内，舰队里的每台设备都要装 dsh（Node 22+）：

```sh
npx @deepseek-ai/dsh web
```

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys)获取 API Key，然后通过 dsh 的凭据服务保存（Web 界面的模型页可以写入），或在启动环境中导出：

```sh
export DEEPSEEK_API_KEY=sk-...
```

#### 3. 安装 dph-fleet 插件

在**每台**设备上，把插件装进你使用的 profile（默认 `web`）：

```sh
npx @deepseek-ai/dsh plugin --profile web add dph-fleet
```

然后重启 dsh。插件会自动注册六个智能体工具（`fleet_discover`、`fleet_pair`、`fleet_ssh_exec`、`fleet_workspace`、`fleet_upload`、`fleet_download`）。

#### 4. 首次运行——配对两台设备，然后一句话指挥

至少需要 2 台装了 dph-fleet 的设备，连接方式二选一：同一局域网（mDNS），或公网可达的 SSH 端点。

在被控设备 B 上查看设备密钥并保持监听。在主控设备 A 上，直接对 dsh 智能体说话：

```
> 配对设备 192.168.1.42，密钥 fleet-d-xxxx
> 我有哪些设备？               （fleet_discover）
> 在 B 上执行 hostname          （fleet_ssh_exec）
> 把 /tmp/report.txt 传到 B:/tmp/（fleet_upload）
> 从 B 取回 /tmp/result.json    （fleet_download）
```

智能体会直接调用 fleet 工具，不需要额外 CLI。同网场景下 `fleet_discover` 自动列出邻居设备；跨网场景与设备的 SSH 主机配对一次并完成公钥授权即可。

#### 说明

- 模型配置（DeepSeek-V4 系列、上下文窗口、推理力度）由 dsh 本身负责，参见 dsh 文档。dph-fleet 只提供设备互连工具，不介入模型路由。
- NAT 内网设备（都在家庭/办公路由器后面）当前版本无法直连，P2P 路线已在规划中。
- 适用前提与完整流程见 [dph-fleet README](https://github.com/polaris-smart/dph-fleet)。
