from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class MetaConfig(AppConfig):
    name = 'meta'

    def ready(self):
        autodiscover_modules('api')

