"""Корзина: товары, промокод, доставка."""
from .catalog import price
from .money import apply_discount

PROMO_CODES = {"SAVE10": 10, "SAVE15": 15}
FREE_DELIVERY_FROM = 300000
DELIVERY_PRICE = 29900


class Cart:
    def __init__(self):
        self.items: dict[str, int] = {}
        self.promo: str | None = None

    def add(self, sku: str, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("quantity must be positive")
        price(sku)
        self.items[sku] = self.items.get(sku, 0) + qty

    def remove(self, sku: str) -> None:
        self.items.pop(sku, None)

    def apply_promo(self, code: str) -> None:
        code = code.strip().upper()
        if code not in PROMO_CODES:
            raise ValueError("unknown promo code")
        self.promo = code

    def subtotal(self) -> int:
        return sum(price(sku) * qty for sku, qty in self.items.items())

    def goods_total(self) -> int:
        """Стоимость товаров с учётом промокода."""
        return apply_discount(self.subtotal(), PROMO_CODES.get(self.promo, 0))

    def delivery(self) -> int:
        """Доставка бесплатная от FREE_DELIVERY_FROM копеек за товары с учётом скидки."""
        if not self.items:
            return 0
        return 0 if self.goods_total() > FREE_DELIVERY_FROM else DELIVERY_PRICE

    def total(self) -> int:
        return self.goods_total() + self.delivery()
