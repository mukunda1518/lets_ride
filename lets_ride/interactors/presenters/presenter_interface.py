from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from lets_ride.dtos.dtos import (
    UserDto,
    RideAssetMatchingDto,
    RideRequestsDto,
    AssetRequestsDto
)


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_datetime_exception(self):
        pass

    @abstractmethod
    def raise_invalid_value_exception(self):
        pass

    @abstractmethod
    def get_ride_requests_response(
        self, ride_requests_dto: RideRequestsDto,
        user_dtos: List[UserDto]
    ):
        pass

    @abstractmethod
    def get_asset_requests_response(
        self, asset_requests_dto: AssetRequestsDto
    ):
        pass

    @abstractmethod
    def get_ride_asset_matching_response(
        self,
        ride_asset_matching_dto: RideAssetMatchingDto
    ):
        pass
