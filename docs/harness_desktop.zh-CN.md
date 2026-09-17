# Harness Desktop

[Harness Desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) 是一个社区维护的 Windows 桌面版，直接使用官方 DeepSeek Harness Web 工作台。它提供中文安装版和免安装版，会在本机启动 Harness，并增加快速换肤、应用内插件市场和桌面更新。

> Harness Desktop 是社区项目，不是 DeepSeek 官方应用。

## 安装

1. 打开[下载页面](https://github.com/baiyuscc13724-max/deepseek-harness-desktop/releases)。
2. 下载 Windows 中文安装版；不想安装时可以下载免安装版。
3. 启动 Harness Desktop，应用会直接进入官方 Harness 工作台。

下载页面会一直指向当前可用版本，因此本指南不依赖某个固定版本号。

## 配置 DeepSeek 模型

1. 点击左下角的**设置**。
2. 打开**模型**。
3. 选择已有的 DeepSeek 服务商；没有时，点击官方的**添加模型**入口。
4. 在官方模型设置中填写 DeepSeek API Key，并选择 **DeepSeek-V4-Pro** 或 **DeepSeek-V4-Flash**。
5. 保存后，把它选为主模型。

DeepSeek V4 支持最高 100 万 token 上下文。更看重效果时可选 V4-Pro，更看重速度时可选 V4-Flash。

Harness Desktop 不会把 API Key 打进安装包，也不会在官方 Harness 设置之外再保存一份服务商配置。

## 第一次使用

1. 添加或选择一个工作区。
2. 新建会话。
3. 输入一个简单任务，例如：`总结这个项目，并建议最先改进的地方。`
4. 发送前确认当前权限级别。

## 可选桌面功能

- 点击顶栏的调色盘图标，可以直接换皮肤，不必先打开完整设置。
- 打开**设置 → DSH插件市场**，可以查看、安装和更新社区插件。
- 在**设置 → 模型**中，主模型和子代理模型可以分开选择；没有单独设置子代理时，会跟随主模型。
- 桌面更新会在后台检查，安装前会校验下载文件。

社区插件会运行第三方代码，安装前请确认来源和许可证可信。

## 相关链接

- [Harness Desktop 项目主页](https://github.com/baiyuscc13724-max/deepseek-harness-desktop)
- [Windows 下载页面](https://github.com/baiyuscc13724-max/deepseek-harness-desktop/releases)
- [DeepSeek Harness 官方项目](https://github.com/deepseek-ai/deepseek-harness)