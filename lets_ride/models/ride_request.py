from django.db import models
from lets_ride.models.user import User
from lets_ride.models.share_ride import ShareRide
from lets_ride.constants.constants import STATUS

class RideRequest(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)
    seats = models.IntegerField()
    laguage_quantity = models.IntegerField()
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'ride_requests'
    )
    accepted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rides_accepted",
        null=True
    )
