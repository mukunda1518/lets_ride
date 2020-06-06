import pytest
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.storages.accept_ride_request_storage_implementaion \
    import AcceptRideRequestStorageImplementation

@pytest.mark.django_db
def test_update_ride_request_status(
    populate_ride_shares, populate_ride_matching_requests
):
    # Arrange
    user_id = 2
    ride_request_id = 2
    ride_matching_id = 2
    seats = 2
    asset_quantity = 0
    storage = AcceptRideRequestStorageImplementation()

    # Act
    storage.update_ride_request_status(
        user_id=user_id,
        ride_request_id=ride_request_id,
        ride_matching_id=ride_matching_id
    )

    # Assert
    ride_request_obj = RideRequest.objects.get(id=ride_request_id)
    ride_matching_obj = ShareRide.objects.get(id=ride_matching_id)
    assert ride_request_obj.accepted_by_id == user_id
    assert ride_matching_obj.seats == seats
    assert ride_matching_obj.asset_quantity == asset_quantity
