[English](./deepcode.md) | [简体中文](./deepcode.zh-CN.md) · [← Back](../README.md)

# Integrate with Deep Code

Deep Code is an open-source terminal AI coding assistant for the DeepSeek-V4 model, supporting deep thinking, reasoning effort control, and Agent Skills.

- **GitHub:** <https://github.com/lessweb/deepcode-cli>

#### 1. Install Deep Code

- Install [Node.js](https://nodejs.org/en/download/) 18+.
- Run the following command in your terminal:

```sh
npm install -g @vegamo/deepcode-cli
```

- Verify the installation:

```sh
deepcode --version
```

#### 2. Configure Deep Code

Create `~/.deepcode/settings.json` with your DeepSeek API key and model settings:

```json
{
  "env": {
    "MODEL": "deepseek-flash",
    "BASE_URL": "https://api.deepseek.com",
    "API_KEY": "sk-..."
  },
  "thinkingEnabled": true,
  "reasoningEffort": "max"
}
```

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

> **Note:** The same settings file is shared with the [Deep Code VSCode extension](https://github.com/lessweb/deepcode).

**Configuration options:**

| Option | Description |
|--------|-------------|
| `MODEL` | Model name, e.g. `deepseek-flash` |
| `BASE_URL` | API base URL, defaults to `https://api.deepseek.com` |
| `thinkingEnabled` | Enable deep thinking mode (defaults to `true` for deepseek-v4 models) |
| `reasoningEffort` | `"max"` or `"high"` — controls how much reasoning the model performs |
| `notify` | Path to a notification script executed after each model turn |
| `webSearchTool` | Enable the web search capability for the agent |

#### 3. Enter a project directory and launch Deep Code

```sh
cd /path/to/my-project
deepcode
```

#### Key Shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Shift+Enter` | Insert a newline (also `Ctrl+J`) |
| `Ctrl+V` | Paste an image from the clipboard |
| `Esc` | Interrupt the current model turn |
| `/` | Open the skills / commands menu |
| `/new` | Start a fresh conversation |
| `/resume` | Choose a previous conversation to continue |
| `/exit` | Quit Deep Code |

#### Using Agent Skills

Agent Skills are discovered from these locations:

- **User-level:** `~/.agents/skills/<name>/SKILL.md`
- **Project-level:** `./.deepcode/skills/<name>/SKILL.md`

Press `/` to open the skill picker, or type the skill name directly (e.g., `/skill-writer`).
