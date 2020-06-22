from django.apps import AppConfig


class FactoryAppConfig(AppConfig):
    name = "factory"

    def ready(self):
        from factory import signals # pylint: disable=unused-variable
