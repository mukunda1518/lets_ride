from django.contrib import admin
from lets_ride.models.asset_request import AssetRequest
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo


admin.site.register(AssetRequest)
admin.site.register(ShareRide)
admin.site.register(RideRequest)
admin.site.register(TravelInfo)