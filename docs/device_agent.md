[English](./device_agent.md) | [简体中文](./device_agent.zh-CN.md) · [← Back](../README.md)

# Integrate DeepSeek with Device Agent for Physical Device Control

[Device Agent](https://github.com/emqx/device-agent) is an MQTT-powered AI assistant that turns IoT devices into conversational, controllable, and collaborative AI agents. It models each device category with a `DeviceSpec`, connects real hardware or browser simulators through MQTT, and uses an LLM to map natural-language requests to concrete device commands, state queries, and event handling.

This guide shows how to run Device Agent with DeepSeek, create a hardware agent, verify command execution with a simulator or real MQTT device, and publish the agent to an A2A network for multi-device collaboration.

#### 1. Install Requirements

- A [DeepSeek API key](https://platform.deepseek.com/api_keys).
- Device Agent, installed from the release script:

```shell
curl -fsSL https://emqx.sh/device-agent | sh
```

- An MQTT broker for device connectivity. For a quick test, Device Agent can create a temporary Zero EMQX broker powered by [EMQX Cloud](https://www.emqx.com/en/cloud). For production or private deployments, use [EMQX](https://www.emqx.com/en/products/emqx), [EMQX Cloud](https://www.emqx.com/en/cloud), or EMQX Edge.

Device Agent needs a model with reliable structured output and tool calling. Use `deepseek-v4-pro` for complex device modeling and A2A planning, or `deepseek-v4-flash` for lower-cost iteration. DeepSeek V4 supports a 1 million token context window; Device Agent does not require a separate context-window field in this setup. If your DeepSeek-compatible runtime exposes reasoning effort controls, keep thinking enabled and use `max` for complex hardware workflows.

#### 2. Start Device Agent with DeepSeek

Start Device Agent with DeepSeek as the primary agent model and Zero EMQX enabled:

```shell
ZERO_EMQX_ENABLED=true \
LLM_PROVIDER=deepseek \
LLM_MODEL=deepseek-v4-pro \
LLM_API_KEY=sk-your-deepseek-api-key \
device-agent
```

Open the console:

```text
http://127.0.0.1:3000
```

`ZERO_EMQX_ENABLED=true` creates a temporary MQTT broker and writes the MQTT settings into the runtime configuration. To use your own broker instead, configure these values before startup or from **Settings -> MQTT**:

```shell
MQTT_BROKER_URL=mqtt://127.0.0.1:1883
VITE_MQTT_WS_URL=ws://127.0.0.1:8083/mqtt
MQTT_USERNAME=
MQTT_PASSWORD=
```

For EMQX Cloud Serverless or other TLS deployments, use `mqtts://` and `wss://` endpoints:

```shell
MQTT_BROKER_URL=mqtts://<deployment-host>:8883
VITE_MQTT_WS_URL=wss://<deployment-host>:8084/mqtt
MQTT_USERNAME=<client-username>
MQTT_PASSWORD=<client-password>
MQTT_TLS_ENABLED=true
MQTT_TLS_REJECT_UNAUTHORIZED=true
```

You can also configure the model after startup from **Settings -> Models**:

| Field | Value |
| --- | --- |
| Provider | `deepseek` |
| Model | `deepseek-v4-pro` or `deepseek-v4-flash` |
| API key | Your DeepSeek API key |
| Max iterations | Keep the default unless the workflow needs more tool steps |

#### 3. Create a Device Agent

On the Device Agent home page, describe a device category or upload a JSON, YAML, or Markdown device definition. Device Agent generates a `DeviceSpec` with:

- `commands`: actions the agent can send to a device.
- `properties`: state fields reported by a device.
- `events`: structured device-originated events.

For a first run, use a thermostat description:

```text
Smart thermostat with on/off control, target temperature setting, and HVAC mode switching (heat, cool, auto, fan_only, eco). It reports current temperature, target temperature, humidity, current mode, heating status, cooling status, and online status. It emits an over-temperature alert when temperature exceeds 30 C and a device-offline error event when the device disconnects.
```

Review the generated `DeviceSpec` before creating the agent. Check that:

- Command names and parameters match what users should control.
- Property names cover state that must be queried or verified.
- Event names and payload fields describe alerts, failures, and important changes.
- Field names are stable English identifiers, such as `set_target_temperature`, `current_temperature`, and `over_temperature`.

When the draft is correct, click **Create**, then enter the new Device Agent workspace.

#### 4. Architecture Flow

The runtime flow is:

```text
User, voice, IM, or another agent
  -> Device Agent runtime with DeepSeek
  -> DeviceSpec-aware command selection, status query, or event handling
  -> EMQX / EMQX Cloud MQTT broker
  -> Browser simulator, generated SDK, existing firmware, edge gateway, or backend adapter
  -> Command response, telemetry, and event reports
  -> Device Agent workspace and optional A2A replies
```

DeepSeek acts as the reasoning layer for understanding user intent and device state. Device Agent turns that reasoning into validated device commands and MQTT messages. EMQX provides the broker infrastructure for device connections, command delivery, telemetry, events, browser simulator access, and A2A discovery or request topics.

#### 5. Verify with a Browser Simulated Device

If hardware is not ready, click **Try a simulated device** in the workspace. The simulator runs in the browser, uses the current `DeviceSpec`, connects to MQTT, reports state, responds to commands, and can emit events.

After the simulated device appears in the device list, select it and send a control request:

```text
Set the target temperature to 24 degrees and switch to auto mode.
```

Then query state and events:

```text
Show the current device status, including current temperature, target temperature, humidity, and mode. Also check whether there have been any recent reported events.
```

Verify the result in the status panel:

- The device is online.
- Current state includes `target_temperature` and `mode`.
- Available commands come from the `DeviceSpec`.
- Recent events are shown when the simulator reports them.

This validates the DeepSeek -> Device Agent -> MQTT -> simulated device loop before real hardware integration.

#### 6. Connect Real Devices

Click **Connect device** in the workspace. Device Agent provides three real-device access paths:

| Path | Use when |
| --- | --- |
| SDK toolkit | You need a runnable device-side project and will add hardware logic yourself |
| Agent-enhanced SDK | You want Device Agent to generate device-side business logic on top of the toolkit |
| Existing device | You already have firmware, a gateway, or a backend service and only need MQTT topics and payload examples |

The SDK toolkit includes MQTT connection settings, device identity, `device-spec.json`, command handling, state reports, event reports, and optional voice or vision code. Existing device access shows the MQTT broker, `productId`, `namespace`, `deviceId`, topics, and payload examples without generating code.

For an existing device, adapt firmware, an edge gateway, or a backend process to the MQTT contract:

```text
Startup:
  Connect to MQTT
  Subscribe to the command topic
  Publish online status and the current state snapshot

On command:
  Execute the existing device capability
  Publish a response with the same requestId
  Publish the latest state if it changed

On state change:
  Publish state telemetry

On alert, failure, or task completion:
  Publish an event
```

Default topics are:

| Direction | Purpose | Default topic |
| --- | --- | --- |
| Device subscribes | Receive commands | `device-agent/{productId}/device/{deviceId}/commands` |
| Device publishes | Return command responses | `device-agent/{productId}/device/{deviceId}/responses` |
| Device publishes | Report online status and telemetry | `v1/{productId}/{deviceId}/telemetry` |
| Device publishes | Report device events | `v1/{productId}/{deviceId}/event` |

After the first accepted status or state report, the device appears in the workspace. Use a conversation request to control it, then confirm that the response, latest state, and recent events are visible.

#### 7. Publish Device Agent to an A2A Network

Use A2A when the Device Agent should collaborate with other agents, not only with the current console. For example, a sensor Device Agent can detect an abnormal state and ask an air conditioner, light, door lock, robot arm, or other hardware agent to act.

Before enabling A2A:

- Use EMQX 6.2.0 or later with the A2A registry enabled.
- Make sure the `DeviceSpec` has at least one command. Device Agent maps commands into A2A skills.
- Make sure Device Agent and other agents connect to the same MQTT broker.

When creating or editing the Device Agent, turn on **Enable A2A Collaboration**. To show it in the marketplace, also turn on **Publish A2A Card**. Device Agent generates an A2A card from the Device Agent name, description, broker address, and command-derived skills.

Other agents can discover the card through the EMQX A2A discovery topic:

```text
$a2a/v1/discovery/{org_id}/{unit_id}/{agent_id}
```

They can call it with MQTT v5 JSON-RPC `SendMessage`:

```text
Request topic: $a2a/v1/request/{org_id}/{unit_id}/{agent_id}
Reply topic:   $a2a/v1/reply/{org_id}/{unit_id}/{caller_agent_id}/{reply_suffix}
```

Example request body:

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

Replies are published to the MQTT v5 `responseTopic` as status updates, text artifacts, completion, or failure messages.

#### 8. Example Multi-Device Scenarios

- **Smart home comfort**: a thermostat agent detects high temperature, asks an air conditioner agent to cool the room, and asks a light agent to switch to energy-saving mode.
- **Access control**: a doorbell or camera agent reports a visitor event, then asks a smart lock agent to query lock state and a display agent to show a message.
- **Industrial safety**: a sensor agent detects abnormal telemetry, asks a fan or pump agent to respond, and returns a handling report.
- **Robotics demo**: a robot arm or robot dog agent exposes command-derived skills so another A2A agent can coordinate physical actions.
- **Edge hardware**: an edge board, such as a SpacemiT-based device, connects through MQTT or a generated SDK and participates in the same Device Agent workflow.

#### Verify

Use this checklist:

1. Device Agent starts with `LLM_PROVIDER=deepseek` and a DeepSeek V4 model.
2. MQTT settings point to a reachable EMQX, EMQX Cloud, or Zero EMQX broker.
3. The generated `DeviceSpec` has accurate commands, properties, and events.
4. A simulated or real device appears online in the device list.
5. A natural-language control request sends a command to the selected device.
6. The device publishes a command response with the same `requestId`.
7. State changes appear in the current state panel.
8. Device-originated events appear in recent events.
9. If A2A is enabled, the card appears in the A2A Marketplace or EMQX A2A registry.
10. Another agent can call the Device Agent through MQTT v5 `SendMessage` and receive a reply.

#### Troubleshooting

- **Device Agent cannot call DeepSeek**: check `LLM_PROVIDER=deepseek`, `LLM_MODEL`, and `LLM_API_KEY`. In the console, verify **Settings -> Models**.
- **Model not found**: use current model IDs such as `deepseek-v4-pro` or `deepseek-v4-flash`.
- **MQTT connection fails**: check broker URL, WebSocket URL, credentials, TLS settings, and whether the browser can reach `VITE_MQTT_WS_URL`.
- **Device does not appear**: publish an online status or state report, then verify `productId`, `deviceId`, topic templates, and `metadata.productId`.
- **Command reaches the device but state does not update**: publish the latest status or state after the command response.
- **A2A card is missing**: confirm that A2A is enabled, the `DeviceSpec` has commands, EMQX A2A registry is enabled, and `VITE_FF_A2A_MARKETPLACE_ENABLE=true` is configured when using the web marketplace.

#### Resources

- [Device Agent Website](https://www.emqx.com/en/device-agent)
- [Device Agent Docs](https://docs.emqx.com/en/device-agent/latest/)
