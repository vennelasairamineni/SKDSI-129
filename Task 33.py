import pandas as pd

start_dt = '2023-06-01'
end_dt = '2023-06-05'
date_idx = pd.date_range(start=start_dt, end=end_dt, freq='D')

date_idx_utc = pd.date_range(start=start_dt, end=end_dt, freq='D', tz='UTC')
print(date_idx_utc)

date_idx_localized = pd.date_range(start=start_dt, end=end_dt, freq='D')
date_idx_localized = date_idx_localized.tz_localize('Asia/Tokyo')
print(date_idx_localized)

date_idx_converted = date_idx_localized.tz_convert('Australia/Sydney')
print(date_idx_converted)

date_idx1_utc = pd.date_range(start=start_dt, periods=3, freq='D', tz='UTC')
date_idx2_tokyo = pd.date_range(start=start_dt, periods=3, freq='D', tz='Asia/Tokyo')
combined_idx = date_idx1_utc.union(date_idx2_tokyo)
print(combined_idx)
