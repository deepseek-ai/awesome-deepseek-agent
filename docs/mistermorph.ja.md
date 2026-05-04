[English](./mistermorph.md) | [简体中文](./mistermorph.zh-CN.md) | [日本語](./mistermorph.ja.md) · [← 戻る](../README.md)

# Morph と連携する

Morph は、個人またはチーム向けの AI Agent を構築するためのオープンソースの実行環境と Console です。CLI、Web Console、チャット連携、tools、skills、memory、MCP、DeepSeek などの OpenAI-compatible provider をサポートします。

- **GitHub:** <https://github.com/quailyquaily/mistermorph>

## 1. Morph をインストールする

一番簡単な方法は、[GitHub Releases](https://github.com/quailyquaily/mistermorph/releases) からデスクトップアプリをダウンロードすることです。デスクトップアプリはローカルのバックエンドを起動し、Console UI を提供します。

CLI を使う場合、またはサーバー上で Morph を実行する場合は、公式インストールスクリプトを使います。

```sh
curl -fsSL -o /tmp/install-mistermorph.sh https://raw.githubusercontent.com/quailyquaily/mistermorph/refs/heads/master/scripts/install-release.sh
sudo bash /tmp/install-mistermorph.sh
```

インストール後、CLI が使えることを確認します。

```sh
mistermorph --help
```

## 2. DeepSeek を設定する

推奨される方法は Console UI を使うことです。

デスクトップアプリを使う場合は、アプリを開いて Setup または Settings -> LLM に進みます。

ローカル CLI 環境で使う場合は、Console を起動します。

```sh
mistermorph console serve --allow-empty-password
```

コマンドが表示するローカル URL を開き、Setup または Settings -> LLM で次の値を設定します。

- Provider: `deepseek`
- Model: `deepseek-v4-pro`
- API Key: DeepSeek API key

DeepSeek API key は [DeepSeek Platform](https://platform.deepseek.com/api_keys) で取得できます。

より速く低コストなデフォルトにしたい場合は、Model に `deepseek-v4-flash` を指定します。

設定ファイルを直接編集したい場合は、まず setup command を実行して Morph のデフォルトの状態ファイルと設定ファイルを作成します。

```sh
mistermorph install
```

次に `~/.morph/config.yaml` を編集し、LLM provider を設定します。

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-pro
  api_key: ${DEEPSEEK_API_KEY}
```

DeepSeek 公式 API を使う場合は、`provider` に `deepseek` を指定します。`provider: openai` は、独自の OpenAI-compatible endpoint を指定する場合だけ使います。

Shell で DeepSeek API key を設定します。

```sh
export DEEPSEEK_API_KEY="sk-..."
```

`deepseek-v4-flash` を使う場合は、次のように設定します。

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
```

## 3. Morph を実行する

コマンドラインからタスクを実行します。

```sh
mistermorph run --task "このプロジェクトのファイル一覧を確認し、何をするものか要約してください。"
```

または、ローカル Console サーバーを起動します。

```sh
mistermorph console serve
```

## 4. 任意: 専用 LLM profile を使う

Morph は名前付き LLM profile をサポートします。タスクごとに異なる DeepSeek model へルーティングしたい場合に使えます。

```yaml
llm:
  provider: deepseek
  model: deepseek-v4-flash
  api_key: ${DEEPSEEK_API_KEY}
  profiles:
    deepseek_pro:
      provider: deepseek
      model: deepseek-v4-pro
      api_key: ${DEEPSEEK_API_KEY}
      reasoning_effort: high
```

必要に応じて Morph のルーティング設定で、この profile を特定の workflow に割り当てます。
