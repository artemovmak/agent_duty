import unittest
from datetime import date, datetime

from shop.delivery import ship_date


class DeliveryTest(unittest.TestCase):
    def test_before_cutoff(self):
        self.assertEqual(ship_date(datetime(2026, 10, 6, 11, 30)), date(2026, 10, 6))

    def test_after_cutoff(self):
        self.assertEqual(ship_date(datetime(2026, 10, 6, 15, 0)), date(2026, 10, 7))

    def test_sunday(self):
        self.assertEqual(ship_date(datetime(2026, 10, 11, 9, 0)), date(2026, 10, 12))


if __name__ == "__main__":
    unittest.main()
