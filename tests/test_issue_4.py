"""Regression test for issue #4:
Заказ в пятницу после 14:00 должен отправляться в понедельник, а не в субботу."""
import unittest
from datetime import date, datetime

from shop.delivery import ship_date


class Issue4SaturdaySkipTest(unittest.TestCase):
    def test_friday_after_cutoff_ships_monday(self):
        """Пятница 09.10.2026 16:20 → следующий рабочий день = понедельник 12.10.2026."""
        ordered_at = datetime(2026, 10, 9, 16, 20)   # пятница, после 14:00
        self.assertEqual(ship_date(ordered_at), date(2026, 10, 12))

    def test_friday_before_cutoff_ships_friday(self):
        """Пятница 09.10.2026 11:00 → отправка в тот же день (пятница)."""
        ordered_at = datetime(2026, 10, 9, 11, 0)    # пятница, до 14:00
        self.assertEqual(ship_date(ordered_at), date(2026, 10, 9))

    def test_saturday_order_ships_monday(self):
        """Заказ в субботу 10.10.2026 09:00 → отправка в понедельник 12.10.2026."""
        ordered_at = datetime(2026, 10, 10, 9, 0)    # суббота, до 14:00
        self.assertEqual(ship_date(ordered_at), date(2026, 10, 12))

    def test_saturday_after_cutoff_ships_monday(self):
        """Заказ в субботу 10.10.2026 15:00 → отправка в понедельник 12.10.2026."""
        ordered_at = datetime(2026, 10, 10, 15, 0)   # суббота, после 14:00
        self.assertEqual(ship_date(ordered_at), date(2026, 10, 12))


if __name__ == "__main__":
    unittest.main()
