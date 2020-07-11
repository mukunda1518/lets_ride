from datetime import datetime

from lets_ride.interactors.presenters.presenter_interface \
    import CreateRideRequestPresenterInterface
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface

from lets_ride.interactors.dtos.dtos import CreateRideRequestDTO
from lets_ride.interactors.storages.dtos import RideRequestDTO

from lets_ride.interactors.mixins.datetime_validations \
    import DateTimeValidationMixin
from lets_ride.interactors.mixins.datetime_conversions \
    import DateTimeConversionsMixin
from lets_ride.interactors.mixins.base_validations \
    import BaseValidationMixin

from lets_ride.exceptions.exceptions import InvalidDateTime, NegativeValue




class CreateRideRequestInteractor(
        DateTimeValidationMixin,
        DateTimeConversionsMixin,
        BaseValidationMixin
):

    def __init__(
        self, storage: StorageInterface,
    ):
        self.storage = storage


    def create_ride_request_wrapper(
        self, user_id: int, ride_request_dto: CreateRideRequestDTO,
        presenter: CreateRideRequestPresenterInterface
    ):

        try:
            self.create_ride_request(user_id, ride_request_dto)
        except InvalidDateTime:
            presenter.raise_invalid_datetime_exception()
        except NegativeValue:
            presenter.raise_invalid_value_exception()


    def create_ride_request(
            self, user_id: int, ride_request_dto: CreateRideRequestDTO
    ):

        self.is_negative_value(ride_request_dto.seats)
        self.is_negative_value(ride_request_dto.laguage_quantity)
        is_flexible_timings = ride_request_dto.flexible_timings

        if is_flexible_timings:
            self._create_ride_request_with_flexible_timings(
                user_id, ride_request_dto
            )

        else:
            self._create_ride_request_with_out_flexible_timings(
                user_id, ride_request_dto
            )



    def _create_ride_request_with_out_flexible_timings(
        self, user_id: int, ride_request_dto: CreateRideRequestDTO
    ):
        travel_date_time = ride_request_dto.travel_date_time
        datetime_obj = self.convert_datetime_to_datetime_object(
            travel_date_time
        )
        self.validate_datetime(datetime_obj)

        create_ride_request_dto = self._get_create_ride_request_dto_without_flexible_timings(
            user_id, ride_request_dto, datetime_obj
        )
        self.storage.create_ride_request(
            user_id, create_ride_request_dto
        )



    def _get_create_ride_request_dto_without_flexible_timings(
        self,
        user_id: int,
        ride_request_dto: CreateRideRequestDTO,
        travel_date_time: datetime
    ):
        create_ride_request_dto = RideRequestDTO(
            source=ride_request_dto.source,
            destination=ride_request_dto.destination,
            travel_date_time= travel_date_time,
            flexible_timings=False,
            flexible_from_date_time="",
            flexible_to_date_time="",
            seats=ride_request_dto.seats,
            laguage_quantity=ride_request_dto.laguage_quantity
        )
        return create_ride_request_dto



    def _create_ride_request_with_flexible_timings(
        self, user_id: int, ride_request_dto: CreateRideRequestDTO
    ):
        flexible_from_date_time = ride_request_dto.flexible_from_date_time
        flexible_to_date_time = ride_request_dto.flexible_to_date_time
        from_datetime_obj = self.convert_datetime_to_datetime_object(
            flexible_from_date_time
        )
        self.validate_datetime(from_datetime_obj)
        to_datetime_obj = self.convert_datetime_to_datetime_object(
            flexible_to_date_time
        )
        self.validate_datetime(to_datetime_obj)
        create_ride_request_dto = self._get_create_ride_request_dto_with_flexible_timings(
            ride_request_dto, from_datetime_obj, to_datetime_obj
        )
        self.storage.create_ride_request_with_flexible_timings(
            user_id, create_ride_request_dto
        )



    def _get_create_ride_request_dto_with_flexible_timings(
        self,
        ride_request_dto: RideRequestDTO,
        from_datetime_obj: datetime,
        to_datetime_obj: datetime
    ):
        create_ride_request_dto = RideRequestDTO(
            source=ride_request_dto.source,
            destination=ride_request_dto.destination,
            travel_date_time= "",
            flexible_timings=True,
            flexible_from_date_time=from_datetime_obj,
            flexible_to_date_time=to_datetime_obj,
            seats=ride_request_dto.seats,
            laguage_quantity=ride_request_dto.laguage_quantity
        )
        return create_ride_request_dto





