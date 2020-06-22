from django.db import models
from django.core.exceptions import ValidationError
from lets_ride.models.user import User
from lets_ride.constants.constants import TRAVEL_MEDIUM


def validate_travel_medium(value):
    if value not in TRAVEL_MEDIUM:
        raise ValidationError("Travel_medium not in ", TRAVEL_MEDIUM)

def validate_asset_quantity(value):
    if value <= 0:
        raise ValidationError("Asset quantity should be positive value")


class TravelInfo(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)

    travel_medium = models.CharField(
        choices=TRAVEL_MEDIUM,
        max_length=50,
        validators=[validate_travel_medium]
    )

    asset_quantity = models.IntegerField(
        validators=[validate_asset_quantity]
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'travel_info'
    )


    def save(self, *args, **kwargs):

        if self.flexible_timings and self.travel_date_time:
            raise ValidationError(
                """
                you cannot select flexible
                timings and travel datetime at same time
                """
            )
        if self.flexible_timings is False:
            if self.flexible_from_date_time or self.flexible_to_date_time:
                raise ValidationError(
                    """
                    you cannot select datetime range
                    when flexible timings set to False
                    """
                )
        super().save(*args, **kwargs)