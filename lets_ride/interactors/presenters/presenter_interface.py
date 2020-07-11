from abc import ABC
from abc import abstractmethod

from typing import List

from django.http import response

from common.dtos import UserAuthTokensDTO
from lets_ride.dtos.dtos import (
    UserDto,
    RideAssetMatchingDto,
    RideRequestsDto,
    AssetRequestsDto
)
from lets_ride.interactors.storages.dtos import TotalRideRequestsDTO


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


class CreateRideRequestPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_datetime_exception(self):
        pass

    @abstractmethod
    def raise_invalid_value_exception(self):
        pass



class GetRideRequestsPresenterInterface(ABC):

    @abstractmethod
    def get_ride_requests_response(
            self, total_ride_requests_dto: TotalRideRequestsDTO
    ) -> response.HttpResponse:
        pass

