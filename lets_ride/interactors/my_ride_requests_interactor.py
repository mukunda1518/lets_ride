from datetime import datetime

from typing import List

from django.http import response

from lets_ride.interactors.storages.ride_requests_storage_interface \
    import RideRequestsStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import GetRideRequestsPresenterInterface

from lets_ride.constants.enums import Status

from lets_ride.adapters.services import get_service

from lets_ride.interactors.dtos.dtos import RideRequestMetricsDTO
from lets_ride.interactors.storages.dtos \
    import TotalRideRequestsDTO, MyRideRequestDTO




class GetRideRequestsInteractor:


    def __init__(
            self,
            storage: RideRequestsStorageInterface,
    ):
        self.storage = storage


    def get_ride_requests_wrapper(
            self, ride_request_metrics_dto: RideRequestMetricsDTO,
            presenter: GetRideRequestsPresenterInterface
    ) -> response.HttpResponse:

       self.get_ride_requests_response(ride_request_metrics_dto, presenter)


    def get_ride_requests_response(
            self, ride_request_metrics_dto: RideRequestMetricsDTO,
            presenter: GetRideRequestsPresenterInterface
    ) -> response.HttpResponse:

        total_ride_requests_dto, user_dtos = \
            self.get_ride_requests(ride_request_metrics_dto)

        response_object = presenter.get_ride_requests_response(
            total_ride_requests_dto=total_ride_requests_dto,
            user_dtos=user_dtos
        )

        return response_object


    def get_ride_requests(
            self, ride_request_metrics_dto: RideRequestMetricsDTO
    ) -> TotalRideRequestsDTO:

        total_ride_requests_dto = \
            self.storage.get_ride_requests(ride_request_metrics_dto)

        ride_request_dtos = total_ride_requests_dto.ride_request_dtos
        self._set_status_for_ride_requests(ride_request_dtos)

        user_ids = self._get_user_ids(ride_request_dtos)
        service = get_service()
        user_dtos = service.auth_service.get_user_dtos(user_ids=user_ids)

        return total_ride_requests_dto, user_dtos



    @staticmethod
    def _get_user_ids(ride_request_dtos: List[MyRideRequestDTO]) -> List[int]:
        user_ids = []
        for ride_request_dto in ride_request_dtos:
            if ride_request_dto.accepted_person_id:
                user_ids.append(ride_request_dto.accepted_person_id)
        return user_ids



    def _set_status_for_ride_requests(
        self,
        ride_request_dtos: List[MyRideRequestDTO],
    ):
        for ride_request_dto in ride_request_dtos:
            ride_request_status = self._get_ride_request_status(ride_request_dto)
            ride_request_dto.status = ride_request_status


    def _get_ride_request_status(
        self,
        ride_request_dto: MyRideRequestDTO
    ) -> str:

        current_datetime_obj = datetime.now()
        flexible_timings = ride_request_dto.flexible_timings
        is_accepted = ride_request_dto.accepted_person_id

        if flexible_timings:
            requested_datetime_obj = \
                ride_request_dto.flexible_to_date_time
        else:
            requested_datetime_obj = \
                ride_request_dto.travel_date_time

        if requested_datetime_obj < current_datetime_obj:
            status = Status.EXPIRED.value
        elif is_accepted:
            status = Status.ACCEPTED.value
        else:
            status = Status.PENDING.value
        return status
