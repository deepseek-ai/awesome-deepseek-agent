[English](./zenmind.md) | [简体中文](./zenmind.zh-CN.md) · [← Back](../README.md)

# Integrate with ZenMind

ZenMind is an open-source AI agent platform that provides Desktop and mobile clients. It uses the AGWUI protocol for agent interaction and viewport rendering, connects to Chinese model ecosystems such as DeepSeek V4, and supports streaming output, HITL approval, usage telemetry, sandbox sessions, and sub-agent invocation.

- **GitHub:** <https://github.com/linlay/zenmind>
- **Website:** <https://www.zenmind.cc>

#### 1. Install ZenMind

Download the ZenMind Desktop installer from the [official website](https://www.zenmind.cc), then install and launch it for your platform.

You can also build ZenMind from source:

```shell
git clone https://github.com/linlay/zenmind.git
cd zenmind
```

Follow the repository README for the current Desktop packaging and service startup instructions. ZenMind Desktop is the recommended path because it prepares local configuration, initializes the required services, and starts them in the right order.

#### 2. Get a DeepSeek API Key

Go to the [DeepSeek Platform](https://platform.deepseek.com/api_keys), create an API key, and keep it ready for the ZenMind model provider settings.

#### 3. Configure DeepSeek V4 Models

Open ZenMind Desktop, go to the model/provider settings, and add a DeepSeek provider. ZenMind's runtime registry stores providers and models separately. A DeepSeek provider entry looks like:

```yaml
key: deepseek
baseUrl: https://api.deepseek.com
apiKey: sk-your-deepseek-api-key
defaultModel: deepseek-v4-pro
protocols:
  OPENAI:
    endpointPath: /chat/completions
    compat:
      messages:
        preserveReasoningContent: true
      response:
        usage:
          promptTokensDetails:
            cacheHitTokens:
              path: prompt_cache_hit_tokens
            cacheMissTokens:
              path: prompt_cache_miss_tokens
          completionTokensDetails:
            reasoningTokens:
              path: completion_tokens_details.reasoning_tokens
```

Then make sure the DeepSeek V4 model entries are available:

```yaml
key: deepseek-v4-pro
name: DS V4 Pro
provider: deepseek
protocol: OPENAI
modelId: deepseek-v4-pro
isVision: false
isReasoner: true
isFunction: true
maxTokens: 1000000
maxInputTokens: 1000000
maxOutputTokens: 384000
```

```yaml
key: deepseek-v4-flash
name: DS V4 Flash
provider: deepseek
protocol: OPENAI
modelId: deepseek-v4-flash
isVision: false
isReasoner: true
isFunction: true
maxTokens: 1000000
maxInputTokens: 1000000
maxOutputTokens: 384000
```

Use **`deepseek-v4-pro`** as the default model for coding agents and long-running agent sessions. Use **`deepseek-v4-flash`** when you want a faster, lower-latency model for lighter tasks.

DeepSeek V4 supports up to **1 million tokens** of context. In OpenAI-compatible terms, the entries above correspond to `context_window: 1000000` and `max_tokens: 384000`.

#### 4. Start ZenMind Services

In ZenMind Desktop, start the local runtime from the control center. The Desktop app coordinates the core services:

- `zenmind-app-server` for authentication, admin access, and app tokens.
- `agent-platform` for model routing, tools, memory, HITL, usage, and sub-agent orchestration.
- `agent-webclient` for chat, timeline replay, model switching, viewport rendering, and usage display.
- `agent-container-hub` for local sandbox sessions and tool environments.

Wait until the services show as running before opening the agent UI.

#### 5. First Run

Open the ZenMind agent UI, create or select a coding agent, and choose **`deepseek-v4-pro`** as the model. For an agent file, set the model and enable reasoning:

```yaml
modelConfig:
  modelKey: deepseek-v4-pro
  reasoning:
    enabled: true
    effort: HIGH
```

Then send a first prompt such as:

```text
Inspect this repository and summarize the main modules before making changes.
```

For the strongest coding experience, keep reasoning enabled and select **HIGH** or the highest effort level exposed by your ZenMind build. ZenMind surfaces usage snapshots for tokens, cache, reasoning tokens, tool calls, and estimated cost, so you can confirm that DeepSeek V4 is being used during the run.

#### Troubleshooting

- `401` or authentication errors: check that the DeepSeek API key is valid and saved in the ZenMind provider settings.
- Model is missing from the picker: refresh or restart the ZenMind services after editing provider/model configuration.
- Short context behavior: verify that the model entry uses `maxTokens: 1000000`, `maxInputTokens: 1000000`, and `maxOutputTokens: 384000`.
- Reasoning is not visible: confirm that the selected model is `deepseek-v4-pro` and that reasoning effort is set to `HIGH` or the highest available level.

#### Resources

- [ZenMind](https://github.com/linlay/zenmind)
- [ZenMind Website](https://www.zenmind.cc)
- [DeepSeek API Docs](https://api-docs.deepseek.com/)
