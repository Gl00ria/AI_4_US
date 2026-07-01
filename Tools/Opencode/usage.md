### Commands

Use '/' to access the built-in commands, read the [DOCs](https://opencode.ai/docs/commands/#create-command-files) to learn how to create a custom command.

Its important to know that a command can also accept '$ARGUMENTS'.

### Agents

There are 2 Modes/Agents for Opencode that you can switch between them using 'Tab':

1. **Plan Agent:** Used to Create Plan, Analyze or provide changes suggestions.
2. **Build Agent:** Here where it starts working and making changes to your project.

---

### Sub-Agent

A sub-agent can be invoked using '@'.

- **@general**:A general-purpose agent for researching complex questions and executing multi-step tasks.
- **@explore**:read-only agent for exploring codebases. Cannot modify files. Use this when you need to quickly find files by patterns, search code for keywords, or answer questions about the codebase.
- **@scout**: A read-only agent for external docs and dependency research. Use this when you need to clone a dependency repository into OpenCode’s managed cache, inspect library source, or cross-reference local code against upstream implementations without modifying your workspace.
- **@compaction:** Hidden system agent that compacts long context into a smaller summary. It runs automatically when needed and is not selectable in the UI.
- **@summary:** Hidden system agent that creates session summaries. It runs automatically and is not selectable in the UI.

---

To create an agent run:

```Bash
opencode agent create
```

See the [DOCs](https://opencode.ai/docs/agents/#json) to learn how to customize an agent in both (md & json) format.
