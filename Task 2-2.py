import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
a = np.random.rand(100)
b = 3 * a + np.random.normal(0, 0.2, 100)
plt.figure(figsize=(10, 6))
plt.scatter(a, b, alpha=0.7)
plt.xlabel('A-axis')
plt.ylabel('B-axis')
plt.title('Scatter Plot of A vs. B')
plt.grid(True)
plt.show()
