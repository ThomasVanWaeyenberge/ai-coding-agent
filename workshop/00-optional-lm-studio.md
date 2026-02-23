# Exercise 0: Explore Local LLMs with LM Studio (Optional)

## Overview

This step is optional, but highly recommended if you want to understand how LLMs work at a fundamental level. You'll download and experiment with a local language model using LM Studio, which allows you to run open-weight models entirely on your own machine without relying on external APIs.

You'll even be able to use this local model as the beating heart of the coding agent we'll build today!

## Learning Objectives

- Understand how to download and run local LLM models
- Experiment with model parameters (temperature, top_p, etc.)
- Learn how to interact with LLMs via HTTP API

## Instructions

### 1. Install LM Studio

Download and install [LM Studio](https://lmstudio.ai/) for your operating system.

### 2. Download a Model

Once LM Studio is installed:

1. Open LM Studio
2. Navigate to the model search/download section
3. Download a small local model, such as:
   - **Qwen/Qwen2.5-Coder-7B-Instruct-GGUF** (recommended for this workshop if you have limited VRAM available)
   - Other lightweight models with tool-calling capabilities

**Note**: Larger models provide *much better* results but require *much more* RAM and processing power. Start with a very small 7B parameter model for this exercise.

### 3. Chat with the Model

1. Load the downloaded model in LM Studio
2. Start a chat conversation
3. Experiment with the settings:
   - **Developer mode**: See raw request/response data
   - **Temperature**: Controls randomness (0.0 = deterministic, 1.0 = creative)
   - **Top P**: Controls diversity of token selection
   - **Max new tokens**: Limits response length

Try asking the model questions and observe how different settings affect its responses.

### 4. Use the Local Server API

LM Studio can expose your local model as an OpenAI-compatible API server:

1. In LM Studio, start the local server (usually on `http://localhost:1234`)
2. Enable settings like:
   - **Verbose logging**: See detailed request/response logs
   - **Log incoming tokens**: Watch tokens being generated in real-time

3. Test the API using curl:

```bash
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder-7b-instruct",
    "messages": [
      {"role": "user", "content": "Hello, who are you?"}
    ]
  }'
```

Or use Postman or equivalent tools to send requests and inspect responses.

## Key Takeaways

- Local LLMs give you full control and privacy
- Model parameters significantly affect output quality and style
- The OpenAI API format is a standard that many tools support (although "agent SDK's" are probably more fit for typical agentic use cases)
- You can use local models for basic tasks

## Quiz Yourself

- [ ] What is the difference between running a model locally versus using a cloud API? What are the trade-offs?
- [ ] How does the `temperature` parameter affect model output, and when would you want it set to 0 versus a higher value?
- [ ] Why do many local model servers (like LM Studio) expose an OpenAI-compatible API format? What advantage does this give you?

## Next Steps

Once you're comfortable with how LLMs work, proceed to [Exercise 1: Hello World](./01-hello-world.md) to start building your coding agent.
