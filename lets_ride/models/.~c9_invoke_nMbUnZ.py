from django.db import models
from lets_ride.models.user import User
from lets_ride.constants.enums import AssetSensitivity
from lets_ride.constants.constants import ASSETTYPE, ASSET_SENSITIVITY

class AssetRequest(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(null=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True)
    flexible_to_date_time = models.DateTimeField(null=True)
    asset_quantity = models.IntegerField()
    asset_type = models.CharField(choices=ASSETTYPE, max_length=50)
    asset_type_others = models.CharField(max_length=100, null=True)
    asset_sensitivity = models.CharField(
        choices=ASSET_SENSITIVITY,
        max_length=50
    )
    deliver_to = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'asset_requests'
    )
    accepted_person = models.Charfield()
