[English](./codecraft.md) | [简体中文](./codecraft.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 CodeCraft

CodeCraft 是一个基于 AI Agent 的桌面端智能编程助手，支持 **19 个工具**（文件读写、命令执行、Git 操作、网络搜索等），并支持子 Agent 并行协作，通过 Electron 打包为跨平台桌面应用，内置 JRE 开箱即用。

### 从零安装 CodeCraft

#### 方式一：下载安装包（推荐）

前往 [CodeCraft Releases](https://github.com/zb614433612/CodeCraft/releases) 页面，下载对应平台的最新安装包：

| 平台 | 安装包 |
|------|--------|
| Windows | `CodeCraft-Setup-{version}.exe` |
| macOS | `CodeCraft-{version}.dmg` |
| Linux | `CodeCraft-{version}.AppImage` / `.deb` |

下载后双击安装即可，**无需安装 Java 或 Node.js**，所有依赖均已内置。

#### 方式二：从源码构建

```bash
# 环境要求：JDK 17+、Maven 3.6+、Node.js 18+
git clone https://github.com/zb614433612/CodeCraft.git
cd CodeCraft
mvn clean package -DskipTests && mvn spring-boot:run
```

启动后访问 **http://localhost:8084**。

### 配置 CodeCraft

CodeCraft 使用 DeepSeek 的 **OpenAI 兼容端点**，在图形界面中即可完成全部配置，无需手动编辑配置文件。

#### 第一步：获取 API Key

在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 创建并复制你的 API Key。

#### 第二步：在 CodeCraft 中配置

1. 启动 CodeCraft，默认账号 `admin` / `123456` 登录
2. 点击左侧菜单 **设置 → 系统配置**
3. 找到 **DeepSeek API Key** 配置项，粘贴你的 API Key
4. 点击保存

#### 第三步：选择模型与推理强度

在聊天页面顶部，你可以切换模型和思考模式：

| 配置项 | 推荐值 | 说明 |
|--------|--------|------|
| **模型** | `deepseek-v4-pro` | V4 Pro 适合复杂编程任务；V4 Flash 响应更快、成本更低 |
| **思考模式** | `深度思考 (thinking_max)` | 开启后 AI 会先深度推理再执行，获得最佳编程体验 |
| **执行模式** | `auto` 或 `manual` | auto 模式 AI 自动执行工具；manual 模式操作前需确认 |

> 💡 **1M 上下文**：DeepSeek V4 系列支持高达 **100 万 token** 的上下文窗口。CodeCraft 内置了智能上下文压缩系统（三级渐进：预警 → 压缩 → 丢弃），自动管理 Token 消耗，让你专注对话而无需手动清理历史。

### 使用 CodeCraft

1. 在左侧菜单中，为当前会话设置 **工作目录**（即你的项目根目录）
2. 在聊天框中输入编程任务，例如：「帮我创建一个 Spring Boot REST API 项目」
3. AI 会自动调用工具完成任务——读写文件、执行命令、搜索代码等
4. 复杂任务会被自动拆解，子 Agent 并行执行，完成后汇总结果

```
工作目录示例：/path/to/my-project

输入：帮我写一个用户注册接口，包含参数校验和数据库存储
AI 操作：
  ├─ 读取项目结构，了解现有代码
  ├─ 创建 UserController、UserService、UserMapper
  ├─ 编写参数校验逻辑
  ├─ 自动编译验证
  └─ 报告完成情况
```

### 更多资源

- [CodeCraft 源码](https://github.com/zb614433612/CodeCraft)
- [架构文档](https://github.com/zb614433612/CodeCraft/blob/master/docs/ARCHITECTURE.md)（英文版：[ARCHITECTURE_EN.md](https://github.com/zb614433612/CodeCraft/blob/master/docs/ARCHITECTURE_EN.md)）
- [开发速查表](https://github.com/zb614433612/CodeCraft/blob/master/docs/DEV_QUICKREF.md)
