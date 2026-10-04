"""Regression test for issue #8.

«Бесплатная доставка от 3 000 ₽» — при сумме ровно 3 000 ₽ (300 000 копеек)
доставка должна быть бесплатной, а не 299 ₽.
"""
import unittest
from unittest.mock import patch

from shop.cart import DELIVERY_PRICE, FREE_DELIVERY_FROM, Cart


class FreeDeliveryAtExactThresholdTest(unittest.TestCase):
    def _cart_with_goods_total(self, amount: int) -> Cart:
        """Возвращает корзину, у которой goods_total() == amount копеек."""
        cart = Cart()
        # Подменяем goods_total, чтобы точно контролировать сумму
        cart.goods_total = lambda: amount
        # items должен быть непустым, чтобы delivery() не вернул 0 по пустой корзине
        cart.items = {"__mock__": 1}
        return cart

    def test_delivery_is_free_at_exact_threshold(self):
        """При сумме ровно FREE_DELIVERY_FROM доставка должна быть бесплатной."""
        cart = self._cart_with_goods_total(FREE_DELIVERY_FROM)
        self.assertEqual(
            cart.delivery(),
            0,
            msg=(
                f"Ожидалась бесплатная доставка при сумме {FREE_DELIVERY_FROM} коп. "
                f"(= {FREE_DELIVERY_FROM / 100:.2f} ₽), но получили {cart.delivery()} коп."
            ),
        )

    def test_delivery_is_charged_below_threshold(self):
        """При сумме ниже порога доставка должна взиматься."""
        cart = self._cart_with_goods_total(FREE_DELIVERY_FROM - 1)
        self.assertEqual(cart.delivery(), DELIVERY_PRICE)

    def test_delivery_is_free_above_threshold(self):
        """При сумме выше порога доставка по-прежнему бесплатна."""
        cart = self._cart_with_goods_total(FREE_DELIVERY_FROM + 1)
        self.assertEqual(cart.delivery(), 0)


if __name__ == "__main__":
    unittest.main()
