import abc
from abc import ABC, abstractmethod

from lets_ride_v2.interactors.dtos import RideRequestDTO

class StorageInterface(ABC):

    @abstractmethod
    def create_ride_request(
        self, user_id: int, ride_request_dto: RideRequestDTO
    ):
        pass