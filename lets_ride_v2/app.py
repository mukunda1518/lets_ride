from django.apps import AppConfig


class LetsRideV2AppConfig(AppConfig):
    name = "lets_ride_v2"

    def ready(self):
        from lets_ride_v2 import signals # pylint: disable=unused-variable
