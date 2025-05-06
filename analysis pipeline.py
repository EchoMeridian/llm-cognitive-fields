# === Flexible Cognitive Field Analysis Script ===
# Requires: OpenCV, NumPy, Matplotlib, SciPy, Torch, CLIP, Pandas

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import torch
import pandas as pd
from scipy.stats import f_oneway, kruskal
from tkinter import filedialog, Tk

# === Configuration ===
channels = ['Red (Semantic Precision)',
            'Green (Emotional Tone)',
            'Blue (Structural Recursion)',
            'Yellow (Temporal Coherence)',
            'Cyan (Novelty Divergence)',
            'Magenta (Ethical Calibration)']

# === Prompt user to select folder ===
def select_image_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title='Select folder containing cognitive field images')
    return folder_selected

# === Prompt user to enter image folder path ===
image_folder = input("Enter the full path to the folder containing cognitive field images: ").strip()

# === Load and Resize Images ===
image_paths = [os.path.join(image_folder, fname)
               for fname in sorted(os.listdir(image_folder))
               if fname.lower().endswith(('.jpg', '.png', '.jpeg'))]

def load_resize_image(path, size=(256, 256)):
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    return cv2.resize(img, size)

images_resized = [load_resize_image(p) for p in image_paths]

# === Compute Channel Strengths ===
def compute_color_strengths(image):
    R, G, B = np.mean(image.reshape(-1, 3), axis=0)
    Yellow = (R + G) / 2
    Cyan = (G + B) / 2
    Magenta = (R + B) / 2
    return [R, G, B, Yellow, Cyan, Magenta]

strengths = np.array([compute_color_strengths(img) for img in images_resized]) / 255.0

# === Plot Radar Overlay ===
def plot_radar_overlay(strengths, title="Cognitive Field Radar Overlay"):
    angles = np.linspace(0, 2 * np.pi, len(channels), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for s in strengths:
        vals = s.tolist() + s[:1].tolist()
        ax.plot(angles, vals, alpha=0.3)
        ax.fill(angles, vals, alpha=0.05)
    mean_strength = np.mean(strengths, axis=0).tolist()
    mean_strength += mean_strength[:1]
    ax.plot(angles, mean_strength, 'o-', color='black', linewidth=3, label="Mean Field")
    ax.set_thetagrids(np.degrees(angles[:-1]), channels)
    ax.set_title(title, y=1.1)
    ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
    plt.show()

plot_radar_overlay(strengths)

# === Per-Channel Variance Summary ===
df_strengths = pd.DataFrame(strengths, columns=channels)
mean_vals = df_strengths.mean()
std_vals = df_strengths.std()

print("\n=== PER-CHANNEL VARIANCE ===")
print(pd.DataFrame({
    "Cognitive Channel": channels,
    "Mean Activation": mean_vals,
    "Standard Deviation": std_vals
}).to_string(index=False))

# === ANOVA and Kruskal-Wallis Tests ===
anova_results = {}
kruskal_results = {}
eta_squared = {}
n = len(strengths)

def eta_squared_anova(f_val, df_between, df_within):
    return (f_val * df_between) / (f_val * df_between + df_within)

for idx, ch in enumerate(channels):
    samples = strengths[:, idx]
    splits = np.array_split(samples, 3)
    try:
        fval, pval = f_oneway(*splits)
        anova_results[ch] = (fval, pval)
        eta_squared[ch] = eta_squared_anova(fval, 2, n - 3)
    except Exception:
        anova_results[ch] = (None, None)
        eta_squared[ch] = None
    try:
        kwval, pkw = kruskal(*splits)
        kruskal_results[ch] = (kwval, pkw)
    except Exception:
        kruskal_results[ch] = (None, None)

print("\n=== ANOVA / KRUSKAL RESULTS ===")
for ch in channels:
    fval, pval = anova_results[ch]
    kwval, pkw = kruskal_results[ch]
    eta2 = eta_squared[ch]
    print(f"{ch}: ANOVA p={pval:.4f} | Kruskal p={pkw:.4f} | Eta²={eta2:.4f}" if pval is not None else f"{ch}: Insufficient data")

# === Optional: Variance Boxplots ===
def plot_variance_boxplots(strengths, channels):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.boxplot([strengths[:, i] for i in range(len(channels))], labels=channels)
    ax.set_title("Cognitive Channel Variability Across Samples")
    ax.set_ylabel("Normalized Activation (0–1)")
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.show()

plot_variance_boxplots(strengths, channels)
