from datetime import datetime

from lets_ride_v2.interactors.storages.storage_interface \
    import StorageInterface

from lets_ride_v2.interactors.presenters.create_ride_request_presenter_interface \
    import CreateRideRequestPrenterInterface

from lets_ride_v2.exceptions.exceptions import (
    InvalidFromPlaceException,
    InvalidToPlaceException,
    InvalidTravelDateTimeException,
    InvalidNumberOfSeatsException
)

from lets_ride_v2.interactors.dtos import RideRequestDTO

class CreateRideRequestInteractor:


    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def create_ride_request_wrapper(
        self, user_id: int, ride_request_dto: RideRequestDTO,
        presenter: CreateRideRequestPrenterInterface
    ):

        try:
            self.create_ride_request_response(
                user_id, ride_request_dto
            )
        except InvalidFromPlaceException:
            return presenter.raise_invalid_from_place_exception()
        except InvalidToPlaceException:
            return presenter.raise_invalid_to_place_exception()
        except InvalidTravelDateTimeException:
            return presenter.raise_invalid_travel_datetime_exception()
        except InvalidNumberOfSeatsException:
            return presenter.raise_invalid_no_of_seats_exception()


    def create_ride_request_response(
            self, user_id: int, ride_request_dto: RideRequestDTO
    ):

        self.create_ride_request(user_id, ride_request_dto)



    def create_ride_request(
            self, user_id: int, ride_request_dto: RideRequestDTO
    ):

        is_from_place_empty = not ride_request_dto.from_place
        if is_from_place_empty:
            raise InvalidFromPlaceException

        is_to_place_empty = not ride_request_dto.to_place
        if is_to_place_empty:
            raise InvalidToPlaceException

        current_datetime = datetime.now()
        travel_datetime = ride_request_dto.travel_datetime
        if travel_datetime <= current_datetime:
            raise InvalidTravelDateTimeException

        if ride_request_dto.no_of_seats <=0:
            raise InvalidNumberOfSeatsException

        self.storage.create_ride_request(user_id, ride_request_dto)


