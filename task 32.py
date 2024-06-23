import pandas as pd
start_dt1 = '2023-01-01'
end_dt1 = '2023-12-31'
date_idx1 = pd.date_range(start=start_dt1, end=end_dt1)
print(date_idx1)
start_dt2 = '2023-01-01'
num_periods = 365  # for a full year
date_idx2 = pd.date_range(start=start_dt2, periods=num_periods)
print(date_idx2)
end_dt2 = '2023-12-31'
num_periods2 = 365  # for a full year
date_idx3 = pd.date_range(end=end_dt2, periods=num_periods2)
print(date_idx3)
start_dt3 = '2023-01-01'
end_dt3 = '2023-12-31'
date_idx4 = pd.date_range(start=start_dt3, end=end_dt3, freq='D')  # 'D' generates dates on a daily basis
print(date_idx4)
