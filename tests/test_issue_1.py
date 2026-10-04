"""Regression tests for issue #1.

Promo codes must be accepted regardless of letter case and leading/trailing
whitespace (e.g. "save10", "Save10", "SAVE10  " should all work like "SAVE10").
"""
import unittest

from shop.cart import Cart


class PromoNormalisationTest(unittest.TestCase):
    """apply_promo() should normalise the code before lookup."""

    def test_lowercase_promo(self):
        """Промокод строчными буквами должен приниматься."""
        cart = Cart()
        cart.add("k1")
        cart.apply_promo("save10")
        self.assertEqual(cart.goods_total(), 224100)

    def test_mixedcase_promo(self):
        """Промокод в смешанном регистре должен приниматься."""
        cart = Cart()
        cart.add("k1")
        cart.apply_promo("Save10")
        self.assertEqual(cart.goods_total(), 224100)

    def test_promo_with_trailing_spaces(self):
        """Промокод с пробелами по краям (как при копировании) должен приниматься."""
        cart = Cart()
        cart.add("k1")
        cart.apply_promo("  SAVE10  ")
        self.assertEqual(cart.goods_total(), 224100)

    def test_lowercase_with_spaces(self):
        """Комбинация: строчные буквы и пробелы по краям."""
        cart = Cart()
        cart.add("k1")
        cart.apply_promo("  save10 ")
        self.assertEqual(cart.goods_total(), 224100)

    def test_unknown_promo_still_raises(self):
        """Несуществующий промокод по-прежнему должен вызывать ValueError."""
        with self.assertRaises(ValueError):
            Cart().apply_promo("FREE100")


if __name__ == "__main__":
    unittest.main()
