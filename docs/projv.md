[English](./projv.md) | [简体中文](./projv.zh-CN.md) · [← Back](../README.md)

# Integrate with proJV

proJV is a native C++20 terminal agent built for DeepSeek: a single ~3.4 MB binary with no runtime to install, a codebase every line of which was written by proJV itself, and an extension model where a skill, a role, a tool and a theme are all just files — no MCP layer, no plugin registry. It talks to `api.deepseek.com` directly, supports DeepSeek-V4-Pro and DeepSeek-V4-Flash with the full 1M-token context window, and behaves the same locally, over SSH and inside tmux.

- **GitHub:** <https://github.com/MilesKHuang/proJV>

#### 1. Install proJV

Download the archive for your platform from the [Releases page](https://github.com/MilesKHuang/proJV/releases):

- Windows: `proJV-0.6.3-windows-x64.zip`
- Linux: `proJV-0.6.3-linux-x64.tar.gz`

```sh
# or build from source (CMake 3.16+ and a C++20 compiler)
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

Unpack anywhere. You get `proJV_tui` (`.exe` on Windows), `projv_files/`, the READMEs and the license. **Keep the executable and `projv_files/` together — that pair is the installation.** Everything else (FTXUI, SQLiteCpp, nlohmann/json, toml++, loguru) is vendored; no vcpkg, conan, npm or pip.

The archive is larger than the binary because `projv_files/` also carries the CJK font the TUI renders with, the themes and the example skills.

- Windows: the binary is unsigned, so SmartScreen may warn — "More info" → "Run anyway".
- Linux: the release build targets glibc desktops; if you build from source, `sudo apt-get install -y libcurl4-openssl-dev` (Debian/Ubuntu) is the only package you need to add.

#### 2. Get a DeepSeek API Key

Create a key on the [DeepSeek Platform](https://platform.deepseek.com/api_keys). proJV asks for it in a configuration window on first launch; `F2` reopens that window later. The key is stored in `projv_files/config.toml`, next to the executable — packaged builds deliberately exclude that file, so your key and history never ship.

#### 3. Point proJV at your project

```sh
cd /path/to/my-project
./proJV_tui          # Windows: proJV_tui.exe
```

`workspace_path` is the only directory tree the file tools may touch, and **an empty value means "the folder holding the executable"**. Set it to your project in the configuration window (`F2`) before asking the agent to edit code; the tools are re-registered with the new root as soon as you save.

#### 4. First message

Type a request and press `Enter`. Multi-step work shows up in the chat and, when the model plans, in the TODO panel (`F9`). `/help` lists the in-chat commands. Two skills ship as examples: `/monica <dir>` runs ten concurrent workers over a repository, `/bigbang <topic>` runs a three-role debate that ends in one execution document.

#### 5. Key shortcuts

| Key | Action |
|-----|--------|
| `Enter` | Send the prompt |
| `Esc` | Cancel the running turn; quit when idle |
| `F1` | About |
| `F2` | Configuration (API key, model, workspace) |
| `F3` | New chat |
| `F5` | Open a stored session |
| `F6` / `F7` | Switch theme / theme editor |
| `F8` | Toggle the reasoning chain (summary ↔ full trace) |
| `F9` | Toggle the TODO panel |
| `F10` | Switch model (list fetched from the API) |
| `Tab` | Cycle role (built-in prompts in `projv_files/prompts/`) |
| `PgUp` / `PgDn` | Scroll the chat |
| `Ctrl+C` | Quit (the session is checkpointed) |

#### 6. Configuration

`projv_files/config.toml` sits next to the binary and is created on the first save.

| Key | Meaning |
|-----|---------|
| `api_key` | DeepSeek API key |
| `model` | `deepseek-v4-flash` (default) or `deepseek-v4-pro` |
| `base_url` | API endpoint, default `https://api.deepseek.com` |
| `max_tokens` | reply budget, default `65536` |
| `temperature` | `0.0` by default; the API docs note it has no effect in thinking mode |
| `reasoning_effort` | thinking depth: `none` / `low` / `high` / `max`, default `max` |
| `workspace_path` | the only tree the file tools may touch; empty = the executable's folder |
| `context_window` | `0` = auto (the full V4 window) |
| `theme` | active theme name |
| `python_path` | interpreter for `projv_files/pytool/` tools; empty = `python` from `PATH` |
| `cpp_compiler_path`, `clang_format_path` | optional, for build tasks and `format_file` |
| `[model_prices]` | model-id prefix → input/output price per 1M tokens, for the cost estimate |

#### 7. Thinking mode and reasoning effort

Thinking is on by default — proJV turns it on the way the API documents it, and sends `reasoning_effort` so you get the deepest level, `max`, out of the box. The API's own default level is `high`, so `max` here is a deliberate upgrade, not a requirement:

| `reasoning_effort` | What proJV sends |
|---|---|
| `max` / `high` / `low` | `reasoning_effort` with that level; `F8` shows the chain |
| `none` | `thinking: {"type": "disabled"}` and no effort field (the documented way to switch thinking off) |
| anything else | ignored with a log line; proJV falls back to the official default, `high` |

The aliases the API documents (`minimal` → `low`, `medium`/`xhigh` → `high`, `ultra` → `max`) are accepted too. The full reasoning content is kept and replayed on every request, so tool calling works with thinking on.

#### 8. The full 1M-token context window

DeepSeek V4 supports a 1M-token context window and proJV uses all of it: `context_window = 0` (the default) resolves to **1,048,576 tokens** for both V4 models, minus the reply budget. Long sessions are compacted automatically as pressure grows — an early summary replaces the oldest messages — and `/compress` triggers the same pass on demand. The status bar shows the current pressure.

#### 9. `AGENTS.md`

Put an `AGENTS.md` in the workspace root and proJV injects it into every new conversation, wrapped in `[AGENTS.MD] ... [END AGENTS.MD]`, right after the directory tree. It is the place for build commands and project rules that the agent cannot infer from the code. The file is capped at 16 KiB per conversation, and edits take effect in the next conversation (`F3`) or after `/clear`.

#### 10. Skills, roles, tools and themes — all files

| What | Where | How to use |
|---|---|---|
| Skills | `projv_files/skills/<name>/` (`config.json`, one `.md` per agent, `tools/*.json`) | `/skill list`, then `/<name> <topic>`; `skill_maker` writes new ones |
| Roles | `projv_files/prompts/*.md` | `Tab` cycles them |
| Extra tools | `projv_files/pytool/<name>/` (Python) | picked up at startup; needs `python_path` |
| Themes | `projv_files/theme/*.json` | `F6` switches, `F7` edits with live preview |

#### 11. Images

On a Flash model you can attach images with `@path` (directories expand, up to 8 per message), and the agent can fetch them itself: it calls `view_image(paths=[...])`, the current turn ends, and the images arrive in the next turn as a user message marked `(auto)`. `deepseek-v4-pro` does not accept images and proJV refuses to attach them instead of failing with a 400.

#### 12. Pricing

Snapshot of the official [pricing page](https://api-docs.deepseek.com/quick_start/pricing) — check it before quoting:

| Model | Input / M tokens | Output / M tokens | Cache hit / M tokens |
|-------|-----------------|-------------------|----------------------|
| deepseek-v4-pro | $0.435 | $0.87 | $0.003625 |
| deepseek-v4-flash | $0.14 | $0.28 | $0.0028 |

The cost estimate in the status bar uses the `[model_prices]` table in `config.toml`, so update it when prices move.
