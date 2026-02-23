# Exercise 5: Reading Files

## Overview

Implement your first really practical tool: `read_file`. This allows the LLM to read file contents from disk, making it useful for real coding tasks.

## Learning Objectives

- Define tools with parameters
- Parse tool arguments from the LLM
- Handle tool errors gracefully

## Background

A coding agent needs to inspect code files to understand existing implementations, debug issues, or answer questions about codebases. The `read_file` tool is fundamental for these tasks.

## Instructions

### 1. Define the read_file Tool with Parameters

Unlike `get_secret`, this tool needs a parameter (the file path):

```csharp
ChatTool.CreateFunctionTool(
    name: "read_file",
    description: "Reads the contents of a file and returns it as a string",
    parameters: BinaryData.FromString("""
    {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to the file to read"
            }
        },
        "required": ["file_path"]
    }
    """)
)
```

### 2. Parse Tool Arguments

The LLM will provide arguments as JSON:

```csharp
// Example tool call arguments from LLM:
// {"file_path": "secret.txt"}

var arguments = JsonSerializer.Deserialize<Dictionary<string, string>>(
    toolCall.FunctionArguments
);

var filePath = arguments["file_path"];
```

### 3. Implement the Tool Logic

Read the file and return its contents:

```csharp
string ExecuteReadFile(Dictionary<string, string> arguments)
{
    var filePath = arguments["file_path"];

    if (!File.Exists(filePath))
    {
        return $"Error: File '{filePath}' not found";
    }

    try
    {
        var contents = File.ReadAllText(filePath);
        return contents;
    }
    catch (Exception ex)
    {
        return $"Error reading file: {ex.Message}";
    }
}
```

### 4. Wire It Up in Your Tool Dispatcher

```csharp
string ExecuteTool(string toolName, string argumentsJson)
{
    var arguments = JsonSerializer.Deserialize<Dictionary<string, string>>(argumentsJson);

    return toolName switch
    {
        "get_secret" => "42",
        "read_file" => ExecuteReadFile(arguments),
        _ => $"Unknown tool: {toolName}"
    };
}
```

## Acceptance Criteria

Your implementation should pass this test:

**Setup:**
1. Create a file named `secret.txt`
2. Write a unique value to it (e.g., "1234" or a GUID)

**Input:**
```
> Can you tell me the contents of the file secret.txt?
```

**Expected Behavior:**
1. LLM requests `read_file` tool call with argument `{"file_path": "secret.txt"}`
2. Your code reads the file
3. Adds contents to the conversation: "1234"
4. LLM generates response

**Expected Output:**
```
The contents of secret.txt are: 1234
```

(Or similar phrasing that includes the file contents)

## Security Considerations

⚠️ **Warning**: This tool can read ANY file the agent has permissions to access. In production scenario's consider:

- **Path validation**: Restrict to certain directories
- **Blacklists**: Prevent reading sensitive files (e.g., `.env`, private keys)
- **Sandboxing**: Run in a container or restricted environment

For this workshop, we'll skip these protections, but they're critical for production systems!

## Testing Tips

Test various scenarios and watch the LLM try to find its way to the file:

**Different file paths:**
```
> Read the file at C:\temp\test.txt
> What's in ./data/config.json?
```

**Non-existent files:**
```
> Read the file non_existent.txt
```

Should return an error message gracefully.

**Relative vs absolute paths:**
```
> Read ./secret.txt
> Read C:\projects\secret.txt
```

## Common Pitfalls

- **Not handling file not found**: Always check if file exists and make sure the LLM sees clear error messages in the conversation so it knows what went wrong.
- **Incorrect argument parsing**: Make sure you extract the `file_path` correctly
- **Path separators**: Windows uses `\`, Unix uses `/` - consider normalizing paths or put your OS in the system prompt.
- **Encoding issues**: `File.ReadAllText()` uses UTF-8 by default; ensure your test files match

## Debugging Tips

Add logging to see what the LLM is requesting:

```csharp
Console.WriteLine($"[Tool Call] {toolCall.FunctionName}({toolCall.FunctionArguments})");
```

This helps verify the LLM is calling the tool correctly.

## Quiz Yourself

- [ ] How does defining a tool with parameters differ from a parameterless tool like `get_secret`? What extra information must you provide to the LLM and what extra data does the LLM send in a tool request message?
- [ ] What should your tool return when the requested file doesn't exist — and why is it important to return an error message rather than throwing an exception?
- [ ] What security risks does a `read_file` tool introduce, and what mitigations would you consider for a production system?

## Next Steps

Once you can read files, proceed to [Exercise 6: Writing Files](./06-writing-files.md) to enable your agent to create and modify files.
