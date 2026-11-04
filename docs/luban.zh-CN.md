[English](./luban.md) | [简体中文](./luban.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Luban

Luban 是一款装在 VS Code / VSCodium 侧边栏里的编程 Agent：它直接改工作区里的文件、跑命令自验结果，每个改动都以编辑器 diff 的形式呈现，可以逐块接受或撤销。它对接 OpenAI 兼容的 chat completions 接口，所以 DeepSeek V4 Pro / V4 Flash 可以直接当一等公民用。

- **GitHub：** <https://github.com/eppen/luban>
- **VS Code 市场：** <https://marketplace.visualstudio.com/items?itemName=liuhualiang.luban>

#### 1. 安装 Luban

| 安装方式 | 步骤 |
| --- | --- |
| VS Code | 扩展面板（`Ctrl+Shift+X`）→ 搜索 `Luban` → **安装** |
| VSCodium / Open VSX | 扩展面板 → 搜索 `Luban` → **安装** |
| VSIX | 从 [Releases](https://github.com/eppen/luban/releases) 下载 `luban-v*.vsix`，然后 `⋯` → **从 VSIX 安装…** |
| 内置扩展 | 仓库里的 `./install-into-vscodium.sh`，把 Luban 装成应用级扩展（仅 VSCodium） |

要求 VS Code / VSCodium **1.100** 及以上版本。

#### 2. 获取 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建 API Key 并复制。

#### 3. 配置 DeepSeek

Luban 内置了 DeepSeek 供应商模板，通常只需要填 Key 并调整模型限额。

**方式一：设置面板（推荐）**

1. 用 `Ctrl+Shift+L`（macOS 为 `Cmd+Shift+L`）打开侧边栏，点击聊天面板底部的 **⚙** 按钮，或在命令面板执行 **Provider settings (model / API key)**。
2. 面板默认停在内置的 **DeepSeek** 供应商（`https://api.deepseek.com/v1`）。把 API Key 填进 key 输入框：它存进 VS Code SecretStorage，不会写进 `providers.json`。
3. 把每个模型的 **max input** 改成 `1000000`（DeepSeek V4 支持 100 万 token 上下文），**max output** 改成 `65536`（V4 最大输出 384000 token）。
4. 展开模型的 **thinking** 一行 → **Fill template…**（填入模板）→ **DeepSeek**，再把 `on` 档里的 `"reasoning_effort": "high"` 改成 `"max"`。这是开启 DeepSeek 最高推理强度的开关。
5. 点 **Test connection**（发一次 `max_tokens=1` 的请求，显示状态码与耗时），再点 **Save**。配置写入 `~/.luban/providers.json`（原文件备份为 `providers.json.bak`）并热重载。

日常可以：重规划用 `deepseek-v4-pro`，便宜迭代用 `deepseek-flash`，面板底部的模型下拉框可随时切换。

**方式二：手改 `~/.luban/providers.json`**

```json
{
  "defaultModel": "deepseek::deepseek-v4-pro",
  "providers": [
    {
      "id": "deepseek",
      "name": "DeepSeek",
      "baseUrl": "https://api.deepseek.com/v1",
      "apiKeyEnv": "DEEPSEEK_API_KEY",
      "webSearch": {
        "baseUrl": "https://api.deepseek.com/v1/tools",
        "count": 8,
        "engine": "deepseek"
      },
      "models": [
        {
          "id": "deepseek-v4-pro",
          "name": "DeepSeek V4 Pro",
          "maxInputTokens": 1000000,
          "maxOutputTokens": 65536,
          "toolCalling": true,
          "thinking": {
            "default": "on",
            "on": {
              "thinking": { "type": "enabled" },
              "reasoning_effort": "max"
            },
            "off": {
              "thinking": { "type": "disabled" }
            }
          }
        },
        {
          "id": "deepseek-flash",
          "name": "DeepSeek Flash",
          "maxInputTokens": 1000000,
          "maxOutputTokens": 65536,
          "toolCalling": true,
          "vision": true,
          "thinking": {
            "default": "on",
            "on": {
              "thinking": { "type": "enabled" },
              "reasoning_effort": "high"
            },
            "off": {
              "thinking": { "type": "disabled" }
            }
          }
        }
      ]
    }
  ]
}
```

保存后在命令面板执行 **Reload providers.json**，或重开面板即可生效。

- **模型 id 会原样发给接口**：用 `deepseek-v4-pro` 和 `deepseek-flash`（当前 V4.1 Flash 的名字；旧名 `deepseek-v4-flash` 仍被接受）。
- `maxInputTokens` 是 Luban 的上下文预算基准：填 `1000000` 才能用满 V4 的 1M 上下文。想更早触发压缩、控制花费就调小（如 `262144`），因为它的高水位是窗口的 80%。
- Agent 模式要求 `toolCalling` 为 `true`；`vision` 只给 `deepseek-flash`（V4 Pro 不支持图片输入）。
- `thinking` 块会原样合并进请求体（`{"thinking": {"type": "enabled"}, "reasoning_effort": "max"}`）；`off` 档用于收尾总结和你手动关闭思考时，能省 token。
- **API Key 解析顺序**：供应商的 `apiKey` 字段 → VS Code SecretStorage（面板保存的位置）→ `apiKeyEnv` 环境变量 → `~/.hermes/.env` 里的同名变量。
- `webSearch` 指向 DeepSeek 的 Search / Fetch 接口，对应 `@web` 前缀和 `web_search` / `web_fetch` 工具。Search 与 Fetch 按成功请求计费，详见 [Search & Fetch 价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。

#### 4. 首次运行

1. 在模型下拉框选中 `deepseek-v4-pro`，保持 **Agent** 模式。
2. 提一个具体的任务，例如 `在 src/utils.js 里加一个 debounce 工具，然后跑一遍测试`：
   - Luban 会自动附上光标附近的代码；还可以用 `@文件`、`@文件夹/`、`#选区`，或在资源管理器里右键文件 → **Add File to Luban Chat** 补充上下文。
   - 每个写入都会在编辑器里打开真实 diff，逐块接受 / 撤销（每块上方的 CodeLens，或 diff 标题栏）。
3. 用 `Shift+Tab` 切换模式：**Plan** 只读调研、先产出计划文件再动手，**Chat** 不碰文件只问答。
4. 思考内容流式显示在回答上方的可折叠「思考过程」块里。模型配了 `thinking` 后，面板底部会出现 **🧠** 按钮，可按消息循环切换「默认 / 开 / 关」。

可选：命令面板执行 **Toggle Tab completion** 启用 DeepSeek FIM 补全。Luban 会从 `api.deepseek.com` 自动推导 `/beta` 的 FIM 端点；该项默认关闭（`luban.inlineCompletion.enabled`）。

#### 说明

- 会话落在 `~/.luban/sessions`，重载窗口不丢历史；多轮记忆默认开启。
- 消息布局对齐前缀缓存，每轮显示输入 / 输出 / 缓存命中 / 上下文占用；**Token usage dashboard** 汇总本地用量账本。
- `run_command` 在你自己的 shell 里执行，没有 OS 级沙箱。Plan 模式额外做命令级只读校验；`luban.fs.allowOutsideWorkspace=false` 可把文件工具限制在工作区内。
- 本地 stdio MCP 服务器与 `SKILL.md` 技能接进同一套工具循环；Plan 模式只能看到声明为只读的工具。
