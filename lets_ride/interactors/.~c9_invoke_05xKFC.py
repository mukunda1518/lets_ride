from datetime import datetime
from typing import List
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.constants.enums import Status
from lets_ride.dtos.dtos

class MyRideRequestsInteractor:

    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter
    
    def my_ride_requests_wrapper(
        self,
        user_id: int,
        filter_key: str,
        filter_value: str,
        sort_key: str,
        sort_value: str,
        offset: int,
        limit: int
    ):
        now_datetime_obj = datetime.now()
        is_filter_key = not filter_key
        is_sort_key = not filter_key
        if is_filter_key and is_sort_key:
            ride_request_dtos = self.storage.get_matching_ride_requests(
                user_id,offset,limit
            )
        elif is_filter_key:
            ride_request_dtos = self.storage.get_matching_ride_requests_by_appling_sort(
                user_id, sort_key, sort_value, offset, limit
            )
        else:
            if filter_key is "source":
                ride_request_dtos = self.storage.get_matching_ride_requests_by_appling_source_filter(
                    user_id,
                    filter_value
                )
            else: 
                ride_request_dtos = self.storage.get_matching_ride_requests_by_appling_destination_filter(
                    user_id,
                    filter_value
                )
        ride_dtos = ride_request_dtos.ride_dtos
        self._set_status_for_ride_requests(ride_dtos, now_datetime_obj)


    def _set_status_for_ride_requests(
        self,
        ride_dtos: List[RideRequestDto],
        now_datetime_obj: datetime
    ):
        for ride_dto in ride_dtos:
            ride_status = self._get_ride_request_status(
                ride_request_dto=ride_request_dto,
                now_datetime_obj=now_datetime_obj
            )
            ride_request_dto.status = ride_status