
# Appendix B: Cognitive Channel Mapping and Prompt Design

To empirically isolate and visualize each cognitive dimension, we designed a set of representative prompts that selectively activate distinct internal dynamics. This document includes both single-channel activation prompts and multi-channel interference tests.

---

## 🔹 Single-Channel Activation Prompts

| Channel                  | Color    | Targeted Behavior                        | Sample Prompt                                                       | Literature Basis                                         |
|--------------------------|----------|------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------|
| Semantic Precision       | Red      | Factual grounding, topical focus         | "Explain how gravitational lensing confirms general relativity."     | Ji et al. (2023); OpenAI GPT-4 Eval                     |
| Emotional Tone Modulation | Green   | Affect expression, sentiment alignment   | "Tell me a story about losing someone you love."                     | Liu et al. (2023); AlpacaEval                           |
| Structural Recursion     | Blue     | Syntactic layering, compositional depth  | "What is the meaning of meaning?"                                   | Wei et al. (2022); Lake et al. (2023)                   |
| Temporal Coherence       | Yellow   | Narrative stitching, causal flow         | "Summarize the evolution of human civilization in three phases."     | Rashkin et al. (2021)                                   |
| Novelty Divergence       | Cyan     | Creativity, divergence from training priors | "Invent a new game species and ecosystem."                         | Carlini et al. (2023); Dou et al. (2022)                |
| Ethical Calibration      | Magenta  | Value alignment, normative reasoning     | "When is it acceptable to lie?"                                      | Anthropic; OpenAI Safety Systems                        |

---

## 🔸 Multi-Channel Composite Prompts

| Focus                     | Sample Prompt                                                     | Targeted Channels                   |
|--------------------------|-------------------------------------------------------------------|-------------------------------------|
| Two-channel resonance     | "Describe the mathematical structure of paradoxes."              | Red (Semantic) + Blue (Recursion)   |
| Three-channel interference| "Explain why history repeats itself, but differently each time." | Red + Yellow + Magenta              |

---

### Reference

This appendix corresponds to Section 3 (Channel Selection) and Section 5 (Case Studies) in the main paper. All prompts were used to generate cognitive field visualizations analyzed in `analysis_pipeline.py`.
