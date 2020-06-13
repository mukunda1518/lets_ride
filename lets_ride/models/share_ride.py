from django.db import models
from django.core.exceptions import ValidationError

from lets_ride.models.user import User


class ShareRide(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)
    seats = models.IntegerField()
    asset_quantity = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'share_rides'
    )

    def save(self, *args, **kwargs):
            if self.flexible_timings and self.travel_date_time:
                raise ValidationError("you cannot select flexible timings and travel datetime at same time")
            if self.flexible_timings is False:
                if self.flexible_from_date_time or self.flexible_to_date_time:
                    raise ValidationError("you cannot select datetime range when flexible timings set to False")
