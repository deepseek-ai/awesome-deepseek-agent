[English](./ontheia.md) · [← Back](../README.md)

# Integrate with Ontheia

[Ontheia](https://ontheia.ai) is an open-source, self-hosted AI agent platform.
It supports multiple AI providers, MCP tool servers, chain-based workflow automation,
and long-term vector memory — all running on your own infrastructure.

#### 1. Install Ontheia

Run the guided install script — it handles environment setup, secret generation, database migrations, and admin account creation:

```bash
git clone https://github.com/Ontheia/ontheia.git
cd ontheia
bash scripts/install.sh
```

Then open the Ontheia Web UI:

```
http://localhost:5173
```

See the [full installation guide](https://docs.ontheia.ai/en/getting-started/installation) for requirements and manual setup options.

#### 2. Add DeepSeek as a Provider

In the Ontheia Web UI, open **Settings → AI Models**.

Click **+ Add Provider**, then:

- **Provider type:** OpenAI-compatible
- **Name:** DeepSeek
- **Base URL:** `https://api.deepseek.com`
- **API Key:** your [DeepSeek API key](https://platform.deepseek.com/api_keys)

Save the configuration.

#### 3. Select a DeepSeek Model

Still in **Settings → AI Models**, click **+ Add Model** and enter one of the following model IDs:

| Model | Description |
|-------|-------------|
| `deepseek-chat` | DeepSeek-V4 — fast, cost-efficient general model |
| `deepseek-reasoner` | DeepSeek-R1 — extended reasoning for complex tasks |

Save, then set the model as default or assign it to a specific agent.

#### 4. Get Started

Open the **Chat** view and start a conversation — Ontheia will route your messages
through the DeepSeek model you configured.

To use DeepSeek in an automated workflow, open the **Chain Engine**, create a new chain,
and select your DeepSeek model as the model for any agent step.
