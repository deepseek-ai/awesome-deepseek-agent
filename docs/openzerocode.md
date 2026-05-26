[English](./openzerocode.md) | [简体中文](./openzerocode.zh-CN.md) · [← Back](../README.md)

# Integrate with OpenZeroCode

OpenZeroCode is a local-first terminal AI coding agent inspired by OpenCode. It provides a TUI experience with built-in tools, session persistence, provider switching, model switching, and workspace memory.

- **GitHub:** <https://github.com/arborlogic/openzerocode>

#### 1. Install OpenZeroCode

- Install [Bun](https://bun.sh/docs/installation) 1.2+ and make sure `npm` is available on your `PATH`.
- Install OpenZeroCode from npm:

```sh
npm install -g openzerocode
```

- Verify the installation:

```sh
openzerocode --version
```

You can also install from source:

```sh
git clone https://github.com/arborlogic/openzerocode.git
cd openzerocode
python3 scripts/dev-install.py
```

#### 2. Launch OpenZeroCode

Enter your project directory and run:

```sh
cd /path/to/my-project
openzerocode
```

Open the command palette with `Ctrl+P` or `F2`, then choose **Switch provider**.

<div align="center">
<img src="./assets/openzerocode_step2.png" width="1024" border="1" />
</div>

#### 3. Select DeepSeek as the Provider

In the provider selector, choose **DeepSeek**.

<div align="center">
<img src="./assets/openzerocode_step1.png" width="1024" border="1" />
</div>

#### 4. Add or Select a DeepSeek API Key

OpenZeroCode stores provider credentials locally. In the DeepSeek key panel, you can select an existing key, continue with the selected key, add a new key, or edit the base URL.

To add a new key, choose **Add key...**.

<div align="center">
<img src="./assets/openzerocode_step4.png" width="1024" border="1" />
</div>

Enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys), then confirm.

#### 5. Select a DeepSeek Model

After the key is configured, choose a DeepSeek model. OpenZeroCode supports DeepSeek V4 Flash and DeepSeek V4 Pro.

OpenZeroCode configures DeepSeek V4 models with a 1M-token context window.

<div align="center">
<img src="./assets/openzerocode_step5.png" width="1024" border="1" />
</div>

<div align="center">
<img src="./assets/openzerocode_step6.png" width="1024" border="1" />
</div>

<div align="center">
<img src="./assets/openzerocode_step6-2.png" width="1024" border="1" />
</div>

#### 6. Start Coding with DeepSeek

Once the provider and model are selected, the active model is shown in the input bar. Type a request and press `Enter` to send it.

<div align="center">
<img src="./assets/openzerocode_step7.png" width="1024" border="1" />
</div>

#### Useful Commands

| Command | Description |
|---------|-------------|
| `Ctrl+P` / `F2` | Open the command palette |
| `/provider-key list deepseek` | List saved DeepSeek keys |
| `/provider-key use deepseek <key-name>` | Switch to a saved DeepSeek key |
| `/provider-key path` | Show the local provider config path |
| `--provider deepseek` | Launch with DeepSeek as the provider |
| `--model <name>` | Launch with a specific model |
