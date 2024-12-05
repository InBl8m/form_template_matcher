import requests

BASE_URL = "http://localhost:8000/get_form"

# Пример данных для тестирования
test_data = [
    # Пример с валидной формой, которая должна подойти к шаблону
    {
        "email_field": "test@example.com",
        "phone_field": "+7 999 123 45 67",
        "dob_field": "01.01.2000",
        "text_field": "Some text"
    },
    # Пример с валидной формой, которая должна подойти к шаблону, с дополнительным полем
    {
        "email_field": "test@example.com",
        "phone_field": "+7 999 123 45 67",
        "dob_field": "01.01.2000",
        "text_field": "Some text",
        "extra_field": "Some extra"
    },
    # Пример с ошибкой в поле email
    {
        "email_field": "invalid-email",
        "phone_field": "+7 999 123 45 67",
        "dob_field": "01.01.2000",
        "text_field": "Some text"
    },
    # Пример с отсутствующим полем (например, phone)
    {
        "email_field": "test@example.com",
        "dob_field": "01.01.2000",
        "text_field": "Some text"
    },
    # Пример с неправильным форматом даты, порядком и дополнительным полем
    {
        "email_field": "test@example.com",
        "dob_field": "2000/01/01",  # Неправильный формат даты
        "phone_field": "+7 999 123 45 67",
        "text_field": "Some text",
        "extra_field": "Some extra",
        "extra_field_2": "Some extra"
    },
]


def test_get_form(data):
    """Функция для отправки тестовых данных на сервер"""
    response = requests.post(BASE_URL, data=data)  # Используем 'data' для формы

    if response.status_code == 200:
        print(f"Ответ: {response.json()}")
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")


def run_tests():
    """Запуск всех тестов"""
    for i, data in enumerate(test_data, 1):
        print(f"Тест {i}: Отправка данных")
        test_get_form(data)
        print("-" * 30)


if __name__ == "__main__":
    run_tests()
