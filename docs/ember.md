[English](./ember.md) | [简体中文](./ember.zh-CN.md) · [← Back](../README.md)

# Integrate with Ember

Ember is a text-first terminal coding agent written in C++20. The Windows
binary is standalone; the Linux one needs only the system `libcurl.so.4`. It
ships for Windows and Linux, groups models across multiple providers, exposes
thinking-effort control, and can be extended with MCP servers, plugin
executables and sub-agents.

Source and pre-built binaries: <https://github.com/yyfdfsyyf-source/ember>

#### 1. Install Ember

**Windows** — download
[`Ember-0.10.1-win64.zip`](https://github.com/yyfdfsyyf-source/ember/releases/download/v0.10.1/Ember-0.10.1-win64.zip)
from the [release page](https://github.com/yyfdfsyyf-source/ember/releases/latest)
(the same bytes are also committed in-tree under
[`releases/`](https://github.com/yyfdfsyyf-source/ember/tree/main/releases)),
unzip it, and run `agent.exe`.

**Linux** — download
[`ember-0.10.1-linux-x86_64.tar.gz`](https://github.com/yyfdfsyyf-source/ember/releases/download/v0.10.1/ember-0.10.1-linux-x86_64.tar.gz),
then:

```bash
tar -xzf ember-0.10.1-linux-x86_64.tar.gz
cd ember-0.10.1-linux-x86_64
./ember --version
```

The Linux binary is dynamically linked against the system `libcurl.so.4` and
needs glibc 2.30+; the package ships a `verify.sh` that checks both before you
run anything.

**Build from source** (Windows needs a plain `g++`; CMake + Ninja works on both
platforms):

```powershell
.\build.ps1        # Windows -> out/agent.exe plus the test binaries
```

```bash
cmake -B build -G Ninja && cmake --build build && ctest --test-dir build
./build-linux.sh   # what produces the released Linux binary: out-linux/dynamic/ember
```

Check the copy you have with `agent.exe --version` / `./ember --version`.

#### 2. Configure DeepSeek

Ember reads `settings.json` from the working directory (override with
`--config PATH`). Precedence is: built-in defaults < `AGENT_*` env vars <
`settings.json` < command-line options.

```json
{
  "model": "deepseek-v4-pro",
  "thinking": "max",
  "providers": [
    {
      "name": "deepseek",
      "base_url": "https://api.deepseek.com/v1",
      "api_key_env": "DEEPSEEK_API_KEY"
    }
  ],
  "groups": [
    { "name": "ds", "provider": "deepseek", "models": ["deepseek-v4-pro", "deepseek-v4-flash"] }
  ]
}
```

- `api_key_env` names an environment variable, so the secret stays out of the
  file. Set it with `setx DEEPSEEK_API_KEY <key>` (Windows) or
  `export DEEPSEEK_API_KEY=<key>` (Linux), or use `"api_key"` inline instead.
- A **group** binds a list of models to one provider. `/model` lists them
  grouped, and `/model <N|NAME>` switches the model **and** its base URL and
  key in one step. Models in no group fall back to the top-level
  `base_url`/`api_key`.
- DeepSeek speaks the effort spelling natively (`"reasoning_effort"`), which is
  Ember's default `thinking_style`, so you do not need to set `thinking_style`
  for DeepSeek.

Get your API Key from the [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. Run and select the model

```bash
cd /path/to/your/repo
ember            # or agent.exe on Windows
```

- `/model` lists every configured model; `/model deepseek-v4-flash` switches.
- `/think` shows the current thinking level, `/think max` (or `high`, `low`,
  `none`) changes it live. The top edge of the frame shows `[think:max]` (nothing
  extra while the level is `auto`, which sends no field at all). At startup use
  `--thinking NAME` or `AGENT_THINKING`.
- `/settings` opens the built-in editor for the same keys, and `/help` lists
  all commands.

DeepSeek names three effort levels — `low`, `high`, `max`. Ember sends whatever
level you pick verbatim as `reasoning_effort`, so `max` reaches DeepSeek as-is.

#### Context window

DeepSeek V4 supports up to 1 million tokens of context. Ember has no per-model
`context_window` field; it manages the conversation with a **budget** instead:

- `"budget"` (or `--budget N`): the token budget that triggers summarizing the
  oldest part of the conversation. The default is `6000`, which suits short
  focused edits — raise it (for example `200000`) if you want Ember to keep a
  long raw history before it compresses. `0` disables compression.
- `"prune_before_send"` (default `true`): drops redundant tool output before
  each request.
- `--tool-cap N`: byte cap per tool result (default 4096; `0` = unlimited).

Because compression is budget-driven rather than capped at a fixed context
size, Ember stays inside DeepSeek's 1M limit simply by keeping `budget` below
it.

#### Going further

Ember's tool set includes shell execution, file editing with structured
patches, headless browser automation over CDP, Windows desktop automation via
UI Automation, parallel sub-agents, and PTC batch tool runs. MCP servers and
plugin executables register additional tools; conversations persist per session
so `/sessions` can resume earlier work.
