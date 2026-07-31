[English](./soloncode.md) | [简体中文](./soloncode.zh-CN.md) · [← Back](../README.md)

# Getting Started with SolonCode

SolonCode is an open-source coding agent built in Java, running as a terminal CLI tool. It helps developers with code writing, project analysis, refactoring, test generation, documentation, and other development tasks.

## Install SolonCode from Scratch

### 1. Requirements

- **Java 8+** (must be installed in advance; supports Java 8 ~ 26)
- Supports macOS, Linux, Windows, Harmony PC

### 2. Installation

**Mac / Linux / Harmony PC:**

```bash
curl -fsSL https://solon.noear.org/soloncode/setup.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://solon.noear.org/soloncode/setup.ps1 | iex
```

Verify the installation:

```bash
soloncode --version
```

### 3. Configure a Model

Launch the web settings page:

```bash
soloncode web 0
```

Go to **Settings → Models → Add Model** and fill in the model details:

<img src="assets/solon_code_llm.png" width='512' border='1'  />

Get your API Key from the [DeepSeek Open Platform](https://platform.deepseek.com/api_keys).

### 4. Start Using

Navigate to your project directory and launch SolonCode Web:

```bash
cd your-project
soloncode web 0
```

<img src="assets/solon_code_hello.png" width='512' border='1'  />
