import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import BadRequest
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from lets_ride.interactors.sign_up_interactor import SignUpInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.user_storage_interface \
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
def test_sign_up(create_user_auth_tokens):
    # Arrange
    user_id = 1
    username = "user1"
    password = "user1"
    phone_number = "1234354657689"

    mock_presenter_response = {
        "user_id": user_id,
        "access_token": "JBSJBNKJ",
        "refresh_token": "DKBKVJBKJV",
        "expires_in": 3436564574
    }
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    oauth_storage =OAuth2SQLStorage()
    interactor = SignUpInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    storage.sign_up.return_value = user_id
    presenter.get_sign_up_response.return_value = mock_presenter_response

    # Act
    response = interactor.sign_up_wrapper(
        username=username,
        phone_number=phone_number,
        password=password
        )

    # Assert
    storage.sign_up.assert_called_once_with(
        username=username,
        phone_number=phone_number,
        password=password
    )
    presenter.get_sign_up_response.assert_called_once_with(
        token_dto=token_dto
    )
    assert response == mock_presenter_response

# @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=token_dto)
# def test_sign_up_with_username_already_exist(create_user_auth_tokens):
#     # Arrange
#     username = "user1"
#     password = "user1"
#     phone_number = "1234567891"
#     presenter = create_autospec(PresenterInterface)
#     storage = create_autospec(UserStorageInterface)
#     oauth_storage =OAuth2SQLStorage()
#     interactor = SignUpInteractor(
#         storage=storage,
#         presenter=presenter,
#         oauth_storage=oauth_storage
#     )
#     storage.check_username_exists.return_value = True
#     presenter.raise_username_already_exist.side_effect = BadRequest

#     # Act
#     interactor.sign_up_wrapper(
#         username=username,
#         phone_number=phone_number,
#         password=password
#     )

#     # Assert

#     storage.check_username_exists.assert_called_once_with(username=username)
#     presenter.raise_username_already_exist.assert_called()

# @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=token_dto)
# def test_sign_up_with_user_with_phone_number_already_exist(create_user_auth_tokens):
#     # Arrange
#     username = "user1"
#     password = "user1"
#     phone_number = "1234567891"
#     presenter = create_autospec(PresenterInterface)
#     storage = create_autospec(UserStorageInterface)
#     oauth_storage =OAuth2SQLStorage()
#     interactor = SignUpInteractor(
#         storage=storage,
#         presenter=presenter,
#         oauth_storage=oauth_storage
#     )
#     storage.check_username_exists.return_value = False
#     storage.check_phone_number_exists.return_value = True
#     presenter.raise_username_already_exist.side_effect = BadRequest

#     # Act
#     interactor.sign_up_wrapper(
#         username=username,
#         phone_number=phone_number,
#         password=password
#     )

#     # Assert

#     storage.check_phone_number_exists.assert_called_once_with(
#         phone_number=phone_number
#     )
#     presenter.raise_user_with_phone_number_already_exist.assert_called()

