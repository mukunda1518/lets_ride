from datetime import datetime
from typing import List, Union, Tuple
from django_swagger_utils.drf_server.exceptions \
    import NotFound, Forbidden, BadRequest
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.dtos.dtos import UserDto
from common.dtos import UserAuthTokensDTO
from lets_ride.constants.exception_messages import (
    INVALID_PHONE_NUMBER,
    INVALID_PASSWORD,
    INVALID_OFFSET_LIMIT_VALUE,
    INVALID_USERNAME,
    PHONE_NUMBER_WITH_USER_EXIST
)
from lets_ride.dtos.dtos import (
    RideRequestDto,
    AssetRequestDto,
    RideRequestsDto,
    AssetRequestsDto,
    RideAssetMatchingDto,
    RideMatchingDto,
    AssetMatchingDto,
    BaseRideRequestDto,
    BaseAssetRequestDto
)
from lets_ride.utils.datetime_conversion \
    import convert_datetime_object_to_string_format
from lets_ride.constants.constants \
    import FILTER_OPTIONS, RIDE_SORT_OPTIONS, ASSET_SORT_OPTIONS
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT



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

    def raise_invalid_for_limit_and_offset(self):
        raise BadRequest(*INVALID_OFFSET_LIMIT_VALUE)

    def raise_username_already_exist(self):
        raise BadRequest(*INVALID_USERNAME)

    def raise_user_with_phone_number_already_exist(self):
        raise BadRequest(*PHONE_NUMBER_WITH_USER_EXIST)

    def  get_asset_requests_response(
        self, asset_requests_dto: AssetRequestsDto
    ):
        asset_request_dtos = asset_requests_dto.asset_dtos
        total_assets = asset_requests_dto.total_assets
        asset_request_list = []
        for asset_request_dto in asset_request_dtos:
            asset_request_dict = \
                self._get_asset_request_dict(asset_request_dto)
            asset_request_list.append(asset_request_dict)
        response_dict = {
            "assets": asset_request_list,
            "total_assets": total_assets,
            "filter_options": FILTER_OPTIONS,
            "sort_options": ASSET_SORT_OPTIONS
        }
        return response_dict


    def _get_asset_request_dict(self, asset_request_dto: AssetRequestDto):
        base_asset_request_dto = asset_request_dto.asset_dto
        asset_request_dict = self._get_base_asset_dict(base_asset_request_dto)
        asset_request_dict["accepted_person"] = \
            asset_request_dto.accepted_person
        asset_request_dict["accepted_person_phone_number"] = \
            asset_request_dto.accepted_person_phone_number
        asset_request_dict["status"] = asset_request_dto.status
        return asset_request_dict


    def get_ride_requests_response(self, ride_requests_dto: RideRequestsDto):
        ride_request_dtos = ride_requests_dto.ride_dtos
        total_rides = ride_requests_dto.total_rides
        ride_request_list = []
        for ride_request_dto in ride_request_dtos:
            ride_request_dict = self._get_ride_request_dict(ride_request_dto)
            ride_request_list.append(ride_request_dict)
        response_dict = {
            "rides": ride_request_list,
            "total_rides": total_rides,
            "filter_options": FILTER_OPTIONS,
            "sort_options": RIDE_SORT_OPTIONS
        }
        return response_dict


    def _get_ride_request_dict(self, ride_request_dto: RideRequestDto):
        base_ride_request_dto = ride_request_dto.ride_dto
        ride_request_dict = self._get_base_ride_dict(base_ride_request_dto)
        ride_request_dict["accepted_person"] = \
            ride_request_dto.accepted_person
        ride_request_dict["accepted_person_phone_number"] = \
            ride_request_dto.accepted_person_phone_number
        ride_request_dict["status"] = ride_request_dto.status
        return ride_request_dict


    def _get_datetime_in_string_format(self, datetime_obj: datetime):
        datetime_str = convert_datetime_object_to_string_format(
            datetime_obj
        )
        return datetime_str


    def get_ride_asset_matching_response(
        self,
        ride_asset_matching_dto: RideAssetMatchingDto
    ):
        ride_dtos = ride_asset_matching_dto.ride_dtos
        total_rides = ride_asset_matching_dto.total_rides
        asset_dtos = ride_asset_matching_dto.asset_dtos
        total_assets = ride_asset_matching_dto.total_assets

        list_of_ride_dict = self._get_list_of_ride_dict(ride_dtos)
        list_of_asset_dict = self._get_list_of_asset_dict(asset_dtos)

        ride_asset_matching_dict = {
            "rides" : list_of_ride_dict,
            "total_rides": total_rides,
            "assets": list_of_asset_dict,
            "total_assets": total_assets
        }
        return ride_asset_matching_dict


    def _get_list_of_ride_dict(self, ride_dtos: List[RideMatchingDto]):
        list_of_ride_dict = []
        for ride_dto in ride_dtos:
            ride_dict = self._get_ride_dict(ride_dto)
            list_of_ride_dict.append(ride_dict)

        return list_of_ride_dict

    def _get_ride_dict(self, ride_dto: RideMatchingDto):
        base_ride_dto = ride_dto.ride_dto
        base_ride_dict = self._get_base_ride_dict(base_ride_dto)
        ride_dict = base_ride_dict
        ride_dict["ride_matching_id"] = ride_dto.ride_matching_id
        ride_dict["username"] = ride_dto.username
        ride_dict["user_phone_number"] = ride_dto.user_phone_number
        return ride_dict


    def _get_base_ride_dict(self, base_ride_dto: BaseRideRequestDto):
        travel_date_time_str, from_datetime_str, to_datetime_str = \
            self._get_datetime_based_on_flexible_timings(base_ride_dto)
        ride_request_dict = {
            "ride_request_id": base_ride_dto.ride_request_id,
            "source": base_ride_dto.source,
            "destination": base_ride_dto.destination,
            "travel_date_time": travel_date_time_str,
            "flexible_timings": base_ride_dto.flexible_timings,
            "flexible_from_date_time": from_datetime_str,
            "flexible_to_date_time": to_datetime_str,
            "seats": base_ride_dto.seats,
            "laguage_quantity": base_ride_dto.laguage_quantity,
        }
        return ride_request_dict


    def _get_list_of_asset_dict(self, asset_dtos: List[AssetMatchingDto]):
        list_of_asset_dict = []
        for asset_dto in asset_dtos:
            asset_dict = self._get_asset_dict(asset_dto)
            list_of_asset_dict.append(asset_dict)
        return list_of_asset_dict


    def _get_asset_dict(self, asset_dto: AssetMatchingDto):
        base_asset_dto = asset_dto.asset_dto
        asset_dict = self._get_base_asset_dict(base_asset_dto)
        asset_dict["ride_matching_id"] = asset_dto.ride_matching_id
        asset_dict["travel_matching_id"] = asset_dto.travel_matching_id
        asset_dict["username"] = asset_dto.username
        asset_dict["user_phone_number"] = asset_dto.user_phone_number
        return asset_dict


    def _get_base_asset_dict(self, base_asset_dto: BaseAssetRequestDto):
        travel_date_time_str, from_datetime_str, to_datetime_str = \
            self._get_datetime_based_on_flexible_timings(base_asset_dto)
        base_asset_dict = {
            "asset_request_id": base_asset_dto.asset_request_id,
            "source": base_asset_dto.source,
            "destination": base_asset_dto.destination,
            "travel_date_time": travel_date_time_str,
            "flexible_timings": base_asset_dto.flexible_timings,
            "flexible_from_date_time": from_datetime_str,
            "flexible_to_date_time": to_datetime_str,
            "asset_quantity": base_asset_dto.asset_quantity,
            "asset_type": base_asset_dto.asset_type,
            "asset_type_others": base_asset_dto.asset_type_others,
            "asset_sensitivity": base_asset_dto.asset_sensitivity,
            "deliver_to": base_asset_dto.deliver_to,
            "phone_number": base_asset_dto.phone_number,
        }
        return base_asset_dict

    def _get_datetime_based_on_flexible_timings(
        self, base_dto: Union[BaseAssetRequestDto, BaseRideRequestDto]
    ) -> Tuple:
        travel_date_time_str = ""
        from_datetime_str = ""
        to_datetime_str = ""
        from_datetime_obj = base_dto.flexible_from_date_time
        to_datetime_obj = base_dto.flexible_to_date_time
        if base_dto.flexible_timings:
            from_datetime_str = self._get_datetime_in_string_format(
                from_datetime_obj
            )
            to_datetime_str = self._get_datetime_in_string_format(
                to_datetime_obj
            )
        else:
            travel_datetime_obj = base_dto.travel_date_time
            travel_date_time_str = self._get_datetime_in_string_format(
                travel_datetime_obj
             )
        return travel_date_time_str, from_datetime_str, to_datetime_str