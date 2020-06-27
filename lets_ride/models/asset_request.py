from django.db import models
from django.core.exceptions import ValidationError
from lets_ride.models.user import User
from lets_ride.models.share_ride import ShareRide
from lets_ride.constants.enums import AssetSensitivity
from lets_ride.constants.constants \
    import ASSETTYPE, ASSET_SENSITIVITY

class AssetRequest(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(null=True, blank=True)
    flexible_timings = models.BooleanField(default=False)
    flexible_from_date_time = models.DateTimeField(null=True, blank=True)
    flexible_to_date_time = models.DateTimeField(null=True, blank=True)
    asset_quantity = models.IntegerField()
    asset_type = models.CharField(choices=ASSETTYPE, max_length=50)
    asset_type_others = models.CharField(max_length=100, null=True, blank=True)
    asset_sensitivity = models.CharField(
        choices=ASSET_SENSITIVITY,
        max_length=50
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'asset_requests'
    )
    accepted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assets_accepted",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.flexible_timings and self.travel_date_time:
            raise ValidationError("you cannot select flexible timings and travel datetime at same time")
        if self.flexible_timings is False:
            if self.flexible_from_date_time or self.flexible_to_date_time:
                raise ValidationError("you cannot select datetime range when flexible timings set to False")
        super(AssetRequest, self).save(*args, **kwargs)
