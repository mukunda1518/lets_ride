from dataclasses import dataclass

@dataclass
class UserDto():
    user_id: int
    username: str
    phone_number: str
    profile_pic: str
