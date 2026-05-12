[English](./musacode.md) | [简体中文](./musacode.zh-CN.md) · [← Back](../README.md)

# Integrate with MUSACode

MUSACode is an AI Coding Agent developed by Moore Threads. Based on TUI or desktop, it helps developers quickly complete tasks such as code generation, debugging, and refactoring through natural language commands. MUSACode not only has universal programming capabilities, helps you DIY your software， More committed to becoming the best MUSA programming tool, providing full process support for operator development, testing, compilation, and optimization.

#### 1. Install MUSACode

##### Quick Install

Get MUSACode up and running with the one-line installer.

###### TUI for Linux / macOS / WSL2

```bash
curl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash
```
- After installation, run the following command. If the version number is displayed, the installation is successful：

```
musacode --version
```

###### Desktop for Linux / Windows

```bash
curl -fsSL https://musacode.tos-cn-beijing.volces.com/desktop/install-desktop | bash
```

#### 2. Run and Configure

- First, execute the `musacode` command<br/>
- Then, in the input box, type `/connect`, and select `deepseek` as the provider<br/>
- Next, enter your [DeepSeek API Key](https://platform.deepseek.com/api_keys) in the input field that appears<br/>
- Finally, select the DeepSeek-V4-Pro model from the list to finish the configuration