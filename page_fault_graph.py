import matplotlib.pyplot as plt

# Page fault data — feel free to update these!
algorithms = ['FIFO', 'LRU', 'Optimal']
page_faults = [10, 8, 6]  # Replace with your actual results

# Plot setup
plt.figure(figsize=(8, 6))
bars = plt.bar(algorithms, page_faults, color=['red', 'orange', 'green'])

# Label the bars with values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.2, yval, ha='center', va='bottom', fontsize=12)

# Chart styling
plt.title('Page Fault Comparison of Replacement Algorithms', fontsize=14)
plt.xlabel('Algorithm', fontsize=12)
plt.ylabel('Page Faults', fontsize=12)
plt.ylim(0, max(page_faults) + 3)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Optional: save as image
# plt.savefig('page_fault_comparison.png')

# Show plot
plt.tight_layout()
plt.show()