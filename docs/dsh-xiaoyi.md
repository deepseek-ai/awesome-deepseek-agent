# DeepSeek Harness (DSH) + Huawei XiaoYi

Use **DeepSeek-V4-Pro / DeepSeek-V4-Flash** from your phone by wiring **Huawei XiaoYi** into a **DeepSeek Harness (DSH)** session running on your own machine.

This guide walks through installation, configuration and a first successful run.

---

## What you get

XiaoYi becomes an entry point to a DSH session on your own computer — the same session, tools, working directory and files. There is no second agent and no cloud copy of your project.

```
Huawei XiaoYi (phone)  →  Huawei Cloud OpenClaw channel  →  DSH on your PC  →  DeepSeek-V4
```

Once connected you can talk to, dictate to, or send photos to your DSH session from anywhere, and the replies come back into the XiaoYi conversation.

## Prerequisites

| Requirement | Notes |
| --- | --- |
| **DSH (DeepSeek Harness)** | Installed and working on the machine that will run the agent. |
| **Node.js ≥ 20** | The plugin uses the built-in `fetch` / `FormData` / `Blob`. |
| **A DeepSeek API key** | From the [DeepSeek Platform](https://platform.deepseek.com/). |
| **XiaoYi Open Platform credentials** | An OpenClaw-mode agent, giving you `AK` / `SK` / `agentId`. Apply for these on the Huawei XiaoYi Open Platform. |

> Only the first two are needed to run DSH itself; the last one is what makes the phone work.

---

## Step 1 — Install and configure DSH

Install DSH and point it at DeepSeek with your API key. Confirm it works locally first — for example by starting a session and asking a question.

Set the model to a current DeepSeek V4 model:

- `deepseek-v4-pro` — highest capability
- `deepseek-v4-flash` — fastest and cheapest

DeepSeek V4 models support up to a **1,000,000-token context window**, and `deepseek-v4-pro` supports multiple reasoning-effort levels (`max` and `high`). Turn reasoning effort up for hard problems.

## Step 2 — Install the `dsh-xiaoyi` plugin

The plugin is open source (MIT): <https://github.com/HangZhouXi/dsh-xiaoyi>

```bash
dsh plugin --profile web add git+https://github.com/HangZhouXi/dsh-xiaoyi
dsh plugin --profile web install
```

Then **cold-start the DSH host**. Host-side plugins are not applied by hot reload — a cold start is required.

## Step 3 — Add your XiaoYi credentials

Create or edit `~/.dsh/xiaoyi/state.json`:

```json
{
  "enabled": true,
  "ak": "your AK",
  "sk": "your SK",
  "agentId": "your OpenClaw-mode agentId",
  "wsUrl": "wss://hag.cloud.huawei.com/openclaw/v1/ws/link",
  "sessionId": "",
  "cwd": "C:\\Users\\<you>\\Desktop"
}
```

You can also let the agent do it at runtime with the `xiaoyi_set` tool.

The plugin connects to Huawei Cloud over a WebSocket, authenticating with `AK`/`SK` and sending a heartbeat every 30 seconds.

## Step 4 — First run

1. Cold-start the DSH host.
2. Check the channel with the `xiaoyi_status` tool — it should report `ready: true` and `connected: true`.
3. Say something to XiaoYi on your phone.
4. The message is delivered into a DSH session named `xiaoyi-listen-*`, the agent answers, and the reply is sent back to the XiaoYi conversation.

## Tips

- **Reasoning effort** — for hard tasks set the effort to `max`. For quick everyday questions, `high` is usually enough and noticeably cheaper.
- **Long context** — DeepSeek V4 handles up to 1M tokens, so you can hand the session large files and long logs.
- **Session reuse** — the plugin resumes the same `xiaoyi-listen-*` session across restarts, so the conversation history stays in one place.
- **Photos** — images you send from XiaoYi are downloaded locally and handed to the agent, which can read them directly.
- **Sending files back** — the XiaoYi protocol only accepts public https URLs for outbound files. Either run a tunnel and set `publicBaseUrl`, or explicitly opt into a third-party host.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `xiaoyi_status` reports `ready: false` | One of AK / SK / agentId is missing. |
| Never connects | `wsUrl` is correct, and the machine can reach `hag.cloud.huawei.com:443`. |
| Keeps reconnecting | Look for "stale connection" in `~/.dsh/xiaoyi/xiaoyi.log`. |
| No reply from XiaoYi | Confirm the plugin loaded in the DSH host log and inspect `~/.dsh/xiaoyi/xiaoyi.log`. |
| Messages need the instance to be awake | The machine running DSH must be on and online for the phone to reach it. |

## Links

- Plugin repository: <https://github.com/HangZhouXi/dsh-xiaoyi>
- DeepSeek Platform: <https://platform.deepseek.com/>
- DeepSeek API docs: <https://api-docs.deepseek.com/>
- DSH: <https://deepseek.com/harness>
