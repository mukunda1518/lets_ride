from dataclasses import dataclass

from datetime import datetime

@dataclass
class RideRequestDTO:
    from_place: str
    to_place: str
    travel_date_time: datetime
    no_of_seats: int


