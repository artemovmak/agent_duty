"""История заказов покупателя."""
from .money import rub


def sort_orders(orders: list[dict]) -> list[dict]:
    """Заказы от новых к старым. Поле date в формате ДД.ММ.ГГГГ."""
    return sorted(orders, key=lambda order: order["date"], reverse=True)


def summary(order: dict) -> str:
    return f"№ {order['number']} от {order['date']}: {rub(order['total'])}"
