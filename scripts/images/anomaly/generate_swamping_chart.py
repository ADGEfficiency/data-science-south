import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Generate clustered data with one extreme outlier
np.random.seed(42)
cluster1 = np.random.normal(0, 0.5, 50)
cluster2 = np.random.normal(5, 0.5, 50)
extreme_outlier = [20]  # This will cause swamping

data = np.concatenate([cluster1, cluster2, extreme_outlier])

# Z-score detection (affected by swamping)
z_scores = np.abs(stats.zscore(data))
outliers_zscore = data[z_scores > 2]

# Robust detection using median and MAD
median_val = np.median(data)
mad = np.median(np.abs(data - median_val))
modified_z_scores = 0.6745 * (data - median_val) / mad
outliers_mad = data[np.abs(modified_z_scores) > 2]

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Z-score method (affected by swamping)
ax1.scatter(range(50), cluster1, alpha=0.6, label="Cluster 1", color="blue")
ax1.scatter(range(50, 100), cluster2, alpha=0.6, label="Cluster 2", color="green")
ax1.scatter([100], extreme_outlier, color="red", s=100, label="Extreme outlier")

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

ax1.set_title("Z-score Detection (Swamping Effect)")
ax1.set_xlabel("Data Point Index")
ax1.set_ylabel("Value")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: MAD method (robust)
ax2.scatter(range(50), cluster1, alpha=0.6, label="Cluster 1", color="blue")
ax2.scatter(range(50, 100), cluster2, alpha=0.6, label="Cluster 2", color="green")
ax2.scatter([100], extreme_outlier, color="red", s=100, label="Extreme outlier")

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
    project_root, "static", "images", "anomaly", "swamping_example.png"
)
plt.savefig(output_path, dpi=300, bbox_inches="tight")

print(f"Z-score outliers (swamping): {len(outliers_zscore)} points")
print(f"MAD outliers (robust): {len(outliers_mad)} points")
print(f"Z-score detected: {outliers_zscore}")
print(f"MAD detected: {outliers_mad}")
print(
    f"The extreme outlier {extreme_outlier[0]} inflated variance, causing normal points to be flagged as outliers"
)

