#### Stages of RAG:

The RAG process has **2 stages**:

1. **Indexing**: a pipeline for ingesting data from source and indexing it..
   - **Load**: Load the data.
   - **Split**: Brake large docs into smaller chunks. This helpful for both indexing the data & passing it into the model, as large chunks are harder to search over and it won't fit in the model's context window.
   - **Store**: Store & index the splits, so they can be searched over later. This is done by using a **VictorDB** & **Embedding Models**.
   ```markdown
   Workflow
   Load --> Split --> Embed --> Store
   ```
1. **Retrieve and Generate**:
   - **Retrieve**: Splits/chunks are retrieved from the storage using a **Retriever** based on the user's input.
   - **Generate**: Produce an answer using a prompt that includes both the Question & the Retrieved data.
   ```markdown
   Workflow
   Question --> Retrieve --> Prompt --> LLM --> Answer
   ```
