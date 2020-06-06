import datetime
import pytest
from lets_ride.storages.matching_shares_storage_implementation \
    import MatchingSharesStorageImplementation


@pytest.mark.django_db
def test_get_ride_shares(ride_share_dtos, populate_ride_shares):
    # Arrange
    user_id = 1
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_ride_shares(user_id=user_id)

    # Assert
    assert ride_share_dtos == response


@pytest.mark.django_db
def test_get_ride_shares_with_no_ride_shares(populate_ride_shares):
    # Arrange
    user_id = 3
    ride_share_dtos = []
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_ride_shares(user_id=user_id)

    # Assert
    assert ride_share_dtos == response

@pytest.mark.django_db
def test_get_travel_shares(travel_share_dtos, populate_travel_shares):
    # Arrange
    user_id = 1
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_travel_shares(user_id=user_id)

    # Assert
    assert travel_share_dtos == response


@pytest.mark.django_db
def test_get_travel_shares_with_no_travel_shares(populate_travel_shares):
    # Arrange
    user_id = 3
    travel_share_dtos = []
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_travel_shares(user_id=user_id)

    # Assert
    assert travel_share_dtos == response


@pytest.mark.django_db
def test_get_ride_matching_requests(
    ride_matching_dtos, populate_ride_matching_requests
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    seats = 10
    asset_quantity = 12
    from_datetime = datetime.datetime(2020,7,14,5,50)
    to_datetime = datetime.datetime(2020,7,16,5,45)
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_ride_matching_requests(
        source, destination, seats, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert ride_matching_dtos == response

@pytest.mark.django_db
def test_get_ride_matching_requests_with_case_sensitive(
    ride_matching_dtos, populate_ride_matching_requests
):
    # Arrange
    source = "kurnool"
    destination = "Hyderabad"
    seats = 10
    asset_quantity = 12
    from_datetime = datetime.datetime(2020,7,14,5,50)
    to_datetime = datetime.datetime(2020,7,16,5,45)
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_ride_matching_requests(
        source, destination, seats, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert ride_matching_dtos == response

@pytest.mark.django_db
def test_get_ride_matching_requests_with_no_matches(
    ride_matching_dtos, populate_ride_matching_requests
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    seats = 10
    asset_quantity = 12
    from_datetime = datetime.datetime(2020,7,15,5,50)
    to_datetime = datetime.datetime(2020,7,15,5,45)
    ride_matching_dtos = []
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_ride_matching_requests(
        source, destination, seats, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert ride_matching_dtos == response

@pytest.mark.django_db
def test_get_asset_matching_requests(
    asset_matching_dtos, populate_asset_matching_requests
):
    # Arrange
    source = "Delhi"
    destination = "Hyderabad"
    asset_quantity = 20
    from_datetime = datetime.datetime(2020,1,14,3,50)
    to_datetime = datetime.datetime(2020,4,16,3,50)
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_travel_matching_requests(
        source, destination, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert asset_matching_dtos == response


@pytest.mark.django_db
def test_get_asset_matching_requests_with_no_matchings_found(
    asset_matching_dtos, populate_asset_matching_requests
):
    # Arrange
    source = "Delhi"
    destination = "Hyderabad"
    asset_quantity = 20
    asset_matching_dtos = []
    from_datetime = datetime.datetime(2020,7,14,3,50)
    to_datetime = datetime.datetime(2020,8,15,3,50)
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_travel_matching_requests(
        source, destination, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert asset_matching_dtos == response

@pytest.mark.django_db
def test_get_asset_matching_requests_with_case_sensitive(
    asset_matching_dtos, populate_asset_matching_requests
):
    # Arrange
    source = "Delhi"
    destination = "hyderabad"
    asset_quantity = 20
    from_datetime = datetime.datetime(2020,1,14,3,50)
    to_datetime = datetime.datetime(2020,4,16,3,50)
    storage = MatchingSharesStorageImplementation()

    # Act
    response = storage.get_travel_matching_requests(
        source, destination, asset_quantity, from_datetime, to_datetime
    )

    # Assert
    assert asset_matching_dtos == response
