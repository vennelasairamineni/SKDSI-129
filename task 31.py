import pandas as pd
import numpy as np
new_date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
new_data = np.random.randn(len(new_date_range))
new_time_series_df = pd.DataFrame(new_data, index=new_date_range, columns=['Measurement'])
print(new_time_series_df.head())
