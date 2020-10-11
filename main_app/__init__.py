# Файл с описанием приложения

# Импорты
from flask import Flask

# Экземпляр класса нашего приложение которое и будет его именем
app = Flask(__name__)


#  Импортов маршрутов
from main_app import view

#  Импорт настроек для приложения и блюпринтов
from main_app.config import App_Conf

#  Установка настроек для приложения и блюпринтов
app.config.from_object(App_Conf)  # Настраиваем конфигурацию Flask передавая в него конфиги из объекта Configuratiion

# Импорт блюпринтов и их регистрация
