[English](./device_agent.md) | [简体中文](./device_agent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 将 DeepSeek 与 Device Agent 集成，用于实体设备控制

[Device Agent](https://github.com/emqx/device-agent) 是一个由 MQTT 驱动的 AI 助手，可以把 IoT 设备变成可对话、可控制、可协作的 AI Agent。它使用 `DeviceSpec` 为每类设备建模，通过 MQTT 连接真实硬件或浏览器模拟器，并使用大模型把自然语言请求映射成具体设备命令、状态查询与事件处理。

本指南介绍如何用 DeepSeek 运行 Device Agent，创建一个硬件 Agent，用模拟器或真实 MQTT 设备验证命令执行，并将该 Agent 发布到 A2A 网络中实现多设备协作。

#### 1. 安装要求

- 一个 [DeepSeek API Key](https://platform.deepseek.com/api_keys)。
- 通过发布脚本安装 Device Agent：

```shell
curl -fsSL https://emqx.sh/device-agent | sh
```

- 一个用于设备连接的 MQTT Broker。快速测试时，Device Agent 可以创建由 [EMQX Cloud](https://www.emqx.com/en/cloud) 提供的临时 Zero EMQX Broker。生产环境或私有部署可使用 [EMQX](https://www.emqx.com/en/products/emqx)、[EMQX Cloud](https://www.emqx.com/en/cloud) 或 EMQX Edge。

Device Agent 需要一个能稳定生成结构化输出并支持工具调用的模型。复杂设备建模和 A2A 规划建议使用 `deepseek-v4-pro`，低成本迭代可以使用 `deepseek-v4-flash`。DeepSeek V4 支持 100 万 token 上下文；在本配置流程中，Device Agent 不需要单独设置上下文窗口。如果你的 DeepSeek 兼容运行时提供推理强度控制，请保持思考模式开启，并在复杂硬件工作流中使用 `max`。

#### 2. 使用 DeepSeek 启动 Device Agent

用 DeepSeek 作为主 Agent 模型，并启用 Zero EMQX：

```shell
ZERO_EMQX_ENABLED=true \
LLM_PROVIDER=deepseek \
LLM_MODEL=deepseek-v4-pro \
LLM_API_KEY=sk-your-deepseek-api-key \
device-agent
```

打开控制台：

```text
http://127.0.0.1:3000
```

`ZERO_EMQX_ENABLED=true` 会创建临时 MQTT Broker，并把 MQTT 配置写入运行时配置。如果要使用自己的 Broker，可在启动前或通过 **Settings -> MQTT** 配置：

```shell
MQTT_BROKER_URL=mqtt://127.0.0.1:1883
VITE_MQTT_WS_URL=ws://127.0.0.1:8083/mqtt
MQTT_USERNAME=
MQTT_PASSWORD=
```

对于 EMQX Cloud Serverless 或其他 TLS 部署，使用 `mqtts://` 和 `wss://` 地址：

```shell
MQTT_BROKER_URL=mqtts://<deployment-host>:8883
VITE_MQTT_WS_URL=wss://<deployment-host>:8084/mqtt
MQTT_USERNAME=<client-username>
MQTT_PASSWORD=<client-password>
MQTT_TLS_ENABLED=true
MQTT_TLS_REJECT_UNAUTHORIZED=true
```

也可以在启动后通过 **Settings -> Models** 配置模型：

| 字段 | 值 |
| --- | --- |
| Provider | `deepseek` |
| Model | `deepseek-v4-pro` 或 `deepseek-v4-flash` |
| API key | 你的 DeepSeek API Key |
| Max iterations | 保持默认值，除非工作流需要更多工具调用步骤 |

#### 3. 创建设备 Agent

在 Device Agent 首页描述一个设备类别，或上传 JSON、YAML、Markdown 设备定义。Device Agent 会生成包含以下内容的 `DeviceSpec`：

- `commands`：Agent 可以下发给设备的动作。
- `properties`：设备上报的状态字段。
- `events`：设备主动上报的结构化事件。

首次运行可使用恒温器描述：

```text
Smart thermostat with on/off control, target temperature setting, and HVAC mode switching (heat, cool, auto, fan_only, eco). It reports current temperature, target temperature, humidity, current mode, heating status, cooling status, and online status. It emits an over-temperature alert when temperature exceeds 30 C and a device-offline error event when the device disconnects.
```

创建前先检查生成的 `DeviceSpec`：

- 命令名称与参数是否覆盖用户需要控制的动作。
- 属性名称是否覆盖需要查询或验证的状态。
- 事件名称与事件载荷是否能描述告警、故障和关键变化。
- 字段名是否是稳定的英文标识符，例如 `set_target_temperature`、`current_temperature`、`over_temperature`。

草稿正确后点击 **Create**，进入新 Device Agent 的工作区。

#### 4. 架构流程

运行时流程如下：

```text
用户、语音、IM 或其他 Agent
  -> 使用 DeepSeek 的 Device Agent 运行时
  -> 基于 DeviceSpec 选择命令、查询状态或处理事件
  -> EMQX / EMQX Cloud MQTT Broker
  -> 浏览器模拟器、生成的 SDK、现有固件、边缘网关或后端适配器
  -> 命令响应、遥测数据与事件上报
  -> Device Agent 工作区以及可选的 A2A 回复
```

DeepSeek 作为推理层理解用户意图和设备状态。Device Agent 将推理结果转换为经过校验的设备命令和 MQTT 消息。EMQX 提供设备连接、命令下发、遥测、事件、浏览器模拟器访问，以及 A2A 发现或请求主题所需的 Broker 基础设施。

#### 5. 使用浏览器模拟设备验证

如果硬件还没有准备好，在工作区点击 **Try a simulated device**。模拟器运行在浏览器中，使用当前 `DeviceSpec`，连接 MQTT，上报状态，响应命令，并可以上报事件。

模拟设备出现在设备列表后，选中它并发送控制请求：

```text
Set the target temperature to 24 degrees and switch to auto mode.
```

然后查询状态和事件：

```text
Show the current device status, including current temperature, target temperature, humidity, and mode. Also check whether there have been any recent reported events.
```

在状态面板中确认：

- 设备在线。
- 当前状态包含 `target_temperature` 和 `mode`。
- 可用命令来自 `DeviceSpec`。
- 模拟器上报事件后，Recent events 中能看到事件记录。

这一步可以在真实硬件接入前验证 DeepSeek -> Device Agent -> MQTT -> 模拟设备的完整链路。

#### 6. 连接真实设备

在工作区点击 **Connect device**。Device Agent 提供三种真实设备接入路径：

| 路径 | 适用场景 |
| --- | --- |
| SDK toolkit | 需要一个可运行的设备端项目，并由你自己补充硬件逻辑 |
| Agent-enhanced SDK | 希望 Device Agent 在基础 SDK 上生成设备端业务逻辑 |
| Existing device | 已有固件、网关或后端服务，只需要 MQTT topic 和 payload 示例 |

SDK toolkit 包含 MQTT 连接配置、设备身份、`device-spec.json`、命令处理、状态上报、事件上报，以及可选的语音或视觉代码。Existing device 接入不会生成代码，而是展示 MQTT Broker、`productId`、`namespace`、`deviceId`、topics 和 payload 示例。

对于已有设备，将固件、边缘网关或后端进程适配到 MQTT 契约：

```text
启动时：
  连接 MQTT
  订阅命令主题
  发布在线状态和当前状态快照

收到命令时：
  执行已有设备能力
  使用相同 requestId 发布响应
  如果状态变化，发布最新状态

状态变化时：
  发布状态遥测

出现告警、故障或任务完成时：
  发布事件
```

默认 topics 如下：

| 方向 | 用途 | 默认 topic |
| --- | --- | --- |
| 设备订阅 | 接收命令 | `device-agent/{productId}/device/{deviceId}/commands` |
| 设备发布 | 返回命令响应 | `device-agent/{productId}/device/{deviceId}/responses` |
| 设备发布 | 上报在线状态和遥测 | `v1/{productId}/{deviceId}/telemetry` |
| 设备发布 | 上报设备事件 | `v1/{productId}/{deviceId}/event` |

第一条有效状态或遥测上报被接收后，设备会出现在工作区中。发送对话控制请求后，确认响应、最新状态和事件记录可见。

#### 7. 将 Device Agent 发布到 A2A 网络

当 Device Agent 需要与其他 Agent 协作，而不只是服务当前控制台时，启用 A2A。例如，一个传感器 Device Agent 检测到异常状态后，可以请求空调、灯光、门锁、机械臂或其他硬件 Agent 执行动作。

启用 A2A 前确认：

- 使用 EMQX 6.2.0 或更高版本，并启用 A2A registry。
- `DeviceSpec` 至少包含一个命令。Device Agent 会将命令映射为 A2A skills。
- Device Agent 和其他 Agent 连接到同一个 MQTT Broker。

创建或编辑 Device Agent 时，开启 **Enable A2A Collaboration**。如果要在 Marketplace 中展示，再开启 **Publish A2A Card**。Device Agent 会根据 Device Agent 名称、描述、Broker 地址和命令派生 skills 生成 A2A card。

其他 Agent 可以通过 EMQX A2A discovery topic 发现该 card：

```text
$a2a/v1/discovery/{org_id}/{unit_id}/{agent_id}
```

也可以通过 MQTT v5 JSON-RPC `SendMessage` 调用它：

```text
Request topic: $a2a/v1/request/{org_id}/{unit_id}/{agent_id}
Reply topic:   $a2a/v1/reply/{org_id}/{unit_id}/{caller_agent_id}/{reply_suffix}
```

示例请求体：

```json
{
  "jsonrpc": "2.0",
  "id": "task-001",
  "method": "SendMessage",
  "params": {
    "message": {
      "role": "user",
      "parts": [
        {
          "type": "text",
          "text": "Check the current temperature. If it is too high, switch the air conditioner to cooling mode."
        }
      ],
      "taskId": "task-001"
    },
    "metadata": {
      "sender": "my-a2a-client"
    }
  }
}
```

回复会发布到 MQTT v5 `responseTopic`，包含状态更新、文本结果、完成状态或失败状态。

#### 8. 多设备示例场景

- **智能家居舒适度控制**：恒温器 Agent 检测到高温，请求空调 Agent 制冷，并请求灯光 Agent 切换到节能模式。
- **门禁控制**：门铃或摄像头 Agent 上报访客事件，然后请求智能门锁 Agent 查询锁状态，并请求显示设备 Agent 展示提示。
- **工业安全**：传感器 Agent 检测到异常遥测数据，请求风扇或水泵 Agent 响应，并返回处理报告。
- **机器人演示**：机械臂或机器狗 Agent 暴露由命令派生的 skills，让其他 A2A Agent 协调实体动作。
- **边缘硬件**：SpacemiT 等边缘开发板通过 MQTT 或生成的 SDK 接入，并参与同一套 Device Agent 工作流。

#### 验证

按以下清单检查：

1. Device Agent 使用 `LLM_PROVIDER=deepseek` 和 DeepSeek V4 模型启动。
2. MQTT 配置指向可访问的 EMQX、EMQX Cloud 或 Zero EMQX Broker。
3. 生成的 `DeviceSpec` 包含准确的 commands、properties 和 events。
4. 模拟设备或真实设备在设备列表中显示在线。
5. 自然语言控制请求会向选中的设备发送命令。
6. 设备使用相同 `requestId` 发布命令响应。
7. 状态变化显示在当前状态面板中。
8. 设备主动上报的事件显示在 Recent events 中。
9. 如果启用了 A2A，A2A Marketplace 或 EMQX A2A registry 中能看到 card。
10. 其他 Agent 可以通过 MQTT v5 `SendMessage` 调用该 Device Agent 并收到回复。

#### 故障排查

- **Device Agent 无法调用 DeepSeek**：检查 `LLM_PROVIDER=deepseek`、`LLM_MODEL` 和 `LLM_API_KEY`。也可以在控制台 **Settings -> Models** 中确认。
- **找不到模型**：使用当前模型 ID，例如 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
- **MQTT 连接失败**：检查 Broker URL、WebSocket URL、凭据、TLS 配置，以及浏览器是否能访问 `VITE_MQTT_WS_URL`。
- **设备没有出现**：发布在线状态或状态上报，然后检查 `productId`、`deviceId`、topic 模板和 `metadata.productId`。
- **命令到达设备但状态不更新**：命令响应后发布最新 status 或 state。
- **A2A card 缺失**：确认已启用 A2A、`DeviceSpec` 中有 commands、EMQX A2A registry 已启用；使用 Web Marketplace 时也要确认 `VITE_FF_A2A_MARKETPLACE_ENABLE=true`。

#### 资源

- [Device Agent](https://github.com/emqx/device-agent)
- [Device Agent 文档](https://device-agent-web.vercel.app/docs)
- [Device Agent MQTT Broker](https://device-agent-web.vercel.app/docs/mqtt-broker)
- [Use a Device Agent](https://device-agent-web.vercel.app/docs/usage/use-device-agent)
- [Device Agent A2A Collaboration](https://device-agent-web.vercel.app/docs/usage/a2a)
- [EMQX](https://www.emqx.com/en/products/emqx)
- [EMQX Cloud](https://www.emqx.com/en/cloud)
- [DeepSeek 开放平台](https://platform.deepseek.com/)
- [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/)
