import pandas as pd

current_period = pd.Period('2023-05', freq='M')
future_period = current_period + 4
print("Future Period:", future_period)

past_period = current_period - 3
print("Past Period:", past_period)

periods_range = pd.period_range(start='2023-05', end='2024-04', freq='M')
print("Periods Range:", periods_range)
