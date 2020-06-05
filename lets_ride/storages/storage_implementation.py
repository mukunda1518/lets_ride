import datetime
from typing import List, Union
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo
from lets_ride.models.asset_request import AssetRequest
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT
from lets_ride.dtos.dtos import (
    AssetRequestDto,
    RideRequestDto,
    BaseRideRequestDto,
    BaseAssetRequestDto,
)

class StorageImplementation(StorageInterface):

    def create_ride_request(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        seats: int,
        laguage_quantity: int
    ):
        RideRequest.objects.create(
            source=source,
            destination=destination,
            travel_date_time=travel_date_time,
            flexible_timings=flexible_timings,
            seats=seats,
            laguage_quantity=laguage_quantity,
            user_id=user_id
        )

    def create_ride_request_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        seats: int,
        laguage_quantity: int
    ):
        RideRequest.objects.create(
            source=source,
            destination=destination,
            flexible_timings=flexible_timings,
            flexible_from_date_time=flexible_travel_from_date_time,
            flexible_to_date_time=flexible_travel_to_date_time,
            seats=seats,
            laguage_quantity=laguage_quantity,
            user_id=user_id
        )

    def create_share_ride(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        seats: int,
        asset_quantity: int
    ):
        ShareRide.objects.create(
            source=source,
            destination=destination,
            travel_date_time=travel_date_time,
            flexible_timings=flexible_timings,
            seats=seats,
            asset_quantity=asset_quantity,
            user_id=user_id
        )

    def create_share_ride_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        seats: int,
        asset_quantity: int
    ):
        ShareRide.objects.create(
            source=source,
            destination=destination,
            flexible_timings=flexible_timings,
            flexible_from_date_time=flexible_travel_from_date_time,
            flexible_to_date_time=flexible_travel_to_date_time,
            seats=seats,
            asset_quantity=asset_quantity,
            user_id=user_id
        )

    def create_share_travel_info(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        travel_medium: str,
        asset_quantity: int
    ):
        TravelInfo.objects.create(
            source=source,
            destination=destination,
            travel_date_time=travel_date_time,
            flexible_timings=flexible_timings,
            travel_medium=travel_medium,
            asset_quantity=asset_quantity,
            user_id=user_id
        )

    def create_share_travel_info_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        travel_medium: str,
        asset_quantity: int
    ):
        TravelInfo.objects.create(
            source=source,
            destination=destination,
            flexible_timings=flexible_timings,
            travel_medium=travel_medium,
            flexible_from_date_time=flexible_travel_from_date_time,
            flexible_to_date_time=flexible_travel_to_date_time,
            asset_quantity=asset_quantity,
            user_id=user_id
        )

    def create_asset_request(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        asset_quantity: int,
        asset_type: str,
        asset_type_others: str,
        asset_sensitivity: str,
        deliver_to: str,
        phone_number: str
    ):
        AssetRequest.objects.create(
            source=source,
            destination=destination,
            travel_date_time=travel_date_time,
            flexible_timings=flexible_timings,
            asset_quantity=asset_quantity,
            asset_type=asset_type,
            asset_type_others=asset_type_others,
            asset_sensitivity=asset_sensitivity,
            deliver_to=deliver_to,
            phone_number=phone_number,
            user_id=user_id
        )

    def create_asset_request_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        asset_quantity: int,
        asset_type: str,
        asset_type_others: str,
        asset_sensitivity: str,
        deliver_to: str,
        phone_number: str
    ):
        AssetRequest.objects.create(
            source=source,
            destination=destination,
            flexible_timings=flexible_timings,
            flexible_from_date_time=flexible_travel_from_date_time,
            flexible_to_date_time=flexible_travel_to_date_time,
            asset_quantity=asset_quantity,
            asset_type=asset_type,
            asset_type_others=asset_type_others,
            asset_sensitivity=asset_sensitivity,
            deliver_to=deliver_to,
            phone_number=phone_number,
            user_id=user_id
        )
