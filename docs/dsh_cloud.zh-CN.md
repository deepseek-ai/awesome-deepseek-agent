[English](./dsh_cloud.md) | [简体中文](./dsh_cloud.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DSH Cloud

DSH Cloud 是一个开源平台，把 DeepSeek Harness 变成多用户产品：账号体系、积分
计量、服务端模型网关（DeepSeek API Key 只留在服务端，不下发任何客户端），以及
可选的按会话隔离云端智能体工作台。可自部署，也可使用托管服务。

- **GitHub：** <https://github.com/AgentsDanceAI/deepseek-harness-cloud>
- **官网：** <https://dshcloud.online>

配合 DeepSeek 模型有两种用法。

#### 方式 A —— 原版 DeepSeek Harness 直接接入

如果你已经在用 DeepSeek Harness，一条命令即可把 DSH Cloud 加为模型
provider（无需自备 API Key；托管账号注册即送 500 积分）：

```bash
npx --yes dsh-plugin-cloud setup
```

命令会打开浏览器做设备授权，拉取网关的实时模型目录，并把 provider 写入
`$DSH_HOME/cordis.patch.yml`（写在独立行里，绝不触碰你已有的配置）。

重启 DeepSeek Harness，在 **DSH Cloud** 分组里选模型——`deepseek-v4-pro` 与
`deepseek-v4-flash` 均以完整 **1M token 上下文窗口**提供，目录中还有其他模型。

#### 方式 B —— 自部署整套平台

装好 Docker 后：

```bash
npx --yes @agentsdanceai/dsh-cloud start
```

然后把你自己的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)
填进生成的 `./dsh-cloud/.env`：

```
UPSTREAM_BASE_URL=https://api.deepseek.com/v1
UPSTREAM_API_KEY=sk-your-key
```

再执行一次同样的命令，打开 <http://localhost:8787>。整个团队即可通过网关共享
一把 DeepSeek API Key，并拥有独立账号与积分计量。Python 用户可改用
`uvx dsh-cloud start`。

#### 首次运行

登录后进入工作台（或你已接入的 DeepSeek Harness），快任务选
`deepseek-v4-flash`，深度推理选 `deepseek-v4-pro`，直接开始对话。用量按
token 计入积分。
