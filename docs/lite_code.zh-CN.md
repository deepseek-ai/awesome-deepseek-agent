[English](./lite_code.md) | [简体中文](./lite_code.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 lite-code

lite-code 是一个内核纯手写的开源桌面 Code Agent：Python 内核 + React UI + Electron 外壳，不依赖 LangChain 等高层框架。内置 20 个工具（文件读写、Ripgrep 搜索、Tree-sitter 大纲、精确编辑、受限 Shell、Git、子 Agent、技能加载），配合三级风险模型与人工审批的安全沙箱，以及缓存优先的上下文管理。DeepSeek 是其**默认内置供应商**。

- **GitHub:** <https://github.com/LaynePeng/lite-code>

#### 1. 安装 lite-code

从 [Releases](https://github.com/LaynePeng/lite-code/releases) 页面下载对应平台的安装包：

- macOS（Apple Silicon）：`lite-code-<版本>-arm64.dmg`
- Windows：`lite-code Setup <版本>.exe`

> **注意：** macOS 安装包未签名。若提示「无法验证开发者」，右键应用选择「打开」；若提示「已损坏」，执行 `xattr -dr com.apple.quarantine "/Applications/lite-code.app"` 后重试。

也可以从源码运行（需要 Python 3.11+ 和 Node 18+）：

```bash
git clone https://github.com/LaynePeng/lite-code.git
cd lite-code
python3 -m venv .venv
.venv/bin/pip install -e .    # Windows: .venv\Scripts\pip install -e .
npm install
npm run dev                   # 开发模式：Python Core + Vite + Electron 窗口
```

#### 2. 配置 DeepSeek 供应商

DeepSeek 开箱即用，无需填写 Base URL。

1. 启动 lite-code，打开**设置**界面。
2. 选择 **DeepSeek** 供应商（默认即处于激活状态）。
3. 将你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 粘贴到 **API Key** 输入框。Key 会保存在本地 `~/.lite-code/config.json`。

也可以在启动前设置 `DEEPSEEK_API_KEY` 环境变量，lite-code 会自动读取。

#### 3. 选择模型并开始编码

在**设置**中选择模型：

- **`deepseek-v4-flash`** — 默认模型，性价比高
- **`deepseek-v4-pro`** — 推理最强，适合复杂任务

两个模型均可使用完整的 **100 万 token** 上下文窗口，长度自动解析（断网时回退到内置元数据表），无需手动配置。

打开项目目录即可开始对话。工具调用会以审批卡片的形式呈现——中/高风险操作需要你确认后才会执行。右侧面板会实时显示 Prompt 缓存命中率与上下文占用，上下文过大时自动压缩。
