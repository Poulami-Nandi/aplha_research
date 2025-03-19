import unittest
import pandas as pd
from trading_strategy import trading_strategy

class TestTradingStrategy(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'momentum': [0.05, -0.02, 0.1, -0.03],
            'macd': [0.02, -0.01, 0.04, -0.02],
            'macd_signal': [0.01, -0.02, 0.03, -0.01]
        })
    
    def test_trading_signals(self):
        df = trading_strategy(self.data)
        self.assertEqual(df['signal'].tolist(), [1, -1, 1, -1])

if __name__ == '__main__':
    unittest.main()
