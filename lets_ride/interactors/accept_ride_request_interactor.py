from lets_ride.interactors.storages.accept_ride_request_storage_interface \
    import AcceptRideRequestStorageInterface

class AcceptRideRequestInteractor:

    def __init__(
        self,
        storage: AcceptRideRequestStorageInterface
    ):
        self.storage = storage

    def accept_ride_request_wrapper(
        self, user_id: int, ride_request_id: int, ride_matching_id: int
    ):
        self.storage.update_ride_request_status(
            ride_request_id, ride_matching_id, user_id
        )
