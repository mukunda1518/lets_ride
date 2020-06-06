from datetime import datetime
from typing import List
from abc import abstractmethod
from abc import ABC
from lets_ride.dtos.dtos import RideRequestsDto


class RideRequestsStorageInterface(ABC):

    @abstractmethod
    def get_ride_request_with_status_accepted(
        self, user_id: int, offset: int,
        limit: int, sort_key: str, sort_value: str
    ) -> RideRequestsDto:
        pass

    @abstractmethod
    def get_ride_request_with_status_expired(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> RideRequestsDto:
        pass

    @abstractmethod
    def get_ride_request_with_status_pending(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> RideRequestsDto:
        pass

    @abstractmethod
    def get_ride_requests(
        self, user_id: int, offset: int, limit: int,
        sort_key: str, sort_value: str
    ) -> RideRequestsDto:
        pass
