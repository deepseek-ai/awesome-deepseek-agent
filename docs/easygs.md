[English](./easygs.md) | [简体中文](./easygs.zh-CN.md) · [← Back](../README.md)

# Integrate with EasyGS

For researchers without a computer science background, EasyGS gives a practical answer to what LLM agents can do for bioinformatics: it helps check files, complete parameters, run curated crop genomic selection workflows, and organize results. EasyGS is a natural-language-driven AI agent for crop genomic selection analysis, supports DeepSeek models, and can run GS workflows through a Web UI, command line, or messaging channels.

- **GitHub:** <https://github.com/lukegood/EasyGS>

#### 1. Install EasyGS

EasyGS requires Python 3.11 or newer, conda or mamba, and a DeepSeek API Key.

Install the released wheel:

```
pip install https://github.com/lukegood/EasyGS/releases/download/v0.1.5/easygs-0.1.5-py3-none-any.whl
```

Check the installation:

```
easygs --version
```

For GS analysis tools, create the conda environments from the source repository:

```
git clone https://github.com/lukegood/EasyGS.git
cd EasyGS
conda env create -f env_all/EasyGS_1.yml
conda env create -f env_all/EasyGS_2.yml
conda env create -f env_all/EasyGS_3.yml
conda env create -f env_all/EasyGS_4.yml
```

#### 2. Configure the DeepSeek Provider

Initialize the EasyGS configuration:

```
easygs onboard
```

Edit `~/.easygs/config.json`:

```json
{
  "providers": {
    "deepseek": {
      "apiKey": "<your DeepSeek API Key>",
      "apiBase": "https://api.deepseek.com"
    }
  },
  "agents": {
    "defaults": {
      "model": "deepseek-v4-pro",
      "maxTokens": 384000,
      "reasoningEffort": "max"
    }
  }
}
```

Use `deepseek-v4-pro` for stronger reasoning, or `deepseek-v4-flash` for lower latency. `maxTokens` controls the maximum generation length for a single response, and `reasoningEffort` sets the reasoning intensity for DeepSeek V4 Pro. DeepSeek V4 models support up to 1M context and up to 384000 output tokens on the model side. EasyGS does not expose a `contextWindow` control; it passes the current conversation, tool results, and analysis context to the selected model.

EasyGS passes `reasoningEffort` to OpenAI-compatible requests and preserves returned `reasoning_content`. When using DeepSeek V4 Pro, setting `reasoningEffort` to `max` is recommended for stronger reasoning.

Check the configuration:

```
easygs status
```

#### 3. Start EasyGS

Enable the Web UI channel in `~/.easygs/config.json`:

```json
{
  "channels": {
    "websocket": {
      "enabled": true,
      "port": 25685
    }
  }
}
```

Start the service:

```
easygs gateway
```

Open the Web UI:

```
http://127.0.0.1:25685
```

You can also run EasyGS from the command line:

```
easygs agent -m "Please check the basic statistics for /data/example.vcf.gz"
```

Or start an interactive session:

```
easygs agent
```

#### 4. Interface Preview

<div align="center">
<table>
  <tr>
    <td align="center">
      <img src="./assets/easygs_ui.png" width="1000" border="1" />
      <br />
      <sub>EasyGS Web UI and GS analysis workflow</sub>
    </td>
  </tr>
</table>
</div>

#### 5. Analysis Result Examples

<div align="center">
<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <img src="./assets/easygs_gwas_result.jpg" height="400" border="1" />
      <br />
      <sub>GS analysis result</sub>
    </td>
    <td align="center" valign="top" width="50%">
      <img src="./assets/easygs_correlation_result.png" height="400" border="1" />
      <br />
      <sub>Correlation analysis result</sub>
    </td>
  </tr>
</table>
</div>
