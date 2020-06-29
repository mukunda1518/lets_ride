import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from lets_ride_auth.interactors.sign_in_interactor import SignInInteractor
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage

token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="JBSJBNKJ",
        refresh_token="DKBKVJBKJV",
        expires_in=3436564574
    )

@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=token_dto)
def test_login(create_user_auth_tokens):
    # Arrange
    user_id = 1
    password = "user1"
    phone_number = "1234354657689"

    mock_presenter_response = {
        "user_id": 1,
        "access_token": "JBSJBNKJ",
        "refresh_token": "DKBKVJBKJV",
        "expires_in": 3436564574
    }
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    oauth_storage =OAuth2SQLStorage()
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    storage.login.return_value = user_id
    presenter.get_login_response.return_value = mock_presenter_response

    # Act
    response = interactor.login_wrapper(
        phone_number=phone_number,
        password=password
        )

    # Assert
    storage.login.assert_called_once_with(
        phone_number=phone_number,
        password=password
    )
    presenter.get_login_response.assert_called_once_with(
        token_dto=token_dto
    )
    storage.validate_phone_number.assert_called_once_with(
        phone_number=phone_number
    )
    storage.validate_password.assert_called_once_with(
        phone_number=phone_number,
        password=password
    )
    assert response == mock_presenter_response

@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=token_dto)
def test_login_with_invalid_phone_number_raise_exception(create_user_auth_tokens):
    # Arrange
    password = "user1"
    phone_number = "1234354657689"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    oauth_storage =OAuth2SQLStorage()
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    presenter.raise_invalid_phone_number.side_effect = NotFound
    # Act
    interactor.login_wrapper(phone_number=phone_number, password=password)

    # Assert
    storage.validate_phone_number.assert_called_once_with(
        phone_number=phone_number
    )

@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=token_dto)
def test_login_with_invalid_password_raise_exception(create_user_auth_tokens):
    # Arrange
    password = "user1"
    phone_number = "1234354657689"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    oauth_storage =OAuth2SQLStorage()
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    presenter.raise_invalid_password.side_effect = NotFound
    # Act
    interactor.login_wrapper(phone_number=phone_number, password=password)

    # Assert
    storage.validate_password.assert_called_once_with(
        phone_number=phone_number,
        password=password
    )
