from datetime import datetime
from dataclasses import dataclass
from typing import Optional, List
from lets_ride.constants.enums \
    import AssetType, AssetSensitivity, Status, TravelMedium

@dataclass
class UserDto():
    username: str
    phone_number: str
    profile_pic: str

@dataclass
class BaseRideRequestDto:
    source: str
    destination: str
    travel_date_time: Optional[datetime]
    flexible_timings: bool
    flexible_from_date_time: Optional[datetime]
    flexible_to_date_time: Optional[datetime]
    seats: int
    laguage_quantity: int

@dataclass
class BaseAssetRequestDto:
    source: str
    destination: str
    travel_date_time: Optional[datetime]
    flexible_timings: bool
    flexible_from_date_time: Optional[datetime]
    flexible_to_date_time: Optional[datetime]
    asset_quantity: int
    asset_type: AssetType
    asset_type_others: Optional[str]
    asset_sensitivity: AssetSensitivity
    deliver_to: str
    phone_number: str

@dataclass
class RideRequestDto:
    ride_request_id: int
    ride_dto: BaseRideRequestDto
    accepted_person: str
    accepted_person_phone_number: str
    status: Optional[str]

@dataclass
class RideRequestsDto:
    ride_dtos: 
    t
@dataclass
class AssetRequestDto:
    asset_request_id: int
    asset_dto: BaseAssetRequestDto
    accepted_person: str
    accepted_person_phone_number: str
    status: Optional[str]

@dataclass
class RideAssetRequestsDto:
    ride_dtos: List[RideRequestDto]
    total_rides_count: int
    asset_dtos: List[AssetRequestDto]
    total_assets_count: int


@dataclass
class RideMatchingDto:
    ride_dto: BaseRideRequestDto
    username: str
    user_phone_number: str

@dataclass
class AssetMatchingDto:
    asset_dto: BaseAssetRequestDto
    username: str
    user_phone_number: str

@dataclass
class RideAssetMatchingDto:
    ride_dtos: List[RideMatchingDto]
    total_rides_count: int
    asset_dtos: List[AssetMatchingDto]
    total_assets_count: int

@dataclass
class RideShareDto:
    source: str
    destination: str
    flexible_timings: bool
    travel_date_time: Optional[datetime]
    flexible_from_date_time: Optional[datetime]
    flexible_to_date_time: Optional[datetime]
    seats: int
    asset_quantity: int

@dataclass
class TravelInfoDto:
    source: str
    destination: str
    flexible_timings: bool
    travel_date_time: Optional[datetime]
    flexible_from_date_time: Optional[datetime]
    flexible_to_date_time: Optional[datetime]
    travel_medium: TravelMedium
    asset_quantity: int
