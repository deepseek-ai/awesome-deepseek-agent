[English](./deepseek-harness-github.md) | [简体中文](./deepseek-harness-github.zh-CN.md) · [← 返回](../README.zh-CN.md)

# 接入 DeepSeek Harness for GitHub

[DeepSeek Harness for GitHub](https://github.com/Lixiaoyiao/deepseek-harness-action) 是一个 **社区维护** 的 GitHub Action，可用于：

- PR review（PR 事件）
- CI 诊断（工作流失败事件）
- 受信任修复与 Issue 自动化实现（仅当 `allow-write: "true"` 时）

> 当前仓库仅实现了 `action.yml` 中实际公开的输入项。

#### 1. 安装

在目标仓库新增 `.github/workflows/dsh-review.yml`：

```yaml
name: DSH review

on:
  pull_request_target:
    types: [opened, synchronize, ready_for_review, reopened]

permissions:
  contents: read
  pull-requests: write

concurrency:
  group: dsh-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  review:
    if: github.event.pull_request.draft == false
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.base.sha }}
          persist-credentials: false
          fetch-depth: 1
      - uses: Lixiaoyiao/deepseek-harness-action@v0.2.0
        with:
          deepseek-api-key: ${{ secrets.DEEPSEEK_API_KEY }}
```

#### 2. 配置 `DEEPSEEK_API_KEY`

1. 在仓库进入 `Settings → Secrets and variables → Actions`。
2. 新增 `DEEPSEEK_API_KEY`。
3. 填入你的 DeepSeek API Key（`sk-` 开头）。

API Key 获取地址：[DeepSeek 开放平台](https://platform.deepseek.com/api_keys)。

#### 3. GitHub Actions 快速开始

打开一个非草稿 PR，即可触发：

- checkout 到 PR base 的可信提交
- 发送 PR 上下文给 DeepSeek Harness
- 发布 review summary 与必要时的逐行评论

你还可以配合官方示例文件使用：

- `examples/commands.yml`：`@dsh review`、`@dsh diagnose`、`@dsh fix`、`@dsh implement`
- `examples/ci-diagnose.yml`：CI 失败自动诊断
- `examples/ci-auto-fix.yml`：受信任 CI 自动修复

#### 4. 第一次运行与验证

1. 提交任意改动并打开 PR。
2. 在 PR 页面确认：
   - 是否出现 action bot 的 review summary
   - 是否在相关代码行出现 inline comments
3. 在 Actions 里查看本次 run，确认：
   - 主步骤成功
   - 输出状态清晰（`conclusion`/`operation`）
   - `result-json` 记录完整
4. 要触发命令式复查，在 PR/Issue 评论第一行输入：

```text
@dsh review
```

无需再次推送即可刷新 review。

若要测试修复流程：

```text
@dsh fix
```

请在受信任 write 工作流中开启 `allow-write: "true"`，并配置 `run-tests` + `test-commands`。

#### 5. 注意事项

- 示例中使用的是当前公开模型：`deepseek-v4-pro`、`deepseek-v4-flash`。
- 本 Action 的输入里没有 `model` 字段。
- 本项目为社区维护且非官方产品（非 DeepSeek 官方/GitHub 官方）。
