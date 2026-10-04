"""Деньги в магазине храним в копейках, целыми числами."""


def rub(kopecks: int) -> str:
    """Сумма для показа покупателю: 1999050 -> '19 990,50 ₽'."""
    sign = "-" if kopecks < 0 else ""
    rubles, kop = divmod(abs(kopecks), 100)
    return f"{sign}{rubles:,}".replace(",", " ") + f",{kop:02d} ₽"


def apply_discount(kopecks: int, percent: int) -> int:
    """Цена со скидкой в процентах. Копейки округляются по правилам арифметики."""
    if not 0 <= percent <= 100:
        raise ValueError("discount must be between 0 and 100 percent")
    return int(kopecks * (100 - percent) / 100)
