[English](./cline_cli.md) | [简体中文](./cline_cli.zh-CN.md) · [← Back](../README.md)

# Integrate with Cline CLI

Cline CLI is the command-line version of Cline, an AI coding assistant that can read and edit files, run shell commands, and work from your terminal.

#### 1. Install Cline CLI

- Install [Node.js](https://nodejs.org/en/download/) 20+.
- Run the following command in your terminal to install Cline CLI:

```
npm install -g cline
```

- After installation, run the following command. If the version number is displayed, the installation is successful:

```
cline version
```

#### 2. Start the Authentication Wizard

Run the Cline authentication wizard:

```
cline auth
```

When the welcome screen appears, select **Use your own API key**.

This option is also called **Bring your own API key** in Cline documentation. It means Cline will use your DeepSeek API key directly, so DeepSeek handles model billing and rate limits for your requests.

#### 3. Select DeepSeek as the Provider

In the provider picker, select **DeepSeek**.

If you prefer non-interactive setup, Cline also exposes DeepSeek as the `deepseek` provider id.

#### 4. Enter Your DeepSeek API Key

Paste your [DeepSeek API Key](https://platform.deepseek.com/api_keys) when prompted.

Keep this key private. An API key is a credential that lets Cline call DeepSeek on your behalf, similar to a password for programmatic access.

#### 5. Select a Model

Choose one of the available DeepSeek models:

- `deepseek-chat` — general coding and chat tasks.
- `deepseek-reasoner` — reasoning-heavy tasks where step-by-step problem solving is useful.

After selecting a model, authentication is complete.

#### 6. Start Cline

```
cd /path/to/my-project
cline
```

#### Optional: Configure DeepSeek with Flags

The wizard path above is the easiest way to configure DeepSeek. For scripted setup, you can also skip the wizard and pass the DeepSeek provider, API key, and model directly:

```
cline auth -p deepseek -k <your DeepSeek API Key> -m deepseek-chat
```

Use `deepseek-reasoner` instead of `deepseek-chat` if you want the reasoning model.
