from django.apps import AppConfig


class TelebotConfig(AppConfig):
    name = 'telebot'
    init = True

    def ready(self):
        pass
