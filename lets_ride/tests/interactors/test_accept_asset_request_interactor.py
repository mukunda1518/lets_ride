from unittest.mock import create_autospec
from lets_ride.interactors.storages.accept_asset_request_storage_interface \
    import AcceptAssetRequestStorageInterface
from lets_ride.interactors.accept_asset_request_interactor \
    import AcceptAssetRequestInteractor

def test_accept_asset_request_wrapper_with_ride_matching():
    # Arrange
    user_id = 1
    asset_request_id = 1
    ride_matching_id = 2
    travel_matching_id = 0
    storage = create_autospec(AcceptAssetRequestStorageInterface)
    interactor = AcceptAssetRequestInteractor(storage=storage)

    # Act
    interactor.accept_asset_request_wrapper(
        user_id=user_id,
        asset_request_id=asset_request_id,
        ride_matching_id=ride_matching_id,
        travel_matching_id=travel_matching_id
    )

    # Assert
    storage.update_asset_request_status_with_ride_matching_deatails.assert_called_once_with(
        user_id, asset_request_id, ride_matching_id
    )


def test_accept_asset_request_wrapper_with_travel_info_matching():
    # Arrange
    user_id = 1
    asset_request_id = 1
    ride_matching_id = 0
    travel_matching_id = 2
    storage = create_autospec(AcceptAssetRequestStorageInterface)
    interactor = AcceptAssetRequestInteractor(storage=storage)

    # Act
    interactor.accept_asset_request_wrapper(
        user_id=user_id,
        asset_request_id=asset_request_id,
        ride_matching_id=ride_matching_id,
        travel_matching_id=travel_matching_id
    )

    # Assert
    storage.update_asset_request_status_with_travel_matching_deatails.assert_called_once_with(
        user_id, asset_request_id, travel_matching_id
    )

