import backtrader as bt
import pandas as pd

# Load trading signals
data = pd.read_csv("AAPL_trading_signals.csv", index_col=0, parse_dates=True)

# Define a Trading Strategy
class MomentumStrategy(bt.Strategy):
    def __init__(self):
        self.signal = self.datas[0].lines.signal

    def next(self):
        if self.signal[0] > 0:  # Buy Signal
            self.buy()
        elif self.signal[0] < 0:  # Sell Signal
            self.sell()

# Load data into Backtrader
class PandasData(bt.feeds.PandasData):
    lines = ('signal',)
    params = (('signal', -1),)

datafeed = PandasData(dataname=data)

# Backtest
cerebro = bt.Cerebro()
cerebro.addstrategy(MomentumStrategy)
cerebro.adddata(datafeed)
cerebro.broker.set_cash(100000)
cerebro.run()
cerebro.plot()
