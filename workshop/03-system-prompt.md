# Exercise 3: Adding a System Prompt

## Overview

Learn about different message types in LLM conversations and how system prompts control model behavior. You'll enhance your REPL to include a system message that guides how the model responds.

## Learning Objectives

- Understand the three types of chat messages: system, user, and assistant
- Learn how system prompts influence model behavior
- Modify your agent to load and use a system prompt

## Background: Message Types

In chat-based LLMs, conversations consist of different message roles:

- **System**: Instructions that set the model's behavior, personality, or constraints
- **User**: Messages from the human user
- **Assistant**: Responses from the LLM

System messages are powerful because they establish context that persists throughout the conversation.

## Instructions

### 1. Create a System Prompt

Create a system message that instructs the model to behave in a specific way. For testing purposes, use something distinctive like:

`system-prompt.md:`
```
You are a helpful assistant who always talks like a pirate.
Respond to every message in pirate speak, using phrases like "Ahoy matey!", "Arr", and "ye" instead of "you".
```

### 2. Store the System Prompt

Choose one of these approaches:

**Option A: Load from a file**
- Create a file `system-prompt.md`
- Read the file contents at startup

**Option B: Hardcode it**
- Define the system prompt as a string constant in your code

### 3. Modify Your Chat API Call

Update your LLM API call to include the system message as a first separate message:

```
[
    {"role": "system", "content": "You are a helpful assistant who talks like a pirate..."},
    {"role": "user", "content": user_input}
]
```

## Acceptance Criteria

Your implementation should pass this test:

**Setup:**
- System prompt configured to make the model talk like a pirate

**Input:**
```
> Hi there!
```

**Expected Output:**
```
Ahoy matey! How can I be of service to ye today?
```

(Note: The exact phrasing may vary, but the response should clearly be in pirate speak with words like "Ahoy", "matey", "ye", etc.)

## Common Pitfalls

- **Forgetting to include the system message**: Make sure it's the first message in your messages array
- **Not resending the system message**: Each API call should include the system message

## Experiment!

Try different system prompts to see how they affect behavior:
- "You are a helpful coding assistant. Always provide code examples and nothing else if not explicitly requested."
- "You are a Shakespearean poet. Respond in the style of Shakespeare."
- "You are a terse assistant. Keep all responses under 10 words."

## Quiz Yourself

- [ ] What is the difference between a system message and a user message, and why does the system message come first?
- [ ] If you remove the system prompt between subsequent turns, will the model still behave as instructed? Why or why not?
- [ ] Can a clever user prompt override the system prompt's instructions? What does this imply about security?

## Next Steps

Once you can control the model's behavior with system prompts, proceed to [Exercise 4: Tool Calling Basics](./04-tool-calling-basics.md) to give it real capabilities.
