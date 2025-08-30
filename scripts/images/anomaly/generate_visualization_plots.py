import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
import os

# Set style for better looking plots
plt.style.use("default")
sns.set_palette("husl")

# Create output directory relative to project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))
output_dir = os.path.join(project_root, "static", "images", "anomaly")
os.makedirs(output_dir, exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# 1. Histogram
print("Generating histogram...")
data = [1, 2, 3, 4, 5, 100]  # 100 is an outlier
plt.figure(figsize=(8, 5))
plt.hist(data, bins=10, alpha=0.7, edgecolor="black", color="skyblue")
plt.title("Histogram: Distribution with Outliers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/histogram.png", dpi=300, bbox_inches="tight")
plt.close()

# 2. KDE
print("Generating KDE plot...")
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True, alpha=0.7, color="lightcoral")
plt.title("KDE: Density Estimation")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/kde.png", dpi=300, bbox_inches="tight")
plt.close()

# 3. Boxplot
print("Generating boxplot...")
plt.figure(figsize=(6, 6))
box_plot = plt.boxplot(data, patch_artist=True)
box_plot["boxes"][0].set_facecolor("lightgreen")
plt.title("Boxplot: Outlier Detection")
plt.ylabel("Value")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# 4. Scatterplot
print("Generating scatterplot...")
x = [1, 2, 3, 4, 10]
y = [1, 2, 3, 4, 10]  # (10, 10) is an outlier
plt.figure(figsize=(8, 6))
plt.scatter(x[:-1], y[:-1], alpha=0.7, s=60, color="blue", label="Normal points")
plt.scatter([x[-1]], [y[-1]], color="red", s=100, label="Outlier")
plt.title("Scatterplot: Two Numeric Variables")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/scatterplot.png", dpi=300, bbox_inches="tight")
plt.close()

# 5. Heatmap
print("Generating heatmap...")
df = pd.DataFrame(
    {
        "cat1": ["A", "A", "A", "B", "B", "C"],
        "cat2": ["X", "Y", "X", "Y", "X", "Z"],  # Z is rare combination
    }
)
heatmap_data = pd.crosstab(df["cat1"], df["cat2"])
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap="viridis", fmt="d")
plt.title("Heatmap: Two Categorical Variables")
plt.tight_layout()
plt.savefig(f"{output_dir}/heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# 6. Boxplot by category
print("Generating boxplot by category...")
group_a = [1, 2, 3, 4]
group_b = [10, 11, 12, 100]  # 100 is outlier in group B
plt.figure(figsize=(8, 6))
box_plot = plt.boxplot(
    [group_a, group_b], tick_labels=["Group A", "Group B"], patch_artist=True
)
box_plot["boxes"][0].set_facecolor("lightblue")
box_plot["boxes"][1].set_facecolor("lightcoral")
plt.title("Boxplot by Category: Outliers Within Groups")
plt.xlabel("Category")
plt.ylabel("Value")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/boxplot_by_category.png", dpi=300, bbox_inches="tight")
plt.close()

# 7. Z-score visualization
print("Generating z-score visualization...")
data_zscore = [1, 2, 3, 4, 5, 100]
z_scores = np.abs(stats.zscore(data_zscore))
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    range(len(data_zscore)), data_zscore, c=z_scores, cmap="Reds", s=80
)
plt.axhline(
    np.mean(data_zscore) + 2 * np.std(data_zscore),
    color="red",
    linestyle="--",
    alpha=0.7,
    label="2σ threshold",
)
plt.axhline(
    np.mean(data_zscore) - 2 * np.std(data_zscore),
    color="red",
    linestyle="--",
    alpha=0.7,
)
plt.title("Z-score Visualization: Color-coded Outlier Scores")
plt.xlabel("Data Point Index")
plt.ylabel("Value")
plt.colorbar(scatter, label="|Z-score|")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/zscore.png", dpi=300, bbox_inches="tight")
plt.close()

# 8. Density contour plot
print("Generating density contour plot...")
# Create more varied normal points to avoid singular matrix
normal_points = np.array(
    [[1, 1.2], [2, 2.1], [3, 2.8], [1.5, 1.8], [2.5, 2.3], [1.8, 1.1], [2.2, 2.6]]
)
outlier_points = np.array([[10, 1]])  # Far from normal cluster

plt.figure(figsize=(8, 6))
plt.scatter(
    normal_points[:, 0],
    normal_points[:, 1],
    alpha=0.7,
    s=60,
    color="blue",
    label="Normal points",
)
plt.scatter(
    outlier_points[:, 0], outlier_points[:, 1], color="red", s=100, label="Outliers"
)

# Add density contours for normal points
from scipy.stats import gaussian_kde

try:
    kde = gaussian_kde(normal_points.T)
    xi, yi = np.mgrid[0:4:50j, 0:4:50j]
    zi = kde(np.vstack([xi.flatten(), yi.flatten()]))
    plt.contour(xi, yi, zi.reshape(xi.shape), alpha=0.6, colors="gray")
except:
    # Skip contours if KDE fails
    pass

plt.title("Density Contours with Outliers")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/density_contour.png", dpi=300, bbox_inches="tight")
plt.close()

print(f"\nAll plots generated successfully in {output_dir}/")
print("Generated files:")
for filename in sorted(os.listdir(output_dir)):
    if filename.endswith(".png"):
        print(f"  - {filename}")

