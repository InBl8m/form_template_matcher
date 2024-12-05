# form_template_matcher

Приложение для поиска подходящих шаблонов форм и типизации полей.

## Установка и запуск

1. **Сборка Docker-образа**:
    ```bash
    docker build -t form_template_matcher .
    ```

2. **Запуск контейнера**:
    ```bash
    docker run -d -p 8000:8000 form_template_matcher
    ```

3. **Тестирование**:
    Выполните тестовый скрипт:
    ```bash
    python test_requests.py
    ```
