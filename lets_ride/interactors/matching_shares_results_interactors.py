from datetime import datetime
from datetime import timedelta
from typing import Tuple, Union, List
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT
from lets_ride.interactors.storages.matching_shares_results_storage_interface \
    import MatchingSharesStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface

from lets_ride.dtos.dtos import (
    BaseRideShareDto,
    BaseTravelInfoDto,
    RideAssetMatchingDto,
    RideMatchingDto,
    AssetMatchingDto
)

class MatchingSharesResultsInteractor:

    def __init__(
        self,
        storage: MatchingSharesStorageInterface,
        presenter: PresenterInterface
    ):
        self.storage = storage
        self.presenter = presenter


    def matching_share_results_wrapper(
        self, user_id: int, offset: int, limit: int
    ):
        if limit < 0 or offset < 0:
            self.presenter.raise_invalid_for_limit_and_offset()
            return
        limit = offset + limit
        ride_share_dtos = self.storage.get_ride_shares(user_id=user_id)
        travel_info_dtos = self.storage.get_travel_shares(user_id=user_id)

        ride_matching_dtos = self._get_all_ride_matching_dtos(ride_share_dtos)
        total_matching_rides = len(ride_matching_dtos)
        ride_matching_dtos = ride_matching_dtos[offset:limit]

        asset_matching_for_ride_share_dtos = \
            self._get_all_asset_request_matching_dtos(ride_share_dtos)

        asset_request_matching_dtos = \
            self._get_all_asset_request_matching_dtos(travel_info_dtos)

        asset_request_matching_dtos += asset_matching_for_ride_share_dtos
        total_matching_asset_request = len(asset_request_matching_dtos)
        asset_request_matching_dtos = asset_request_matching_dtos[offset:limit]

        ride_asset_matching_dto = RideAssetMatchingDto(
            ride_dtos=ride_matching_dtos,
            total_rides=total_matching_rides,
            asset_dtos=asset_request_matching_dtos,
            total_assets=total_matching_asset_request
        )
        response = self.presenter.get_ride_asset_matching_response(
            ride_asset_matching_dto=ride_asset_matching_dto
        )
        return response


    def _get_all_ride_matching_dtos(
        self,
        ride_share_dtos: List[BaseRideShareDto]
    ) -> List[RideMatchingDto]:

        all_ride_matching_dtos = []
        for ride_share_dto in ride_share_dtos:
            ride_matching_dtos = self._get_ride_matching_dtos(ride_share_dto)
            all_ride_matching_dtos += ride_matching_dtos
        return all_ride_matching_dtos


    def _get_ride_matching_dtos(
        self,
        ride_share_dto:BaseRideShareDto
    ) -> List[RideMatchingDto]:

        source = ride_share_dto.source
        destination = ride_share_dto.destination
        seats = ride_share_dto.seats
        asset_quantity = ride_share_dto.asset_quantity
        ride_share_id = ride_share_dto.ride_share_id
        from_datetime, to_datetime = \
            self._get_from_and_to_datetime(ride_share_dto)
        ride_matching_dtos = self.storage.get_ride_matching_requests(
            source, destination,
            seats, asset_quantity,
            from_datetime, to_datetime,
        )
        for ride_matching_dto in ride_matching_dtos:
            ride_matching_dto.ride_matching_id = ride_share_id
        return ride_matching_dtos


    def _get_all_asset_request_matching_dtos(
        self,
        base_info_dtos: Union[List[BaseTravelInfoDto], List[BaseRideShareDto]]
    ) ->List[AssetMatchingDto]:

        all_asset_matching_dtos = []
        for base_info_dto in base_info_dtos:
            asset_matching_dtos = \
                self._get_asset_matching_dtos(base_info_dto)
            all_asset_matching_dtos += asset_matching_dtos
        return all_asset_matching_dtos


    def _get_asset_matching_dtos(
        self,
        base_info_dto: Union[BaseTravelInfoDto, BaseRideShareDto]
    ) -> List[AssetMatchingDto]:

        source = base_info_dto.source
        destination = base_info_dto.destination
        asset_quantity = base_info_dto.asset_quantity
        from_datetime, to_datetime = \
            self._get_from_and_to_datetime(base_info_dto)
        asset_matching_dtos = self.storage.get_travel_matching_requests(
            source, destination,
            asset_quantity,
            from_datetime,
            to_datetime
        )
        if isinstance(base_info_dto, BaseRideShareDto):
            ride_matching_id = base_info_dto.ride_share_id
            for asset_matching_dto in asset_matching_dtos:
                asset_matching_dto.ride_matching_id = ride_matching_id
        else:
            travel_matching_id = base_info_dto.travel_share_id
            for asset_matching_dto in asset_matching_dtos:
                asset_matching_dto.travel_matching_id = travel_matching_id
        return asset_matching_dtos


    def _get_from_and_to_datetime(
        self,
        share_obj: Union[BaseRideShareDto,
        BaseTravelInfoDto]
    ) -> Tuple:

        flexible_timings = share_obj.flexible_timings
        if flexible_timings:
            from_datetime = \
                share_obj.flexible_from_date_time - timedelta(days=1)
            to_datetime = share_obj.flexible_to_date_time + timedelta(days=1)
        else:
            from_datetime = share_obj.travel_date_time
            to_datetime = share_obj.travel_date_time + timedelta(days=1)
        return from_datetime,to_datetime
