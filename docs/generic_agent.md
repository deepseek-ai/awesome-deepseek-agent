[English](./deepseek-generic-agent.md) | [简体中文](../zh/deepseek-generic-agent.md) · [← Back Home](../index.md)

# Integrate DeepSeek into GenericAgent

This guide shows how to connect DeepSeek to GenericAgent in three steps: install GenericAgent, configure your DeepSeek API key, and start using it.

## 1. Install GenericAgent

Prepare Python 3.11 or 3.12 first, then get the GenericAgent source code.

Run:

```bash
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
pip install streamlit pywebview
```

If your environment uses `pip3`, run:

```bash
pip3 install streamlit pywebview
```

## 2. Configure the DeepSeek API Key

GenericAgent reads model settings from `mykey.py`.

> ### Quick `mykey.py` Setup
>
> **Step 1: Copy the template**
> In the GenericAgent project folder, copy `mykey_template.py` and rename the copy to `mykey.py`.
>
> **Step 2: Edit `mykey.py`**
> Open `mykey.py` in any text editor. Lines starting with `#` are comments, so they will be ignored at runtime.
>
> There are two ways to add your config:
> - Option A: fill an existing config block and remove the leading `#`
> - Option B: keep the original comments and add a new active config block
>
> In short: lines with `#` do not take effect, lines without `#` do.
>
> **Step 3: Save the file**
> Save `mykey.py` after editing.
>
> **Step 4: Restart GA**
> After changing `mykey.py`, restart GenericAgent so the new config is loaded.

For this DeepSeek setup, put the following config into `mykey.py`:

```python
oai_config = {
    'apikey': 'sk-', #DEEPSEEK_API_KEY
    'apibase': 'https://api.deepseek.com',
    'model': 'deepseek-v4-pro',
}
```

Notes:

- Put your actual DeepSeek key into `apikey`
- Keep `apibase` as `https://api.deepseek.com`
- Use `deepseek-v4-pro` as the model
- If you have multiple active configs in `mykey.py`, GA uses the first active one by default

## 3. Start and Use GenericAgent

### First Launch

From the GenericAgent project directory, run:

```bash
python launch.pyw
```

On Windows, you can also start it by double-clicking `launch.pyw`.

If a Streamlit chat page opens in the browser, or a pywebview window appears, the launch succeeded.

### Let GA Install the Remaining Dependencies

After the first launch, you do not need to install every remaining package manually. Send this message in the chat:

```text
请查看你的代码，安装所有用得上的 python 依赖
```

GA will inspect its own code and install the remaining Python dependencies.

### Start Using It

After that:

1. Open the GenericAgent UI
2. Confirm it is reading the DeepSeek config from `mykey.py`
3. Send a simple test message such as `Hello, introduce yourself`
4. If you get a normal reply, DeepSeek is connected successfully

## Further Reading

If you want the full GenericAgent tutorial covering installation, configuration, capabilities, and advanced usage, see:

- [hello-generic-agent detailed tutorial](https://github.com/datawhalechina/hello-generic-agent)
