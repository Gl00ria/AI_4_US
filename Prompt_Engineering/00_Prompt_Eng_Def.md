#### What is Prompt Engineering?

It's the art of designing a high quality prompts to guide the **LLM** to produce an accurate output.

#### The effect of Output-Length:

| **Long Output**                    | **Short Output**                                                           |
| ---------------------------------- | -------------------------------------------------------------------------- |
| More Computation time from the LLM | Doesn't make the **LLM** to become more stylish                            |
| Higher Energy                      | Causes the **LLM** to stop consuming more tokens once the limit is reached |
| Higher Cost                        |                                                                            |
| Slower Response                    |                                                                            |

Output length restriction is important for some **LLM** techniques like **ReAct (Reasoning Act)** since the **LLM** will keep emitting useless tokens after the response you want.

#### Temperature Control (Top-K & Top-P) aka _(Nucleus Sampling)_:

Used to control the degree of randomness in token selection.

- **Lower temp**: good for deterministic response.
- **Higher temp**: can lead to unexpected response.

**Top-K VS Top-P?** You should experiment the results by yourself

#### What is **Repetition Loop Bug**?

It happens when the **LLM** keeps generating the same **(filler words, phrase, sentence structure)**. SO, the clearer your prompt, the better results you get.
