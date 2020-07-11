from datetime import datetime
from typing import List
from abc import abstractmethod
from abc import ABC
from lets_ride.dtos.dtos import (
    RideRequestsDto,
    AssetRequestsDto,
    RideRequestDTO,
    CreateRideRequestDTO,
)

class StorageInterface(ABC):

    @abstractmethod
    def create_ride_request(
        self, user_id: int, create_ride_request_dto: CreateRideRequestDTO
    ):
        pass

    @abstractmethod
    def create_ride_request_with_flexible_timings(
        self, user_id: int, create_ride_request_dto: CreateRideRequestDTO
    ):
        pass

    @abstractmethod
    def create_share_travel_info(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        travel_medium: str,
        asset_quantity: int
    ):
        pass

    @abstractmethod
    def create_share_travel_info_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        travel_medium: str,
        asset_quantity: int
    ):
        pass

    @abstractmethod
    def create_share_ride(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        seats: int,
        asset_quantity: int
    ):
        pass

    @abstractmethod
    def create_share_ride_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        seats: int,
        asset_quantity: int
    ):
        pass

    @abstractmethod
    def create_asset_request(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: datetime,
        flexible_timings: bool,
        asset_quantity: int,
        asset_type: str,
        asset_type_others: str,
        asset_sensitivity: str,
        deliver_to: str,
        phone_number: str
    ):
        pass

    @abstractmethod
    def create_asset_request_with_flexible_timings(
        self,
        user_id: int,
        source: str,
        destination: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: datetime,
        flexible_travel_to_date_time: datetime,
        asset_quantity: int,
        asset_type: str,
        asset_type_others: str,
        asset_sensitivity: str,
        deliver_to: str,
        phone_number: str
    ):
        pass
