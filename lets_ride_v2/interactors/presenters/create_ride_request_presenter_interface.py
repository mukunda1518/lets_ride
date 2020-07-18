import abc
from abc import ABC, abstractmethod

class CreateRideRequestPrenterInterface(ABC):

    @abstractmethod
    def raise_invalid_from_place_exception(self):
        pass

    @abstractmethod
    def raise_invalid_to_place_exception(self):
        pass

    @abstractmethod
    def raise_invalid_travel_datetime_exception(self):
        pass

    @abstractmethod
    def raise_invalid_no_of_seats_exception(self):
        pass