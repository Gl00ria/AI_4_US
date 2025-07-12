#### Challenges with AI and Foundation Models?

- High Cost.
- Technical demands of developing a custom model, means that most companies cannot afford to build their own.
- Resource Intensive.
- Latency. **See in depth section below**
- Running Out of Data. **See in depth section below**

#### Challenges in depth:

- **Latency**: users have low tolerance for slow loading time, since delays frustrates them. Today's **LLMs** use **Autoregressive Architecture** where each generated word depends on the words that came before it, this sequential process limits the speed at which outputs can be produced. A workaround is by optimizing the model size. The smaller, the faster.

- **Running Out of Data:** Taking **GPT** as an example, **AI developers** risk running out of data, if **GPT-4** which has a **1.5T parameters** had been fed on big part of the internet, from where would the new data for **GPT-5** come from?. Also, big portion of the data available on the internet are made by **AI**, this makes the learning process for future **LLMs** challenging because they frequently encounter **Repetitive** or **Derivative** content. Which increases the risk of (Hallucination, Biases, Inaccuracy). Worth to mention that, papular platforms changed their policies to make it illegal for **AI developers** to scrape their platform data, and other allowed to sign a **Content Licensing Agreement** that allows the developers to use the data on their platform.
