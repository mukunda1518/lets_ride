from typing import List

from abc import abstractmethod
from abc import ABC

from lets_ride_auth.interactors.storages.dtos import UserDTO


class UserStorageInterface(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def sign_up(self, username: str, phone_number: str, password: str) -> int:
        pass

    @abstractmethod
    def validate_password(self, phone_number: str, password: str):
        pass

    @abstractmethod
    def validate_phone_number(self, phone_number: str):
        pass

    @abstractmethod
    def login(self, phone_number: str, password: str) -> int:
        pass

    @abstractmethod
    def user_profile(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    def update_user_password(self,user_id: int, password: str):
        pass

    @abstractmethod
    def check_username_exists(self, username: str):
        pass

    @abstractmethod
    def check_phone_number_exists(self, phone_number: str):
        pass

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass

    @abstractmethod
    def get_user_ids(self) -> List[int]:
        pass