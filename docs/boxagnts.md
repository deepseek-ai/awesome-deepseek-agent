# BoxAgnts


BoxAgnts is an open-source AI Agent ToolBox built with Rust, dedicated to delivering an ultimate out-of-the-box experience. Leveraging WebAssembly sandbox, it provides a runtime environment that balances security and flexibility, helping users effortlessly tackle a wide range of complex tasks and thus becoming an efficient and trustworthy personal AI assistant.

## Core Architecture

### 🎯 AI Agent Tool**Box**

BoxAgnts is a fully-featured AI Agent toolkit providing:

- **Multi-model support**: Compatible with major AI model providers including OpenAI, Anthropic, CodeX, Google, Deepseek, MiniMax, OpenCode
- **Tool system**: Built-in file operations, web access, code execution, and many other tools
- **Skill system**: Create specialized AI skills through simple configuration

### 🛡️ WebAssembly Sand**Box**

Build a secure runtime environment using WebAssembly technology:

- **Isolated execution**: All custom tools and skills run in a WASM sandbox
- **Security control**: Fine-grained permission management and network access control
- **Cross-platform**: Compile once, run everywhere
- **High performance**: Based on Wasmtime runtime, near-native performance

### ✨ Out of the **Box**

Out-of-the-box experience:

- **Zero-configuration startup**: Download and run, no complex configuration
- **Web interface**: Built-in beautiful Dashboard for visual management of all features
- **Built-in extensions**: Pre-configured with commonly used tools and skills, ready to use
- **Quick start**: Simple API and intuitive workflow

## Key Features

### 🤖 AI Chat and Intelligent Agents
- Stream-based chat with multiple AI models (20+ providers supported)
- Create and manage custom Agents, each with independent model, prompt, and max turns configuration
- Save and manage complete chat history
- MD file-driven Agents (define Agent behavior via `.md` files)

### 🔧 Tool Execution
- File read/write and intelligent editing (diff-level modifications)
- Secure shell command execution (with command risk parsing and classification)
- Web content scraping and HTTP requests
- Document reading (PDF, DOCX, etc.)
- File search (glob pattern matching + regex content search)

### 📦 Skill System
- Quickly create specialized skills via Markdown files
- Skill combination and reuse
- Built-in skills: code review, CSS refactor advisor, DOCX/PPTX/XLSX generators, file compression, front-end component generation, etc.

### ⏰ Scheduled Tasks (Cron)
- Create and manage scheduled tasks with standard Cron expressions
- Automatic task execution with logging
- Flexible task configuration: specify Agent, message content, and working directory

### 🌐 Web Service
- Custom static website deployment and hosting
- Custom API endpoint management
- Real-time file system browsing

### 🔌 MCP Protocol Support
- Connect to external MCP (Model Context Protocol) services
- Extend AI tool and resource access capabilities via MCP

### 🛡️ Security & Permissions
- WebAssembly sandbox isolated execution
- Network access control (domain allowlist + IP blocklist)
- HTTP Basic Auth for Dashboard protection

## Quick Start

### Download Executable

Download the latest compressed package from the [Releases](https://github.com/guyoung/boxagnts/releases) page, extract and run.

### Start Service

```bash
# Start service
boxagnts

# Specify workspace directory
boxagnts --workspace-dir /path/to/workspace

# Specify port
boxagnts --workspace-dir /path/to/workspace --port 30002
```

> Suggestion: BoxAgnts supports multiple workspaces, each with its own configuration file and data directory. It is recommended not to run in the default directory, but to specify a workspace directory or workspace-dir.

Command line arguments:

```bash
BoxAgnts is an open-source AI Agent ToolBox built with Rust.

Usage: boxagnts [OPTIONS]

Options:
      --port <PORT>          Port to run the web server on [default: 30001]
      --host <HOST>          Host to bind to (0.0.0.0 for all interfaces) [default: 127.0.0.1]
      --workspace-dir <DIR>  Set workspace dir, default current dir
      --app-dir <DIR>        Set app dir, default Boxagnts executable file dir
      --admin-user <USERNAME>  Set admin username
      --admin-pass <PASSWORD>  Set admin password
  -h, --help                 Print help
  -V, --version              Print version
```

### Access Dashboard

Open your browser and visit `http://127.0.0.1:30001/dashboard`

### Configure Model

Add AI models and API Keys in the settings page

## Project Structure and Source Code Compilation

This project is developed based on [claurst](https://github.com/Kuberwastaken/claurst) project code

### Directory Structure

```
boxagnts-pub/
├── boxagnts/                 # Rust backend core code
│   ├── api/                 # Multi-provider AI model API adapters
│   ├── core/                # Core types, constants, error handling & cost tracking
│   ├── gateway/             # API gateway (Cron scheduler + site management)
│   ├── mcp/                 # MCP protocol client implementation
│   ├── query/               # Agent query orchestration engine (query loop, context compaction)
│   ├── server/              # Web server (Axum REST API + WebSocket)
│   ├── tools/               # Tool system (Tool trait + built-in tools)
│   ├── tools-manager/       # Tool manager (Shell command parser, etc.)
│   ├── wasm-sandbox/        # WebAssembly sandbox runtime (Wasmtime)
│   ├── wasm-tools/          # WASM tool registration, parsing & execution wrapper
│   └── workspace/           # Workspace management (config/auth/history)
├── boxagnts-dashboard-web/  # Vue 3 frontend source code
│   ├── src/
│   │   ├── api/            # API wrappers & type definitions
│   │   ├── components/     # Shared Vue components
│   │   ├── composables/    # Composables (chat/scroll/session/Markdown)
│   │   ├── stores/         # Pinia state management (11 business stores)
│   │   ├── views/          # Page components (13 pages)
│   │   ├── types/          # TypeScript type exports
│   │   └── router/         # Vue Router configuration
│   └── package.json        # Frontend dependencies
├── app/                     # Application resources
│   ├── dashboard-web/      # Compiled web static assets
│   └── extensions/         # Built-in extensions (WASM tools + skill definitions)
├── docs/                    # Documentation
├── examples/                # Examples (WASM tool development samples)
├── Cargo.toml              # Rust workspace configuration
└── Cargo.lock              # Dependency lock file
```

### Backend Code Analysis

The backend is developed in Rust using Tokio async runtime and the Axum web framework. The main modules are:

- **api/**: Multi-provider adapter layer. Wraps APIs from 20+ AI providers including OpenAI, Anthropic, Google, Azure, Bedrock, DeepSeek, MiniMax, Cohere, GitHub Copilot, providing unified interface calling and streaming/non-streaming message format conversion
- **core/**: Core layer. Defines core data types (Message, ContentBlock, ToolDefinition, etc.), constants, error handling, cost tracking, and system prompts
- **gateway/**: API gateway layer. Handles business logic routing, includes Cron task scheduling system (cron/ subdirectory) and custom site management (site/ subdirectory)
- **mcp/**: MCP (Model Context Protocol) client implementation, supporting connection to external MCP services to extend tool capabilities
- **query/**: Query orchestration engine. Implements the core Agent query loop, including multi-provider dynamic routing, tool call loop, streaming response handling, automatic context compaction, and budget control
- **server/**: Web server layer. Provides Dashboard REST API and WebSocket support based on Axum, with HTTP Basic Auth security
- **tools/**: Tool system. Defines the unified Tool trait interface and built-in tools (file operations, shell commands, MCP resources, skill invocation, plan mode, etc.)
- **tools-manager/**: Tool manager. Contains a complete Shell command parser for Bash tools (lexer + parser + AST)
- **wasm-sandbox/**: WebAssembly sandbox runtime. Based on Wasmtime, implements secure isolated execution environment with directory mapping, network access control, and resource limits (timeout/memory/fuel)
- **wasm-tools/**: WASM tool wrappers. Provides WASM component registration, parsing, parameter validation, and execution encapsulation
- **workspace/**: Workspace management. Handles configuration files, OAuth authentication, session history storage, and permission management

### Frontend Code Analysis

The frontend uses Vue 3 + TypeScript + Vuetify technology stack:

- Uses **Pinia** for state management, with 11 business stores in stores/ directory (sessions, files, agents, skills, tools, crons, sites, mcp, usage, settings, app state), all inheriting from the `baseCrud` generic base class
- Uses **Vue Router** for routing management (Hash mode, router/ directory)
- Main pages: Chat, Home, Agents, Skills, Tools, Crons, Sites, MCP, Usage, Settings (Model/API Endpoints/Security/Agents.md), etc.
- Supports Markdown rendering (Marked + DOMPurify), code editor (CodeMirror 6), charts (Chart.js + vue-chartjs), and more
- Communicates with backend via REST API and WebSocket for bidirectional real-time messaging and file change notifications

### Source Code Compilation Method

#### Environment Requirements

- Rust 1.75+ (Install: https://www.rust-lang.org/tools/install)
- Node.js 18+ (Install: https://nodejs.org/)
- npm or pnpm

#### Compile Backend

```bash
# Enter project root directory
cd boxagnts-pub

# Compile Debug version
cargo build

# Compile Release version (optimize for size and performance)
cargo build --release

# Compiled executable is located at target/release/boxagnts
```

#### Compile Frontend

```bash
# Enter frontend directory
cd boxagnts-dashboard-web

# Install dependencies
npm install

# Start development mode (hot reload)
npm run dev

# Compile production version
npm run build

# Compiled static files will be output to app/dashboard-web/
```

#### Complete Build Process

```bash
# 1. Compile frontend
cd boxagnts-dashboard-web
npm install
npm run build

# 2. Compile backend
cd ..
cargo build --release

# 3. Run
./target/release/boxagnts
```

## License

MIT


---

**Repository**: [https://github.com/guyoung/boxagnts](https://github.com/guyoung/boxagnts)
