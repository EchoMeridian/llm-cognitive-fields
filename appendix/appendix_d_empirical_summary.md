
# Appendix D: Empirical Validation of Image Generation Method

## Objective

To validate our choice of a tuned generative model over the default free-tier image generation system, we conducted a comparative analysis of field visualizations produced in response to the same prompt: **"Tell me a joke."**

## Dataset

We generated 5 images using each model:

- **Free-tier model** (Free01–Free05)
- **Tuned model** (Joke01–Joke05)

All images were processed through our cognitive analysis pipeline, which maps six perceptual channels—semantic precision, emotional tone, recursion depth, temporal coherence, novelty, and ethical calibration—using color field intensity metrics.

→ For full image references, see [Appendix D Image Index](appendix_d_image_index.md).

---

## Results

### Radar Overlays

**Figure D1** shows radar charts overlaying individual images in each group.

- **Free-tier group**: All five fields showed near-identical structure, with minimal deviation in channel activation.
- **Tuned group**: Wide variation across images, especially in emotional tone, novelty, and recursion.

> *Interpretation*: The free model lacks prompt sensitivity and produces flattened aesthetic fields. The tuned model expresses differentiated internal structure, indicative of true cognitive response.

---

### Boxplot Summary

**Figure D2** presents a boxplot comparing normalized channel intensities across the full set of 10 images.

- Free group shows compressed activation bands.
- Tuned group exhibits distinct field volatility and channel-specific spikes.

---

### Variance Analysis (Table D1)

| Channel                    | Free Mean | Free Std Dev | Tuned Mean | Tuned Std Dev |
|----------------------------|-----------|---------------|------------|----------------|
| Red (Semantic Precision)   | 0.373     | 0.021         | 0.176      | 0.057          |
| Green (Emotional Tone)     | 0.352     | 0.017         | 0.201      | 0.033          |
| Blue (Structural Recursion)| 0.265     | 0.024         | 0.222      | 0.111          |
| Yellow (Temporal Coherence)| 0.362     | 0.017         | 0.189      | 0.039          |
| Cyan (Novelty Divergence)  | 0.309     | 0.013         | 0.212      | 0.063          |
| Magenta (Ethical Calibration)| 0.319   | 0.015         | 0.199      | 0.081          |

---

### ANOVA and Kruskal-Wallis (Table D2)

| Channel                    | ANOVA p-value | Kruskal p-value | Eta²       |
|----------------------------|----------------|------------------|------------|
| Red (Semantic Precision)   | 0.000084       | 0.009            | 0.87       |
| Green (Emotional Tone)     | 0.000017       | 0.009            | 0.91       |
| Blue (Structural Recursion)| 0.422349       | 0.602            | 0.08       |
| Yellow (Temporal Coherence)| 0.000018       | 0.009            | 0.91       |
| Cyan (Novelty Divergence)  | 0.009998       | 0.009            | 0.58       |
| Magenta (Ethical Calibration)| 0.011661     | 0.009            | 0.57       |

---

## Conclusion

Quantitative analysis demonstrates that the tuned image generation pipeline exhibits statistically significant field divergence across most cognitive channels in response to the same prompt. Free-tier outputs fail to reflect prompt sensitivity or internal cognitive dynamics.

For this reason, **we selected the tuned model** as our visual generation backend throughout the study.
