from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from lets_ride.dtos.dtos import (
    UserDto,
    RideAssetMatchingDto,
    RideRequestsDto,
    AssetRequestsDto
)


class PresenterInterface(ABC):

    @abstractmethod
    def get_ride_requests_response(self, ride_requests_dto: RideRequestsDto):
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