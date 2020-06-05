from datetime import datetime
from typing import List
from lets_ride.interactors.storages.asset_requests_storage_interface \
    import AssetRequestsStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.constants.enums import Status
from lets_ride.dtos.dtos import (
    AssetRequestDto
)


class MyAssetRequestsInteractor:

    def __init__(
        self,
        storage: AssetRequestsStorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter


    def my_asset_requests_wrapper(
        self,
        user_id: int,
        status: str,
        sort_key: str,
        sort_value: str,
        offset: int,
        limit: int
    ):
        if limit < 0 or offset < 0:
            self.presenter.raise_invalid_for_limit_and_offset()
            return
        current_datetime_obj = datetime.now()
        if status == Status.ACCEPTED.value:
            asset_requests_dto = self.storage.get_asset_request_with_status_accepted(
                user_id, offset, limit, sort_key, sort_value
            )
        elif status == Status.EXPIRED.value:
            asset_requests_dto = self.storage.get_asset_request_with_status_expired(
                user_id, offset, limit, sort_key,
                sort_value, current_datetime_obj
            )
        elif status == Status.PENDING.value:
            asset_requests_dto = self.storage.get_asset_request_with_status_pending(
                user_id, offset, limit, sort_key,
                sort_value, current_datetime_obj
            )
        else:
            asset_requests_dto = self.storage.get_asset_requests(
                user_id, offset, limit, sort_key, sort_value
            )
        asset_dtos = asset_requests_dto.asset_dtos
        self._set_status_for_asset_requests(asset_dtos)
        response = self.presenter.get_asset_requests_response(
            asset_requests_dto=asset_requests_dto
        )
        return response


    def _set_status_for_asset_requests(
        self,
        asset_dtos: List[AssetRequestDto]
    ):
        for asset_dto in asset_dtos:
            asset_status = self._get_asset_request_status(asset_dto)
            asset_dto.status = asset_status


    def _get_asset_request_status(
        self,
        asset_dto: AssetRequestDto
    ) -> str:

        current_datetime_obj = datetime.now()
        flexible_timings = asset_dto.asset_dto.flexible_timings
        is_accepted = asset_dto.accepted_person
        if flexible_timings:
            request_datetime_obj = \
                asset_dto.asset_dto.flexible_to_date_time
        else:
            request_datetime_obj = \
                asset_dto.asset_dto.travel_date_time

        if request_datetime_obj < current_datetime_obj:
            status = Status.EXPIRED.value
        elif is_accepted:
            status = Status.ACCEPTED.value
        else:
            status = Status.PENDING.value
        return status


