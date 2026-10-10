[English](./deepseek_harness_android.md) | [简体中文](./deepseek_harness_android.zh-CN.md) · [← Back](../README.md)

# DeepSeek Harness for Android

[DeepSeek Harness for Android](https://github.com/guzhou079-arch/deepseek-harness-android) packages the DeepSeek Harness agent runtime into an installable Android APK — no Termux, no root, no computer. The terminal, file access and command execution run inside the app, 21 skills ship with it, and it can even compile, package and sign its own APK on the device.

#### 1. Install

Requirements: Android 7.0 (API 24) or newer — Android 11+ for screenshot and virtual-display features; about 0.6 GB of app data after the first launch; a network connection (model calls are remote).

1. Download the latest `DeepSeekHarness-vX.Y-dist.apk` from [Releases](https://github.com/guzhou079-arch/deepseek-harness-android/releases). Each release lists the APK's SHA-256, so you can verify the download.
2. Open the APK and allow "install unknown apps" when Android asks.
3. Open the app. The first launch extracts the bundled runtime (a few hundred MB; 1–3 minutes depending on the device).
4. Grant only the permissions you want — accessibility (screen reading, taps, screenshots), notifications, overlay. Chat on its own needs nothing but the network.

#### 2. Configure DeepSeek

The app registers DeepSeek's official provider as `provider: deepseek-official`, composed with one of two authentication plugins — an API key, or a DeepSeek account login.

**Option A — API key (recommended)**

1. Create a key at [platform.deepseek.com](https://platform.deepseek.com/).
2. In the app, open the settings page and the model/account card, then paste the key.

The key is stored as a credential reference (`apiKeyEnv: DEEPSEEK_API_KEY` for the `dsh-llm-deepseek` adapter) and resolved per request; error messages name the reference, never the key.

**Option B — account login**

Sign in with your DeepSeek account in the same card, which composes the account variant of the provider instead.

**Models**

| Model | Input | Context window |
| --- | --- | --- |
| `deepseek-flash` | text + images | 1,000,000 tokens |
| `deepseek-v4-pro` | text | 1,000,000 tokens |

These are the default catalog entries the adapter advertises; the model id is passed through to the wire, so a newer DeepSeek model can be used without re-registering anything. The default base URL is `https://api.deepseek.com/anthropic` and can be overridden with `baseURL` or `$DEEPSEEK_BASE_URL` — useful if you route through a gateway. The default per-request output cap is 256,000 tokens and the context fallback is 1,000,000.

**Reasoning effort**

`off`, `low`, `high` and `max` are advertised. `low`, `high` and `max` enable thinking and are sent as `output_config.effort`; `off` sends `thinking.type: disabled`. Pick the level in the model selector, or set `reasoningEffort` in the provider config.

#### 3. First run

- Send a message and the agent streams its answer; shell commands, file reads and web fetches appear as tool cards you can inspect.
- For phone automation, grant the accessibility service and — optionally — start Shizuku, which the app uses for a privileged shell. Automation can run apps on a **virtual display**, so it does not take over the screen you are using.
- Optional: **Settings → Build environment** downloads a ~190 MB toolchain (proot + Alpine + OpenJDK 17) that lets the app compile, package and sign APKs on the phone.

#### 4. Troubleshooting

| Symptom | What it means |
| --- | --- |
| `MISSING_CREDENTIAL` | No API key is configured for the provider — add one as in step 2. |
| `INVALID_CREDENTIAL` / `AUTH` | The key is wrong or revoked; the message names the credential reference to fix. |
| `CONTEXT_WINDOW_EXCEEDED` | The conversation exceeded the model's context; start a new session or let compaction run. |
| `RATE_LIMIT` / `QUOTA` | Provider-side limits — retry later or check your DeepSeek account balance. |
| First launch spins for minutes | The runtime is still being extracted. If it keeps failing, retry from the in-app console. |
| `INSTALL_FAILED_UPDATE_INCOMPATIBLE` on update | The installed app was signed by a different key. Back up inside the app first and do **not** just uninstall — that wipes app-private data. |
