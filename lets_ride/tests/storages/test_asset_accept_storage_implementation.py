import pytest
from lets_ride.models.asset_request import AssetRequest
from lets_ride.models.travel_info import TravelInfo
from lets_ride.models.share_ride import ShareRide
from lets_ride.storages.accept_asset_request_storage_implementation \
    import AcceptAssetRequestStorageImplementation

@pytest.mark.django_db
def test_update_asset_request_status_with_ride_matching_deatails(
    populate_asset_matching_requests, populate_ride_shares
):
    # Arrange
    user_id = 1
    asset_request_id = 1
    ride_matching_id = 1
    seats = 3
    asset_quantity = 0
    storage = AcceptAssetRequestStorageImplementation()

    # Act
    storage.update_asset_request_status_with_ride_matching_deatails(
        user_id=user_id,
        asset_request_id=asset_request_id,
        ride_matching_id=ride_matching_id
    )

    # Assert

    asset_request_obj = AssetRequest.objects.get(id=asset_request_id)
    ride_matching_obj = ShareRide.objects.get(id=ride_matching_id)
    assert asset_request_obj.accepted_by_id == user_id
    assert ride_matching_obj.seats == seats
    assert ride_matching_obj.asset_quantity == asset_quantity


@pytest.mark.django_db
def update_asset_request_status_with_travel_matching_deatails(
    populate_asset_matching_requests, populate_ride_shares
):
    # Arrange
    user_id = 2
    asset_request_id = 2
    travel_matching_id = 2
    asset_quantity = 4
    storage = AcceptAssetRequestStorageImplementation()

    # Act
    storage.update_asset_request_status_with_travel_matching_deatails(
        user_id=user_id,
        asset_request_id=asset_request_id,
        travel_matching_id=travel_matching_id
    )

    # Assert
    asset_request_obj = AssetRequest.objects.get(id=asset_request_id)
    travel_matching_obj = TravelInfo.objects.get(id=travel_matching_id)
    assert asset_request_obj.accepted_by_id == user_id
    assert travel_matching_obj.asset_quantity == asset_quantity
