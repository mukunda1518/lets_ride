import pytest
import datetime
from lets_ride.dtos.dtos import (
    BaseRideRequestDto,
    BaseAssetRequestDto,
    RideRequestDto,
    AssetRequestDto,
    RideAssetRequestsDto,
)

@pytest.fixture
def base_ride_request_dto():
    base_ride_request_dto = BaseRideRequestDto(
        source="Kurnool",
        destination="Hyderabad",
        travel_date_time="2020-04-12 03:50 PM",
        flexible_timings=False,
        flexible_from_date_time="",
        flexible_to_date_time="",
        seats=4,
        laguage_quantity=5
    )
    return base_ride_request_dto

@pytest.fixture
def base_asset_request_dto():
    base_asset_request_dto = BaseAssetRequestDto(
        source="Kurnool",
        destination="Hyderabad",
        travel_date_time="2020-04-12 03:50 PM",
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
def ride_request_dto():
    ride_request_dto = RideRequestDto(
        accepted_person="User2",
        accepted_person_phone_number="1234567890",
        status="PENDING"
    )
    return ride_request_dto

@pytest.fixture
def asset_request_dt