from lets_ride_auth.dtos.dtos import UserDto
from common.dtos import UserAuthTokensDTO

from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest

from lets_ride.constants.exception_messages import (
    INVALID_PHONE_NUMBER,
    INVALID_PASSWORD,
    INVALID_USERNAME,
    PHONE_NUMBER_WITH_USER_EXIST
)

from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def get_sign_up_response(self, token_dto: UserAuthTokensDTO):
        response_dict = {
            "user_id": token_dto.user_id,
            "access_token": token_dto.access_token,
            "refresh_token": token_dto.refresh_token,
            "expires_in": token_dto.expires_in
        }
        return response_dict


    def get_login_response(self, token_dto: UserAuthTokensDTO):
        response_dict = {
            "user_id": token_dto.user_id,
            "access_token": token_dto.access_token,
            "refresh_token": token_dto.refresh_token,
            "expires_in": token_dto.expires_in
        }
        return response_dict


    def user_profile_response(self, user_dto: UserDto):
        user_dict = {
            "username": user_dto.username,
            "phone_number": user_dto.phone_number,
            "profile_pic_url": user_dto.profile_pic
        }
        return user_dict

    def raise_invalid_phone_number(self):
        raise NotFound(*INVALID_PHONE_NUMBER)


    def raise_invalid_password(self):
        raise NotFound(*INVALID_PASSWORD)


    def raise_username_already_exist(self):
        raise BadRequest(*INVALID_USERNAME)


    def raise_user_with_phone_number_already_exist(self):
        raise BadRequest(*PHONE_NUMBER_WITH_USER_EXIST)

