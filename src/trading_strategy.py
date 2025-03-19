import pandas as pd
import numpy as np

# Load the stock data with alpha factors
data = pd.read_csv("AAPL_alpha_factors.csv", index_col=0, parse_dates=True)

# Define trading strategy: Buy when momentum is positive and MACD crosses above the signal line
def trading_strategy(data):
    data['signal'] = 0
    data.loc[(data['momentum'] > 0) & (data['macd'] > data['macd_signal']), 'signal'] = 1  # Buy Signal
    data.loc[(data['momentum'] < 0) & (data['macd'] < data['macd_signal']), 'signal'] = -1  # Sell Signal
    return data

data = trading_strategy(data)
data.to_csv("AAPL_trading_signals.csv")
print("Trading signals saved to file.")
