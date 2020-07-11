from dataclasses import dataclass

from datetime import datetime

from typing import Optional, List


@dataclass
class RideRequestDTO:
    source: str
    destination: str
    flexible_timings: bool
    travel_date_time: Optional[datetime]
    flexible_from_date_time: Optional[datetime]
    flexible_to_date_time: Optional[datetime]
    seats: int
    laguage_quantity: int



@dataclass
class MyRideRequestDTO(RideRequestDTO):
    ride_request_id: int
    status: Optional[str]
    accepted_person_id: int


@dataclass
class TotalRideRequestsDTO:
    ride_request_dtos: List[MyRideRequestDTO]
    total_ride_requests: int

