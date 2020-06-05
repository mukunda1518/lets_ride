import pytest
import datetime
from lets_ride.storages.ride_requests_storage_implementation \
    import RideRequestsStorageImplementation


@pytest.mark.django_db
def test_get_ride_request_with_status_accepted(
    ride_requests_dto_with_status_accepted,
    populate_ride_requests,
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 1
    sort_key = "seats"
    sort_value = "ASC"
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_accepted(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    assert ride_requests_dto_with_status_accepted == response

@pytest.mark.django_db
def test_get_ride_request_with_status_expired(
    ride_requests_dto_with_status_expired,
    populate_ride_requests,
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 1
    sort_key = "seats"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime(2020,5,8,9,50)
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_expired(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    assert ride_requests_dto_with_status_expired == response


@pytest.mark.django_db
def test_get_ride_request_with_status_pending(
    ride_requests_dto_with_status_pending,
    populate_ride_requests,
):
    # Arrange
    user_id = 2
    offset = 0
    limit = 1
    sort_key = "seats"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime(2020,3,4,5,30)
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_pending(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    assert ride_requests_dto_with_status_pending == response


@pytest.mark.django_db
def test_get_ride_request(
    ride_requests_dto_with_status_pending,
    populate_ride_requests,
):
    # Arrange
    user_id = 2
    offset = 0
    limit = 1
    sort_key = "seats"
    sort_value = "ASC"
    storage = RideRequestsStorageImplementation()

    # Act
    response = storage.get_ride_requests(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
    )

    # Assert
    assert ride_requests_dto_with_status_pending == response


