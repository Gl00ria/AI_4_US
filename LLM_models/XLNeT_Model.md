#### What is XLNet?

A pre-trained Model that uses the [Transformer Architecture](https://github.com/Gl00ria/AI_4_US/blob/main/00_Warm_Up/04_Neural_Network_Architecture.md) to process and understand Natural Language, by Google '2019'.

#### XLNet Types:

**XLNet BASE:** has 110 million parameters, with 12 Encoders.
**XLNet LARGE:** has 340 million parameters, with 24 Encoders.

#### How it works?

During the pre-training XLNet considers all words in the context,, not just the words to the left or right of the target, it samples different permutations of the input data. **Basically,** it considers different ways to mask and predict words in the sequence, it learns to predict the probability of each word given in the entire context.

#### XLNet Advantages?

- Improved contextually understanding.
- Capture bidirectional context effectively.
- Prediction each word by considering all other words.
- Ability to capture long range dependencies in text contributed to its success.

#### What XLNet is good at? (Same as BERT)

- Classification.
- Question and Answering.
- Named entity recognition.
