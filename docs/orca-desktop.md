[English](./orca-desktop.md) | [简体中文](./orca-desktop.zh-CN.md) · [Back](../README.md)

# Integrate with O.R.C.A. Desktop

[O.R.C.A.](https://github.com/nanbo0ne/O.R.C.A-for-Windows) (Open Reasoning & Computing Agent) is an open-source desktop assistant and coding workspace built with Go and Wails. It supports DeepSeek conversations, project files, tool calls, subagents, MCP, and Skills, with Modern and Classic interfaces.

This guide covers desktop release **3.0.13**. This is the `nanbo0ne/O.R.C.A-for-Windows` project, distinct from the Rust terminal agent named Orca at `echoVic/blade-deepseek`.

## 1. Install

Download the package for your platform from the [3.0.13 release](https://github.com/nanbo0ne/O.R.C.A-for-Windows/releases/tag/desktop-v3.0.13):

- Windows x64: installer or portable ZIP. Extract the ZIP before launching `Orca.exe`; WebView2 is required.
- macOS 12 or later: Universal DMG for Intel and Apple Silicon.
- Linux x64: DEB for Debian/Ubuntu, with the required GTK/WebKitGTK runtime.

Check the release checksums and installation notes. Windows packages lack Authenticode signing and macOS packages are not notarized; update signatures are separate from operating-system publisher signing.

## 2. Connect DeepSeek

1. Obtain an API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).
2. Launch O.R.C.A. On first run, enter the key in the **DEEPSEEK_API_KEY** field and submit it for validation. No shell environment variable is required for this desktop flow.
3. The built-in provider connects directly to `https://api.deepseek.com`. New installations select **DeepSeek V4.1 Flash**, whose API model ID is `deepseek-flash` and whose O.R.C.A. reference is `deepseek/deepseek-flash`.
4. If setup was skipped, open the model/provider settings and configure the built-in DeepSeek provider there. Skipping setup does not supply a free API key.

Keep the key in the credential field, not a chat message or project file. API use is billed by DeepSeek.

## 3. Choose model and effort

Use the model selector beside the message input:

| Model | API ID | O.R.C.A. reference | Images |
| --- | --- | --- | --- |
| DeepSeek V4.1 Flash | `deepseek-flash` | `deepseek/deepseek-flash` | Supported |
| DeepSeek V4 Pro | `deepseek-v4-pro` | `deepseek/deepseek-v4-pro` | Text only |

The release supports a **1M-token context window** for these official models. Actual usable context also includes instructions and tool results. The model's maximum output allowance is not the application's per-request default.

Select **max** in the effort selector for maximum reasoning effort, or choose **low**, **high**, or **auto** as appropriate. For the built-in DeepSeek configuration, auto uses high. The Compact/Detailed display control changes reasoning visibility, not effort.

The older `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` IDs are compatibility aliases, not additional models to add. Check the [official model catalog](https://api-docs.deepseek.com/quick_start/pricing/) and [thinking-mode documentation](https://api-docs.deepseek.com/guides/thinking_mode/) for current service availability and behavior.

## 4. First run

Create a session and send:

> Explain the difference between a process and a thread in three short points.

For a coding task, open a disposable project directory, choose Coding mode, and keep the permission mode on Ask:

> List the files in this project and explain its entry point. Do not modify files or install dependencies.

Review any requested tool approval. A text answer checks the conversation path; inspecting the actual tool result checks tool execution. Subagents, MCP servers, and Skills can be configured later and are not required for this first task.

For vision, select Flash, attach a synthetic image you are willing to send to DeepSeek, and ask it to transcribe the visible text. Image processing sends the image to the configured provider and remains subject to attachment permissions. Pro cannot accept images.

## Troubleshooting and scope

- Authentication or insufficient balance: check the key and billing on the DeepSeek Platform. Do not paste credentials into an issue.
- Model unavailable: verify the selected provider and exact API model ID. A custom proxy can expose different models; matching display names do not establish compatibility.
- Reasoning/tool protocol errors: use an up-to-date release and report the version and sanitized error. Do not disable reasoning as a general workaround.
- Tool approval denied: inspect the requested action and workspace. Full access is not required for setup.
- Managed local AI and whole-desktop Computer Use remain disabled in 3.0.13. This guide does not cover the unreleased embedded-browser preview.

See the project's [English documentation](https://github.com/nanbo0ne/O.R.C.A-for-Windows/blob/desktop-v3.0.13/README.en.md) for configuration, platform requirements, and limitations.
