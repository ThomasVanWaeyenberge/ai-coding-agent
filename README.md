# AI Coding Agent Workshop

Build your own working AI coding agent from scratch. For educational purposes only.

## Inspiration

This workshop was modeled after Geoffrey Huntley's amazing blog post [how to build a coding agent: free workshop](https://ghuntley.com/agent/)

## Overview

This workshop guides you through building a functional AI coding agent that can:
- Can be fully tweaked by using a system prompt
- Maintain conversational context
- Use tool calling to interact with the system
- Read and write files
- Execute code and shell commands

By the end, you'll understand the core concepts behind AI assistants like GitHub Copilot, Cursor, and Claude Code.

## Prerequisites

- Advanced (networking, async, IO) programming knowledge in your chosen language (C#, Python, JavaScript, etc.)
- Familiarity with http APIs and JSON
- A development environment set up
- Either:
  - LM Studio with a local model (highly recommended for learning about LLM's), OR
  - An OpenAI API key provided by the facilitator

## Can I use AI to build this agent for me?

Yes. But remember that the goal of this workshop is to understand how these things work by building one yourself. Make sure to work step by step and verify your understanding at each stage. The "Quiz Yourself" sections are designed to help with this. If in doubt, ask your AI clarifying questions or call over your facilitator to discuss the exercise topics more in detail.

## Workshop Exercises

Follow these exercises in order. Each step builds upon the previous one:

### 0. [Explore Local LLMs with LM Studio](./workshop/00-optional-lm-studio.md) *(Optional)*
Get hands-on experience with local language models before building your agent.

### 1. [Hello World - Building Your First REPL](./workshop/01-hello-world.md)
Create a basic conversation loop that sends messages to an LLM and displays responses.

### 2. [Conversation History](./workshop/02-conversation-history.md)
Implement memory so your agent can maintain context across multiple turns.

### 3. [Adding a System Prompt](./workshop/03-system-prompt.md)
Learn how to control LLM behavior using system messages.

### 4. [Tool Calling Basics](./workshop/04-tool-calling-basics.md)
Understand the fundamentals of function calling with a simple `get_secret` tool.

### 5. [Reading Files](./workshop/05-reading-files.md)
Implement a practical tool that allows the LLM to read file contents.

### 6. [Writing Files](./workshop/06-writing-files.md)
Enable your agent to create and modify files on disk.

### 7. [Running Scripts](./workshop/07-running-scripts.md)
Add the ability to execute shell commands and scripts. ⚠️ **Use with caution!**

## Expected Time

- Core exercises (1-7): ~60-90 minutes
- With optional LM Studio exploration: +30 minutes

## Tips for Success

- **Work incrementally**: Complete each exercise before moving to the next
- **Test frequently**: Verify each feature works before adding complexity
- **Keep it simple**: Don't over-engineer early exercises, we'll be pressed for time already
- **Consider automated testing**: End-to-end automated tests save time on regression testing

## What You'll Learn

- How LLMs process conversations and maintain context
- The OpenAI chat completion API format
- Tool calling / function calling mechanisms
- Architecture of AI agents with tool calling capabilities
- Security considerations for AI agents with system access

## Reference Implementation

A complete C# implementation is available in this repository for reference. See `JCode/ChatCommand.cs` for the main implementation and `JCode.Tests/Tests.cs` for test examples.

## Safety Warning

⚠️ **Important**: Exercise 7 (Running Scripts) allows the AI to execute arbitrary commands on your system. This can be dangerous!

## Stretch Goals

Completed the workshop? Here are ideas for taking your agent further. Each represents a real capability found in production AI coding agents.

### Context Window Compression

As conversations grow, you'll eventually hit the model's context window limit. Implement a strategy to compress older messages — for example, by summarizing earlier turns into a single system message while keeping recent messages intact. This lets your agent handle long sessions without losing important context.

### Spawning and Managing Sub-Agents

Instead of handling everything in a single conversation, your agent can delegate subtasks to separate agent instances. For example, a "research" sub-agent could explore the codebase while the main agent continues planning. This requires managing multiple conversations, passing context between them, and merging results.

### MCP (Model Context Protocol) Integration

[MCP](https://modelcontextprotocol.io) is an open standard for connecting AI agents to external tools and data sources. Instead of hardcoding tools like `read_file` and `write_file`, you can implement an MCP client that dynamically discovers and uses tools exposed by MCP servers — making your agent extensible without code changes.

### Streaming Responses

Show the model's output token-by-token as it's generated instead of waiting for the full response. This dramatically improves perceived responsiveness and lets users interrupt early if the model is heading in the wrong direction.

### Human-in-the-Loop Confirmation

Add a confirmation step before executing dangerous operations (file writes, script execution). The agent presents what it intends to do and waits for user approval. This is how production agents like Claude Code and GitHub Copilot balance autonomy with safety.

### Multi-Tool Calls Per Turn

Some models can request multiple tool calls in a single response (e.g., reading three files at once). Implement parallel tool execution to speed up multi-step workflows.

### Persistent Memory Across Sessions

Save and reload conversation history so your agent can pick up where it left off. Consider what should be persisted (full history? a summary?) and how to handle stale context.

## Next Steps After the Workshop

Happy building! 🤖
