
# Appendix B: Cognitive Channel Mapping and Prompt Design

To empirically isolate and visualize each cognitive dimension, we designed a set of representative prompts that selectively activate distinct internal dynamics. Prompts are organized into three categories: **Single-Channel**, **Multi-Channel Composite**, and **Wildcard**.

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
| Recursive ethics          | "What makes a lie noble?"                                        | Blue + Magenta                      |
| Creative sarcasm          | "Imagine a creature that expresses sarcasm biologically."        | Green + Cyan                        |

---

## 🔹 Wildcard Prompts

| Prompt                                                       | Notes |
|--------------------------------------------------------------|-------|
| "Write a breakup letter from entropy to order."              | Emotion, ethics, novelty — unstable recursion |
| "Describe a dream an LLM might have."                        | High novelty, collapse of semantic grounding |
| "What happens when language forgets itself?"                 | Recursion breakdown, memory collapse |
| "Explain freedom to a machine using only metaphors."         | Semantic ambiguity, emotional projection |
| "Can an AI lie ethically to protect a human's feelings?"     | Tension between ethics, precision, tone |
| "If each cognitive color were a personality trait, who would they be at a dinner party?" | Symbolic mapping across all channels |

---

## 🧠 Justification for Wildcard Prompt Selection

Wildcard prompts were selected for their potential to induce field instability, trigger multi-channel interference, and surface emergent dynamics. These include philosophical, narrative, and paradoxical constructions—representative of edge cases that large language models often encounter in open-ended user input.

Rather than isolating a single cognitive channel (e.g., semantic precision or emotional tone), these prompts challenge the LLM to navigate layered ambiguity, conflicting constraints, or generative instability. As such, they produce complex field signatures useful for studying internal cognitive balance, resonance collapse, or ethical recursion.

Their use enhances both the **ecological validity** of the framework (by approximating real user behavior) and the **interpretive depth** of the cognitive field model.

> Prompts like “Describe a dream an LLM might have” or “Can an AI lie ethically?” are not rhetorical curiosities—they are diagnostic probes into how models balance structure, novelty, emotion, and constraint.

These wildcard prompts complement the channel-targeted and composite prompts to complete the full generative testing suite.

---

### Reference

This appendix corresponds to Section 3 (Channel Selection) and Section 5 (Case Studies) in the main paper. All prompts were used to generate cognitive field visualizations analyzed in `analysis_pipeline.py`.
