"""Regression tests for issue #6: история заказов перемешана.

Проблема: sort_orders сортировала строку ДД.ММ.ГГГГ лексикографически,
из-за чего день сравнивался раньше месяца и года.
"""
import unittest

from shop.orders import sort_orders


class TestSortOrdersCrossMonth(unittest.TestCase):
    """02.11.2026 новее 15.10.2026, но лексикографически '02' < '15'."""

    def test_different_months_same_year(self):
        orders = [
            {"number": 1050, "date": "15.10.2026"},
            {"number": 1055, "date": "02.11.2026"},
        ]
        result = [o["number"] for o in sort_orders(orders)]
        self.assertEqual(result, [1055, 1050],
                         "Ноябрьский заказ должен стоять выше октябрьского")


class TestSortOrdersCrossYear(unittest.TestCase):
    """Январские заказы нового года новее декабрьских прошлого."""

    def test_january_newer_than_december(self):
        orders = [
            {"number": 2001, "date": "15.12.2025"},
            {"number": 2010, "date": "03.01.2026"},
        ]
        result = [o["number"] for o in sort_orders(orders)]
        self.assertEqual(result, [2010, 2001],
                         "Январь 2026 должен стоять выше декабря 2025")

    def test_full_cross_year_sequence(self):
        orders = [
            {"number": 3001, "date": "05.12.2025"},
            {"number": 3002, "date": "20.12.2025"},
            {"number": 3003, "date": "01.01.2026"},
            {"number": 3004, "date": "15.01.2026"},
        ]
        result = [o["number"] for o in sort_orders(orders)]
        self.assertEqual(result, [3004, 3003, 3002, 3001],
                         "Заказы должны идти строго от новых к старым")


if __name__ == "__main__":
    unittest.main()
