import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Generate normal data with two types of outliers
np.random.seed(42)
normal_data = np.random.normal(0, 1, 100)
moderate_outliers = [3.5, 3.7]  # These should be detected
extreme_outliers = [15, 16]  # These mask the moderate ones

data = np.concatenate([normal_data, moderate_outliers, extreme_outliers])

# Z-score detection (affected by masking)
z_scores = np.abs(stats.zscore(data))
outliers_zscore = data[z_scores > 2]

# Robust detection using MAD
mad = np.median(np.abs(data - np.median(data)))
modified_z_scores = 0.6745 * (data - np.median(data)) / mad
outliers_mad = data[np.abs(modified_z_scores) > 2]

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Z-score method (affected by masking)
ax1.scatter(range(len(normal_data)), normal_data, alpha=0.6, label="Normal data")
ax1.scatter(
    [100, 101], moderate_outliers, color="orange", s=100, label="Moderate outliers"
)
ax1.scatter([102, 103], extreme_outliers, color="red", s=100, label="Extreme outliers")

# Highlight detected outliers
outlier_indices = np.where(z_scores > 2)[0]
ax1.scatter(
    outlier_indices,
    data[outlier_indices],
    facecolors="none",
    edgecolors="black",
    s=150,
    linewidths=2,
    label="Detected by Z-score",
)

ax1.set_title("Z-score Detection (Masking Effect)")
ax1.set_xlabel("Data Point Index")
ax1.set_ylabel("Value")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: MAD method (robust)
ax2.scatter(range(len(normal_data)), normal_data, alpha=0.6, label="Normal data")
ax2.scatter(
    [100, 101], moderate_outliers, color="orange", s=100, label="Moderate outliers"
)
ax2.scatter([102, 103], extreme_outliers, color="red", s=100, label="Extreme outliers")

# Highlight detected outliers
mad_outlier_indices = np.where(np.abs(modified_z_scores) > 2)[0]
ax2.scatter(
    mad_outlier_indices,
    data[mad_outlier_indices],
    facecolors="none",
    edgecolors="black",
    s=150,
    linewidths=2,
    label="Detected by MAD",
)

ax2.set_title("MAD Detection (Robust)")
ax2.set_xlabel("Data Point Index")
ax2.set_ylabel("Value")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
# Get the project root directory (3 levels up from this script)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
output_path = os.path.join(
    project_root, "static", "images", "anomaly", "masking_example.png"
)
plt.savefig(output_path, dpi=300, bbox_inches="tight")

print(f"Z-score outliers: {outliers_zscore}")
print(f"MAD outliers: {outliers_mad}")
print(
    f"Moderate outliers {moderate_outliers} missed by Z-score due to masking from extreme outliers {extreme_outliers}"
)

