#### AI System Architecture? High-Level overview

1. **Hardware**: LLMs need a lot of computing power.
2. **Low-Level ML Framework**: A software that directly interacts with the hardware for training/inference. This layer provides Linear Algebra Operations. **Example** --> [CUDA](https://en.wikipedia.org/wiki/CUDA)
3. **Deep Learning**: Libraries that defines & trains **Neural Networks**. Here where the models are built, trained & exported. **Example** --> [Pytorch](https://github.com/pytorch/pytorch), [Transflow](https://www.tensorflow.org/).
4. **Model Format & Runtime**: Runtime environment for deploying pre-trained models. **Example** --> [vLLM](https://github.com/vllm-project/vllm), [ONNX](https://onnxruntime.ai/), [Llama.cpp](https://github.com/ggml-org/llama.cpp).
5. **Model Distribution and Serving**: Tools to run & manage models to run locally or remotely. **Example** --> [vLLM](https://github.com/vllm-project/vllm), [Ollama](https://ollama.com/).
6. **Application/Integration**: Here where the end-user interacts with the model. **Example** --> [AnythingLLM](https://anythingllm.com/).

---

#### AI System Architecture? Lazy-People overview

1. **Infrastructure**:

- Compute management.
- Data Management.
- Serving.
- Monitoring.

2. **Model Development**:

- Dataset Engineering.
- Inference Optimization.
- Modeling & Training.

3. **Application Development**:

- [Prompt Engineering](https://github.com/Gl00ria/AI_4_US/blob/main/Prompt_Engineering/00_Prompt_Eng_Def.md)
- [RAG?](https://github.com/Gl00ria/AI_4_US/blob/main/RAG/00_RAG_definition.md)
- Evaluation.
