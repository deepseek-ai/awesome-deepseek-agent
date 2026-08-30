[English](./deepseek_harness.md) | [简体中文](./deepseek_harness.zh-CN.md) · [← 返回](../README.md)

# 接入 DeepSeek Harness

DeepSeek Harness 是 DeepSeek 官方出品的 agent harness：一切能力都是插件，由 `cordis.yml` profile 组装，模型与插件运行在同一套工具接口上。

- **GitHub：** <https://github.com/deepseek-ai/deepseek-harness>
- **官方文档：** <https://www.deepseek.com/harness>

#### 1. 安装 DeepSeek Harness

- 安装 [Node.js](https://nodejs.org/en/download/) 22.19+（或 24+）与 [pnpm](https://pnpm.io/)。
- 从源码检出运行：

```sh
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
```

- 验证安装：

```sh
pnpm dsh --version
```

#### 2. 配置 DeepSeek API

在环境中设置你的 API Key（从 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取，仓库根 `.env` 亦可）：

```sh
export DEEPSEEK_API_KEY="sk-..."
```

可选设置 `DEEPSEEK_BASE_URL` 覆盖 DeepSeek 平台端点。

请使用现行模型名 `deepseek-v4-pro`（支持 `max` / `high` 推理强度）与 `deepseek-v4-flash`；DeepSeek V4 模型支持最高 1M token 上下文。

#### 3. 运行 DeepSeek Harness

```sh
pnpm dsh web                                   # Web UI：http://127.0.0.1:3080
pnpm dsh --profile headless "你的任务"           # 一次性无头运行
```

#### 一切皆插件

插件是声明了 `dsh.bundle` manifest 的 npm 包，安装到 profile 即可生效：

```sh
pnpm dsh plugin --profile web add dsh-auto-review   # 示例：第二模型审批评审
```

社区插件注册表：<https://awesome-dsh-plugin.com> · 插件市场：<https://deepseek1024.com>
