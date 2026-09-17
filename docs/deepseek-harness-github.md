[English](./deepseek-harness-github.md) | [简体中文](./deepseek-harness-github.zh-CN.md) · [← Back](../README.md)

# Integrate with DeepSeek Harness for GitHub

[DeepSeek Harness for GitHub](https://github.com/Lixiaoyiao/deepseek-harness-action) is a **community-maintained** GitHub Action that can run:

- PR review (pull request events)
- CI diagnosis (workflow failure events)
- Trusted repo fix / implement flow (only when `allow-write: "true"`)

> This action currently exposes only action inputs defined in the upstream `action.yml`.

#### 1. Install

Add this workflow file to your target repository as `.github/workflows/dsh-review.yml`:

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
      - uses: Lixiaoyiao/deepseek-harness-action@243926cbd3d013f07b364e188ff84826bfa6f678
        with:
          deepseek-api-key: ${{ secrets.DEEPSEEK_API_KEY }}
```

#### 2. Configure `DEEPSEEK_API_KEY`

1. Open `Settings → Secrets and variables → Actions` in your repository.
2. Add a new secret named `DEEPSEEK_API_KEY`.
3. Paste your DeepSeek API key (starts with `sk-`).

Get the key from [DeepSeek Platform](https://platform.deepseek.com/api_keys).

#### 3. GitHub Actions Quick Start

Open or update any pull request (non-draft). This workflow will:

- Checkout the trusted base commit
- Send PR context to DeepSeek Harness
- Publish a review summary and inline comments if needed

You can also add commands or diagnosis flows from examples:

- `examples/commands.yml` for `@dsh review`, `@dsh diagnose`, `@dsh fix`, `@dsh implement`
- `examples/ci-diagnose.yml` for failed-workflow diagnosis
- `examples/ci-auto-fix.yml` for trusted CI autofix

#### 4. First Run and Verification

1. Push a small change and open a PR.
2. In the PR page, check:
   - A new review summary from the action bot
   - Inline comments on suspicious lines (if any)
3. Open the workflow run log and verify:
   - Step succeeds with expected `conclusion`/`operation`
   - `result-json` is present and includes a clean status
4. To verify command workflows, comment on the PR:

```text
@dsh review
```

The action should post a refreshed review for that PR without waiting on a new push.

If you need fix mode:

```text
@dsh fix
```

and set `allow-write: "true"` in a trusted-write workflow (with `run-tests` and `test-commands` configured).

#### 5. Notes

- This project uses current DeepSeek model names (`deepseek-v4-pro`, `deepseek-v4-flash`) in the examples.
- There is no `model` input in the action interface; model selection is handled in the action runtime configuration paths.
- This repository and action are community-maintained, not an official DeepSeek or GitHub product.
- DeepSeek V4 supports up to **1M tokens** of context (where applicable).
- Max thinking / reasoning effort controls are handled by the upstream DeepSeek runtime and are **not exposed** in this action input schema (the interface only exposes fields in `action.yml`).
