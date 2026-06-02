#### What BERT stands for?

It stands for **B**idirectional **E**ncoder **R**presentations **T**ransformers.
it can generate human like text & can continue the text in a contextually appropriate manner.

#### What is BERT?

A pre-trained Model that uses the [Transformer Architecture](https://github.com/Gl00ria/AI_4_US/blob/main/00_Warm_Up/04_Neural_Network_Architecture.md) to process and understand Natural Language, by Google '2018'.

#### BERT Types:

**BERT BASE:** has 110 million parameters, with 12 Encoders.
**BERT LARGE:** has 340 million parameters, with 24 Encoders.

#### How it works?

It predicts missing words in a sentence by considering the entire context, which helps in understanding the meaning of the words in a more contextually relevant way.

#### How the model pre-trained?

The model's pre-trained using two objectives:
**1. Masked Language Model (MLM):** Trained to predict the masked word based on the context provided by the surrounding tokens. **The Goal is** to try to figure out which words fill in the masked tokens which forces the model to learn bidirectional context as it is allowed to see all unmasked words from either sides of the masked token. **Basically,** use the output of the masked words postions to predict the masked word.
**2. Next Sentence Prediction (NSP):** Trained to predict whether two sentences in a pair are consecutive in the orginal text or not. 50% of the input sentence are paired with their next sentences in the original input text, the other 50% are paired with a random sentence from the text. **Basically,** predict whether the two next sentence are paired with their next sentence or not, which helps the model to understand the relationships between sentences.

#### BERT fine-tuning?

By adding a task specific layer on the top of the pre-trained encoder. The added layer will format the output to be relevant for the task.

#### BERT Advantages?

- Flexibility.
- Adaptability.

#### What BERT is good at?

- Classification.
- Question and Answering.
- Named entity recognition.
