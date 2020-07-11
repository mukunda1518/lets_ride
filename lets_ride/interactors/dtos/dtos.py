from dataclasses import dataclass

from datetime import datetime

from typing import Union, Optional, List


from lets_ride.constants.enums import (
    SortByEnums, FilterByEnums, OrderByEnums, Status
)



@dataclass
class SortByDTO:
    sort_by: SortByEnums
    order: OrderByEnums


@dataclass
class FilterByDTO:
    filter_by: FilterByEnums
    value: str


@dataclass
class RequestMetricsDTO:
    user_id: int
    offset: int
    limit: int
    sort_by_dto: SortByDTO
    filter_by_dto: FilterByDTO


@dataclass
class RideRequestMetricsDTO(RequestMetricsDTO):
    pass


@dataclass
class AssetRequestMetricsDTO(RequestMetricsDTO):
    pass



@dataclass
class CreateRideRequestDTO:
    source: str
    destination: str
    flexible_timings: bool
    travel_date_time: str
    flexible_from_date_time: str
    flexible_to_date_time: str
    seats: int
    laguage_quantity: int





