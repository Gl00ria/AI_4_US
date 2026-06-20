### What is Claude Code?
Its an agentic coding tool that:
- Read and Understand your code base
- Edits your files
- Runs commands
- Integrates with your dev tools


### What is Claude VS Claude Code?
Claude code has a direct access to your files, it works like an AI agent.


### Most Important Features:
- **The CLAUDE.md File:** its a file you add to the root of your project, and Claude Code reads it automatically every time you start a session. The contents of the CLAUDE.md file are appended to your prompt. Without it, Cladue Code will scan the whole project each time.
- **Subagents:** break tasks down and run component tasks in parallel, improving your context management. Each subagent operates in its own isolated context window.
- **Skills:** these are folders of instructions that Claude Code can discover and use to handle tasks more accurately. Each skill lives in a SKILL.md file with a name and description. Skills do load only on demand.
- **Hooks:** lets you run commands at a specific point. Example: running code formatter after each file edit.
- **SDK:** lets you run Claude Code programmatically from your application and scripts. Available for (Python & TypeScript) by the time of writing this.

Cladue Code also can be integrated with Github & MCP servers.


### Cluade.md VS Skills VS Slash Commands:
- **Claude.md:** loads into every conversation.
- **Skills:** loads on demand when they match your request.
- **Slash Commands:** You have to manually invoke them.


### How to use Cladue Code Effectively?
Explore --> Plan --> Code --> Commit


### Useful Cladue Code Commands:
- **(/init):** Analyze your entire code base
- **(@file_name):** Let Cladue look at a specific file
- **(/plan):** Lets Cladue to make a thorough exploration before implementing changes
- **(/effort):** Control how Claude reasons through a problem
- **(/memory):** When Cladue does mistakes, you can use this to add a note about the correct approach to its memory "project related". Or you can just edit the "CLAUDE.md" file.
- **(/rewind):** Self explanatory. Or press "ESC" twice.
- **(/compact):** Summarize the entire conversation history while preserving the key info Claude's learned. Useful when you have a long conversation and contains important context.
- **(/clear):** nuke all the conversation and start with a new context

### Custom Commands:
You can create a custom command by adding "My_New_Command.md" file inside (./claude/commands/) then use "/My_New_Command" from Claude code's chat window normally as you'd with any other command.

Example Taken from [Custom Commands](https://anthropic.skilljar.com/claude-code-in-action/303234).
"Audit.md":
```
This audit command does three things:

    1. Runs npm audit to find vulnerable installed packages
    2. Runs npm audit fix to apply updates
    3. Runs tests to verify the updates didn't break anything
```

You also can Create a Command With Arguments
Example Taken from [Custom Commands](https://anthropic.skilljar.com/claude-code-in-action/303234).
"write_tests.md ":
```
Write comprehensive tests for: $ARGUMENTS

Testing conventions:
* Use Vitest with React Testing Library
* Place test files in a __tests__ directory in the same folder as the source file
* Name test files as [filename].test.ts(x)
* Use @/ prefix for imports

Coverage:
* Test happy paths
* Test edge cases
* Test error states
```
the run (/write_tests the use-auth.ts file in the hooks directory )

### Benefits of Custom Commands:
- **Automation**
- **Consistency**
- **Flexibility:** Using arguments to make commands to work with different inputs

