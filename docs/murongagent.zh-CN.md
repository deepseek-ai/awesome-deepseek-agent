[English](./murongagent.md) | [简体中文](./murongagent.zh-CN.md)

# 在 MurongAgent 中接入 DeepSeek

MurongAgent 是一个面向 Android 的移动端多模型 AI Agent，支持本地项目浏览、代码编辑、GitHub 仓库工作流、工具调用和多轮 Agent 会话。

这份指南说明如何安装 MurongAgent、将 DeepSeek 配置为当前模型提供商，并完成第一次实际使用。

## 安装 MurongAgent

安装 MurongAgent 最简单的方式，是直接下载安装 Android 安装包。

### 方式 1：从官网安装

访问：

```text
https://murongagent.rl1.cc/
```

下载安装最新 Android 安装包后，直接在设备上安装即可。

### 方式 2：从 GitHub Release 安装

如果你更习惯从 GitHub 获取发行版本，也可以直接从项目仓库的 Release 页面下载安装。

```text
https://github.com/murongruyan/MurongAgent/releases
```

### 方式 3：从源码构建

源码构建更适合开发者或需要自行修改应用的人。

前置条件：

- Android Studio
- JDK 26
- Android SDK / Build Tools 37
- Android 13 及以上设备（`minSdk 33`）

然后执行：

```bash
git clone https://github.com/murongruyan/MurongAgent.git
cd murongagent
./gradlew :app:assembleRelease
```

如果你想直接安装到已连接设备：

```bash
./gradlew :app:installRelease
```

如果你的本地环境没有 release 签名材料，也可以先使用 debug 构建：

```bash
./gradlew :app:assembleDebug
```

## 在 MurongAgent 中配置 DeepSeek

打开 MurongAgent 后，进入设置页。

### 1. 选择模型提供商

在 `设置` → `AI 模型提供商` 中：

- 将 **Provider** 设为 `DeepSeek`

MurongAgent 也支持 `OpenAI Compatible` 和 `Claude`，但如果你要接官方 DeepSeek 接口，应直接选择 `DeepSeek`。

### 2. 填写 API Key

填写：

- `API Key`：你的 DeepSeek API Key，可在 [DeepSeek Platform](https://platform.deepseek.com/api_keys) 获取

### 3. 设置 Base URL

如果你使用官方 DeepSeek API，保持：

```text
https://api.deepseek.com
```

如果你走兼容中转站或自定义网关，也可以在这里改成对应地址。

### 4. 选择模型

请使用当前的 DeepSeek V4 模型名：

- `deepseek-v4-pro`
- `deepseek-v4-flash`

不要再使用已经过时的 V3 命名：

- `deepseek-chat`
- `deepseek-reasoner`
- `deepseek-coder`

### 5. 设置推理强度

MurongAgent 已经把 DeepSeek 的推理强度直接做进设置项里。

当前应用支持：

- `low`
- `medium`
- `high`
- `max`

如果你主要拿它做代码与 Agent 工作流，推荐高配方案是 `deepseek-v4-pro` + `max`。

## 推荐配置

用于较强的代码与 Agent 任务：

```text
Provider: DeepSeek
Base URL: https://api.deepseek.com
Model: deepseek-v4-pro
Reasoning effort: max
```

用于日常更快、更省钱的使用：

```text
Provider: DeepSeek
Base URL: https://api.deepseek.com
Model: deepseek-v4-flash
Reasoning effort: high
```

## 100 万上下文说明

DeepSeek V4 系列模型支持最高 **100 万 token** 上下文。

MurongAgent 当前没有在设置页里单独暴露 `context_window` 字段，而是直接把你选择的 DeepSeek 模型和推理配置透传给 Provider。也就是说，只要你选择的是当前 V4 模型，就已经是在使用支持 1M context 的 DeepSeek 模型家族。

## 首次运行

保存设置之后：

1. 打开 `聊天`
2. 新建会话
3. 输入类似下面的请求：

```text
读一下这个 Android 项目，告诉我聊天工作流是怎么组织的。
```

如果你已经绑定了本地项目，也可以直接问：

```text
找到 ChatScreen 的实现，并总结消息发送流程。
```

这时 MurongAgent 可以：

- 浏览本地项目
- 搜索文件
- 阅读和分析代码
- 运行带工具调用的 Agent 工作流
- 结合本地项目上下文和 GitHub 远端仓库上下文协作

## GitHub 联动

MurongAgent 还支持 GitHub 联动工作流。

在 `设置` → `GitHub` 中登录或配置 GitHub Token 后，应用就可以在项目页和聊天链路里使用 GitHub 仓库浏览、远端文件引用等能力。

这和 DeepSeek API Key 是两套独立配置。通常如果你希望同时获得：

- DeepSeek 作为模型
- GitHub 仓库作为远端项目上下文

那就需要把这两项都配置好。

## 说明

- 这是一个明显偏移动端交互的 Agent 应用。
- 工具调用、项目上下文、GitHub 上下文、会话状态之间耦合较深，所以建议先把 DeepSeek Provider 配好，再开始正式会话。
- MurongAgent 已支持 DeepSeek 的推理强度控制，并会向 DeepSeek Provider 透传 `reasoning_effort`。
