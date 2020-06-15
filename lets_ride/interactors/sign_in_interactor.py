from lets_ride.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride.exceptions.exceptions \
    import InvalidPhoneNumber, InvalidPassword


class SignInInteractor:

    def __init__(
        self,
        storage: UserStorageInterface,
        oauth_storage = OAuth2SQLStorage
    ):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def login_wrapper(
        self,
        phone_number: str,
        password: str,
        presenter: PresenterInterface
    ):
        try:
            token_dto = self.login(
                phone_number=phone_number, password=password
            )
        except InvalidPhoneNumber:
            presenter.raise_invalid_phone_number()
        except InvalidPassword:
            presenter.raise_invalid_password()

        response = presenter.get_login_response(
            token_dto=token_dto
        )
        return response

    def login(self, phone_number: str, password: str):
        self.storage.validate_phone_number(phone_number=phone_number)
        self.storage.validate_password(
            phone_number=phone_number, password=password
        )
        user_id = self.storage.login(
            phone_number=phone_number, password=password
        )
        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )
        token_dto = service.create_user_auth_tokens(
            user_id=user_id
        )
        return token_dto
