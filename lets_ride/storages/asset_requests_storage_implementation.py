from typing import List
from datetime import datetime
from django.db.models import Case, Value, When, Q, CharField, F
from lets_ride.dtos.dtos import(
    AssetRequestsDto,
    AssetRequestDto,
    BaseAssetRequestDto
)
from lets_ride.models.asset_request import AssetRequest
from lets_ride.interactors.storages.asset_requests_storage_interface \
    import AssetRequestsStorageInterface


class AssetRequestsStorageImplementation(AssetRequestsStorageInterface):

    def get_asset_request_with_status_accepted(
        self, user_id: int, offset: int,
        limit: int, sort_key: str, sort_value: str
    ) -> AssetRequestsDto:

        limit = offset+limit
        filtered_asset_request_objs =  AssetRequest.objects.filter(
            user_id=user_id, accepted_by_id__isnull=False
        )
        asset_request_objs = self._get_ordered_asset_requests(
            sort_key, sort_value, filtered_asset_request_objs,
        )

        total_assets = len(asset_request_objs)
        asset_request_objs = asset_request_objs[offset:limit]
        asset_request_dtos = self._get_asset_request_dtos(asset_request_objs)
        asset_requests_dto = self._get_asset_requests_dto(
            asset_request_dtos, total_assets
        )
        return asset_requests_dto


    def get_asset_request_with_status_expired(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> AssetRequestsDto:

        limit = offset + limit
        filtered_asset_request_objs = AssetRequest.objects.filter(
            Q(
                flexible_timings=False,
                travel_date_time__lte=current_datetime_obj
            ) |
            Q(
                flexible_timings=True,
                flexible_to_date_time__lte=current_datetime_obj
            ),
            user_id=user_id
        )

        asset_request_objs = self._get_ordered_asset_requests(
            sort_key, sort_value, filtered_asset_request_objs,
        )
        total_assets = len(asset_request_objs)
        asset_request_objs = asset_request_objs[offset:limit]
        asset_request_dtos = self._get_asset_request_dtos(asset_request_objs)
        asset_requests_dto = self._get_asset_requests_dto(
            asset_request_dtos, total_assets
        )
        return asset_requests_dto


    def get_asset_request_with_status_pending(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> AssetRequestsDto:

        limit = offset+limit
        filtered_asset_request_objs = AssetRequest.objects.filter(
            Q(
                flexible_timings=False,
                travel_date_time__gt=current_datetime_obj
            ) |
            Q(
                flexible_timings=True,
                flexible_to_date_time__gt=current_datetime_obj
            ),
            user_id=user_id, accepted_by_id__isnull=True
        )
        asset_request_objs = self._get_ordered_asset_requests(
            sort_key, sort_value, filtered_asset_request_objs,
        )
        total_assets = len(asset_request_objs)
        asset_request_objs = asset_request_objs[offset:limit]
        asset_request_dtos = self._get_asset_request_dtos(asset_request_objs)
        asset_requests_dto = self._get_asset_requests_dto(
            asset_request_dtos, total_assets
        )
        return asset_requests_dto


    def get_asset_requests(
        self, user_id: int, offset: int, limit: int,
        sort_key: str, sort_value: str
    ) -> AssetRequestsDto:

        limit = offset+limit
        filtered_asset_request_objs = AssetRequest.objects.filter(
            user_id=user_id
        )
        asset_request_objs = self._get_ordered_asset_requests(
            sort_key, sort_value, filtered_asset_request_objs,
        )
        total_assets = len(asset_request_objs)
        asset_request_objs = asset_request_objs[offset:limit]
        asset_request_dtos = self._get_asset_request_dtos(asset_request_objs)
        asset_requests_dto = self._get_asset_requests_dto(
            asset_request_dtos, total_assets
        )
        return asset_requests_dto


    def _get_ordered_asset_requests(
        self,
        sort_key: str, sort_value: str,
        filtered_asset_request_objs: List[AssetRequest]
    ) -> List[AssetRequest]:

        if sort_key == "asset_quantity":
            asset_request_objs = filtered_asset_request_objs\
                .order_by(("-" if sort_value=="DESC" else "")+sort_key)
        else:
            asset_request_objs = filtered_asset_request_objs.annotate(
                date_time = Case(
                    When(
                        flexible_timings=True,
                        then=F("flexible_from_date_time")
                    ),
                    When(
                        flexible_timings=False,
                        then=F("travel_date_time")
                    ),
                    output_field=CharField()
                )
                ).order_by(("-" if sort_value=="DESC" else "")+"date_time")

        asset_request_objs = list(asset_request_objs)
        return asset_request_objs


    def _get_asset_request_dtos(
        self,
        asset_request_objs: AssetRequest,
    ) -> List[AssetRequestDto]:

        asset_request_dtos = []

        for asset_request_obj in asset_request_objs:
            base_asset_request_dto = self._get_base_asset_request_dto(
                asset_request_obj=asset_request_obj
            )
            asset_request_dto = self._get_asset_request_dto(
                asset_request_obj, base_asset_request_dto
            )
            asset_request_dtos.append(asset_request_dto)

        return asset_request_dtos


    def _get_base_asset_request_dto(
        self,
        asset_request_obj: AssetRequest,
    ) -> BaseAssetRequestDto:

        from_datetime_obj = ""
        to_datetime_obj = ""
        travel_datetime_obj = ""

        if asset_request_obj.flexible_timings:
            from_datetime_obj = asset_request_obj.flexible_from_date_time
            to_datetime_obj = asset_request_obj.flexible_to_date_time
        else:
            travel_datetime_obj = asset_request_obj.travel_date_time

        base_asset_request_dto = BaseAssetRequestDto(
                asset_request_id=asset_request_obj.id,
                source=asset_request_obj.source,
                destination=asset_request_obj.destination,
                travel_date_time=travel_datetime_obj,
                flexible_timings=asset_request_obj.flexible_timings,
                flexible_from_date_time= from_datetime_obj,
                flexible_to_date_time=to_datetime_obj,
                asset_quantity=asset_request_obj.asset_quantity,
                asset_type=asset_request_obj.asset_type,
                asset_type_others=asset_request_obj.asset_type_others,
                asset_sensitivity=asset_request_obj.asset_sensitivity,
                deliver_to=asset_request_obj.deliver_to,
                phone_number=asset_request_obj.phone_number
            )
        return base_asset_request_dto



    def _get_asset_request_dto(
        self,
        asset_request_obj: AssetRequest,
        base_asset_request_dto: BaseAssetRequestDto
    ) -> AssetRequestDto:

        accepted_person = ""
        accepted_person_phone_number = ""
        is_accepted_by = self._is_request_accepted(
                request_obj=asset_request_obj
        )
        if is_accepted_by:
            accepted_person = asset_request_obj.accepted_by.username
            accepted_person_phone_number = \
            asset_request_obj.accepted_by.phone_number

        asset_request_dto = AssetRequestDto(
            asset_dto=base_asset_request_dto,
            accepted_person=accepted_person,
            accepted_person_phone_number=accepted_person_phone_number,
            status=""
        )
        return asset_request_dto


    def _get_asset_requests_dto(
        self, asset_request_dtos: List[AssetRequestDto],
        total_assets: int
    ) -> AssetRequestsDto:

        asset_requests_dto = AssetRequestsDto(
            asset_dtos=asset_request_dtos,
            total_assets=total_assets
        )
        return asset_requests_dto


    def _is_request_accepted(
        self,
        request_obj: AssetRequest
    ) -> bool:
        accepted_by = request_obj.accepted_by
        if accepted_by:
            return True
        else:
            return False
