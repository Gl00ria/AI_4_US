#### 1. Model Design & Dataset Engineering:

1. Select an architecture depending on the intended application. See [Neural Network Architecture](https://github.com/Gl00ria/AI_4_US/blob/main/00_Warm_Up/04_Neural_Network_Architecture.md)
2. Decide the Depth & Number of parameters it will contain, as this is important to define the Model's capabilities and limitations.
3. Collect data from publicly available sources a.k.a **(Scrape)** or propriety datasets. Keep in mind, that the amount & quality of the data will influence the model's performance.
4. Cleanse and Structure the data to ensure that the model will train on high-quality information.

---

#### 2. Pre-training:

- Address the key issues such as the data diversity biases within the training data.
- Early assessment of the model to understand its strength and the areas that needs improvement.

---

#### 3. Post-training:

- Enhance the model's performance by using high-quality/targeted data **'Supervised'**.
- Refine the model further through human feedback and annotations to improve its accuracy.

---

#### 4. Final Testing & Evaluation:

- Optimize the model's weight for specific tasks improving speed & efficiency
- Comprehensive Review for:
  - Response quality.
  - Response accuracy.
  - Ethical Behavior.

---

#### How to determine how powerful the AI model is?

1. **Dataset:** the larger, the more it enhances the model's learning capacity, think of it as a **Book library**.
2. **Model Size:** Determines the model's learning capacity, think of it as a **Student's learning capacity**.

**NOTE:** the larger the model's **Dataset** & **Model Size**, the higher performance to be expected. **BUT!!** always consider the available budget & the model size. (Hardware for computing, Performance, efficiency). Try to find the right balance between:

- How will AI works.
- And how much it costs.

| **Large Model**      | **Small Model**  |
| -------------------- | ---------------- |
| Expinsive            | Cost effective   |
| More computing power | Quicker to train |
| Effective            |                  |

---

#### What is Retrieval Augmented Generation (RAG)?

Enhancing the model's response by integrating an external **database** for the model to query in order to pull additional context or information.

**Why?** to provide richer context for model response, useful for providing detailed knowledge.
