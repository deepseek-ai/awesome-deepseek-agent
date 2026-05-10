# Integrating with SolonCode

SolonCode is an open-source coding agent built on Java that runs as a terminal CLI, helping developers accomplish a wide range of software engineering tasks — including code writing, project analysis, refactoring suggestions, test generation, and documentation authoring.

## Installing SolonCode from Scratch

### 1. System Requirements

- **Java 8+** (supports Java 8 through Java 26; must be pre-installed)
- macOS, Linux, or Windows

### 2. Install SolonCode

**Mac / Linux:**

```bash
curl -fsSL https://solon.noear.org/soloncode/setup.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://solon.noear.org/soloncode/setup.ps1 | iex
```

After installation, run the following command to verify. If a version number is displayed, the installation was successful:

```bash
soloncode --version
```

### 3. Configure the DeepSeek Model

Once installed, you need to edit the configuration file `~/.soloncode/config.yml`. You can obtain your API Key from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys).

Open `~/.soloncode/config.yml`, locate the `models` section, and fill in the DeepSeek API details:

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<your DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
```

> **Note:**
> - `apiUrl` can be a full endpoint URL (or an OpenAI-compatible baseUrl).

### 4. Start Using

Once configured, navigate to your project directory and run the `soloncode` command to get started:

```bash
cd /path/to/my-project
soloncode

# Or launch with the web-based interactive UI
soloncode web 0
```

## Switching to DeepSeek from an Existing Installation

If you already have SolonCode installed and are using another model provider (e.g., OpenAI, Qwen), simply update the `models` section in `~/.soloncode/config.yml` to switch to DeepSeek:

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<your DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
```

Restart SolonCode for the changes to take effect.

## Multi-Model Configuration

SolonCode supports configuring multiple models simultaneously. The first entry is used as the default model, and you can freely switch between models at runtime:

```yaml
soloncode:
  models:
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<your DeepSeek API Key>"
      model: "deepseek-v4-flash"
      timeout: "180s"
    - apiUrl: "https://api.deepseek.com"
      apiKey: "<your DeepSeek API Key>"
      model: "deepseek-v4-pro"
      timeout: "180s"
```
