from typing import List
from lets_ride.dtos.dtos import UserDto

class AuthService:

    @property
    def service_interface(self):
        from lets_ride_auth.interface.service_interface import ServiceInterface
        return ServiceInterface()


    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.service_interface.get_user_dtos(user_ids=user_ids)
        user_details_dtos = []
        for user_dto in user_dtos:
            user_details_dto = UserDto(
                user_id=user_dto.user_id,
                username=user_dto.username,
                phone_number=user_dto.phone_number
            )
            user_details_dtos.append(user_details_dto)
        return user_details_dtos

    