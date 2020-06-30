from typing import List

from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.models.user import User
from lets_ride_auth.dtos.dtos import UserDto
from lets_ride_auth.exceptions.exceptions import (
    InvalidPhoneNumber,
    InvalidPassword
)


class UserStorageImplementation(UserStorageInterface):

    def sign_up(
        self,
        username: str,
        phone_number: str,
        password: str
    ) -> int:
        user_obj = User.objects.create(
            username=username,
            phone_number=phone_number,
            password=password
        )
        user_obj.set_password(user_obj.password)
        user_obj.save()
        return user_obj.id


    def validate_password(self, phone_number: str, password: str):
        try:
            user_obj = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise InvalidPhoneNumber

        is_invalid_password = not user_obj.check_password(password)

        if is_invalid_password:
            raise InvalidPassword


    def validate_phone_number(self, phone_number: str):
        try:
            User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise InvalidPhoneNumber


    def check_username_exists(self, username: str):

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return False
        return True

    def check_phone_number_exists(self, phone_number: str):
        try:
            User.objects.get(phone_number=phone_number)
        except  User.DoesNotExist:
            return False
        return True


    def login(
        self,
        phone_number: str,
        password: str
    ) -> int:
        user_obj = User.objects.get(
            phone_number=phone_number,
        )
        return user_obj.id


    def user_profile(self, user_id: int) -> UserDto:
        user_obj = User.objects.get(id=user_id)
        user_dto = self._get_user_dto(user_obj)
        return user_dto


    def update_user_password(self, user_id: int, password: str):
        user_obj = User.objects.get(id=user_id)
        user_obj.set_password(password)
        user_obj.save()


    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDto]:
        user_objs = list(User.objects.filter(id__in=user_ids))
        user_dtos = []
        for user_obj in user_objs:
            user_dto = self._get_user_dto(user_obj)
            user_dtos.append(user_dto)
        return user_dtos

    def _get_user_dto(self, user_obj: User) -> UserDto:
        user_dto = UserDto(
            user_id=user_obj.id,
            username=user_obj.username,
            phone_number=user_obj.phone_number,
            profile_pic=user_obj.profile_pic
        )
        return user_dto


    def get_user_ids(self) -> List[int]:
        user_ids = list(User.objects.values_list('id', flat=True))
        return user_ids
