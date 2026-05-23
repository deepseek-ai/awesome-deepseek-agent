[English](../en/deepseek-generic-agent.md) | [简体中文](./deepseek-generic-agent.md) · [← 返回首页](../index.md)

# 把 DeepSeek 接入 GenericAgent

本文介绍如何把 DeepSeek 接入 GenericAgent。整体只需要三步：安装 GenericAgent、配置 DeepSeek API Key、启动后开始使用。

## 1. 安装 GenericAgent

先准备好 Python 3.11 或 3.12，然后获取 GenericAgent 项目代码。

在终端执行：

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
pip install streamlit pywebview
```

如果你的环境使用 `pip3`，则改为：

```bash
pip3 install streamlit pywebview
```

## 2. 配置 DeepSeek API Key

GenericAgent 通过 `mykey.py` 读取模型配置。

> ### 🔰 mykey 配置最简流程
>
> **第 1 步：复制模板文件**
> 进入 GenericAgent 项目目录，找到 `mykey_template.py`，复制一份，然后把副本重命名为 `mykey.py`。
>
> **第 2 步：编辑 `mykey.py`**
> 用任意文本编辑器打开 `mykey.py`。你会看到很多 `#` 开头的行，这些都是注释，程序运行时会自动忽略。
>
> 填写配置有两种方式：
> - 方式 A：找到对应配置区域，填好信息后，删掉该行前面的 `#`
> - 方式 B：不改原注释，直接在文件里另起一行写生效配置
>
> 简单来说：有 `#` 的行不会生效，没有 `#` 的行才会生效。
>
> **第 3 步：保存文件**
> 改完后保存 `mykey.py`。
>
> **第 4 步：重启 GA**
> 每次修改 `mykey.py` 后，都建议关掉 GenericAgent 再重新启动，让新配置生效。

下面是这次接入 DeepSeek 需要填写的最简配置，直接复制到 `mykey.py` 即可：

```python
oai_config = {
    'apikey': 'sk-', #DEEPSEEK_API_KEY
    'apibase': 'https://api.deepseek.com',
    'model': 'deepseek-v4-pro',
}
```

说明：

- `apikey` 填你的 DeepSeek Key
- `apibase` 固定为 `https://api.deepseek.com`
- `model` 使用 `deepseek-v4-pro`
- 如果你在 `mykey.py` 里同时写了多组配置，GA 默认首先读取第一个生效配置

## 3. 启动并使用 GenericAgent

### 首次启动

在 GenericAgent 项目目录下执行：

```bash
python launch.pyw
```

如果你是 Windows，也可以直接双击 `launch.pyw` 启动。

看到浏览器弹出 Streamlit 聊天界面，或者出现 pywebview 窗口，就说明启动成功了。

### 让 GA 自动安装剩余依赖

最小依赖装完后，其余依赖不用手动一个个补。启动成功后，在对话框里输入这句话：

```text
请查看你的代码，安装所有用得上的 python 依赖
```

GA 会自己读代码、找出需要的包，并把剩余依赖安装好。

### 开始使用

依赖补完后：

1. 打开 GenericAgent 界面
2. 确认当前模型读取到了你在 `mykey.py` 中配置的 DeepSeek
3. 输入一条测试消息，例如“你好，请介绍一下你自己”
4. 看到正常回复，就说明 DeepSeek 已经成功接入 GenericAgent

## 详细教程参考

如果你想系统了解 GenericAgent 的完整安装、配置、能力和进阶使用，可以参考：

- [hello-generic-agent 详细教程](https://github.com/datawhalechina/hello-generic-agent)
