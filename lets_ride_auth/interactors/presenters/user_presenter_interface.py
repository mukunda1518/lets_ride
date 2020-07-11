from abc import ABC
from ABC import abstractmethod

from common.dtos import UserAuthTokensDTO

from lets_ride_auth.interactors.storages.dtos import UserDTO


class SignUpPresenterInterface(ABC):

    @abstractmethod
    def raise_username_already_exist(self):
        pass


    @abstractmethod
    def raise_user_with_phone_number_already_exist(self):
        pass


    @abstractmethod
    def get_sign_up_response(self, user_auth_token_dto: UserAuthTokensDTO):
        pass


class LoginPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_phone_number(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def get_login_response(self, token_dto: UserAuthTokensDTO):
        pass


class UserPofilePresenterInterface(ABC):

    @abstractmethod
    def user_profile_response(self, user_dto: UserDTO):
        pass
