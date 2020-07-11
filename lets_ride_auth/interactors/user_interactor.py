from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.presenters.user_presenter_interface \
    import SignUpPresenterInterface
from lets_ride_auth.interactors.presenters.user_presenter_interface \
    import LoginPresenterInterface
from lets_ride_auth.interactors.presenters.user_presenter_interface \
    import UserPofilePresenterInterface

from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage

from lets_ride_auth.exceptions.exceptions import (
    UserNameAlreadyExist,PhoneNumberAlreadyExist,
    InvalidPhoneNumber, InvalidPassword
)


class UserInteractor:

    def __init__(self, storage: UserStorageInterface):
        self.storage = storage


    def sign_up_wrapper(
            self, username: str, phone_number: str, password: str,
            presenter: SignUpPresenterInterface,
            oauth_storage: OAuth2SQLStorage
    ):
        try:
            self.sign_up_response(
                username, phone_number, password, presenter, oauth_storage
            )
        except UserNameAlreadyExist:
            presenter.raise_username_already_exist()
        except PhoneNumberAlreadyExist:
            presenter.raise_user_with_phone_number_already_exist()


    def sign_up_response(
            self, username: str, phone_number: str,password: str,
            presenter: SignUpPresenterInterface,
            oauth_storage: OAuth2SQLStorage
    ):
        user_auth_token_dto = self.sign_up(
            username, phone_number, password, oauth_storage
        )
        presenter.get_sign_up_response(user_auth_token_dto)


    def sign_up(
            self, username: str, phone_number: str,
            password: str, oauth_storage: OAuth2SQLStorage
    ) -> UserAuthTokensDTO:

        is_user_exist = self.storage.check_username_exists(username)
        if is_user_exist:
            raise UserNameAlreadyExist

        is_user_with_phone_number_exist = \
            self.storage.check_phone_number_exists(phone_number)
        if is_user_with_phone_number_exist:
            raise PhoneNumberAlreadyExist

        user_id = self.storage.sign_up(
            username=username, phone_number=phone_number, password=password
        )
        service = OAuthUserAuthTokensService(oauth2_storage=oauth_storage)
        user_auth_token_dto= service.create_user_auth_tokens(user_id=user_id)
        return user_auth_token_dto


    def login_in_wrapper(
            self, phone_number: str, password: str,
            presenter: LoginPresenterInterface,
            oauth_storage: OAuth2SQLStorage
    ):
        try:
            self.login_response(
                phone_number, password, presenter, oauth_storage
            )
        except InvalidPhoneNumber:
            presenter.presenter.raise_invalid_phone_number()
        except InvalidPassword:
            presenter.raise_invalid_password()


    def login_response(
            self, phone_number: str, password: str,
            presenter: LoginPresenterInterface,
            oauth_storage: OAuth2SQLStorage,
    ):
        user_auth_token_dto = self.login(
            phone_number, password, presenter, oauth_storage
        )
        presenter.get_login_response(user_auth_token_dto)


    def login(
            self, phone_number: str, password: str,
            presenter: LoginPresenterInterface,
            oauth_storage: OAuth2SQLStorage,
    ) -> UserAuthTokensDTO:

        self.storage.validate_phone_number(phone_number)
        self.storage.validate_password(phone_number, password)

        user_id = self.storage.login(
            phone_number=phone_number, password=password
        )
        service = OAuthUserAuthTokensService(oauth2_storage=oauth_storage)
        user_auth_token_dto = service.create_user_auth_tokens(user_id=user_id)
        return user_auth_token_dto


    def user_profile_wrapper(
            self, user_id: int, presenter: UserPofilePresenterInterface
    ):
      self.user_profile_response(user_id, presenter)


    def user_profile_response(
            self, user_id: int, presenter: UserPofilePresenterInterface
    ):
        user_dto = self.user_profile(user_id)
        presenter.user_profile_response(user_dto)


    def user_profile(self, user_id: int):
        user_dto = self.storage.user_profile(user_id)
        return user_dto


    def update_user_password_wrapper(self, user_id: int, new_password: str):
        self.update_user_password(user_id, new_password)


    def update_user_password(self, user_id: int, new_password: str):
         self.storage.update_user_password(user_id, new_password)
