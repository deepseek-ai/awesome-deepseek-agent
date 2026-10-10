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
| **XiaoYi Open Platform credentials** | An OpenClaw-mode agent, giving you `AK` / `SK` / `agentId`. See "Getting the XiaoYi credentials" below. |

> Only the first two are needed to run DSH itself; the last one is what makes the phone work.

### Getting the XiaoYi credentials

**These are issued by Huawei. The plugin cannot create them for you.** You have to apply for them yourself:

1. Register a **Huawei developer account** and complete **real-name verification** — <https://developer.huawei.com/consumer/cn/register/>
2. Sign in to the **XiaoYi Open Platform** and create an agent — <https://developer.huawei.com/consumer/cn/hag/hagindex.html#/>
   When creating it, choose the **OpenClaw mode**. Other modes are not compatible with this plugin.
3. Take the values from the agent's detail page:
   - `agentId` — shown in the **AgentCard** block;
   - `AK` / `SK` — under **Credentials → New credential**. **The SK is displayed only once**, so copy it immediately.
4. Add your own Huawei account to the agent's **test whitelist**. Until the agent is published, only whitelisted accounts can reach it; it takes effect after a few minutes.
5. Official documentation for this mode — <https://developer.huawei.com/consumer/cn/doc/doccenter-celia/openclaw-0000002518410344>

> Menu names, entry points and the review process are decided entirely by Huawei and may change at any time. If a step above no longer matches what you see, follow Huawei's own documentation rather than this guide.

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
  "cwd": "C:\\Users\\<you>\\Desktop",
  "publicBaseUrl": "",
  "imageHost": ""
}
```

You can also let the agent do it at runtime with the `xiaoyi_set` tool.

The plugin connects to Huawei Cloud over a WebSocket, authenticating with `AK`/`SK` and sending a heartbeat every 30 seconds.

## Step 4 — First run

1. Cold-start the DSH host.
2. Check the channel with the `xiaoyi_status` tool — it should report `ready: true` and `connected: true`.
3. Say something to XiaoYi on your phone.
4. The message is delivered into a DSH session named `xiaoyi-listen-*`, the agent answers, and the reply is sent back to the XiaoYi conversation.

---

## What can travel in each direction

This is worth knowing before you plan a workflow around it.

| Direction | Support |
| --- | --- |
| **Phone → DSH** (what you send to XiaoYi) | **Text, voice (transcribed) and images/files all work.** Attachments are downloaded to `~/.dsh/xiaoyi/media/` and their local paths are handed to the agent. |
| **DSH → phone** (what you get back in XiaoYi) | **Text works** — the reply body, plus anything sent with `xiaoyi_send`. **Pushing an image or file back to the phone is unreliable**: the protocol accepts only a public https URL, and the XiaoYi client is not guaranteed to render the file part. |

In short: **the inbound direction is the reliable one.**

## Security notes

- **Credentials stay on your machine.** They live in `~/.dsh/xiaoyi/state.json` and are never uploaded by the plugin. Because they sit in plain text, do not commit that file or put it in a synced folder.
- **Inbound attachments are SSRF-hardened.** The `uri` on an attachment arrives from an external message, so it is treated as untrusted: only `http`/`https` is allowed, every redirect hop is checked **before it is fetched**, and a host is rejected both structurally and by **what it actually resolves to** (so `127.0.0.1.nip.io` is refused like `127.0.0.1`). Loopback, private, link-local, unique-local, multicast, site-local, IPv4-mapped, NAT64, 6to4 and Teredo ranges are all blocked, including cloud metadata endpoints such as `169.254.169.254`.
- **Downloads are size-capped** at 50 MB per file and streamed, so a lying `Content-Length` cannot exhaust memory.
- **The plugin's own HTTP routes have no authentication.** Do not expose the DSH port directly to the internet; if you use a tunnel, prefer one with its own auth.

---

## Tips

- **Reasoning effort** — for hard tasks set the effort to `max`. For quick everyday questions, `high` is usually enough and noticeably cheaper.
- **Long context** — DeepSeek V4 handles up to 1M tokens, so you can hand the session large files and long logs.
- **Session reuse** — the plugin resumes the same `xiaoyi-listen-*` session across restarts, so the conversation history stays in one place.
- **Photos** — images you send from XiaoYi are downloaded locally and handed to the agent, which can read them directly.
- **Sending files back** — the protocol only accepts public https URLs for outbound files, and whether the client renders them is outside the plugin's control. Either run a tunnel and set `publicBaseUrl`, or explicitly opt into a third-party host — but treat this direction as experimental.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| `xiaoyi_status` reports `ready: false` | One of AK / SK / agentId is missing. |
| Never connects | `wsUrl` is correct, and the machine can reach `hag.cloud.huawei.com:443`. |
| Keeps reconnecting | Look for "stale connection" in `~/.dsh/xiaoyi/xiaoyi.log`. |
| No reply from XiaoYi | Confirm the plugin loaded in the DSH host log and inspect `~/.dsh/xiaoyi/xiaoyi.log`. |
| Images sent back never arrive | Expected — that direction is unreliable by design. See "What can travel in each direction". |
| Messages need the instance to be awake | The machine running DSH must be on and online for the phone to reach it. |

## Links

- Plugin repository: <https://github.com/HangZhouXi/dsh-xiaoyi>
- DeepSeek Platform: <https://platform.deepseek.com/>
- DeepSeek API docs: <https://api-docs.deepseek.com/>
- DSH: <https://deepseek.com/harness>
- XiaoYi Open Platform (OpenClaw mode): <https://developer.huawei.com/consumer/cn/doc/doccenter-celia/openclaw-0000002518410344>
