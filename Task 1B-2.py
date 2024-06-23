import pandas as pd
import matplotlib.pyplot as plt

# New data
data = {
    'Group X': [10, 20, 15, 25, 30],
    'Group Y': [12, 18, 22, 27, 35],
    'Group Z': [14, 16, 24, 20, 28]
}
index = ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5']

# Create DataFrame
df_new = pd.DataFrame(data, index=index)

# Side-by-side bar plot
ax_new1 = df_new.plot(kind='bar', figsize=(10, 6))
ax_new1.set_xlabel('Products')
ax_new1.set_ylabel('Quantity')
ax_new1.set_title('Side-by-Side Bar Plot')
plt.xticks(rotation=0)
plt.show()

# Stacked bar plot
ax_new2 = df_new.plot(kind='bar', stacked=True, figsize=(10, 6))
ax_new2.set_xlabel('Products')
ax_new2.set_ylabel('Quantity')
ax_new2.set_title('Stacked Bar Plot')
plt.xticks(rotation=0)
plt.show()
