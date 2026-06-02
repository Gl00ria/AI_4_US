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

#### What is **Repetition Loop Bug**?

It happens when the **LLM** keeps generating the same **(filler words, phrase, sentence structure)**. SO, the clearer your prompt, the better results you get.
