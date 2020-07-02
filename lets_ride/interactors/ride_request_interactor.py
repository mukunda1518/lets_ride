from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.utils.datetime_conversion \
    import convert_datetime_to_datetime_object
from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.interactors.mixins.datetime_validations \
    import DateTimeValidationMixin
from lets_ride.interactors.mixins.datetime_conversions \
    import DateTimeConversionsMixin
from lets_ride.exceptions.exceptions import InvalidDateTime, NegativeValue
from lets_ride.interactors.mixins.base_validations \
    import BaseValidationMixin




class RideRequestInteractor(
        DateTimeValidationMixin,
        DateTimeConversionsMixin,
        BaseValidationMixin

):

    def __init__(
        self, storage: StorageInterface,
    ):
        self.storage = storage


    def create_ride_request_wrapper(
        self, user_id: int, ride_request_dto: RideRequestDTO,
        presenter: PresenterInterface
    ):

        try:
            self.create_ride_request(user_id, ride_request_dto)
        except InvalidDateTime:
            presenter.raise_invalid_datetime_exception()
        except NegativeValue:
            presenter.raise_invalid_value_exception()


    def create_ride_request(
            self, user_id: int, ride_request_dto: RideRequestDTO
    ):

        self.is_negative_value(ride_request_dto.seats)
        self.is_negative_value(ride_request_dto.laguage_quantity)
        is_flexible_timings = ride_request_dto.flexible_timings
        flexible_from_date_time = ride_request_dto.flexible_from_date_time
        flexible_to_date_time = ride_request_dto.flexible_to_date_time
        travel_date_time = ride_request_dto.travel_date_time

        if is_flexible_timings:
            from_datetime_obj = self.convert_datetime_to_datetime_object(
                flexible_from_date_time
            )
            self.validate_datetime(from_datetime_obj)
            to_datetime_obj = self.convert_datetime_to_datetime_object(
                flexible_to_date_time
            )
            self.validate_datetime(to_datetime_obj)
            self.storage.create_ride_request_with_flexible_timings(
                user_id=user_id,
                source=ride_request_dto.source,
                destination=ride_request_dto.destination,
                flexible_timings=ride_request_dto.flexible_timings,
                flexible_travel_from_date_time=from_datetime_obj,
                flexible_travel_to_date_time=to_datetime_obj,
                seats=ride_request_dto.seats,
                laguage_quantity=ride_request_dto.laguage_quantity
            )

        else:
            datetime_obj = convert_datetime_to_datetime_object(
                travel_date_time
            )
            self.validate_datetime(datetime_obj)
            self.storage.create_ride_request(
                user_id=user_id,
                source=ride_request_dto.source,
                destination=ride_request_dto.destination,
                travel_date_time=datetime_obj,
                flexible_timings=ride_request_dto.flexible_timings,
                seats=ride_request_dto.seats,
                laguage_quantity=ride_request_dto.laguage_quantity
            )

