import re
from datetime import datetime


def detect_field_type(value: str) -> str:
    try:
        # Попробуем два формата даты
        datetime.strptime(value, "%d.%m.%Y")
        return "date"
    except ValueError:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return "date"
        except ValueError:
            pass

    # Проверка на телефон
    if re.fullmatch(r"\+7 \d{3} \d{3} \d{2} \d{2}", value):
        return "phone"

    # Проверка на email
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
        return "email"

    # Если ничего не подошло
    return "text"
