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
        presenter: PresenterInterface,
        oauth_storage = OAuth2SQLStorage
    ):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def login_wrapper(
        self,
        phone_number: str,
        password: str
    ):
        try:
            self.storage.validate_phone_number(phone_number=phone_number)
        except InvalidPhoneNumber:
            self.presenter.raise_invalid_phone_number()
        try:
            self.storage.validate_password(
                phone_number=phone_number, password=password
            )
        except InvalidPassword:
            self.presenter.raise_invalid_password()

        user_id = self.storage.login(
            phone_number=phone_number, password=password
        )

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )
        token_dto = service.create_user_auth_tokens(
            user_id=user_id
        )
        response = self.presenter.get_login_response(
            token_dto=token_dto
        )
        return response
