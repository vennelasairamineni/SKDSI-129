import pandas as pd
data_values = [10, 20, 30, 40, 50, 60]
index = pd.MultiIndex.from_tuples([('X', 1), ('X', 2), ('Y', 1), ('Y', 2), ('Z', 1), ('Z', 2)])
multi_index_series = pd.Series(data_values, index=index)
print("Series with MultiIndex:")
print(multi_index_series)
subset_X = multi_index_series.loc['X']
print("\nSubset X:")
print(subset_X)
subset_X_inner_2 = multi_index_series.loc[('X', 2)]
print("\nSubset X, Inner 2:")
print(subset_X_inner_2)
subset_Y = multi_index_series.loc['Y']
print("\nSubset Y:")
print(subset_Y)
subset_Z_inner_1 = multi_index_series.loc[('Z', 1)]
print("\nSubset Z, Inner 1:")
print(subset_Z_inner_1)
subset_Y_xs = multi_index_series.xs('Y')
print("\nSubset Y using xs:")
print(subset_Y_xs)
subset_inner_2 = multi_index_series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_2)
