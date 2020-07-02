import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.get_user_details_interactor \
    import GetUserDetailsInteractor
from lets_ride_auth.dtos.dtos import UserDto
from lets_ride_auth.exceptions.exceptions import InvalidUserIds


def test_get_user_details_with_invalid_user_ids_raise_exception():
    # Arrange
    user_ids = [1, 2, 3, 4, 100, 200]
    invalid_user_ids = [100,200]
    storage =  create_autospec(UserStorageInterface)
    presenter =  create_autospec(PresenterInterface)
    storage.get_user_ids.return_value = [1, 2, 3, 4, 5]
    presenter.raise_invalid_user_ids_exception.side_effect = NotFound
    interactor = GetUserDetailsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_user_details_wrapper(
            user_ids=user_ids, presenter=presenter
        )

    # Assert
    storage.get_user_ids.assert_called_once()
    call_tuple = presenter.raise_invalid_user_ids_exception.call_args
    exception_obj = call_tuple.args[0]
    print("ids = ",exception_obj.user_ids)
    assert exception_obj.user_ids == invalid_user_ids


def test_get_user_details_with_valid_user_id_returns_user_dtos():
    # Arrange
    user_ids = [1, 2, 3, 4]
    storage =  create_autospec(UserStorageInterface)
    presenter =  create_autospec(PresenterInterface)
    storage.get_user_ids.return_value = [1, 2, 3, 4, 5]

    user_dtos = [
        UserDto(
            user_id=1,
            username="user1",
            phone_number="1234567890",
            profile_pic=""
        ),
        UserDto(
            user_id=2,
            username="user2",
            phone_number="1234567891",
            profile_pic=""
        )
    ]

    storage.get_user_details_dtos.return_value = user_dtos

    interactor = GetUserDetailsInteractor(storage=storage)

    # Act
    response = interactor.get_user_details_wrapper(
                user_ids=user_ids, presenter=presenter
            )

    # Assert
    storage.get_user_ids.assert_called_once()
    storage.get_user_details_dtos.assert_called_once_with(user_ids)

    assert response == user_dtos





