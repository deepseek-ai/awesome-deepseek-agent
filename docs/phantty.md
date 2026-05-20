[English](./phantty.md) | [简体中文](./phantty.zh-CN.md) · [← Back](../README.md)

# Integrate with Phantty

Phantty is a Windows terminal emulator written in Zig, built on Ghostty's VT parser, with built-in DeepSeek-first AI Agent sessions. It can run local PowerShell/cmd commands, work with WSL and SSH terminals, load local skills, and keep the agent inside the terminal workflow.

- **GitHub:** <https://github.com/xuzhougeng/phantty>

#### 1. Install Phantty

Phantty is Windows-only. Download a portable release from:

```text
https://github.com/xuzhougeng/phantty/releases
```

Choose one of the Windows portable zip assets:

| Asset | Use case |
|---|---|
| `phantty-windows-portable-webview2-vX.Y.Z.zip` | Recommended if you want the embedded browser panel. |
| `phantty-windows-portable-no-webview-vX.Y.Z.zip` | Use when WebView2 is not available or should be disabled. |
| `phantty-windows-portable-vX.Y.Z.zip` | General portable build. |

Extract the zip and run:

```powershell
.\phantty.exe
```

#### 2. Get a DeepSeek API Key

Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

Phantty can store the key in its AI profile, or read it from the `DEEPSEEK_API_KEY` environment variable when the profile's base URL points to DeepSeek:

```powershell
$env:DEEPSEEK_API_KEY = "sk-your-deepseek-api-key"

# Optional: persist for future PowerShell sessions
[Environment]::SetEnvironmentVariable("DEEPSEEK_API_KEY", "sk-your-deepseek-api-key", "User")
```

#### 3. Open and Configure the AI Agent

Start Phantty, then press `Ctrl+Shift+T` and choose `AI Agent`.

If no AI profile exists yet, Phantty opens the AI settings form first. Use:

| Field | Value |
|---|---|
| Profile name | `DeepSeek` |
| Base URL | `https://api.deepseek.com` |
| API key | Your DeepSeek API key, or leave empty when `DEEPSEEK_API_KEY` is set |
| Model | `deepseek-v4-pro` |
| Thinking | `enabled` |
| Effort | `max` |
| Stream | `false` |
| Agent | `true` |

You can also use `deepseek-v4-flash` for a faster, lighter agent profile.

DeepSeek V4 models support up to 1 million tokens of context. Phantty does not require a separate `context_window` setting; it sends OpenAI-compatible Chat Completions requests directly to DeepSeek and relies on the selected DeepSeek V4 model's context window.

#### 4. First Run

After saving the profile, Phantty opens an Agent tab. Try:

```text
Inspect this repository and summarize the build and test commands.
```

When the agent requests a tool command, Phantty shows an approval prompt unless you have configured full agent permission. This keeps local PowerShell/cmd, WSL, and SSH tool execution explicit.

#### Useful Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+Shift+T` | Open the session launcher |
| `Ctrl+Shift+P` | Open the command center |
| `Ctrl+Shift+Alt+E` | Toggle the left file explorer / agent history panel |
| `Esc` | Dismiss overlays or interrupt relevant UI flows |

#### Agent Skills and Local Commands

Phantty discovers local skills from:

- `%APPDATA%\phantty\skills\<skill-name>\SKILL.md`
- `.\skills\<skill-name>\SKILL.md` in the current working directory
- `skills\<skill-name>\SKILL.md` next to `phantty.exe`

Use `$skill-name your request` to load a skill for the next agent request.

Local slash commands inside the AI Agent tab:

| Command | Action |
|---|---|
| `/skills` | List discovered local skills |
| `/commands` | List local AI chat commands |
| `/reload-skills` | Reload skills from disk for future skill calls |

#### Troubleshooting

- `Missing API key`: set `DEEPSEEK_API_KEY`, or save the key in the AI profile.
- `401` or authentication errors: check the API key and base URL.
- `402` or payment errors: check your DeepSeek Platform balance.
- No tool execution: keep `Agent = true`, and approve tool prompts when permission mode is `confirm`.
- Avoid legacy DeepSeek V3 model names; use `deepseek-v4-pro` or `deepseek-v4-flash`.

#### Resources

- [Phantty](https://github.com/xuzhougeng/phantty)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
- [DeepSeek Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode)
