import unittest
from store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertEqual(calculate_price('under 10',5,.1), 4.99)
        self.assertEqual(calculate_price('under 10',5,.15), 5.00)
        self.assertEqual(calculate_price('under 10',5,.2), 3.75)
        self.assertEqual(calculate_price('under 10',10,.1), 5.25)
        self.assertEqual(calculate_price('under 10',10,.15), 5.15)
        self.assertEqual(calculate_price('under 10',10,.2), 5.05)


if __name__ == '__main__':
    unittest.main()
