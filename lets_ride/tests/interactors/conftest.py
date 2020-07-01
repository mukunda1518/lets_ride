import pytest
from datetime import datetime
from lets_ride.constants.enums import Status
from lets_ride.dtos.dtos import (
    BaseRideRequestDto,
    BaseAssetRequestDto,
    RideRequestsDto,
    RideRequestDto,
    AssetRequestDto,
    AssetRequestsDto,
    BaseRideShareDto,
    BaseTravelInfoDto,
    UserDto
)



#-------------Ride Requests----------------

@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDto(
            user_id=2,
            username="user2",
            phone_number="1234567890"
        )
    ]
    return user_dtos


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
def ride_request_dtos(base_ride_request_dto):
    ride_request_dtos = [
        RideRequestDto(
            ride_dto= base_ride_request_dto,
            accepted_person_id=2,
            status=Status.ACCEPTED.value
        )
    ]
    return ride_request_dtos

@pytest.fixture
def ride_requests_dto(
    ride_request_dtos
):
    ride_requests_dto = RideRequestsDto(
        ride_dtos=ride_request_dtos,
        total_rides=1
    )
    return ride_requests_dto


@pytest.fixture()
def get_my_ride_requests_response():
    my_ride_requests_response = {
        "rides": [
            {
                "source": "Kurnool",
                "destination": "Hyderabad",
                "travel_date_time": "2020-06-12 03:50 PM",
                "flexible_timings": False,
                "flexible_from_date_time": "",
                "flexible_to_date_time": "",
                "seats": 4,
                "laguage_quantity": 5,
                "accepted_person_id": 2,
                "status": "ACCEPTED"
            }
        ],
        "total_rides": 1
    }
    return my_ride_requests_response


#--------------Asset Request------------------

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
        deliver_to="User1",
        phone_number="1234567890"
    )
    return base_asset_request_dto

@pytest.fixture
def base_asset_request_dto_with_flexiable_timings():
    base_asset_request_dto = BaseAssetRequestDto(
        source="Kurnool",
        destination="Hyderabad",
        travel_date_time="",
        flexible_timings=True,
        flexible_from_date_time=datetime(2020,6,12,3,50),
        flexible_to_date_time=datetime(2020,6,12,3,50),
        asset_quantity=3,
        asset_type="BAG",
        asset_type_others="",
        asset_sensitivity="HIGH",
        deliver_to="User1",
        phone_number="1234567890"
    )
    return base_asset_request_dto

@pytest.fixture
def asset_request_dtos_with_flexible_timings(
    base_asset_request_dto_with_flexiable_timings
):
    asset_request_dtos = [
        AssetRequestDto(
            asset_dto=base_asset_request_dto_with_flexiable_timings,
            accepted_person=1,
            accepted_person_phone_number="1234567908",
            status=Status.ACCEPTED.value
        )
    ]
    return asset_request_dtos


@pytest.fixture
def asset_request_dtos(base_asset_request_dto):
    asset_request_dtos = [
        AssetRequestDto(
            asset_dto=base_asset_request_dto,
            accepted_person="",
            accepted_person_phone_number="",
            status=Status.EXPIRED.value
        )
    ]
    return asset_request_dtos


@pytest.fixture
def asset_requests_dto_with_flexible_timings(
    asset_request_dtos_with_flexible_timings
):
    asset_requests_dto = AssetRequestsDto(
        asset_dtos=asset_request_dtos_with_flexible_timings,
        total_assets=1
    )
    return asset_requests_dto

@pytest.fixture
def asset_requests_dto(asset_request_dtos):
    asset_requests_dto = AssetRequestsDto(
        asset_dtos=asset_request_dtos,
        total_assets=1
    )
    return asset_requests_dto

@pytest.fixture()
def get_my_asset_requests_response():
    my_asset_requests_response = {
        "assets" : [
            {
                "source": "Kurnool",
                "destination": "Hyderabad",
                "travel_date_time": "2020-04-12 03:50 PM",
                "flexible_timings": False,
                "flexible_from_date_time": "",
                "flexible_to_date_time": "",
                "asset_quantity": 3,
                "asset_type": "BAG",
                "asset_sensitivity": "HIGH",
                "deliver_to": "User1",
                "phone_number": "1234567890",
                "accepted_person": "",
                "accepted_person_phone_number": "",
                "status": "EXPIRED"
            }
        ],
        "total_assets": 1
    }
    return my_asset_requests_response


#----------------Ride Shares--------------


@pytest.fixture
def base_ride_share_dtos():
    base_share_request_dtos = [
        BaseRideShareDto(
            ride_share_id=1,
            source="Kurnool",
            destination="Hyderabad",
            travel_date_time=datetime(2020,6,12,3,50),
            flexible_timings=False,
            flexible_from_date_time="",
            flexible_to_date_time="",
            seats=4,
            asset_quantity=5
        ),
        BaseRideShareDto(
            ride_share_id=2,
            source="Delhi",
            destination="Hyderabad",
            travel_date_time="",
            flexible_timings=True,
            flexible_from_date_time=datetime(2020,4,12,3,50),
            flexible_to_date_time=datetime(2020,4,13,3,50),
            seats=2,
            asset_quantity=4
        )
    ]
    return base_share_request_dtos



#-----------Travel Share--------------

@pytest.fixture
def base_travel_share_dtos():
    base_travel_share_dtos = [
        BaseTravelInfoDto(
            travel_share_id=1,
            source="Kurnool",
            destination="Hyderabad",
            travel_date_time=datetime(2020,6,12,3,50),
            flexible_timings=False,
            flexible_from_date_time="",
            flexible_to_date_time="",
            travel_medium="BUS",
            asset_quantity=5
        ),
        BaseTravelInfoDto(
            travel_share_id=2,
            source="Delhi",
            destination="Hyderabad",
            travel_date_time="",
            flexible_timings=True,
            flexible_from_date_time=datetime(2020,4,12,3,50),
            flexible_to_date_time=datetime(2020,4,12,3,50),
            travel_medium="TRAIN",
            asset_quantity=4
        )
    ]
    return base_travel_share_dtos

