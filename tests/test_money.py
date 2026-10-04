import unittest

from shop.money import apply_discount, rub


class MoneyTest(unittest.TestCase):
    def test_rub(self):
        self.assertEqual(rub(1999050), "19 990,50 ₽")
        self.assertEqual(rub(5), "0,05 ₽")
        self.assertEqual(rub(-12000), "-120,00 ₽")

    def test_discount_round_numbers(self):
        self.assertEqual(apply_discount(100000, 10), 90000)
        self.assertEqual(apply_discount(249000, 15), 211650)
        self.assertEqual(apply_discount(39000, 0), 39000)
        self.assertEqual(apply_discount(39000, 100), 0)

    def test_discount_range(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 120)


if __name__ == "__main__":
    unittest.main()
