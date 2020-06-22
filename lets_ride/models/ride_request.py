from django.db import models
from django.core.exceptions import ValidationError
from lets_ride.models.user import User
from lets_ride.models.share_ride import ShareRide
from lets_ride.constants.constants import STATUS


def validate_seats(value):
    if value <= 0:
        raise ValidationError("No of seats shouldn't be negative")


def validate_laguage_quantity(value):
    if value < 0:
        raise ValidationError("Laguage quantity shouldn't be negative")


class RideRequest(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)
    seats = models.IntegerField(validators=[validate_seats])
    laguage_quantity = models.IntegerField(
        validators=[validate_laguage_quantity]
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'ride_requests'
    )
    accepted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rides_accepted",
        null=True,
        blank=True
    )


    def clean(self):
        if self.seats <= 0:
            raise ValidationError("No of seats shouldn't be negative")
        if self.validate_laguage_quantity < 0:
            raise ValidationError("Laguage quantity shouldn't be negative")

    def save(self, *args, **kwargs):

        self.clean()
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

