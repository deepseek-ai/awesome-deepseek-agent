[English](./nanobot.md) | [简体中文](./nanobot.zh-CN.md)

# Integrating nanobot

nanobot is a lightweight AI agent that supports integration with popular chat tools.

#### 1. Install nanobot

- Install [uv](https://github.com/astral-sh/uv)
- Run the following command to install nanobot:

```
uv tool install nanobot-ai
```

- Note: On Windows, add the `.local/bin` directory under your user home directory to the environment variables:

```powershell
$env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
```

- Or update the terminal via `uv`:

```powershell
uv tool update-shell
```

- After installation, run the following command. If a version number is displayed, the installation was successful:

```
nanobot --version
```

#### 2. Configure nanobot

Run the following command to initialize the nanobot configuration file:

```
nanobot onboard
```

The configuration file path varies by operating system:

- **Windows**: `$env:USERPROFILE\.nanobot\config.json`
- **Linux / macOS**: `~/.nanobot/config.json`

Edit the `config.json` file and modify the following configuration items:

```json
{
    "agents": {
        "defaults": {
            "model": "deepseek-v4-pro",
            "provider": "deepseek",
        }
    },
    "providers": {
        "deepseek": {
            "apiKey": "<your DeepSeek API Key>",
            "apiBase": "https://api.deepseek.com/v1",
        },
    },
}
```

#### 3. Get Started

Run in the terminal:

```
nanobot agent
```
