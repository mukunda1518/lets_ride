from datetime import datetime
from abc import abstractmethod
from abc import ABC
from lets_ride.dtos.dtos import AssetRequestsDto


class AssetRequestsStorageInterface(ABC):

    @abstractmethod
    def get_asset_request_with_status_accepted(
        self, user_id: int, offset: int,
        limit: int, sort_key: str, sort_value: str
    ) -> AssetRequestsDto:
        pass

    @abstractmethod
    def get_asset_request_with_status_expired(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> AssetRequestsDto:
        pass

    @abstractmethod
    def get_asset_request_with_status_pending(
        self, user_id: int, offset: int, limit: int, sort_key: str,
        sort_value: str, current_datetime_obj: datetime
    ) -> AssetRequestsDto:
        pass

    @abstractmethod
    def get_asset_requests(
        self, user_id: int, offset: int, limit: int,
        sort_key: str, sort_value: str
    ) -> AssetRequestsDto:
        pass
