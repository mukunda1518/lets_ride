import datetime
import pytest
from freezegun import freeze_time
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo
from lets_ride.models.asset_request import AssetRequest

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_ride_request_with_given_data_creates_ride_request_record(populate_user):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    travel_date_time = datetime.datetime.now()
    flexible_timings = False
    seats = 2
    laguage_quantity = 3
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_ride_request(
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        seats=seats,
        laguage_quantity=laguage_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = RideRequest.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_ride_request_with_flexible_timings_with_given_data_creates_ride_request_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    flexible_timings = True
    flexible_travel_from_date_time = datetime.datetime.now()
    flexible_travel_to_date_time = datetime.datetime.now()
    seats = 2
    laguage_quantity = 3
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_ride_request_with_flexible_timings(
        source=source,
        destination=destination,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_travel_from_date_time,
        flexible_travel_to_date_time=flexible_travel_to_date_time,
        seats=seats,
        laguage_quantity=laguage_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = RideRequest.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_share_ride_with_given_data_creates_share_ride_record(populate_user):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    travel_date_time = datetime.datetime.now()
    flexible_timings = False
    seats = 3
    asset_quantity = 2
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_share_ride(
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        seats=seats,
        asset_quantity=asset_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = ShareRide.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db


@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_share_ride_with_flexible_timings_with_given_data_creates_share_ride_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    flexible_timings = True
    flexible_travel_from_date_time = datetime.datetime.now()
    flexible_travel_to_date_time = datetime.datetime.now()
    seats = 3
    asset_quantity = 2
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_share_ride_with_flexible_timings(
        source=source,
        destination=destination,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_travel_from_date_time,
        flexible_travel_to_date_time=flexible_travel_to_date_time,
        seats=seats,
        asset_quantity=asset_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = ShareRide.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_share_travel_info_with_given_data_creates_share_travel_info_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    travel_date_time = datetime.datetime.now()
    flexible_timings = False
    travel_medium = "BUS"
    asset_quantity = 3
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_share_travel_info(
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        travel_medium=travel_medium,
        asset_quantity=asset_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = TravelInfo.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_share_travel_info_with_flexible_timings_with_given_data_creates_travel_info_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    flexible_timings = True
    flexible_travel_from_date_time = datetime.datetime.now()
    flexible_travel_to_date_time = datetime.datetime.now()
    travel_medium = "BUS"
    asset_quantity = 3
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_share_travel_info_with_flexible_timings(
        source=source,
        destination=destination,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_travel_from_date_time,
        flexible_travel_to_date_time=flexible_travel_to_date_time,
        travel_medium=travel_medium,
        asset_quantity=asset_quantity,
        user_id=user_id
    )

    # Assert
    actual_no_of_record_in_db = TravelInfo.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_assert_request_with_given_data_creates_share_travel_info_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    travel_date_time = datetime.datetime.now()
    flexible_timings = False
    asset_quantity = 3
    asset_type = "LAPTOP"
    asset_type_others =""
    asset_sensitivity = "HIGH"
    deliver_to = "User1"
    phone_number = "1234567980"
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_asset_request(
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        asset_quantity=asset_quantity,
        asset_type=asset_type,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        user_id=user_id,
        phone_number=phone_number,
    )

    # Assert
    actual_no_of_record_in_db = AssetRequest.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

@pytest.mark.django_db
@freeze_time("2020-01-14 13:21")
def test_asset_request_with_flexible_timings_with_given_data_creates_share_travel_info_record(
    populate_user
):
    # Arrange
    source = "Kurnool"
    destination = "Hyderabad"
    flexible_travel_from_date_time = datetime.datetime.now()
    flexible_travel_to_date_time = datetime.datetime.now()
    flexible_timings = False
    asset_quantity = 3
    asset_type = "LAPTOP"
    asset_type_others =""
    asset_sensitivity = "HIGH"
    deliver_to = "User1"
    phone_number = "1234567980"
    user_id = 1
    storage = StorageImplementation()
    expected_no_of_record_in_db = 1

    # Act
    storage.create_asset_request_with_flexible_timings(
        source=source,
        destination=destination,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_travel_from_date_time,
        flexible_travel_to_date_time=flexible_travel_to_date_time,
        asset_quantity=asset_quantity,
        asset_type=asset_type,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        user_id=user_id,
        phone_number=phone_number,
    )

    # Assert
    actual_no_of_record_in_db = AssetRequest.objects.all().count()
    assert expected_no_of_record_in_db == actual_no_of_record_in_db

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
    storage = StorageImplementation()

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
    current_datetime_obj = datetime.datetime.now()
    storage = StorageImplementation()

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
    current_datetime_obj = datetime.datetime.now()
    storage = StorageImplementation()

    # Act
    response = storage.get_ride_request_with_status_pending(
        user_id=user_id, offset=offset, limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )

    # Assert
    assert ride_requests_dto_with_status_pending == response

