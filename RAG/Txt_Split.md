# What is Text Splitting/Chunking in RAG?

Splitting is the most crucial preprocessing step, it involves breaking down large texts into manageable smaller chunks.

---

# What are the benefits from splitting?

- Consistent processing of varying document lengths.
- Overcome input size limitation of **LLMs**.
- Improving the quality of text representations used in retrieval.

---

# Why splitting?

- **Overcoming input size limitation of LLMs**.
- **Handling non-uniform document lengths:** documents have text of varying sizes, so splitting ensures consistent processing.
- **Improving representation quality**: more focused and accurate representations of each section in the document.
- **Enhancing retrieval precision:** more precise matching of queries to relevant document sections.
- **Optimizing computational resources:** smaller chunks are more memory efficient & allow for parallelization of processing task.

---

# Splitting strategies:

There are 3 strategies for splitting, each with it own advantages.

##### 1. Length Based: in this approach you split the docs based on their length, this one is effective since it ensures that each chunk doesn't exceed the specified limit. The advantages are:

- Straightforward implementation.
- Consistent chunk sizes.
- Easily adaptable to different model requirement.

  - **Types**:

    - **Token Based:** split text based on the number of tokens.
    - **Character Based:** split text based on the number of characters --> more consistent across different types of text.

    ***

##### 2. Text Structured Based: In this approach the splitting strategy is organized into units such as (Paragraphs, Sentences & Words). The advantage is:

- Maintaining natural language flow.

  ***

##### 3. Document Structured Based: some docs has have a specific structure such as (Markdown, JSON, HTML), so its beneficial to structure the document based on its structure.

**Examples:**

- **Splitting Markdown:** based on headers.
- **Splitting HTML:** based on tags.
- **Splitting JSON:** based on objects or array elements.
- **Splitting Code:** based on functions, classes.

**The Advantages:**

- Preserve the logical structure of the document.
- Maintain context within each chunk.
- Effective for downstream tasks like retrieval & summarization.
  ***

##### 4. Semantic Meaning Based: other approaches uses docs or text structure as a proxy for semantic meaning, while this method directly analyzes the text's semantics. The conscript is to split text when there are significant changes in text meaning.

> Difficult to understand, yes i know? see this example on [chunkviz](https://chunkviz.up.railway.app/)
