from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage


class SignUpInteractor:

    def __init__(
        self,
        storage: UserStorageInterface,
        presenter: PresenterInterface,
        oauth_storage: OAuth2SQLStorage
    ):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def sign_up_wrapper(
        self,
        username: str,
        phone_number: str,
        password: str
    ):
        is_user_exist = self.storage.check_username_exists(username)
        if is_user_exist:
            self.presenter.raise_username_already_exist()

        is_user_with_phone_number_exist = \
            self.storage.check_phone_number_exists(phone_number)
        if is_user_with_phone_number_exist:
            self.presenter.raise_user_with_phone_number_already_exist()

        user_id = self.storage.sign_up(
            username=username,
            phone_number=phone_number,
            password=password
        )
        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )
        token_dto= service.create_user_auth_tokens(user_id=user_id)
        response = self.presenter.get_sign_up_response(
            token_dto=token_dto
        )
        return response
