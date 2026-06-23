[English](./happex.md) | [简体中文](./happex.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入Happex

> **Happex 桌面 AI 工程平台** — 一个跨平台桌面应用，用于 AI 辅助软件工程，支持任务管理、工具执行和多供应商模型。

## 下载与安装

### 系统要求

| 平台    | 最低版本            |
| ------- | ------------------- |
| macOS   | 10.15+ (Catalina)   |
| Windows | Windows 10+         |

### 下载

1. 访问 [GitHub Releases 页面](https://github.com/huangsongyuan/happex/releases/latest)
2. 下载适合您平台的安装包：
   - **macOS (Apple Silicon)**：`happex_<version>_aarch64.dmg`
   - **macOS (Intel)**：`happex_<version>_x86_64.dmg`
   - **Windows**：`happex_<version>_x64-setup.exe`（NSIS 安装包）
3. 打开/运行安装包并按提示完成安装

## 更新

### 自动更新（推荐）

Happex 内置基于 Tauri Updater 的自动更新机制。

1. 打开应用，进入 **关于**（齿轮图标 → "关于"）
2. 点击 **"检查更新"**
3. 如果发现新版本：
   - 显示版本号和发布说明
   - 点击 **"立即安装"**
4. 下载过程中显示进度条
5. 下载完成后，应用自动重启以应用更新

### 手动更新

从 [GitHub Releases](https://github.com/huangsongyuan/happex/releases/latest) 下载最新安装包，覆盖安装即可。

## DeepSeek供应商配置

前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。
前往 [DeepSeek 开放平台模型说明](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)获取URL及配置说明。

### 页面配置（UI）

#### 添加供应商

1. 进入 **设置** → **提供商与模型设置**
2. 点击供应商面板右上角的 **+** 按钮
3. 填写表单：
   - **Provider 类型**：选择 OpenAI Compatible 或 Anthropic
   - **显示名称**：可读的标签（例如："我的 DeepSeek"）
   - **Base URL**（openAI协议:https://api.deepseek.com/v1;
   - Anthropic协议:https://api.deepseek.com/anthropic）
   - **API 密钥**：您的 API 密钥（存储在系统钥匙串中）
4. 点击 **"添加 Provider"**

#### 编辑供应商

- 点击列表中供应商旁边的 **编辑（铅笔）** 图标
- 可以更新显示名称、Base URL 和 API 密钥
- 编辑模式下的 API 密钥字段为可选——留空则保持现有密钥不变

#### 删除供应商

点击供应商旁边的 **垃圾桶** 图标。删除供应商会同时移除其下的所有模型配置。

## 模型配置

每个供应商账户可以拥有多个模型配置。模型按供应商管理，并可以设置为全局默认模型。

### 页面配置（UI）

#### 添加DeepSeek模型

1. 从左侧列表中选择一个供应商
2. 点击模型面板右上角的 **"添加模型"**
3. 填写表单：
   - **模型 ID**：发送给 API 的精确模型标识符（例如：`deepseek-v4-pro`、`deepseek-v4-flash`）
   - **显示名称**：可读的标签（例如："deepseek-v4-pro"、"deepseek-v4-flash"）
   - **上下文窗口**：最大上下文长度，以 token 计（可参照deepseek模型说明，配置值：1000000）
   - **最大输出 token**：最大输出长度，以 token 计（可参照deepseek模型说明，配置值：384000）
   - **能力**：逐一开关各能力：
     - `chat` — 对话聊天
     - `tool_use` — 函数/工具调用
     - `streaming` — 流式响应
     - `vision` — 图像输入支持
     - `reasoning` — 扩展推理/思考
     - `embedding` — 嵌入向量生成
4. 点击 **"添加模型"**

#### 设置默认模型

- 点击模型旁边的 **星形** 图标将其设为默认
- 默认模型用于新创建的任务
- 同时只能有一个模型为默认

#### 编辑模型

点击模型中表格旁边的 **编辑（铅笔）** 图标来更新其参数。

#### 删除模型

点击模型旁边的 **垃圾桶** 图标移除该模型。

## 常见问题

### "未选择模型"报错

1. 进入 **设置** → **提供商与模型设置**
2. 确保至少配置了一个供应商
3. 在供应商下至少添加一个模型配置
4. 点击 **星形** 图标设置默认模型

---

