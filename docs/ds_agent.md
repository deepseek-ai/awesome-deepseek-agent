[English](./ds_agent.md) | [简体中文](./ds_agent.zh-CN.md) · [← Back](../README.md)

# Use DeepSeek with DS Agent

DS Agent is an open-source, DeepSeek-first local Windows work agent. It combines
chat with durable memory, scheduled automation, permissioned local tools,
verified computer use, reusable Skills, and auditable run evidence.

- **GitHub:** <https://github.com/Lee-take/dsagent>
- **Stable release:** <https://github.com/Lee-take/dsagent/releases/latest>
- **Platform:** Windows x64

![A real DS Agent run turning meeting notes into a team execution checklist](./assets/ds-agent-office-workflow.png)

#### 1. Get your own DeepSeek API key

Create an API key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
A user-supplied valid key is required: DS Agent does not bundle a shared key or
bypass DeepSeek access requirements. Your use remains subject to DeepSeek's
terms and account policies.

#### 2. Install DS Agent

Download `DS.Agent_1.0.1_x64-setup.exe` from the
[v1.0.1 release](https://github.com/Lee-take/dsagent/releases/tag/v1.0.1).

The v1.0.1 installer is currently unsigned, so Windows may show an
unknown-publisher warning. Before running it, verify the published SHA-256:

```powershell
Get-FileHash .\DS.Agent_1.0.1_x64-setup.exe -Algorithm SHA256
```

Expected value:

```text
469C4EFA54F4C94A6E37D28C9C88D331B26E1770C6792DC93D02B451640E2A6F
```

The installer includes the WebView2 bootstrapper. Users of the installed app do
not need Node.js, Rust, pnpm, or a source checkout.

#### 3. Configure the API key and workspace

For a persistent Windows user environment variable, run:

```powershell
[Environment]::SetEnvironmentVariable("DEEPSEEK_API_KEY", "your-key-here", "User")
```

Restart DS Agent after setting the variable. Alternatively, enter the key in
**Settings → DeepSeek API key** for the current app session; the session value is
kept in memory and is not written to source or local files.

On first run, choose one local workspace. DS Agent maintains approved evidence,
exports, reports, run records, work packages, memory, and logs under that root.

#### 4. Select the DeepSeek model and reasoning level

In **Settings**, choose a model route and thinking level:

| Setting | DS Agent behavior |
|---|---|
| `Auto` | Uses `deepseek-v4-pro` for Auto, Standard, and Deep thinking; Fast uses `deepseek-v4-flash`. |
| `Pro` | Uses `deepseek-v4-pro`. |
| `Flash` | Uses `deepseek-v4-flash`. |
| `Standard` thinking | Sends `reasoning_effort: high`. |
| `Deep` thinking | Sends `reasoning_effort: max`. |

DeepSeek V4 models support up to a 1M-token context window. DS Agent v1.0.1 does
not expose a manual context-window field; it assembles bounded task context,
selected memory, and evidence automatically.

#### 5. Run a first office task

Try this in the main chat:

```text
Turn these meeting notes into a team execution checklist with item, owner,
deadline, acceptance criteria, and risk. Do not write files or use external
accounts.

1. Operations: classify first-half customer complaints by July 18 and mark repeats.
2. Finance: explain items more than 10% over budget by July 19.
3. HR: submit new-hire training covering information security and service standards by July 20.
```

DS Agent shows the selected DeepSeek model in the answer and displays the run
steps in the right rail. When a task proposes local or external actions, DS Agent
validates workspace boundaries, permissions, risk, and confirmation requirements
before execution. In v1.0.1, if one task needs several permissions, the UI shows
one task-level Confirm and run / Reject decision while the Kernel preserves each
capability decision in the audit trail.

More examples and troubleshooting are available in the project's
[installation guide](https://github.com/Lee-take/dsagent/blob/main/docs/INSTALLATION.md).
