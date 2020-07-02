from datetime import datetime
import pytest
from lets_ride.dtos.dtos import (
    BaseRideRequestDto,
    BaseAssetRequestDto,
    RideRequestDto,
    AssetRequestDto,
    RideRequestsDto,
    AssetRequestsDto,
    RideMatchingDto,
    AssetMatchingDto,
    RideAssetMatchingDto,
    UserDto
)
from lets_ride.constants.enums import Status
from lets_ride.constants.constants \
    import FILTER_OPTIONS, RIDE_SORT_OPTIONS, ASSET_SORT_OPTIONS

@pytest.fixture
def base_ride_request_dto():
    base_ride_request_dto = BaseRideRequestDto(
        ride_request_id=1,
        source="Kurnool",
        destination="Hyderabad",
        travel_date_time=datetime(2020,6,12,3,50),
        flexible_timings=False,
        flexible_from_date_time="",
        flexible_to_date_time="",
        seats=4,
        laguage_quantity=5
    )
    return base_ride_request_dto

@pytest.fixture
def user_dtos_for_ride_request():
    user_dtos = [
        UserDto(
            user_id=2,
            username="user2",
            phone_number="1234567890"
        )
    ]
    return user_dtos

@pytest.fixture
def ride_request_dtos(base_ride_request_dto):
    ride_request_dtos = [
        RideRequestDto(
            ride_dto=base_ride_request_dto,
            accepted_person_id=2,
            status="ACCEPTED"
        )
    ]
    return ride_request_dtos


@pytest.fixture
def ride_requests_dto(ride_request_dtos):
    ride_request_dto = RideRequestsDto(
        ride_dtos=ride_request_dtos,
        total_rides=1,
    )
    return ride_request_dto


@pytest.fixture()
def get_my_ride_requests_response():
    my_requests_response = {
        "rides": [
            {
                "ride_request_id": 1,
                "source": "Kurnool",
                "destination": "Hyderabad",
                "travel_date_time": "2020-06-12 03:50 AM",
                "flexible_timings": False,
                "flexible_from_date_time": "",
                "flexible_to_date_time": "",
                "seats": 4,
                "laguage_quantity": 5,
                "accepted_person": "user2",
                "accepted_person_phone_number": "1234567890",
                "status": Status.ACCEPTED.value
            }
        ],
        "total_rides": 1,
        "filter_options": FILTER_OPTIONS,
        "sort_options": RIDE_SORT_OPTIONS
    }
    return my_requests_response




@pytest.fixture
def base_asset_request_dto():
    base_asset_request_dto = BaseAssetRequestDto(
        asset_request_id=1,
        source="Kurnool",
        destination="Hyderabad",
        travel_date_time=datetime(2020,6,12,3,50),
        flexible_timings=False,
        flexible_from_date_time="",
        flexible_to_date_time="",
        asset_quantity=3,
        asset_type="BAG",
        asset_type_others="",
        asset_sensitivity="HIGH",
        deliver_to="user1",
        phone_number="1234567890"
    )
    return base_asset_request_dto


@pytest.fixture
def asset_request_dtos(base_asset_request_dto):
    asset_request_dtos = [
        AssetRequestDto(
            asset_dto=base_asset_request_dto,
            accepted_person="",
            accepted_person_phone_number="",
            status="EXPIRED"
        )
    ]
    return asset_request_dtos

@pytest.fixture
def asset_requests_dto(asset_request_dtos):
    asset_request_dto = AssetRequestsDto(
        asset_dtos=asset_request_dtos,
        total_assets=1,
    )
    return asset_request_dto


@pytest.fixture
def get_my_asset_requests_response():
    my_asset_requests_response = {
        "assets": [
            {
                "asset_request_id": 1,
                "source": "Kurnool",
                "destination": "Hyderabad",
                "travel_date_time": "2020-06-12 03:50 AM",
                "flexible_timings": False,
                "flexible_from_date_time": "",
                "flexible_to_date_time": "",
                "asset_quantity": 3,
                "asset_type": "BAG",
                "asset_type_others": "",
                "asset_sensitivity": "HIGH",
                "deliver_to": "user1",
                "phone_number": "1234567890",
                "accepted_person": "",
                "accepted_person_phone_number": "",
                "status": Status.EXPIRED.value
            }
        ],
        "total_assets": 1,
        "filter_options": FILTER_OPTIONS,
        "sort_options": ASSET_SORT_OPTIONS
    }
    return my_asset_requests_response

#--------------Ride_Asset Matching------------

@pytest.fixture
def ride_matching_dtos(base_ride_request_dto):
    ride_matching_dtos =[
        RideMatchingDto(
            ride_dto=base_ride_request_dto,
            ride_matching_id=2,
            username="user1",
            user_phone_number="1234567895"
        )
    ]
    return ride_matching_dtos


@pytest.fixture
def asset_matching_dtos(base_asset_request_dto):
    asset_matching_dtos = [
        AssetMatchingDto(
            asset_dto=base_asset_request_dto,
            ride_matching_id=0,
            travel_matching_id=3,
            username="user1",
            user_phone_number="1234567895"
        )
    ]
    return asset_matching_dtos

@pytest.fixture
def ride_asset_matching_dto(ride_matching_dtos, asset_matching_dtos):
    ride_asset_matching_dto = RideAssetMatchingDto(
        ride_dtos=ride_matching_dtos,
        total_rides=1,
        asset_dtos=asset_matching_dtos,
        total_assets=1
    )
    return ride_asset_matching_dto


@pytest.fixture()
def get_ride_asset_matching_response():
        ride_asset_matching_response = {
            "rides": [
                {
                    "ride_request_id": 1,
                    "ride_matching_id": 2,
                    "source": "Kurnool",
                    "destination": "Hyderabad",
                    "travel_date_time": "2020-06-12 03:50 AM",
                    "flexible_timings": False,
                    "flexible_from_date_time": "",
                    "flexible_to_date_time": "",
                    "seats": 4,
                    "laguage_quantity": 5,
                    "username": "user1",
                    "user_phone_number": "1234567895"
                }
            ],
            "total_rides": 1,
            "assets": [
                {
                    "asset_request_id": 1,
                    "ride_matching_id": 0,
                    "travel_matching_id": 3,
                    "source": "Kurnool",
                    "destination": "Hyderabad",
                    "travel_date_time": "2020-06-12 03:50 AM",
                    "flexible_timings": False,
                    "flexible_from_date_time": "",
                    "flexible_to_date_time": "",
                    "asset_quantity": 3,
                    "asset_type": "BAG",
                    "asset_type_others": "",
                    "asset_sensitivity": "HIGH",
                    "deliver_to": "user1",
                    "phone_number": "1234567890",
                    "username": "user1",
                    "user_phone_number": "1234567895"
                }
            ],
            "total_assets": 1
        }
        return ride_asset_matching_response
