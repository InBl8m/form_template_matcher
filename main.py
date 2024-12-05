from fastapi import FastAPI
from app import form_router

app = FastAPI()

# Подключение маршрутов из отдельного файла
app.include_router(form_router.router)
