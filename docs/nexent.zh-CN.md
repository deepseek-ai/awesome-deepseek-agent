[English](./nexent.md) | [简体中文](./nexent.zh-CN.md)

# 接入 Nexent

Nexent 是一个零代码智能体自动生成平台，使用纯自然语言即可开发智能体。

#### 1. 安装 Nexent

- 确保已安装 [Docker](https://docs.docker.com/get-started/) 和 Docker Compose
- 执行下面的命令部署 Nexent：

```bash
git clone https://github.com/ModelEngine-Group/nexent.git
cd nexent/docker
cp .env.example .env
bash deploy.sh
```

- 中国大陆用户可在部署时选择"区域优化"以使用国内镜像源
- 部署成功后，在浏览器打开 [http://localhost:3000](http://localhost:3000)

> ⚠️ 首次部署时，注意保存 Docker 日志中输出的 `suadmin` 超级管理员账号密码（仅显示一次）。登录后依次完成：访问租户资源 → 创建租户 → 创建租户管理员，之后使用租户管理员账号即可使用全部功能。

#### 2. 配置 DeepSeek 模型

登录后进入 **模型管理** 页面：

- 点击 **"添加自定义模型"**，模型类型选择 **大语言模型**
- 填写以下关键配置：

| 配置项       | 值                                   |
| ------------ | ------------------------------------ |
| 模型名称     | `deepseek-v4-flash / deepseek-v4-pro`                      |
| 模型 URL     | `https://api.deepseek.com/v1`        |
| API Key      | `<你的 DeepSeek API Key>`            |

- 点击 **"连通性验证"** 确认连接成功，保存

- 然后在 **系统模型配置** 中将基础模型设为刚添加的 DeepSeek 模型

#### 3. 开始使用

进入 **智能体开发** 创建智能体，将运行模型选为 DeepSeek，用自然语言描述需求后发布，即可在 **开始问答** 中对话。

也可以在 **快速配置** 页面按顺序完成：模型管理 → 知识库配置 → 智能体开发。
