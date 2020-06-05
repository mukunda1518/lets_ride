import datetime
from typing import List, Union
from django.db.models import Case, CharField, Value, When, Q
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
    RideRequestsDto
)

class StorageImplementation:

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
        
        
        
        
        
        
        
        
        
        
        

    # def my_requests(
    #     self,
    #     user_id: int,
    #     offset: int,
    #     limit: int
    # ) -> RideAssetRequestsDto:

    #     limit = offset+limit
    #     ride_request_objs = RideRequest.objects\
    #                                   .filter(user_id=user_id)\
    #                                   .select_related("accepted_by")[offset:limit]

    #     total_rides = RideRequest.objects.filter(user_id=user_id).count()
    #     ride_request_dtos = self._get_ride_request_dtos(ride_request_objs)
    #     asset_request_objs = AssetRequest.objects\
    #                                   .filter(user_id=user_id)\
    #                                   .select_related("accepted_by")[offset:limit]

    #     total_assets = AssetRequest.objects.filter(user_id=user_id).count()
    #     asset_request_dtos = self._get_asset_request_dtos(asset_request_objs)

    #     ride_asset_request_dto = RideAssetRequestsDto(
    #         ride_dtos=ride_request_dtos,
    #         total_rides_count=total_rides,
    #         asset_dtos=asset_request_dtos,
    #         total_assets_count=total_assets
    #     )
    #     return ride_asset_request_dto


    # def _get_asset_request_dtos(
    #     self,
    #     asset_request_objs: AssetRequest,
    # ) -> List[AssetRequestDto]:

    #     asset_request_dtos = []

    #     for asset_request_obj in asset_request_objs:
    #         base_asset_request_dto = self._get_base_asset_request_dto(
    #             asset_request_obj=asset_request_obj
    #         )
    #         asset_request_dto = self._get_asset_request_dto(
    #             asset_request_obj, base_asset_request_dto
    #         )
    #         asset_request_dtos.append(asset_request_dto)

    #     return asset_request_dtos


    # def _get_asset_request_dto(
    #     self,
    #     asset_request_obj: AssetRequest,
    #     base_asset_request_dto: BaseAssetRequestDto
    # ) -> AssetRequestDto:

    #     accepted_person = ""
    #     accepted_person_phone_number = ""
    #     is_accepted_by = self._is_request_accepted(
    #             request_obj=asset_request_obj
    #     )
    #     if is_accepted_by:
    #         accepted_person = asset_request_obj.accepted_by.username
    #         accepted_person_phone_number = \
    #         asset_request_obj.accepted_by.phone_number

    #     asset_request_dto = AssetRequestDto(
    #         asset_request_id= asset_request_obj.id,
    #         asset_dto=base_asset_request_dto,
    #         accepted_person=accepted_person,
    #         accepted_person_phone_number=accepted_person_phone_number,
    #         status=""
    #     )
    #     return asset_request_dto


    # def _get_base_asset_request_dto(
    #     self,
    #     asset_request_obj: AssetRequest,
    # ) -> BaseAssetRequestDto:

    #     from_datetime_obj = ""
    #     to_datetime_obj = ""
    #     travel_datetime_obj = ""

    #     if asset_request_obj.flexible_timings:
    #         from_datetime_obj = asset_request_obj.flexible_from_date_time
    #         to_datetime_obj = asset_request_obj.flexible_to_date_time
    #     else:
    #         travel_datetime_obj = asset_request_obj.travel_date_time

    #     base_asset_request_dto = BaseAssetRequestDto(
    #             source=asset_request_obj.source,
    #             destination=asset_request_obj.destination,
    #             travel_date_time=travel_datetime_obj,
    #             flexible_timings=asset_request_obj.flexible_timings,
    #             flexible_from_date_time= from_datetime_obj,
    #             flexible_to_date_time=to_datetime_obj,
    #             asset_quantity=asset_request_obj.asset_quantity,
    #             asset_type=asset_request_obj.asset_type,
    #             asset_type_others=asset_request_obj.asset_type_others,
    #             asset_sensitivity=asset_request_obj.asset_sensitivity,
    #             deliver_to=asset_request_obj.deliver_to,
    #             phone_number=asset_request_obj.phone_number
    #         )
    #     return base_asset_request_dto


    def get_ride_request_with_status_accepted(
        self, user_id: int, offset: int,
        limit: int, sort_key: str, sort_value: str
    ) -> RideRequestsDto:

        limit = offset+limit
        filtered_ride_request_objs =  RideRequest.objects.filter(
            user_id=user_id, accepted_by_id__isnull=False
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, offset, limit,
            filtered_ride_request_objs,
        )
        total_rides = len(ride_request_objs)
        ride_request_objs = ride_request_objs[offset:limit]
        ride_request_dtos = self._get_ride_request_dtos(ride_request_objs)
        ride_requests_dto = self._get_ride_requests_dto(
            ride_request_dtos, total_rides
        )
        return ride_requests_dto



    def get_ride_request_with_status_expired(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> RideRequestsDto:

        limit = offset+limit
        filtered_ride_request_objs = RideRequest.objects.filter(
            Q(flexible_timings=False, travel_date_time__lte=current_datetime_obj) |
            Q(flexible_timings=True, flexible_to_date_time__lte=current_datetime_obj),
            user_id=user_id
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, offset, limit,
            filtered_ride_request_objs,
        )
        total_rides = len(ride_request_objs)
        ride_request_objs = ride_request_objs[offset:limit]
        ride_request_dtos = self._get_ride_request_dtos(ride_request_objs)
        ride_requests_dto = self._get_ride_requests_dto(
            ride_request_dtos, total_rides
        )
        return ride_requests_dto



    def get_ride_request_with_status_pending(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> RideRequestsDto:

        limit = offset+limit
        filtered_ride_request_objs = RideRequest.objects.filter(
            Q(flexible_timings=False, travel_date_time__gt=current_datetime_obj) |
            Q(flexible_timings=True, flexible_to_date_time__gt=current_datetime_obj),
            user_id=user_id, accepted_by_id__isnull=True
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, offset, limit,
            filtered_ride_request_objs,
        )
        total_rides = len(ride_request_objs)
        ride_request_objs = ride_request_objs[offset:limit]
        ride_request_dtos = self._get_ride_request_dtos(ride_request_objs)
        ride_requests_dto = self._get_ride_requests_dto(
            ride_request_dtos, total_rides
        )
        return ride_requests_dto



    def get_ride_requests(
        self, user_id: int, offset: int, limit: int,
        sort_key: str, sort_value: str
    ) -> RideRequestsDto:

        limit = offset+limit
        filtered_ride_request_objs = RideRequest.objects.filter(
            user_id=user_id
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, offset, limit,
            filtered_ride_request_objs,
        )
        total_rides = len(ride_request_objs)
        ride_request_objs = ride_request_objs[offset:limit]
        ride_request_dtos = self._get_ride_request_dtos(ride_request_objs)
        ride_requests_dto = self._get_ride_requests_dto(
            ride_request_dtos, total_rides
        )
        return ride_requests_dto


    def _get_ride_requests_dto(
        self, ride_request_dtos: List[RideRequestDto],
        total_rides: int
    ) -> RideRequestsDto:

        ride_request_dtos = ride_request_dtos
        ride_requests_dto = RideRequestsDto(
            ride_dtos=ride_request_dtos,
            total_rides=total_rides
        )
        return ride_requests_dto



    def _get_ordered_ride_requests(
        self,
        sort_key: str, sort_value: str,
        offset: int, limit: int,
        filtered_ride_request_objs: List[RideRequest]
    ) -> List[RideRequest]:

        if sort_key == "ASC" or sort_key == "asc":
            ride_request_objs = \
                filtered_ride_request_objs.order_by(sort_key)
        else:
            ride_request_objs = \
                filtered_ride_request_objs.order_by("-"+sort_key)
        ride_request_objs = list(ride_request_objs)
        return ride_request_objs



    def _get_ride_request_dtos(
        self,
        ride_request_objs: RideRequest
    ) -> List[RideRequestDto]:

        ride_request_dtos = []
        for ride_request_obj in ride_request_objs:
            base_ride_request_dto = self._get_base_ride_request_dto(
                ride_request_obj
            )
            ride_request_dto = self._get_ride_request_dto(
                ride_request_obj, base_ride_request_dto
            )
            ride_request_dtos.append(ride_request_dto)
        return ride_request_dtos



    def _get_base_ride_request_dto(
        self,
        ride_request_obj: RideRequest
    ) -> BaseRideRequestDto:

        from_datetime_obj = ""
        to_datetime_obj = ""
        travel_datetime_obj = ""
        if ride_request_obj.flexible_timings:
            from_datetime_obj = ride_request_obj.flexible_from_date_time
            to_datetime_obj = ride_request_obj.flexible_to_date_time
        else:
            travel_datetime_obj = ride_request_obj.travel_date_time

        base_ride_request_dto = BaseRideRequestDto(
                ride_request_id=ride_request_obj.id,
                source=ride_request_obj.source,
                destination=ride_request_obj.destination,
                travel_date_time=travel_datetime_obj,
                flexible_timings=ride_request_obj.flexible_timings,
                flexible_from_date_time= from_datetime_obj,
                flexible_to_date_time=to_datetime_obj,
                seats=ride_request_obj.seats,
                laguage_quantity=ride_request_obj.laguage_quantity
            )
        return base_ride_request_dto



    def _get_ride_request_dto(
        self,
        ride_request_obj: RideRequest,
        base_ride_request_dto: BaseRideRequestDto
    ):
        accepted_person = ""
        accepted_person_phone_number = ""
        is_accepted_by = self._is_request_accepted(
                request_obj=ride_request_obj
        )
        if is_accepted_by:
            accepted_person = ride_request_obj.accepted_by.username
            accepted_person_phone_number = \
            ride_request_obj.accepted_by.phone_number

        ride_request_dto = RideRequestDto(
            ride_dto=base_ride_request_dto,
            accepted_person=accepted_person,
            accepted_person_phone_number=accepted_person_phone_number,
            status=""
        )
        return ride_request_dto



    def _is_request_accepted(
        self,
        request_obj: Union[RideRequest, AssetRequest]
    ) -> bool:
        accepted_by = request_obj.accepted_by
        if accepted_by:
            return True
        else:
            return False