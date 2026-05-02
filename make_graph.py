import matplotlib.pyplot as plt
import os

heads = [2, 3, 5, 7]
losses = [3.4644, 3.4629, 3.4573, 3.4376]

plt.figure(figsize=(8, 5))
plt.plot(heads, losses, marker='o', linestyle='-', color='b')

plt.title('Task 3: Validation Loss vs. Number of Heads (Layers=7)')
plt.xlabel('Number of Heads')
plt.ylabel('Validation Loss (at Iteration 5)')
plt.grid(True, linestyle='--', alpha=0.7)

os.makedirs('figures', exist_ok=True)

plt.savefig('figures/heads_vs_loss.png')
print("Graph saved successfully to figures/heads_vs_loss.png")
