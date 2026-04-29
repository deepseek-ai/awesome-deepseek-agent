[English](./hermes.md) | [简体中文](./hermes.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 Hermes

Hermes 是 Nous Research 打造的开源自我进化 AI Agent。它内置学习闭环：能够从经验中生成技能，在使用过程中持续优化，沉淀知识，并在跨会话中逐步构建你偏好的动态模型。

#### 1. 安装 Hermes

##### 快速安装

通过一行安装命令，你可以在两分钟内快速启动 Hermes Agent。

###### Linux / macOS / WSL2

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

唯一前置依赖是 Git，其余内容安装脚本会自动处理。

更多安装说明请参考 [Hermes 安装文档](https://hermes-agent.nousresearch.com/docs/getting-started/installation)。

#### 2. 运行并配置

重新加载 shell 后，开始配置 Hermes：

- 执行 `hermes setup` 命令
- 选择 Quick Setup
- 当提示选择模型提供商时，选择 **DeepSeek**
- 输入你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
- Base URL 填写 `https://api.deepseek.com`
- 选择 `deepseek-v4-pro` 模型
- 继续完成其余配置选项
