from django.apps import AppConfig


class LetsRideAuthAppConfig(AppConfig):
    name = "lets_ride_auth"

    def ready(self):
        from lets_ride_auth import signals # pylint: disable=unused-variable
