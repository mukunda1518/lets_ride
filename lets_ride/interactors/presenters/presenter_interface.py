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
    def get_sign_up_response(self, token_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def get_login_response(self, token_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def user_profile_response(self, user_dto: UserDto):
        pass

    @abstractmethod
    def raise_invalid_phone_number(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

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

    @abstractmethod
    def raise_username_already_exist(self):
        pass

    @abstractmethod
    def raise_user_with_phone_number_already_exist(self):
        pass
