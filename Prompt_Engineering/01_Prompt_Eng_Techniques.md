#### Prompt Techniques/Types:

1.  _**Zero Shot**_: giving the **LLM** a description of a task to give you something to start with.
2.  _**One Shot**_: giving the **LLM** 1 example to understand what you are asking for.
3.  _**Few Shot**_: giving the **LLM** examples to understand what you are asking for, helpful when you want to steer the model to certain output, it also help the **LLM** to follow the pattern.

    _**Few Shot**_ depends on the following:

    - Complexity of the task.
    - Quality of the example.
    - Capabilities of the model you are using.

**NOTE:** for (One Shot & Few Shot techniques), Example\s should be (Diverse, High Quality & well written), otherwise you will confuse the model.

4. _**System Prompting**_: set the purpose 'Big Picture' for the **LLM**, it helps the model to define the fundamental capabilities.
5. _**Contextual Prompting**_: provide specific detail/background information related to the task, this helps to provide task-specific info to guide the response.
6. _**Role Prompting**_: assign a character/Identity for the model to adopt, this will change the model's output (style/voice).
7. _**Step Back Prompting**_: improves the performance by prompting the \*_LLM_ to 1st consider a general question related to the task, it allows the model to activate relevant background knowledge before attempting to solve the task.
8. _**Chain of thoughts Prompting (CoT)**_: makes the model to think step by step --> best combined with **Few Shot** technique.
9. _**Tree of thoughts Prompting (ToT)**_: same as **(CoT)**, but takes multiple paths --> best for complex tasks.
10. _**Self Consistency Prompting**_:
    - Provide the same prompt multiple times.
    - Extract answer from each response.
    - Choose the most common answer.
11. _**Automatic Prompting**_: prompt a model to generate more models, evaluate them, then alter the good once & repeat.

    - Enhances the model's performance.
    - Ease the burden of the human input.

      **NOTE:** for (Automatic Prompting) evaluation, use **Candidate Screening Methods** like [BLEU](https://en.wikipedia.org/wiki/BLEU) or [ROUGE](<https://en.wikipedia.org/wiki/ROUGE_(metric)>).

---

#### What is the Best Practice for **Prompt Engineering**?

1. Provide examples (One-Shot/Few-Shot).
2. Simplicity (Clear, Concise, Easy to Understand).
3. Use **Verbs** to describe the action (Act, Create, Find, Parse, etc...).
4. Be specific about the output (DO & DO NOT).
5. For extracting data, return the output in a **(JSON OR XML)** format to focus only on the data you want to receive.
6. Use **Instructions** over **Constraints**:
   - **Instructions:** to provide explicit instructions about the desired output.
   - **Constraints:** a set of limitations on the response.
7. Use **Variables** in prompts, Example:

```python
city = "London"
prompt example:
    you are a travel guide, tell me a fact about the city:{ city }
```

See [Best Practice](https://github.com/Gl00ria/AI_4_US/blob/main/Prompt_Engineering/02_Prompt_Eng_Best_Practice.md) for more details and examples
