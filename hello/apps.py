from django.apps import AppConfig


class AppNameConfig(AppConfig):
    name = 'hello'

    def ready(self):
        from .models import SearchAreas
        from .bot import main
        from threading import Thread
        Thread(target=main).start()


class YandexbotConfig(AppConfig):
    name = 'hello'
