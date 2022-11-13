import sys

sys.path.insert(1, "/home/kwalker/stem/forage/jpmorgan/jpmc-task-1")

import client
import unittest


class TestClientFuntions(unittest.TestCase):

    quotes = [
        {"stock": "FOO", "top_bid": {"price": 95.0}, "top_ask": {"price": 97.0}},
        {"stock": "BAR", "top_bid": {"price": 98.0}, "top_ask": {"price": 101.0}},
    ]

    def test_GetDataPoint_returns_correct_price(self):
        for quote in self.quotes:
            expect_price = (
                float(quote["top_bid"]["price"]) + float(quote["top_ask"]["price"])
            ) / 2
            stock, bid_price, ask_price, price = client.getDataPoint(quote)
            self.assertEqual(expect_price, price)

    def test_GetRatio(self):
        price_a = 95.0
        price_b = 98.0
        expect_ratio = price_a / price_b
        actual_ratio = client.getRatio(price_a, price_b)
        self.assertEqual(expect_ratio, actual_ratio)

    def test_GetRatio_returns_None_on_ZeroDivision(self):
        price_a = 95.0
        price_b = 0.0
        ratio = client.getRatio(price_a, price_b)
        self.assertIsNone(ratio)


unittest.main()
