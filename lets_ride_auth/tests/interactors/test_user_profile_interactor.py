from unittest.mock import create_autospec
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.user_profile_interactor \
    import UserProfileInteractor
from lets_ride_auth.dtos.dtos import UserDto

def test_user_profile():

    # Arrange
    user_id = 1
    user_dto = UserDto(
        username="user1",
        phone_number="1234567890",
        profile_pic=""
    )
    mock_presenter_response = {
        "username": "user1",
        "phone_number": "1234567890",
        "profile_url_pic": ""
    }
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.user_profile.return_value = user_dto
    presenter.user_profile_response.return_value = mock_presenter_response

    # Act
    response = interactor.user_profile_wrapper(user_id=user_id)

    # Assert
    storage.user_profile.assert_called_once_with(user_id=user_id)
    presenter.user_profile_response.assert_called_once_with(user_dto=user_dto)
    assert response == mock_presenter_response
