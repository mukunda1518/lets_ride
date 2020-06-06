from typing import List, Union, Tuple
from django.db.models import Q
import datetime
from lets_ride.interactors.storages.matching_shares_results_storage_interface \
    import MatchingSharesStorageInterface
from lets_ride.dtos.dtos import (
    BaseRideShareDto,
    BaseTravelInfoDto,
    RideMatchingDto,
    AssetMatchingDto,
    BaseRideRequestDto,
    BaseAssetRequestDto
)
from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo
from lets_ride.models.asset_request import AssetRequest
from lets_ride.models.ride_request import RideRequest



class MatchingSharesStorageImplementation(MatchingSharesStorageInterface):

    def get_ride_shares(self, user_id: int) -> List[BaseRideShareDto]:

        ride_share_objs = ShareRide.objects.filter(user_id=user_id)
        ride_share_dtos = self._get_ride_share_dtos(ride_share_objs)
        return ride_share_dtos


    def _get_ride_share_dtos(
        self, ride_share_objs: List[ShareRide]
    ) -> List[BaseRideShareDto]:

        ride_share_dtos = []
        for ride_share_obj in ride_share_objs:
            ride_share_dto = self._get_ride_share_dto(ride_share_obj)
            ride_share_dtos.append(ride_share_dto)

        return ride_share_dtos


    def _get_ride_share_dto(
        self, ride_share_obj: ShareRide
    ) -> BaseRideShareDto:

        from_datetime_obj, to_datetime_obj, travel_datetime_obj = \
            self._get_datetime_based_on_flexible_timings(ride_share_obj)

        ride_share_dto = BaseRideShareDto(
            ride_share_id=ride_share_obj.id,
            source=ride_share_obj.source,
            destination=ride_share_obj.destination,
            flexible_timings=ride_share_obj.flexible_timings,
            travel_date_time=travel_datetime_obj,
            flexible_from_date_time=from_datetime_obj,
            flexible_to_date_time=to_datetime_obj,
            seats=ride_share_obj.seats,
            asset_quantity=ride_share_obj.asset_quantity
        )
        return ride_share_dto


    def get_travel_shares(self, user_id: int) -> List[BaseTravelInfoDto]:
        travel_share_objs = TravelInfo.objects.filter(user_id=user_id)
        travel_share_dtos = self._get_travel_share_dtos(travel_share_objs)
        return travel_share_dtos


    def _get_travel_share_dtos(
        self, travel_share_objs: List[TravelInfo]
    ) -> List[BaseTravelInfoDto]:

        travel_share_dtos = []
        for travel_share_obj in travel_share_objs:
            travel_share_dto = self._get_travel_share_dto(travel_share_obj)
            travel_share_dtos.append(travel_share_dto)
        return travel_share_dtos


    def _get_travel_share_dto(
        self, travel_share_obj: TravelInfo
    ) -> BaseTravelInfoDto:

        from_datetime_obj, to_datetime_obj, travel_datetime_obj = \
            self._get_datetime_based_on_flexible_timings(travel_share_obj)

        travel_share_dto = BaseTravelInfoDto(
            travel_share_id=travel_share_obj.id,
            source=travel_share_obj.source,
            destination=travel_share_obj.destination,
            flexible_timings=travel_share_obj.flexible_timings,
            travel_date_time=travel_datetime_obj,
            flexible_from_date_time=from_datetime_obj,
            flexible_to_date_time=to_datetime_obj,
            travel_medium=travel_share_obj.travel_medium,
            asset_quantity=travel_share_obj.asset_quantity
        )
        return travel_share_dto


    def get_ride_matching_requests(
        self, source: str, destination: str, seats: int, asset_quantity: int,
        from_datetime: datetime.datetime, to_datetime: datetime.datetime
    ) -> List[RideMatchingDto]:

        ride_request_matching_objs = RideRequest.objects.filter(
            Q(
                flexible_timings=False,
                travel_date_time__gte=from_datetime,
                travel_date_time__lte=to_datetime
            ) |
            Q(
                flexible_timings=True,
                flexible_from_date_time__gte=from_datetime,
                flexible_to_date_time__lte=to_datetime
            ),
            source__iexact=source,
            destination__iexact=destination,
            accepted_by__isnull=True,
            seats__lte=seats,
            laguage_quantity__lte=asset_quantity
        ).select_related('user')

        ride_matching_dtos = self._get_ride_matching_dtos(
            ride_request_matching_objs
        )
        return ride_matching_dtos


    def _get_ride_matching_dtos(
        self, ride_matching_objs: List[RideRequest]
    ) -> List[RideMatchingDto]:

        ride_matching_dtos = []
        for ride_matching_obj in ride_matching_objs:
            ride_matching_dto = self._get_ride_matching_dto(ride_matching_obj)
            ride_matching_dtos.append(ride_matching_dto)
        return ride_matching_dtos



    def _get_ride_matching_dto(
        self, ride_matching_obj: RideRequest
    ) -> RideMatchingDto:

        base_ride_matching_dto = self._get_base_ride_matching_dto(
            ride_matching_obj
        )

        ride_matching_dto = RideMatchingDto(
            ride_dto=base_ride_matching_dto,
            ride_matching_id=0,
            username=ride_matching_obj.user.username,
            user_phone_number=ride_matching_obj.user.phone_number
        )
        return ride_matching_dto


    def _get_base_ride_matching_dto(
        self, ride_matching_obj: RideRequest
    ) -> BaseRideRequestDto:

        from_datetime_obj, to_datetime_obj, travel_datetime_obj = \
            self._get_datetime_based_on_flexible_timings(ride_matching_obj)

        base_ride_matching_dto = BaseRideRequestDto(
            ride_request_id=ride_matching_obj.id,
            source=ride_matching_obj.source,
            destination=ride_matching_obj.destination,
            travel_date_time=travel_datetime_obj,
            flexible_timings=ride_matching_obj.flexible_timings,
            flexible_from_date_time= from_datetime_obj,
            flexible_to_date_time=to_datetime_obj,
            seats=ride_matching_obj.seats,
            laguage_quantity=ride_matching_obj.laguage_quantity
        )
        return base_ride_matching_dto


    def get_travel_matching_requests(
        self, source: str, destination: str, asset_quantity: int,
        from_datetime: datetime.datetime, to_datetime: datetime.datetime
    ) -> List[AssetMatchingDto]:

        asset_request_matching_objs = AssetRequest.objects.filter(
            Q(
                flexible_timings=False,
                travel_date_time__gte = from_datetime,
                travel_date_time__lte=to_datetime
            ) |
            Q(
                flexible_timings=True,
                flexible_from_date_time__gte=from_datetime,
                flexible_to_date_time__lte=to_datetime
            ),
            source__iexact=source,
            destination__iexact=destination,
            accepted_by__isnull=True,
            asset_quantity__lte=asset_quantity
        ).select_related('user')

        asset_matching_dtos = self._get_asset_matching_dtos(
            asset_request_matching_objs
        )
        return asset_matching_dtos


    def _get_asset_matching_dtos(
        self, asset_request_matching_objs: List[AssetRequest]
    ) -> List[AssetMatchingDto]:

        asset_matching_dtos = []
        for asset_request_matching_obj in asset_request_matching_objs:
            asset_matching_dto = self._get_asset_matching_dto(
                asset_request_matching_obj
            )
            asset_matching_dtos.append(asset_matching_dto)
        return asset_matching_dtos


    def _get_asset_matching_dto(
        self, asset_request_matching_obj: AssetRequest
    ) -> AssetMatchingDto:

        base_asset_matching_dto = self._get_base_asset_matching_dto(
            asset_request_matching_obj
        )

        asset_matching_dto = AssetMatchingDto(
            asset_dto=base_asset_matching_dto,
            travel_matching_id=0,
            ride_matching_id=0,
            username=asset_request_matching_obj.user.username,
            user_phone_number=asset_request_matching_obj.user.phone_number
        )
        return asset_matching_dto


    def _get_base_asset_matching_dto(
        self, asset_request_matching_obj: AssetRequest
    ) -> BaseAssetRequestDto:

        from_datetime_obj, to_datetime_obj, travel_datetime_obj = \
            self._get_datetime_based_on_flexible_timings(asset_request_matching_obj)

        base_asset_matching_dto = BaseAssetRequestDto(
            asset_request_id=asset_request_matching_obj.id,
            source=asset_request_matching_obj.source,
            destination=asset_request_matching_obj.destination,
            travel_date_time=travel_datetime_obj,
            flexible_timings=asset_request_matching_obj.flexible_timings,
            flexible_from_date_time= from_datetime_obj,
            flexible_to_date_time=to_datetime_obj,
            asset_quantity=asset_request_matching_obj.asset_quantity,
            asset_type=asset_request_matching_obj.asset_type,
            asset_type_others=asset_request_matching_obj.asset_type_others,
            asset_sensitivity=asset_request_matching_obj.asset_sensitivity,
            deliver_to=asset_request_matching_obj.deliver_to,
            phone_number=asset_request_matching_obj.phone_number
        )
        return base_asset_matching_dto

    def _get_datetime_based_on_flexible_timings(
        self, base_obj: Union[AssetRequest, RideRequest, ShareRide, TravelInfo]
    ) -> Tuple:

        from_datetime_obj = ""
        to_datetime_obj = ""
        travel_datetime_obj = ""

        if base_obj.flexible_timings:
            from_datetime_obj = \
                base_obj.flexible_from_date_time
            to_datetime_obj = base_obj.flexible_to_date_time
        else:
            travel_datetime_obj = base_obj.travel_date_time
        return from_datetime_obj, to_datetime_obj, travel_datetime_obj
