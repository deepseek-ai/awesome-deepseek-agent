[English](./dsh_session_export.md) | [简体中文](./dsh_session_export.zh-CN.md) · [← Back](../README.md)

# Integrate with dsh-session-export

dsh-session-export is an open-source plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) — DeepSeek's official agent runtime. It adds a `/transcript` command that exports a finished or running session as a human-readable transcript written directly to a host path, and (since v0.2.0) an `/archive` command that writes raw session logs as per-session ZIP backups on any backend. Where the shipped export tooling downloads a raw log ZIP through the browser, this plugin renders what you actually read: the full message flow, tool calls with editor diffs, subagent lineage, and token totals — as Markdown and/or JSON, through any `ctx.sessionQuery` persistence backend (JSONL, SQLite, …).

- **GitHub:** <https://github.com/kittimzhe/dsh-session-export>

#### 1. Prerequisite: a DeepSeek Harness installation

This is an out-of-tree DSH plugin, so it rides on an existing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) setup. No extra API key or model configuration — it reads sessions through DSH's own query engine and inherits whatever provider your harness already uses.

#### 2. Install the plugin into a profile

```
dsh plugin --profile web add dsh-session-export@0.2.0
```

The package declares `dsh.bundle`, so it joins the profile's plugin layer stack automatically — no manual composition edits. Restart the `dsh web` process afterwards so the freshly installed layer is loaded.

#### 3. Run `/transcript` in a session

```
/transcript
```

The command runs on DSH's human-command plane — zero tokens, the result never enters model history — and writes `transcript-<session>-<timestamp>.md` under `<session working directory>/dsh-transcripts/`.

Useful variants:

- `/transcript --json` — also write a machine-readable JSON document
- `/transcript --full` — append the log-only events appendix (command lifecycles, compaction markers)
- `/transcript --out <path>` — custom output path
- `/transcript --id <sessionId>` — export a different session

#### 4. Archive raw session logs with `/archive`

```
/archive
```

Writes a per-session ZIP (`session.jsonl` + `manifest.json`) to a host path — the complete, replay-validated raw log — useful as a backup or for migration. It reads through `sessionQuery.readSession`, so it works on any persistence backend, including SQLite (the official browser `/export` cannot read SQLite's raw artifacts).

Useful variants:

- `/archive --all` — archive every session in the current project directory
- `/archive --since 7d` — restrict `--all` to the last 7 days (`7d`/`12h`/`30m`/`90s`)
- `/archive --id <sessionId>` — a specific session, incl. subagent descendants
- `/archive --out <dir>` — output directory (default `.dsh-archives/`)
