from fastapi import APIRouter, Request, Form
from typing import Dict
from app.validators import detect_field_type
from tinydb import TinyDB, Query

router = APIRouter()
db = TinyDB("app/database.json")
Template = Query()


@router.post("/get_form")
async def get_form(request: Request):
    # Получаем все данные из формы
    form_data = await request.form()

    # Преобразуем данные в словарь
    data = dict(form_data)

    # Разделим данные на обычные поля и динамические (например, extra_field_*)
    regular_fields = {key: value for key, value in data.items() if not key.startswith("extra_field")}
    extra_fields = {key: value for key, value in data.items() if key.startswith("extra_field")}

    matched_template = None

    # Поиск подходящего шаблона среди всех в базе данных
    for template in db.all():
        if all(
                field in regular_fields
                and detect_field_type(regular_fields[field]) == template.get(field)
                for field in template
                if field != "name"
        ):
            matched_template = template
            break

    # Если шаблон найден, возвращаем его имя
    if matched_template:
        return {"template_name": matched_template["name"]}

    # Если шаблон не найден, возвращаем типы полей, включая дополнительные
    result = {}
    # Порядок полей: дата, телефон, email, текст
    field_order = ["dob_field", "phone_field", "email_field", "text_field"]

    # Сортируем поля по указанному порядку
    for field in field_order:
        if field in regular_fields:
            result[field] = detect_field_type(regular_fields[field])

    # Для дополнительных полей возвращаем тип данных, если они есть
    for field, value in extra_fields.items():
        result[field] = "text"  # В данном примере мы считаем, что дополнительные поля — это текст

    return result
