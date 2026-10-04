"""История заказов покупателя."""
from .money import rub


def _date_key(date_str: str) -> tuple[int, int, int]:
    """Преобразует строку ДД.ММ.ГГГГ в кортеж (ГГГГ, ММ, ДД) для сортировки."""
    day, month, year = date_str.split(".")
    return int(year), int(month), int(day)


def sort_orders(orders: list[dict]) -> list[dict]:
    """Заказы от новых к старым. Поле date в формате ДД.ММ.ГГГГ."""
    return sorted(orders, key=lambda order: _date_key(order["date"]), reverse=True)


def summary(order: dict) -> str:
    return f"№ {order['number']} от {order['date']}: {rub(order['total'])}"
