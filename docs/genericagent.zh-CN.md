[English](./genericagent.md) | [简体中文](./genericagent.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 GenericAgent

> **物理级全能执行者，有任何任务需要执行，尽管吩咐——从文件操作、脚本执行、浏览器控制到系统级干预，我随时待命。请描述你的目标。**

**GenericAgent（GA）** 是一个极简、自进化的自主 Agent 框架——整个核心仅 ~3000 行种子代码、~100 行 Agent 循环，却拥有完整的**层级记忆系统（L0-L4）**、**9 个原子工具**（浏览器/终端/文件系统/键鼠/屏幕视觉/手机 ADB 等），以及独特的**自进化能力**：每个任务会自动结晶为可复用的 Skill，越用越强。

GA 所有代码完全开源免费，你只需自备 LLM API Key 即可使用。

> 📖 项目主页：[github.com/lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent)
> 📄 技术报告：arXiv 2604.17091

---

#### 1. 安装 GenericAgent

**方法一：一键安装（推荐）**

一键命令会为你创建隔离的 Python 运行环境，下载完整项目并安装依赖。

Linux / macOS：
```bash
GLOBAL=1 bash -c "$(curl -fsSL http://fudankw.cn:9000/files/ga_install.sh)"
```

Windows PowerShell：
```powershell
powershell -ExecutionPolicy Bypass -c "$env:GLOBAL=1; irm http://fudankw.cn:9000/files/ga_install.ps1 | iex"
```

安装完成后，运行 `frontends/GenericAgent.exe` 启动桌面应用。

**方法二：开发者安装**

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
uv venv
uv pip install -e ".[ui]"
cp mykey_template.py mykey.py      # 随后填入 API Key
python launch.pyw
```

---

#### 2. 配置 DeepSeek V4

将 `mykey_template.py` 复制为 `mykey.py`，在其中配置 DeepSeek V4 模型。GA 通过 OpenAI 兼容协议调用 DeepSeek，配置非常简单：

```python
native_oai_deepseek_config = {
    "name": "DeepSeek Flash",
    "apikey": "sk-<你的 DeepSeek API Key>",
    "apibase": "https://api.deepseek.com",
    "model": "deepseek-v4-flash",            # 日常轻量任务
    "reasoning_effort": "medium",
}

native_oai_deepseek_pro_config = {
    "name": "DeepSeek Pro",
    "apikey": "sk-<你的 DeepSeek API Key>",
    "apibase": "https://api.deepseek.com",
    "model": "deepseek-v4-pro",              # 复杂推理任务
    "reasoning_effort": "max",               # 最高推理难度
}
```

> 💡 **提示**：
> - DeepSeek V4 支持 **1M 上下文窗口**，GA 自动兼容。
> - `reasoning_effort` 支持 `none / minimal / low / medium / high / max` 多级调节。
> - 运行时可在 GA 终端输入 `/session.reasoning_effort=high` 实时切换推理难度。

---

#### 3. 首次运行

启动 GA 后，你将进入交互式 REPL 环境。试试你的第一个 DeepSeek V4 任务：

```
GA > 写一个 Python 脚本，统计当前目录下所有 Python 文件的总行数。
```

GA 会自动调用原子工具（文件系统、终端）来完成这个任务。完成后，它会自动将本次操作**结晶为一个 Skill**，下次遇到类似任务时可以直接复用。

你也可以启动桌面 UI：
```bash
python launch.pyw
```

或启动 Streamlit Web 界面：
```bash
streamlit run frontends/ui_app.py
```

---

#### 4. 了解更多

| 特性 | 说明 |
|------|------|
| 🧬 **自进化** | 每个任务自动结晶为 Skill，无需预加载技能库 |
| 🧠 **多级记忆** | L0-META → L1-Insight → L2-Facts → L3-SOP → L4-Raw，长短期自动管理 |
| ⚡ **9 原子工具** | 浏览器 / 终端 / 文件 / 键鼠 / 视觉 / OCR / 手机(ADB) / 语音 / 定时 |
| 🔌 **多模型兼容** | DeepSeek / Claude / GPT / Gemini / Kimi / MiniMax 等，同一框架 |
| 🤖 **自举证明** | 整个仓库从 git init 到所有代码均由 GA 自主完成 |
| 🪶 **极致省 Token** | < 30K 上下文窗口，同类 Agent 的 1/10 ~ 1/30 |
| 💰 **完全开源免费** | MIT 协议，零费用，仅需自备 API Key |

---

#### 常见问题

**Q: 必须使用 DeepSeek 吗？**
A: 不一定。GA 支持多种模型协议，你可以随时在 `mykey.py` 中添加或切换。推荐 DeepSeek V4 是因为性价比高，且 GA 已充分适配。

**Q: 如何更新到最新版？**
A: 在 GA 项目目录下执行 `git pull`，然后让 GA 自己读取更新日志即可。

**Q: 遇到兼容性问题？**
A: 确保使用 **Python 3.11 或 3.12**（3.14 不兼容）。运行 `python --version` 检查。
