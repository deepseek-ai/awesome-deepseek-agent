[English](./trae.md) | [简体中文](./trae.zh-CN.md) · [← 返回](../README.zh-CN.md)
# 接入 Trae
Trae 是一款 AI IDE，内置多款模型，同时支持通过预设模型服务商接入你自己的 API 密钥。本指南将带你用 DeepSeek API 密钥在 Trae 中接入 DeepSeek-V4-Pro 或 DeepSeek-V4-Flash。
> 两种接入方式任选其一：
>
> - **内置模型**：Trae 的模型选择器中已列出 DeepSeek 模型，无需额外配置，费用消耗 Trae 积分。
> - **预设服务商 + 自有密钥**：添加 DeepSeek 预设服务商并填入你的 DeepSeek API 密钥。Trae 仅对内置模型扣除积分，调用自定义模型不消耗 Trae 积分，费用由 DeepSeek API 账户直接结算。本指南介绍这种方式的配置步骤。
### 从零安装 Trae
- 前往[官网](https://www.trae.cn/download)下载安装包。Trae 支持 macOS 12.0 及以上、Windows 10 / 11（x64），以及 Linux（`.deb` 与 `.rpm`，支持 x64 与 ARM64）。
- 运行安装包，启动 Trae 并登录账号。
- 跟随界面指引完成初始设置：选择主题与语言，可按需从 VS Code 或 Cursor 导入已有配置，并添加 Trae 命令行工具。
> 海外用户可从国际站 [trae.ai](https://www.trae.ai/download) 下载与登录。
### 配置 Trae
开始前，先在 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 获取 API 密钥。
1. **进入模型管理面板**：前往 `设置` -> `模型`。
2. **添加模型**：点击 `添加模型`。
3. **选择预设服务商**：添加模型窗口中的 **服务商** 下拉选择 `DeepSeek`。请走预设服务商路径，而不是自定义模型路径——预设服务商会自动填好接口地址与协议，而自定义模型需要手动逐项填写。
4. **完成基础模型配置**：

| 参数 | 取值 |
| --- | --- |
| 服务商 | **DeepSeek** |
| 模型 | 下拉选择 **DeepSeek-V4-Flash** 或 **DeepSeek-V4-Pro** |
| API 密钥 | 你的 DeepSeek API 密钥 |
- 如需在 DeepSeek 平台创建密钥，可点击 API 密钥输入框右侧的 `获取 API 密钥`。
- 模型下拉中列出两个预设模型 **DeepSeek-V4-Pro**、**DeepSeek-V4-Flash**，以及一个用于接入列表外模型的 **使用其他模型** 入口。复杂任务选 Pro，追求速度与轻量选 Flash。
- 如需使用列表中没有的模型或版本，点击 **使用其他模型**，窗口会出现新的 **模型 ID** 输入框，严格按 API 模型 ID 填写，如 `deepseek-v4-pro` 或 `deepseek-v4-flash`，也可点击输入框右侧的链接前往 DeepSeek 平台查询。
5. **展开高级配置**：

| 参数 | 推荐取值 |
| --- | --- |
| 上下文窗口（Token）— 输入 | 点击 **1M** 预设按钮 |
| 上下文窗口（Token）— 输出 | 留空使用最佳默认值，或点击最高的 **128k** 预设按钮。也可手动输入更大数值，但能否保存成功尚未验证 |
| 工具调用轮数 | 留空使用默认值；如需长流程 Agent 工作流可调高，例如 `500` |
| 思考模式 | **跟随模型默认配置**，或选择 **开启** |
| Temperature / Top P / Top K | 留空使用最佳配置。手动取值范围：Temperature `0 ~ 2`、Top P `0 ~ 1`、Top K `1 ~ 100` |
- 输入预设为 `128k`、`256k`、`512k`、`1M`；输出预设为 `4k`、`16k`、`32k`、`128k`。所有数值也支持手动输入；留空则使用 Trae 内置的默认最优值。
- DeepSeek V4 最高支持 **100 万 Token 上下文**，最大输出为 384K Token，因此输入推荐直接使用一键 `1M` 预设。除非你已在自己的版本中实测更大的手动输出值可以保存，否则输出字段建议留空。
6. **添加模型**：点击 `添加模型`。编辑已有模型时该按钮为 `保存模型`。Trae 会向 DeepSeek 发起连通性测试，该测试会发起一次真实请求，消耗少量模型 Token。连接成功则该模型加入模型列表；失败时窗口会显示服务商返回的错误信息与日志，可用于排查问题。
### 使用 Trae
DeepSeek V4 系列模型支持最高 **100 万 Token 上下文**，并支持最高 `max` 级别的思考强度。Trae 的思考模式只提供 **跟随模型默认配置 / 开启 / 关闭** 三档，没有逐档强度选择器，因此保持跟随默认或开启即可保留模型完整的推理能力；不要为了规避接口报错而关闭思考模式。输入上下文设为 `1M` 后，单次任务即可容纳完整代码库。
用 Trae 打开项目，在 AI 对话输入框右下角点击当前模型名称，选择刚添加的 DeepSeek 模型，在 IDE 或 SOLO 模式下均可使用。
> API 模型 ID 为 `deepseek-v4-pro` 和 `deepseek-v4-flash`。这两个是 DeepSeek 侧唯一的当前模型名称；更早的 V3 名称已废弃，不应再使用。最新价格请查阅 [DeepSeek 定价页面](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。
更多细节请参阅 [Trae 内置模型与自定义模型文档](https://docs.trae.ai/ide/models)。
### 常见问题
- 添加或保存模型失败：检查 API 密钥是否正确，无多余空格；确认密钥未过期或被禁用。
- 连通性测试不通过或调用报错：检查 DeepSeek 账户余额是否充足，网络连接是否正常。
- 对话的模型选择器中不显示该模型：确认已在 `设置` -> `模型` 中启用该模型。被禁用的模型仍保留在管理面板，但不会出现在选择器中。
- 你的版本中没有预设服务商：可改用自定义模型路径——API 格式选择 OpenAI Chat Completions 格式，请求地址填写 `https://api.deepseek.com/v1/chat/completions`，模型 ID 填写 `deepseek-v4-pro` 或 `deepseek-v4-flash`。
