#### **Recurrent Neural Network (RNN):**

Processing a sequence of text and returning information from previous inputs which allows for context-aware prediction.

**Problem?** Struggles with long text inputs.

**NOTE:** this one is obsolete for LLMs.

---

#### **Long Short-Term Neural Network (LSTNN):**

Addresses the **RNN** limitations with a gate architecture (input, forget, output) that helps the model to retain/discard information selectively, which helps the model to manage long-term dependencies.

**Problem?** Poor for sequential logic.

**NOTE:** this one is obsolete for LLMs.

---

#### **Convolutional Neural Networks (CNN):**

Specialized neural networks designed for processing grid-like data (e.g., images, videos)

---

#### **Transformers:**

This one's used in modern **LLMs** like (GPT, Gemini), it handles the sequences without the overhead of **LSTNN**, which enhances the scalability & performance in processing large volumes of text.

**NOTE:** this one is the core architecture for LLMs.
