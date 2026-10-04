"""Regression tests for issue #4:
Дата отправки не должна попадать на субботу или воскресенье."""
import unittest
from datetime import date, datetime

from shop.delivery import ship_date


class Issue4ShipDateWeekendTest(unittest.TestCase):

    # --- Exact scenario from the issue ---
    def test_friday_after_cutoff_ships_monday(self):
        """Заказ в пятницу 09.10.2026 в 16:20 → отправка в понедельник 12.10.2026."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 9, 16, 20)),
            date(2026, 10, 12),
        )

    # --- Saturday must never be a ship date ---
    def test_friday_after_cutoff_not_saturday(self):
        """Дата отправки не должна быть субботой."""
        result = ship_date(datetime(2026, 10, 9, 16, 20))
        self.assertNotEqual(result.weekday(), 5, "ship_date вернул субботу")

    # --- Additional weekend-boundary cases ---
    def test_saturday_before_cutoff_ships_monday(self):
        """Заказ в субботу до 14:00 → отправка в понедельник."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 10, 9, 0)),
            date(2026, 10, 12),
        )

    def test_saturday_after_cutoff_ships_monday(self):
        """Заказ в субботу после 14:00 → отправка в понедельник."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 10, 15, 0)),
            date(2026, 10, 12),
        )

    def test_sunday_before_cutoff_ships_monday(self):
        """Заказ в воскресенье до 14:00 → отправка в понедельник."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 11, 9, 0)),
            date(2026, 10, 12),
        )

    def test_sunday_after_cutoff_ships_monday(self):
        """Заказ в воскресенье после 14:00 → отправка в понедельник."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 11, 15, 0)),
            date(2026, 10, 12),
        )

    # --- Weekday cases must still work ---
    def test_weekday_before_cutoff_same_day(self):
        """Заказ в будний день до 14:00 → отправка в тот же день."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 6, 11, 30)),
            date(2026, 10, 6),
        )

    def test_weekday_after_cutoff_next_day(self):
        """Заказ в будний день после 14:00 → отправка на следующий рабочий день."""
        self.assertEqual(
            ship_date(datetime(2026, 10, 6, 15, 0)),
            date(2026, 10, 7),
        )


if __name__ == "__main__":
    unittest.main()
