# Harness Desktop

[Harness Desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) is a community Windows desktop app for the official DeepSeek Harness Web workspace. It provides a Chinese installer and a portable build, starts Harness locally, and adds quick themes, an in-app plugin marketplace, and desktop updates.

> Harness Desktop is a community project, not an official DeepSeek application.

## Install

1. Open the [Releases page](https://github.com/baiyuscc13724-max/deepseek-harness-desktop/releases).
2. Download the Windows installer, or choose the portable build if you do not want to install it.
3. Start Harness Desktop. The official Harness workspace opens directly.

The Releases link always points to the latest available desktop builds, so this guide does not depend on a specific version.

## Configure a DeepSeek model

1. Open **Settings** in the lower-left corner.
2. Open **Models**.
3. Choose an existing DeepSeek provider, or use the official **Add model** entry to add one.
4. Enter your DeepSeek API key in the official model settings and choose **DeepSeek-V4-Pro** or **DeepSeek-V4-Flash**.
5. Save the model, then select it as the main model.

DeepSeek V4 supports up to a 1M-token context window. Use V4-Pro for stronger results or V4-Flash for faster responses.

Harness Desktop does not bundle your API key and does not keep a second provider configuration outside the official Harness settings.

## First run

1. Add or choose a workspace.
2. Start a new session.
3. Enter a small task, such as: `Summarize this repository and suggest the first improvement.`
4. Review the permission level before sending.

## Optional desktop features

- Click the palette icon in the top bar to switch themes without opening the full settings dialog.
- Open **Settings → DSH Plugin Marketplace** to browse, install, and update community plugins.
- In **Settings → Models**, the main model and subagent model can be selected separately. If no subagent model is configured, it follows the main model.
- Desktop updates are checked in the background. Downloaded installers are verified before launch.

Community plugins execute third-party code. Check the source and license before installing a plugin.

## Links

- [Harness Desktop repository](https://github.com/baiyuscc13724-max/deepseek-harness-desktop)
- [Windows downloads](https://github.com/baiyuscc13724-max/deepseek-harness-desktop/releases)
- [Official DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)