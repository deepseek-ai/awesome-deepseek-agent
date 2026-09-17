[English](./dsh_openclaw_acp.md) | [简体中文](./dsh_openclaw_acp.zh-CN.md) · [← Back](../README.md)

# Use DeepSeek Harness from OpenClaw and WeChat

[`dsh-openclaw-acp`](https://github.com/BeAChanger/dsh-openclaw-acp) is a native DeepSeek Harness bundle that exposes a Harness profile through the official Agent Client Protocol (ACP) transport. OpenClaw's official ACPX plugin can register that profile as an external agent, so any configured OpenClaw channel—including WeChat—can invoke it.

The integration keeps three responsibilities separate:

- DeepSeek Harness owns the agent, DeepSeek model, tools, workspace sandbox, and session log.
- OpenClaw ACPX owns the ACP process, dispatch, and conversation routing.
- The OpenClaw channel plugin owns WeChat authentication, sender identity, and message delivery.

The bundle does not read or forward WeChat credentials or sender identifiers; those channel facts remain OpenClaw's responsibility.

## 1. Install DeepSeek Harness and the bundle

Prerequisites:

- pnpm 10 and a Node.js release supported by OpenClaw; stable OpenClaw `2026.7.1-2` requires Node.js 22.22.3+, 24.15.0+, or 25.9.0+
- A [DeepSeek API key](https://platform.deepseek.com/api_keys)
- OpenClaw `2026.7.1-2` or newer with a configured channel; for WeChat, see Tencent's [`openclaw-weixin`](https://github.com/Tencent/openclaw-weixin)

Install the current verified Harness release and the bundle:

```bash
npm install -g pnpm@10.28.2 @deepseek-ai/dsh@0.1.0-rc.6
dsh plugin --profile openclaw add https://github.com/BeAChanger/dsh-openclaw-acp/releases/download/v0.1.3/dsh-openclaw-acp-0.1.3.tgz
dsh --profile openclaw --dump-config
```

This uses the prebuilt release artifact (SHA-256 `51ab3d78a7505448b5827b84a79081ae9fd11a5553949eafa3a317b5ee4763fd`), so installation does not execute a repository build. The release also provides a checksum asset.

The config dump should contain both `id: openclaw-acp` and `name: dsh-openclaw-acp`.

Make the API key available to the OpenClaw Gateway process:

```bash
export DEEPSEEK_API_KEY="your-api-key"
```

PowerShell:

```powershell
$env:DEEPSEEK_API_KEY = "your-api-key"
```

If OpenClaw runs as a service, configure the variable in the service environment rather than only in an interactive shell.

## 2. Register Harness in OpenClaw

Install and enable OpenClaw's official ACP runtime:

```bash
openclaw plugins install @openclaw/acpx@2026.7.1
openclaw config set plugins.entries.acpx.enabled true
```

For WeChat, install the Tencent channel version verified with this stack. The final command displays a QR code and requires operator confirmation:

```bash
openclaw plugins install @tencent-weixin/openclaw-weixin@2.4.6
openclaw config set plugins.entries.openclaw-weixin.enabled true
openclaw channels login --channel openclaw-weixin
```

Add the following settings to the OpenClaw config:

```json5
{
  acp: {
    enabled: true,
    backend: "acpx",
    defaultAgent: "deepseek-harness",
    allowedAgents: ["deepseek-harness"]
  },
  plugins: {
    entries: {
      acpx: {
        enabled: true,
        config: {
          agents: {
            "deepseek-harness": {
              command: "dsh",
              args: ["--profile", "openclaw"]
            }
          }
        }
      },
      "openclaw-weixin": {
        enabled: true
      }
    }
  }
}
```

Restart the Gateway after changing the plugin configuration.

## 3. First run

From an OpenClaw conversation, verify the runtime before delegating real work:

```text
/acp doctor
/acp spawn deepseek-harness --cwd /absolute/path/to/workspace
```

For a WeChat channel, send the same commands in the chat connected to that Gateway. The message path is:

```text
WeChat -> OpenClaw channel -> ACPX -> dsh --profile openclaw -> DeepSeek Harness
```

For multiple logged-in WeChat accounts, isolate direct-message sessions by account, channel, and sender:

```bash
openclaw config set session.dmScope per-account-channel-peer
```

If the channel advertises conversation binding, add `--bind here` to keep follow-up messages on the same ACP session. If it does not, use the unbound one-shot command; OpenClaw relays the completed result to the parent conversation.

## DeepSeek V4 configuration

The bundle uses the verified `deepseek-official` Harness adapter and configures:

- model: `deepseek-v4-flash`
- thinking: enabled
- reasoning effort: `max`
- context window: 1,000,000 tokens
- output cap: 384,000 tokens

Select DeepSeek V4 Pro in the Gateway environment when the task needs the stronger model:

```bash
export DSH_OPENCLAW_MODEL=deepseek-v4-pro
```

The model names are passed through by Harness; both `deepseek-v4-flash` and `deepseek-v4-pro` use the same 1M-context and max-reasoning profile.

## Security and current protocol limits

- OpenClaw's sandbox does not wrap an external ACP process. DeepSeek Harness enforces its own boundary through `DSH_PERMISSION_MODE`; keep the default `workspace-write` mode for normal deployments.
- ACPX defaults to read approvals. Write or shell tasks can fail until an operator selects a non-interactive permission policy. Use `approve-all` only with a dedicated OS account and restricted workspace; it is not a safe shared-Gateway default.
- Do not enable OpenClaw's ACPX MCP tool bridges for this target yet. Harness ACP `0.1.0-rc.6` rejects non-empty `mcpServers`.
- Harness ACP currently supports new sessions only; it does not advertise load, resume, fork, or session listing.
- The ACP transport returns committed assistant text, not live reasoning or tool events.
- Persistent chat binding depends on the channel adapter. One-shot parent relay remains available when binding is unsupported.

## Verification evidence

The bundle repository includes unit, package, and real protocol checks. The smoke test installs the packed bundle into an isolated profile, then completes `initialize` and `session/new` twice: first against the published `dsh` CLI directly with JSON-RPC-only stdout, then through a custom-agent registration in the published `acpx@0.11.2` runtime used by OpenClaw's official ACPX plugin:

```bash
git clone https://github.com/BeAChanger/dsh-openclaw-acp.git
cd dsh-openclaw-acp
pnpm install
pnpm test
pnpm run test:acp
pnpm audit --prod --audit-level high --registry https://registry.npmjs.org
```

The protocol smoke does not make a model request, so a real API key is required only for the first live prompt through OpenClaw. In a separate isolated OpenClaw `2026.7.1-2` state, both `@openclaw/acpx@2026.7.1` and `@tencent-weixin/openclaw-weixin@2.4.6` loaded as enabled plugins with all required dependencies installed; the combined custom-agent, channel, and per-account session configuration passed `openclaw config validate`. QR login and live message delivery remain operator-owned checks.

## References

- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Harness plugin packaging](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.md)
- [OpenClaw ACP agents](https://github.com/openclaw/openclaw/blob/main/docs/tools/acp-agents.md)
- [OpenClaw ACPX setup](https://github.com/openclaw/openclaw/blob/main/docs/tools/acp-agents-setup.md)
- [Tencent OpenClaw WeChat channel](https://github.com/Tencent/openclaw-weixin)
