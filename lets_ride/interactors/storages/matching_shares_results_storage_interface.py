import datetime
from abc import abstractmethod
from abc import ABC
from typing import List
from lets_ride.dtos.dtos import (
    BaseRideShareDto,
    BaseTravelInfoDto,
    RideMatchingDto,
    AssetMatchingDto
)


class MatchingSharesStorageInterface(ABC):

    @abstractmethod
    def get_ride_shares(self, user_id: int) -> List[BaseRideShareDto]:
        pass

    @abstractmethod
    def get_travel_shares(self, user_id: int) -> List[BaseTravelInfoDto]:
        pass

    @abstractmethod
    def get_ride_matching_requests(
        self, source: str, destination: str, seats: int, asset_quantity: int,
        from_datetime: datetime.datetime, to_datetime: datetime.datetime
    ) -> List[RideMatchingDto]:
        pass

    @abstractmethod
    def get_travel_matching_requests(
        self, source: str, destination: str, asset_quantity: int,
        from_datetime: datetime.datetime, to_datetime: datetime.datetime
    ) -> List[AssetMatchingDto]:
        pass
