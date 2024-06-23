import pandas as pd
import numpy as np
d= {
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'C': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}
df = pd.dFrame(d)
print("Original dFrame:")
print(df)
md = df.isna()
print("\nMissing d in dFrame:")
print(md)
ddr = df.dropna()
print("\ndFrame after dropping rows with any missing d:")
print(ddr)
ddc = df.dropna(axis=1)
print("\ndFrame after dropping columns with any missing d:")
print(ddc)
ddf = df.fillna(value={'A': df['A'].mean(), 'B': df['B'].mean(), 'C': 'missing', 'D': 0})
print("\ndFrame after filling missing d:")
print(ddf)
dfdup = df.append(df.iloc[2], ignore_index=True)
print("\ndFrame with dup:")
print(dfdup)
dup = dfdup.duplicated()
print("\ndup in dFrame:")
print(dup)
df_no_dup = dfdup.drop_dup()
print("\ndFrame after removing dup:")
print(df_no_dup)
