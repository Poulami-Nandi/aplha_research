import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock data
def get_stock_data(ticker, start="2020-01-01", end="2025-03-18"):
    data = yf.download(ticker, start=start, end=end)
    return data

# Calculate Momentum (12-month rate of return)
def calculate_momentum(data, period=252):
    data['momentum'] = data['Close'].pct_change(periods=period)
    return data

# Calculate Moving Average Convergence Divergence (MACD)
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    data['ema_short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['ema_long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['macd'] = data['ema_short'] - data['ema_long']
    data['macd_signal'] = data['macd'].ewm(span=signal_window, adjust=False).mean()
    return data

# Calculate Volatility (Rolling Standard Deviation)
def calculate_volatility(data, window=30):
    data['volatility'] = data['Close'].rolling(window=window).std()
    return data

if __name__ == "__main__":
    stock = "AAPL"
    data = get_stock_data(stock)
    
    data = calculate_momentum(data)
    data = calculate_macd(data)
    data = calculate_volatility(data)

    # Plot Momentum
    plt.figure(figsize=(12, 6))
    data['momentum'].plot(title=f"{stock} Momentum Factor (12-Month Change)")
    plt.show()
    
    data.to_csv(f"{stock}_alpha_factors.csv")
