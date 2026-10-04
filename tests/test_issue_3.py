"""Regression test for issue #3: discount rounds down instead of rounding correctly.

Утюг «Ромашка Пар» стоит 4 290,90 ₽ (429090 копеек).
С промокодом SAVE15 (15%) должно быть 4 290,90 × 0,85 = 3 647,265 → 3 647,27 ₽ (364727 копеек).
Раньше int() усекало результат до 3 647,26 ₽ (364726 копеек).
"""

import unittest
from shop.money import apply_discount


class TestDiscountRounding(unittest.TestCase):

    def test_iron_romashka_par_save15(self):
        """Основной кейс из баг-репорта: 4290,90 × 0,85 = 3647,265 → 3647,27."""
        price = 429090   # 4 290,90 ₽ в копейках
        result = apply_discount(price, 15)
        self.assertEqual(result, 364727,
                         "4290,90 × 0,85 должно округляться до 3647,27, а не усекаться до 3647,26")

    def test_round_half_up(self):
        """Общий случай: .5 копейки должны округляться вверх."""
        # 1 копейка × (100-1)/100 = 0.99 → 1
        # 3 копейки × 85/100 = 2.55 → 3
        self.assertEqual(apply_discount(3, 15), 3)

    def test_round_half_down_stays_correct(self):
        """Случай без дробной части не должен измениться."""
        # 200 × 0.85 = 170.0 → 170
        self.assertEqual(apply_discount(200, 15), 170)

    def test_exact_half_kopeck_rounds_up(self):
        """0.5 копейки должно округляться до 1 (не усекаться до 0)."""
        # 1 × 50/100 = 0.5 → должно быть 1, а не 0
        self.assertEqual(apply_discount(1, 50), 1)


if __name__ == "__main__":
    unittest.main()
