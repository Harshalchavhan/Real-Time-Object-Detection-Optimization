import matplotlib.pyplot as plt
import numpy as np

# Your measured values (update these with actual results)
labels = ["Baseline", "Optimized"]
fps = [12, 22]   # replace with YOUR measured values
latency = [80, 40]  # in ms

# FPS Graph
plt.figure(figsize=(12, 5))

# Subplot 1: FPS
plt.subplot(1, 2, 1)
bars1 = plt.bar(labels, fps, color=['tab:red', 'tab:green'])
plt.xlabel("System")
plt.ylabel("FPS")
plt.title("FPS Improvement (+83%)")
plt.ylim(0, max(fps) * 1.4)

# Add value labels on bars
for bar, value in zip(bars1, fps):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{value:.1f}', ha='center', va='bottom')

# Subplot 2: Latency
plt.subplot(1, 2, 2)
bars2 = plt.bar(labels, latency, color=['tab:orange', 'tab:blue'])
plt.xlabel("System")
plt.ylabel("Latency (ms)")
plt.title("Latency Reduction (-50%)")
plt.ylim(0, max(latency) * 1.4)

# Add value labels on bars
for bar, value in zip(bars2, latency):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{value:.1f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
print("📊 Graph saved as 'performance_comparison.png'")

# Also show the plot (comment out if running headless)
# plt.show()

# Print performance summary
print("\n=== Performance Comparison ===")
print(f"FPS Improvement: {fps[0]} → {fps[1]} ({((fps[1]-fps[0])/fps[0]*100):.1f}%)")
print(f"Latency Reduction: {latency[0]}ms → {latency[1]}ms ({((latency[0]-latency[1])/latency[0]*100):.1f}%)")
print("\n=== Final Result Table ===")
print("Metric\t\tBaseline\tOptimized")
print("-" * 40)
print(f"FPS\t\t{fps[0]}\t\t{fps[1]}")
print(f"Latency (ms)\t{latency[0]}\t\t{latency[1]}")
print(f"Resolution\t1280p\t\t480p")
print(f"Frame Skip\tNo\t\tYes (every 2nd)")
print(f"Model\t\tyolov8m.pt\tyolov8n.pt")