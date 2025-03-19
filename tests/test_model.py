import unittest
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class TestMLModel(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load("trading_model.pkl")
        self.test_data = pd.DataFrame({'momentum': [0.05], 'macd': [0.02], 'volatility': [0.03]})

    def test_prediction(self):
        pred = self.model.predict(self.test_data)
        self.assertIn(pred[0], [-1, 0, 1])

if __name__ == '__main__':
    unittest.main()
