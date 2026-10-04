import unittest

from shop.orders import sort_orders, summary


class OrdersTest(unittest.TestCase):
    def test_sort_same_month(self):
        orders = [{"number": 1041, "date": "02.10.2026"}, {"number": 1045, "date": "05.10.2026"},
                  {"number": 1043, "date": "03.10.2026"}]
        self.assertEqual([o["number"] for o in sort_orders(orders)], [1045, 1043, 1041])

    def test_summary(self):
        self.assertEqual(summary({"number": 1047, "date": "06.10.2026", "total": 1248000}), "№ 1047 от 06.10.2026: 12 480,00 ₽")


if __name__ == "__main__":
    unittest.main()
