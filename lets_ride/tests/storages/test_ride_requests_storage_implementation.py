import pytest
import datetime
from lets_ride.storages.ride_requests_storage_implementation \
    import RideRequestsStorageImplementation


@pytest.mark.django_db
def test_get_ride_request_with_status_accepted(
    snapshot,
    ride_request_factory_fixture_with_status_accepted,
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 3
    sort_key = "seats"
    sort_value = "ASC"
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_accepted(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    snapshot.assert_match(response, "my_ride_requests_with_status_accepted")

@pytest.mark.django_db
def test_get_ride_request_with_status_expired(
    snapshot,
    ride_request_factory_fixture_with_status_expired
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 3
    sort_key = "seats"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime.now()
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_expired(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    snapshot.assert_match(response, "my_ride_requests_with_status_expired")


@pytest.mark.django_db
def test_get_ride_request_with_status_pending(
    snapshot,
    ride_request_factory_fixture_with_status_pending
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 1
    sort_key = "seats"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime.now()
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_pending(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    snapshot.assert_match(response, "my_ride_requests_with_status_pending")


# @pytest.mark.django_db
# def test_get_ride_request(
#     ride_requests_dto_with_status_pending,
#     populate_ride_requests,
# ):
#     # Arrange
#     user_id = 2
#     offset = 0
#     limit = 1
#     sort_key = "seats"
#     sort_value = "ASC"
#     storage = RideRequestsStorageImplementation()

#     # Act
#     response = storage.get_ride_requests(
#         user_id=user_id, offset=offset, limit=limit,
#         sort_key=sort_key, sort_value=sort_value,
#     )

#     # Assert
#     assert ride_requests_dto_with_status_pending == response
