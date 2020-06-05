from django.db import models
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
