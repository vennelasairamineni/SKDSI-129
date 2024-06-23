import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
data_new = {
    'Group': np.random.choice(['X', 'Y', 'Z', 'W', 'V'], 100),
    'Score': np.random.randn(100)
}
df_new = pd.DataFrame(data_new)
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Score', data=df_new)
plt.xlabel('Group')
plt.ylabel('Score')
plt.title('Box Plot of Score by Group')
plt.grid(True)
plt.show()
