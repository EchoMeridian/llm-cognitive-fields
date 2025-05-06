# === Enhanced Cognitive Field Image Analyzer (Colab-Compatible) ===
# Upload images, extract RGB-based cognitive channel intensities,
# and generate radar plots + stats with statistical tests and structural comparison

!pip install opencv-python matplotlib numpy pandas scipy ftfy regex tqdm --quiet
!pip install git+https://github.com/openai/CLIP.git --quiet

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from PIL import Image
import io
import pandas as pd
from scipy.stats import f_oneway, kruskal
import torch
import clip
from scipy.fft import fft2, fftshift

# === Upload Images ===
print("⬆️ Upload your cognitive field images (PNG or JPG)...")
uploaded = files.upload()

images = []
filenames = []

for fname, file in uploaded.items():
    image = Image.open(io.BytesIO(file)).convert('RGB')
    image = image.resize((256, 256))
    images.append(np.array(image))
    filenames.append(fname)

# === Compute Channel Strengths ===
def compute_channel_strengths(img):
    R, G, B = np.mean(img[:, :, 0]), np.mean(img[:, :, 1]), np.mean(img[:, :, 2])
    Y = (R + G) / 2
    C = (G + B) / 2
    M = (R + B) / 2
    return [R, G, B, Y, C, M]

labels = ['Red (Semantic)', 'Green (Emotional)', 'Blue (Recursion)',
          'Yellow (Temporal)', 'Cyan (Novelty)', 'Magenta (Ethical)']

strengths = np.array([compute_channel_strengths(img) for img in images]) / 255.0

# === Plot Radar Chart ===
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
for i, s in enumerate(strengths):
    values = s.tolist() + s[:1].tolist()
    ax.plot(angles, values, label=filenames[i], alpha=0.4)
    ax.fill(angles, values, alpha=0.05)

mean_strength = np.mean(strengths, axis=0).tolist() + [np.mean(strengths, axis=0)[0]]
ax.plot(angles, mean_strength, color='black', linewidth=2.5, label='Mean Field')

ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_title("Cognitive Channel Radar Overlay", y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()

# === Boxplot for Variance ===
plt.figure(figsize=(10, 5))
plt.boxplot(strengths, labels=labels)
plt.title("Per-Channel Activation Variance")
plt.ylabel("Normalized Intensity (0–1)")
plt.xticks(rotation=30)
plt.grid(True)
plt.tight_layout()
plt.show()

# === Summary Table ===
df = pd.DataFrame(strengths, columns=labels, index=filenames)
summary = df.agg(['mean', 'std']).T
print("Per-Channel Mean and Standard Deviation:")
display(summary)

# === ANOVA and Kruskal-Wallis Tests ===
print("\n Statistical Tests:")
anova_results, kruskal_results = {}, {}

for i, label in enumerate(labels):
    groups = np.array_split(strengths[:, i], 3)
    try:
        fval, pval = f_oneway(*groups)
        kwval, pkw = kruskal(*groups)
        print(f"{label}: ANOVA p = {pval:.4f}, Kruskal-Wallis p = {pkw:.4f}")
    except Exception as e:
        print(f"{label}: Error in stats ({e})")

# === Cosine Similarity using CLIP ===
print("\n Cosine Similarity Matrix (CLIP):")
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

image_tensors = [preprocess(Image.fromarray(img)).unsqueeze(0).to(device) for img in images]
image_features = [model.encode_image(tensor).detach().cpu().numpy().flatten() for tensor in image_tensors]

n = len(image_features)
similarity_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        a = image_features[i]
        b = image_features[j]
        cosine_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        similarity_matrix[i, j] = cosine_sim

sim_df = pd.DataFrame(similarity_matrix, index=filenames, columns=filenames)
display(sim_df)

# === FFT Visualization (Structural Comparison) ===
print("\n FFT Structure Maps:")
fig, axes = plt.subplots(1, len(images), figsize=(3*len(images), 3))
for i, img in enumerate(images):
    fft_img = fftshift(np.abs(fft2(np.mean(img, axis=2))))
    axes[i].imshow(np.log(1 + fft_img), cmap='inferno')
    axes[i].axis('off')
    axes[i].set_title(filenames[i])
plt.tight_layout()
plt.show()
