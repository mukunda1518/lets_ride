from datetime import datetime
from typing import List
from lets_ride.interactors.storages.ride_requests_storage_interface \
    import RideRequestsStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.constants.enums import Status
from lets_ride.dtos.dtos import (
    RideRequestDto
)
from lets_ride.adapters.services import get_service


class MyRideRequestsInteractor:

    def __init__(
        self,
        storage: RideRequestsStorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter

    def my_ride_requests_wrapper(
        self,
        user_id: int,
        status: str,
        sort_key: str,
        sort_value: str,
        offset: int,
        limit: int
    ):
        if limit < 0 or offset < 0:
            self.presenter.raise_invalid_for_limit_and_offset()
            return
        current_datetime_obj = datetime.now()
        if status == Status.ACCEPTED.value:
            ride_requests_dto = self.storage.get_ride_request_with_status_accepted(
                user_id, offset, limit, sort_key, sort_value
            )
        elif status == Status.EXPIRED.value:
            ride_requests_dto = self.storage.get_ride_request_with_status_expired(
                user_id, offset, limit, sort_key,
                sort_value, current_datetime_obj
            )
        elif status == Status.PENDING.value:
            ride_requests_dto = self.storage.get_ride_request_with_status_pending(
                user_id, offset, limit, sort_key,
                sort_value, current_datetime_obj
            )
        else:
            ride_requests_dto = self.storage.get_ride_requests(
                user_id, offset, limit, sort_key, sort_value
            )
        ride_dtos = ride_requests_dto.ride_dtos
        self._set_status_for_ride_requests(ride_dtos)
        user_ids = self._get_user_ids(ride_dtos)
        service = get_service()
        user_dtos = service.auth_service.get_user_dtos(user_ids=user_ids)

        response = self.presenter.get_ride_requests_response(
            ride_requests_dto=ride_requests_dto,
            user_dtos=user_dtos
        )
        return response


    @staticmethod
    def _get_user_ids(ride_dtos: List[RideRequestDto]) -> List[int]:
        user_ids = []
        for ride_dto in ride_dtos:
            if ride_dto.accepted_person_id:
                user_ids.append(ride_dto.accepted_person_id)
        return user_ids


    def _set_status_for_ride_requests(
        self,
        ride_dtos: List[RideRequestDto],
    ):
        for ride_dto in ride_dtos:
            ride_status = self._get_ride_request_status(ride_dto)
            ride_dto.status = ride_status


    def _get_ride_request_status(
        self,
        ride_dto: RideRequestDto
    ) -> str:

        current_datetime_obj = datetime.now()
        flexible_timings = ride_dto.ride_dto.flexible_timings
        is_accepted = ride_dto.accepted_person_id

        if flexible_timings:
            request_datetime_obj = \
                ride_dto.ride_dto.flexible_to_date_time
        else:
            request_datetime_obj = \
                ride_dto.ride_dto.travel_date_time

        if request_datetime_obj < current_datetime_obj:
            status = Status.EXPIRED.value
        elif is_accepted:
            status = Status.ACCEPTED.value
        else:
            status = Status.PENDING.value
        return status

