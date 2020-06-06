from unittest.mock import create_autospec
from lets_ride.interactors.storages.accept_ride_request_storage_interface \
    import AcceptRideRequestStorageInterface
from lets_ride.interactors.accept_ride_request_interactor \
    import AcceptRideRequestInteractor

def test_accept_ride_request_wrapper():
    # Arrange
    user_id = 1
    ride_request_id = 1
    ride_matching_id = 2
    storage = create_autospec(AcceptRideRequestStorageInterface)
    interactor = AcceptRideRequestInteractor(storage=storage)

    # Act
    interactor.accept_ride_request_wrapper(
        user_id=user_id,
        ride_request_id=ride_request_id,
        ride_matching_id=ride_matching_id
    )

    # Assert
    storage.update_ride_request_status.assert_called_once_with(
        user_id, ride_request_id, ride_matching_id
    )

