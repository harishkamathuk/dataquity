import unittest
from app.fetch_stock_data import fetch_stock_data

class TestFetchStockData(unittest.TestCase):

    def test_fetch_stock_data_success(self):
        symbol = "AAPL"
        data = fetch_stock_data(symbol)
        self.assertIsInstance(data, dict)
        self.assertIn('symbol', data)

    def test_fetch_stock_data_error(self):
        symbol = "INVALID"
        with self.assertRaises(Exception):
            fetch_stock_data(symbol)

if __name__ == "__main__":
    unittest.main()
