# Understanding the requirements & What matters

- Are you stuck at an **8B** model?
- Can you run bigger model?
- Which model for which job?
- What part of the hardware that actually makes a difference?
- What's the difference between all the Quants you see out there?

---

# Understanding the Quantization & Model Parameters 'Warm-Up'

## Quantization

- BF16 = 16-Bit = 2 Bytes
- Q8 = 8-Bit = 1 Byte
- Q6 = 6-Bit = 0.75 Byte
- Q5 = 5-Bit = 0.62 Byte
- Q4 = 4-Bit = 0.5 Byte
- Q3 = 3-Bit = 0.37 Byte
- Q2 = 2-Bit = 0.25 Byte
- Q1 = 1-Bit = 0.12 Byte

Note that, the smaller the quant, the more the model loses its wight. In this case the model loses its value. However, the sweet spot is the **Q4**. Smaller, but the model barely looses any quality.

---

## Model Anatomy

Example: unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M

- 35B = 35 Billion Parameter
- A3B = Active Parameters are 3B, this is an MoE model
- GGUF = The Architecture of the model. For **llama.cpp**
- Q4 = The quantization
- K = Is a smarter way of quantizing, where different wight gets different precision. Meaning, the weights that really matter gets higher Bits, where the low value weights gets lower Bits.
- M = Medium, the Balanced one. This tells you how many of those layers get more Bits. There's also (S & L), which stands for (Small & Large).
- IQ = Uses an **Importance Matrix** to squeeze the model even smaller at the same quality. Its slower, but you will get a good speed if you have a powerful CPU.
- UD = This from **Unsloth**, based on the **IQ** matrix called **Unsloth Dynamic**.

What mode for which task?
You have 2 kinds of Models:
**The Specialist:** For Specific task like Coding
**The Generalist:** For general purpose like Chatting & get basic things done
You can get both where the Specialist does the required task, the switch to the Generalist for the rest.
Examples:
Coding: [Qwen3.6-35B-A3B-GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF)
Agents: [GLM-4.7-Flash-REAP-23B-A3B-GGUF](https://huggingface.co/unsloth/GLM-4.7-Flash-REAP-23B-A3B-GGUF)
Writing: [gpt-oss-20b-GGUF](https://huggingface.co/unsloth/gpt-oss-20b-GGUF)
Vision: [gemma-4-E2B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-qat-GGUF) or [gemma-4-E4B-it-qat-GGUF](https://huggingface.co/unsloth/gemma-4-E4B-it-qat-GGUF)
General & Multi Model: [gemma-4-12b-it-GGUF](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)
RAG: [Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)

What license?
Keep in mind the **Open Weight** doesn't mean its an **Open Source**.

What Kind of model?
If the model don't have (Instruct, It, Chat), it means this one is Base model, and won't answer you, it just auto completes your text.

Whose Quant Should I download?
Stick to the ppl who does it well:

- Official Repository
- [bartowski](https://huggingface.co/bartowski)
- [unsloth](https://huggingface.co/unsloth)
- [mradermacher](https://huggingface.co/mradermacher)

---

## Model Context

The context is a short term memory for the model. It contains every (instructions, actions, messages you sent...etc) basically every thing you & your model did in that session.
All of the context is stored in the short term memory "KV CACHE". Without it, the model has to re-read everything again and again.

The more you interact with the model, the more short term memory it uses. Until you reach a point where the context window is bigger than the model itself. Here comes the "KV CACHE Quantization", same as the model's quantization.

---

# Can I fit/run this model?

Ask yourself the following questions:

- Are you going to run a **Dense Model** fully loaded in VRAM? or using an **MoE Model** with off loading the experts on the CPU & the attention layers on GPU?
- Does it fit my system (VRAM, RAM)?
- Can you run it fast enough to do meaningful work?

In order to answer the above questions, we need to brake the model down and analyze it.

First, the model's brain 'Parameters':
A model file is a bunch of numbers which determines how much to (Amplify or De-Amplify) the signals running inside the virtual brain inside an AI. For example: 8B, 20B, 35B. This tells you how many connections/Parameters this model has inside its brain.

---

## The Math to roughly estimate how much RAM/VRAM you need

Parameters × Bytes per Parameter = Total Bytes required to run a model

Example:
2B model with a Q4 quant = 2B x 0.5 = 1GB

I have an off-shelf script that does the math, see [Calculate Requirements](https://github.com/Gl00ria/AI_4_US/blob/main/scripts/calc_reqs.py).

---
