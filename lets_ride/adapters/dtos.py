from dataclasses import dataclass


@dataclass
class UserDetailsDTO:
    user_id: int
    username: str
    phone_number: str
