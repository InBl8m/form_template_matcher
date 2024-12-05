# Поиск подходящих шаблонов форм

## Установка и запуск

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/InBl8m/form_template_matcher
    ```

2. **Перейдите в директорию проекта**:
    ```bash
    cd form_template_matcher
    ```

3. **Сборка Docker-образа**:
    Выполните команду для сборки Docker-образа:
    ```bash
    docker build -t form_template_matcher .
    ```

4. **Запуск контейнера**:
    Запустите контейнер с приложением:
    ```bash
    docker run -d -p 8000:8000 form_template_matcher
    ```

5. **Тестирование**:
    После запуска контейнера выполните тестовый скрипт:
    ```bash
    python3 test_requests.py
    ```
