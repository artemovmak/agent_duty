import unittest

from shop.cart import DELIVERY_PRICE, Cart


class CartTest(unittest.TestCase):
    def test_subtotal(self):
        cart = Cart()
        cart.add("k1")
        cart.add("h1", 2)
        self.assertEqual(cart.subtotal(), 249000 + 2 * 39000)

    def test_unknown_sku(self):
        with self.assertRaises(KeyError):
            Cart().add("zz")

    def test_promo(self):
        cart = Cart()
        cart.add("k1")
        cart.apply_promo("SAVE10")
        self.assertEqual(cart.goods_total(), 224100)

    def test_unknown_promo(self):
        with self.assertRaises(ValueError):
            Cart().apply_promo("FREE100")

    def test_delivery(self):
        cart = Cart()
        cart.add("h1")
        self.assertEqual(cart.delivery(), DELIVERY_PRICE)
        cart.add("n1")
        self.assertEqual(cart.delivery(), 0)

    def test_empty_cart_has_no_delivery(self):
        self.assertEqual(Cart().total(), 0)


if __name__ == "__main__":
    unittest.main()
