[English](./musacode.md) | [简体中文](./musacode.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 MUSACode

MUSACode 是摩尔线程自主打造的 AI Coding Agent，基于终端或桌面应用交互，通过自然语言命令帮助开发者快速完成代码生成、调试、重构等任务。MUSACode 不仅具备通用编程能力，helps you DIY your software，更致力于成为最好的 MUSA 编程工具，为算子开发、测试、编译和优化提供全流程支持。

#### 1. 安装 MUSACode

##### 快速安装

通过一行安装命令快速安装并启动 MUSACode。

###### TUI for Linux / macOS / WSL2

```bash
curl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash
```
- 安装结束后，执行以下命令，若显示版本号则安装成功：

```
musacode --version
```

###### Desktop for Linux / Windows

```bash
curl -fsSL https://musacode.tos-cn-beijing.volces.com/desktop/install-desktop | bash
```

#### 2. 运行与配置

- 首先，请运行 `musacode` 指令<br/>
- 接着，在输入框中键入 `/connect`，并在随后出现的供应商列表中选择 deepseek<br/>
- 然后，在接下来出现的API密钥输入框中，填入您的 [DeepSeek API Key](https://platform.deepseek.com/api_keys)<br/>
- 最后，在模型选择列表中找到并选中 DeepSeek-V4-Pro 即可完成设置