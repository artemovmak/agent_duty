"""Дата отправки заказа со склада."""
from datetime import date, datetime, timedelta

CUTOFF_HOUR = 14


def ship_date(ordered_at: datetime) -> date:
    """Заказ до 14:00 уезжает в тот же рабочий день, после 14:00 в следующий рабочий.
    Склад не работает в субботу и воскресенье."""
    day = ordered_at.date()
    if ordered_at.hour >= CUTOFF_HOUR:
        day += timedelta(days=1)
    if day.weekday() == 6:
        day += timedelta(days=1)
    return day
