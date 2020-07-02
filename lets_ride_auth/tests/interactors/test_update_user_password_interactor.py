from unittest.mock import create_autospec
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.update_user_password_interactor \
    import UpdateUserPasswordInteractor

def test_update_user_password():
    # Arrange
    user_id = 1
    new_password = "user2"
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(UserStorageInterface)
    interactor = UpdateUserPasswordInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    interactor.update_user_password_wrapper(
        user_id=user_id,
        new_password=new_password
    )

    # Assert
    storage.update_user_password(user_id=user_id, password=new_password)
