from abc import abstractmethod
from abc import ABC

class AcceptAssetRequestStorageInterface(ABC):

    @abstractmethod
    def update_asset_request_status_with_ride_matching_deatails(
        self, user_id: int, asset_request_id: int, ride_matching_id: int
    ):
        pass

    @abstractmethod
    def update_asset_request_status_with_travel_matching_deatails(
        self, user_id: int, asset_request_id: int, travel_matching_id: int
    ):
        pass
