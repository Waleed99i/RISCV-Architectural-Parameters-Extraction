# Model Information

This table summarizes every Large Language Model used during benchmarking.

**Total Models:** 12

| LLM | Provider | Model | Context Length |
|-----|----------|-------|----------------|
| Claude | Anthropic | Claude Sonnet 5 | 1,048,576 tokens |
| DeepSeek | DeepSeek | DeepSeek V4-Flash-0731 | 1,048,576 tokens |
| Gemini | Google | Gemini 3 | Up to 1M tokens |
| Gemini | Google | Gemini 3.6 Flash | 1,048,576 tokens |
| GLM | Zhipu AI | GLM-5.2 | 128K tokens |
| ChatGPT | OpenAI | GPT-5.5 | 1,048,576 tokens |
| NVIDIA | NVIDIA | Ising-Calibration-1.5 | 4096 tokens |
| Kimi | Moonshot AI | K2.6 | 256K tokens (2M characters extended) |
| Mistral | Mistral AI | Mistral Medium 3.5 | 32K tokens |
| Copilot | Microsoft | Proprietary Microsoft Build | Not publicly disclosed |
| Qwen | Alibaba Tongyi Lab | Qwen | Up to 256K+ tokens |
| Perplexity | Perplexity AI | Sonar-Perplexity | 128K tokens |


## Notes

- Generated automatically from `run_metadata.json`.
- One metadata file is read for each model.
- Metadata is independent of prompt version and benchmark results.