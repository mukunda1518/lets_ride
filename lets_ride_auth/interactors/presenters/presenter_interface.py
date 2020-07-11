from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from lets_ride_auth.dtos.dtos import UserDto
from lets_ride_auth.exceptions.exceptions import InvalidUserIds


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
    def raise_user_with_phone_number_already_exist(self):
        pass

    @abstractmethod
    def raise_username_already_exist(self):
        pass

    @abstractmethod
    def raise_invalid_user_ids_exception(self, err: InvalidUserIds):
        pass

