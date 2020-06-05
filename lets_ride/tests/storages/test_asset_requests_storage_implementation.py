import datetime
import pytest
from lets_ride.storages.asset_requests_storage_implementation \
    import AssetRequestsStorageImplementation


@pytest.mark.django_db
def test_get_asset_request_with_status_accepted(
    asset_requests_dto_with_status_accepted,
    populate_asset_requests,
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 1
    sort_key = "asset_quantity"
    sort_value = "ASC"
    storage = AssetRequestsStorageImplementation()

    # Act
    response = storage.get_asset_request_with_status_accepted(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    assert asset_requests_dto_with_status_accepted == response


@pytest.mark.django_db
def test_get_asset_request_with_status_pending(
    asset_requests_dto_with_status_pending,
    populate_asset_requests,
):
    # Arrange
    user_id = 2
    offset = 0
    limit = 1
    sort_key = "date_time"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime(2020,3,1,3,50)
    storage = AssetRequestsStorageImplementation()

    # Act
    response = storage.get_asset_request_with_status_pending(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    assert asset_requests_dto_with_status_pending == response


@pytest.mark.django_db
def test_get_asset_request_with_status_expired(
    asset_requests_dto_with_status_expired,
    populate_asset_requests,
):
    # Arrange
    user_id = 1
    offset = 0
    limit = 1
    sort_key = "asset_quantity"
    sort_value = "ASC"
    current_datetime_obj = datetime.datetime(2020,3,1,3,50)
    storage = AssetRequestsStorageImplementation()

    # Act
    response = storage.get_asset_request_with_status_expired(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    assert asset_requests_dto_with_status_expired == response


@pytest.mark.django_db
def test_get_asset_request_without_status(
    asset_requests_dto_with_status_pending,
    populate_asset_requests,
):
    # Arrange
    user_id = 2
    offset = 0
    limit = 1
    sort_key = "asset_quantity"
    sort_value = "ASC"
    storage = AssetRequestsStorageImplementation()

    # Act
    response = storage.get_asset_requests(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    assert asset_requests_dto_with_status_pending == response
