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
- **Hooks:** it lets you run commands at a specific point. Example: running code formatter after each file edit.


### Cluade.md VS Skills VS Slash Commands:
- **Claude.md:** loads into every conversation.
- **Skills:** loads on demand when they match your request.
- **Slash Commands:** You have to manually invoke them.


### How to use Cladue Code Effectively?
Explore --> Plan --> Code --> Commit
