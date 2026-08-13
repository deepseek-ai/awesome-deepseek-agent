[简体中文](./dsh.zh-CN.md) | [English](./dsh.md) · [← 返回](../README.md)

# 接入 DeepSeek Harness（dsh）

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）是 DeepSeek 官方开源的 Agent 运行时——"一切皆插件"架构（基于 Cordis），自带 `web` 与 `headless` 两种形态。

> 📚 新手教程：社区白皮书 **dsh-handbook**（中英双语，9 章 + PDF，从零到插件开发）：https://github.com/Electricitysheep/dsh-handbook

#### 1. 安装

需要 Node.js ≥ 22。

```bash
# 直接运行（免安装）
npx -y @deepseek-ai/dsh --version

# 或全局安装
npm install -g @deepseek-ai/dsh
```

#### 2. 运行与配置

**Web UI：**

```bash
dsh web   # → http://127.0.0.1:3080
```

**Headless（一次性任务，脚本/CI）：**

```bash
dsh --profile headless "你好，请用一句话介绍自己"
```

**在 `~/.dsh/settings.yaml` 配置模型与 API Key：**

```yaml
agent-default-model:
  model: deepseek-v4-flash    # 或 deepseek-v4-pro
  reasoningEffort: high       # low / high / max
```

#### 3. 推理档位

`low`（最快，简单轮次）· `high`（默认）· `max`（最强，复杂推理）。关键认知：模型在每次工具调用前都会重新思考——降低档位是工具链提速的最高杠杆。

#### 4. 插件

一切皆插件。两步挂载（详见 [dsh-handbook 第 3 章](https://github.com/Electricitysheep/dsh-handbook)）：

```yaml
# ~/.dsh/profiles/web/cordis.patch.yml
- insert:
    - id: <插件id>
      name: <npm包名>
```

社区插件：[dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo)（工具调用提速）、[DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar)（文件/终端/Git 侧边栏）。
