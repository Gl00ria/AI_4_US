### Why [graphify](https://github.com/safishamsi/graphify)?

When you ask the model about a large repo, it has to grep through files every time, which wastes **Tokens**. It saves about 71x fewer tokens per query vs reading the raw files
So what it does is:

- Builds a queryable knowledge graph
- Input supported (Code, Docs, PDFs, screenshots, whiteboard, YT Videos & Audio files)

### How It works?

It works in three phases with no LLM cost:

1. **AST (Abstract Syntax Tree):** Uses **Tree-Sitter** to walk every file looking for (Classes, Functions, Imports) and Call graphs.
2. Transcribes any Audio or Video
3. Sends the data to the model running

### Graphify's output

- **graph.json:** the full graph, query it anytime without re-reading your files
- **graph.html:** Open via browser to (click nodes, filter, search)
- **GRAPH_REPORT.md:** this highlights (key concepts, surprising connections, suggested questions)
