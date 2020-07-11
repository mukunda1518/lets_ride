from dataclasses import dataclass

@dataclass
class UserDTO():
    user_id: int
    username: str
    phone_number: str
    profile_pic: str