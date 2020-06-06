from abc import abstractmethod
from abc import ABC

class AcceptRideRequestStorageInterface(ABC):

    @abstractmethod
    def update_ride_request_status(
        self, user_id: int, ride_request_id: int, ride_matching_id: int
    ):
        pass
