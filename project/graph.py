import matplotlib.pyplot as plt


def plot_performance(baseline_fps=12, optimized_fps=22):
    labels = ['Baseline', 'Optimized']
    fps = [baseline_fps, optimized_fps]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, fps, color=['tab:red', 'tab:green'])
    plt.xlabel('System')
    plt.ylabel('FPS')
    plt.title('Performance Improvement')

    for bar, value in zip(bars, fps):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'{value:.1f}', ha='center', va='bottom')

    plt.ylim(0, max(fps) * 1.4)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.show()


if __name__ == '__main__':
    plot_performance()