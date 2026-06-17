[English](./vibeseek.md) | [简体中文](./vibeseek.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 VibeSeek

VibeSeek 是一款以 DeepSeek 为原生后端的开源 vibecoding 桌面客户端(Windows)。它只为 DeepSeek 打造、直连 `api.deepseek.com` —— 没有协议转换层,也无需配置供应商。它把文档流对话和会改代码的 agent 结合在一起:三档权限、先出方案再动手的计划模式、全库上下文、git 安全网(一键回滚),以及每个任务后的成本透明结算小票。

- **GitHub:** <https://github.com/getvibeseek/vibeseek>

<div align="center">
<img src="./assets/vibeseek_home.png" width="720" border="1" />
</div>

#### 1. 安装 VibeSeek

从 [Releases 页面](https://github.com/getvibeseek/vibeseek/releases)下载 `VibeSeek-Setup-*.exe` 并运行。安装包未签名,首次启动 Windows SmartScreen 可能提示 —— 点「更多信息 → 仍要运行」即可。

#### 2. 填入 DeepSeek API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API Key。VibeSeek 首次启动会有简短引导(先选主题,再粘贴 Key),并把它加密存在本机 —— 无需配置环境变量。之后可随时在「设置 → API」更改;API 端点默认 `https://api.deepseek.com`。

#### 3. 开始写代码

选一个项目文件夹,在输入框描述任务并发送。agent 会读文件、改代码、跑命令,受三档权限约束:读取直接放行、修改前先征求同意、删除等危险操作需二次确认。打开**计划模式**可让它先列出分步方案、等你确认再动手。

VibeSeek 默认在 DeepSeek 两个模型间自动路由 —— 日常迭代走 **`deepseek-v4-flash`**、复杂任务升 **`deepseek-v4-pro`**,也可用 `/pro`、`/flash` 固定。DeepSeek V4 的 **1M 上下文**开箱即用;把思考强度设为 **max**(或 `/think`)可获得最强的编码与推理。VibeSeek 不会关闭思考模式。

#### 4. 进阶

- **全库模式**把整个项目放进上下文 —— 借 1M 窗口,模型无需反复 grep/读取就能定位并修改代码。
- **技能与 MCP:** 现成的技能目录一字不改就能用;接入 MCP 服务器后 agent 即可调用其工具。
- **git 安全网:** 每个任务自动建还原点 —— 一键回滚全部改动,或逐文件 / 逐段接受、拒绝。
- **成本透明:** 实时余额、缓存命中率,以及每个任务后可截图分享的结算小票。
