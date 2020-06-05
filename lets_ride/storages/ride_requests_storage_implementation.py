from typing import List
from datetime import datetime
from django.db.models import Case, Value, When, Q, CharField, F
from lets_ride.dtos.dtos import(
    RideRequestsDto,
    RideRequestDto,
    BaseRideRequestDto
)
from lets_ride.models.ride_request import RideRequest
from lets_ride.interactors.storages.ride_requests_storage_interface \
    import RideRequestsStorageInterface

class RideRequestsStorageImplementation(RideRequestsStorageInterface):

    def get_ride_request_with_status_accepted(
        self, user_id: int, offset: int,
        limit: int, sort_key: str, sort_value: str
    ) -> RideRequestsDto:

        limit = offset+limit
        filtered_ride_request_objs =  RideRequest.objects.filter(
            user_id=user_id, accepted_by_id__isnull=False
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, filtered_ride_request_objs
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
            Q(
                flexible_timings=False,
                travel_date_time__lte=current_datetime_obj
            ) |
            Q(
                flexible_timings=True,
                flexible_to_date_time__lte=current_datetime_obj
            ),
            user_id=user_id
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, filtered_ride_request_objs,
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
            Q(
                flexible_timings=False,
                travel_date_time__gt=current_datetime_obj
            ) |
            Q(
                flexible_timings=True,
                flexible_to_date_time__gt=current_datetime_obj
            ),
            user_id=user_id, accepted_by_id__isnull=True
        )
        ride_request_objs = self._get_ordered_ride_requests(
            sort_key, sort_value, filtered_ride_request_objs,
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
            sort_key, sort_value, filtered_ride_request_objs,
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

        ride_requests_dto = RideRequestsDto(
            ride_dtos=ride_request_dtos,
            total_rides=total_rides
        )
        return ride_requests_dto


    def _get_ordered_ride_requests(
        self,
        sort_key: str, sort_value: str,
        filtered_ride_request_objs: List[RideRequest]
    ) -> List[RideRequest]:

        if sort_key == "seats":
            ride_request_objs = filtered_ride_request_objs\
                .order_by(("-" if sort_value=="DESC" else "")+sort_key)
        else:
            ride_request_objs = filtered_ride_request_objs.annotate(
                date_time = Case(
                    When(
                        flexible_timings=True,
                        then=F("flexible_from_date_time")
                    ),
                    When(
                        flexible_timings=False,
                        then=F("travel_date_time")
                    ),
                    output_field=CharField()
                )
                ).order_by(("-" if sort_value=="DESC" else "")+"date_time")

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
        request_obj: RideRequest
    ) -> bool:
        accepted_by = request_obj.accepted_by
        if accepted_by:
            return True
        else:
            return False
