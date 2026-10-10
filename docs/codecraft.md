[English](./codecraft.md) | [简体中文](./codecraft.zh-CN.md) · [← Back](../README.md)

# Integrate with CodeCraft

CodeCraft is an AI Agent-based desktop intelligent programming assistant with **19 tools** (file read/write, command execution, Git operations, web search, etc.) and sub-agent parallel collaboration. Packaged as a cross-platform Electron desktop app with a bundled JRE — no Java installation required.

### Install CodeCraft

#### Option 1: Download Installer (Recommended)

Go to [CodeCraft Releases](https://github.com/zb614433612/CodeCraft/releases) and download the latest installer for your platform:

| Platform | Installer |
|----------|-----------|
| Windows | `CodeCraft-Setup-{version}.exe` |
| macOS | `CodeCraft-{version}.dmg` |
| Linux | `CodeCraft-{version}.AppImage` / `.deb` |

Double-click to install — **no Java or Node.js setup needed**. All dependencies are bundled.

#### Option 2: Build from Source

```bash
# Prerequisites: JDK 17+, Maven 3.6+, Node.js 18+
git clone https://github.com/zb614433612/CodeCraft.git
cd CodeCraft
mvn clean package -DskipTests && mvn spring-boot:run
```

After startup, visit **http://localhost:8084**.

### Configure CodeCraft

CodeCraft uses DeepSeek's **OpenAI-compatible endpoint**. All configuration is done through the GUI — no manual config file editing needed.

#### Step 1: Get Your API Key

Create and copy your API Key from [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### Step 2: Configure in CodeCraft

1. Launch CodeCraft, log in with default account `admin` / `123456`
2. Click **Settings → System Config** in the left menu
3. Find the **DeepSeek API Key** field, paste your API Key
4. Click Save

#### Step 3: Choose Model & Reasoning Effort

At the top of the chat page, you can switch model and thinking mode:

| Setting | Recommended | Notes |
|---------|-------------|-------|
| **Model** | `deepseek-v4-pro` | V4 Pro for complex coding tasks; V4 Flash for faster, lower-cost responses |
| **Thinking Mode** | `thinking_max` | Enables deep reasoning before execution for the best coding experience |
| **Execution Mode** | `auto` or `manual` | `auto` lets AI execute tools automatically; `manual` prompts for confirmation before each operation |

> 💡 **1M Context Window**: DeepSeek V4 models support up to **1 million tokens** of context. CodeCraft includes a built-in intelligent context compaction system (three-tier progressive: WARN → COMPACT → DROP) that automatically manages token consumption, so you can focus on the conversation without manually clearing history.

### Use CodeCraft

1. Set a **working directory** for the current session in the left menu (your project's root directory)
2. Type a programming task in the chat input, e.g., "Create a Spring Boot REST API with CRUD endpoints"
3. AI automatically invokes tools — reading/writing files, executing commands, searching code, etc.
4. Complex tasks are automatically decomposed into sub-agents that execute in parallel, with results summarized upon completion

```
Working directory: /path/to/my-project

Input: Write a user registration endpoint with validation and database persistence
AI operations:
  ├─ Read project structure to understand existing code
  ├─ Create UserController, UserService, UserMapper
  ├─ Write parameter validation logic
  ├─ Auto compile to verify
  └─ Report completion status
```

### More Resources

- [CodeCraft Source Code](https://github.com/zb614433612/CodeCraft)
- [Architecture Documentation](https://github.com/zb614433612/CodeCraft/blob/master/docs/ARCHITECTURE.md) (Chinese) / [ARCHITECTURE_EN.md](https://github.com/zb614433612/CodeCraft/blob/master/docs/ARCHITECTURE_EN.md) (English)
- [Development Quick Reference](https://github.com/zb614433612/CodeCraft/blob/master/docs/DEV_QUICKREF.md)
