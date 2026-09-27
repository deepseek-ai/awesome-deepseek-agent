[English](./pi_mono.md) | [简体中文](./pi_mono.zh-CN.md) · [← Back](../README.md)

# Integrate with Pi

Pi is a minimal, aggressively extensible terminal coding harness. It adapts to your workflows through TypeScript extensions, skills, prompt templates, and themes, with tree-structured sessions and built-in DeepSeek support.

#### 1. Install Pi

- Install [Node.js](https://nodejs.org/en/download/) 22.19 or later.
- Run the following command in your terminal to install Pi:

```bash
npm install -g @earendil-works/pi-coding-agent
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```bash
pi --version
```

This guide requires Pi 0.83.0 or later. If `pi --version` shows an older version, upgrade to the latest release:

```bash
npm install -g @earendil-works/pi-coding-agent@latest
```

> **Note:** Linux / macOS users can also install via the official script:
> ```bash
> curl -fsSL https://pi.dev/install.sh | sh
> ```

#### 2. Configure DeepSeek

Pi includes DeepSeek as a built-in provider, so you do not need to create or edit `models.json`. Get your API key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys), then choose one of the following authentication methods.

**Option 1: Environment variable**

Linux / macOS users:

```bash
export DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

Windows users:

```powershell
$env:DEEPSEEK_API_KEY="<your DeepSeek API Key>"
```

**Option 2: Pi login**

Skip the environment variable and use `/login` after starting Pi in the next step. Pi stores the API key in `~/.pi/agent/auth.json` on Linux and macOS, or `%USERPROFILE%\.pi\agent\auth.json` on Windows.

#### 3. Run and Select Model

Enter the project directory and start Pi:

```bash
cd /path/to/my-project
pi
```

On first launch, Pi initializes its `.pi` configuration directory. If you chose **Pi login** above, enter the following command, select **DeepSeek**, and paste your API key:

```text
/login
```

Enter the following command to open the model switcher:

```text
/model
```

Select **deepseek** and choose `deepseek-v4-pro` or `deepseek-v4-flash`.

DeepSeek uses `high` reasoning effort by default. For complex coding and agent tasks, you can open the settings and select `max`:

```text
/settings
```

For general use, keep `high`. Pi's built-in DeepSeek entries already configure the 1M-token context window and 384K maximum output.

For provider authentication and custom model overrides, see the [Pi providers documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/providers.md) and [custom models documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md).
