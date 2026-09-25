[English](./veloce_lab.md) | [简体中文](./veloce_lab.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 在 Veloce Lab 中接入 DeepSeek

Veloce Lab 是一个基于 YumeriJS 框架构建的个人助理 harness，通过 Web 管理后台配置个人助理使用的模型渠道。

- **GitHub：** <https://github.com/veloce-ailab/veloce-lab>

#### 1. 安装并启动 Veloce Lab

- 安装 [Node.js](https://nodejs.org/) 24 LTS 或更高版本。
- 在一个空项目目录中下载 Veloce 配置文件：

```powershell
irm -OutFile yumeri.json https://raw.githubusercontent.com/veloce-ailab/veloce-lab/main/scripts/yumeri.json
```

- 启动服务。推荐使用 `npx`，因为不需要提前在项目中安装 Yumeri：

```sh
npx yumeri@latest -c yumeri.json --auto-install
```

`--auto-install` 会自动安装配置中声明的依赖。Veloce Lab 启动后，打开对应的 Web 管理后台，并使用管理员账号登录。

#### 2. 添加 DeepSeek 上游渠道

1. 在管理后台打开 **Channels（渠道）**，选择 **Add upstream（添加上游渠道）**。
2. 填写渠道表单：

| 字段 | 值 |
|------|----|
| 名称 | 例如 `DeepSeek` |
| 类型 | `DeepSeek` |
| Base URL | `https://api.deepseek.com` |
| API Key | 从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取的密钥 |
| 启用 | 打开 |

3. 如果没有配置多渠道路由，可以保留默认优先级和权重，然后点击 **Save（保存）**。

类型列表只显示当前 Veloce 配置中已经注册的适配器。如果看不到 `DeepSeek`，请在 `yumeri.json` 中启用对应适配器并重启服务。Base URL 可以填写主机地址，也可以带上 `/v1`；Veloce 构造请求地址时会避免重复添加 `/v1`。

#### 3. 添加 DeepSeek 模型

点击新渠道对应的模型列表按钮，打开 **Model configs（模型配置）**。有两种添加方式：

**从 API 同步（推荐）**

1. 保持 **Sync format（同步格式）** 为 `OpenAI /v1/models`。
2. 点击 **Sync models（同步模型）**。
3. 在预览窗口中保留需要的模型，点击 **Submit sync（提交同步）**。

请使用当前的 DeepSeek 模型名称，例如 `deepseek-v4-pro` 或 `deepseek-v4-flash`。DeepSeek V4 模型支持最高 100 万 token 上下文；Veloce 的模型配置窗口没有上下文窗口字段，因此实际请求上限取决于所选模型以及下游客户端或适配器。Veloce 支持 `max` 以及自定义思考等级标识；对于支持该配置的客户端，请使用 `max` 获得最高推理强度。

**手动添加模型**

1. 点击 **Add model config（添加模型配置）**。
2. 填写模型名称，例如 `deepseek-v4-pro`。
3. 如果上游模型名称相同，可以不填 **Upstream model name（上游模型名称）**；否则填写供应商要求的准确名称。
4. **Provider（供应商）** 保持 **Auto detect（自动识别）**。Veloce 会识别包含 `deepseek` 的模型名；必要时也可以显式选择供应商，或使用 **Custom provider（自定义供应商）**。
5. 保持 **Enabled（启用）** 打开，点击 **Save（保存）**。

#### 4. 首次运行请求

同步或保存后，模型即可供个人助理使用。打开 Veloce Lab 的聊天页面，选择刚启用的 DeepSeek 模型并发送一条简单的代码问题。确认收到回复后，再到管理后台检查该渠道的请求数和 Token 计数是否增加。

#### 模型同步故障排查

- **服务端无法请求 `/v1/models`：** Veloce 会打开失败回退窗口并显示请求地址。可以选择 **Fetch in browser（使用浏览器获取）**，必要时携带渠道令牌；也可以把模型列表 JSON 粘贴到 **Manual JSON（手动 JSON）** 中，再点击 **Parse JSON（解析 JSON）**。
- **没有获取到模型：** 检查 Base URL、API Key、适配器类型，并确认上游能从 `/v1/models` 返回模型列表。上游使用其他路径时，也可以选择 `Generic /models`、`Generic /api/models` 或 `Custom path（自定义路径）`。
- **模型无法选择：** 确认模型配置和上游渠道都处于启用状态，然后刷新模型目录。
