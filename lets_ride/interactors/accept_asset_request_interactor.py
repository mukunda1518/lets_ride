from lets_ride.interactors.storages.accept_asset_request_storage_interface \
    import AcceptAssetRequestStorageInterface

class AcceptAssetRequestInteractor:

    def __init__(
        self,
        storage: AcceptAssetRequestStorageInterface
    ):
        self.storage = storage

    def accept_asset_request_wrapper(
        self, user_id: int, asset_request_id: int,
        ride_matching_id: int, travel_matching_id: int
    ):
        if ride_matching_id:
            self.storage.update_asset_request_status_with_ride_matching_deatails(
                user_id, asset_request_id, ride_matching_id
            )
        else:
            self.storage.update_asset_request_status_with_travel_matching_deatails(
                user_id, asset_request_id, travel_matching_id
            )
