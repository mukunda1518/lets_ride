import datetime
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.utils.datetime_conversion \
    import convert_datetime_to_datetime_object

class ShareTravelInfoInteractor:

    def __init__(
        self,
        storage: StorageInterface
    ):
        self.storage = storage

    def share_travel_info_wrapper(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: str,
        flexible_travel_to_date_time: str,
        travel_medium: str,
        asset_quantity: int
    ):
        if flexible_timings:
            from_datetime_obj = convert_datetime_to_datetime_object(
                flexible_travel_from_date_time
            )
            to_datetime_obj = convert_datetime_to_datetime_object(
                flexible_travel_to_date_time
            )
            self.storage.create_share_travel_info_with_flexible_timings(
                user_id=user_id,
                source=source,
                destination=destination,
                flexible_timings=flexible_timings,
                flexible_travel_from_date_time=from_datetime_obj,
                flexible_travel_to_date_time=to_datetime_obj,
                travel_medium=travel_medium,
                asset_quantity=asset_quantity
            )
        else:
            datetime_obj = convert_datetime_to_datetime_object(
                travel_date_time
            )
            self.storage.create_share_travel_info(
                user_id=user_id,
                source=source,
                destination=destination,
                travel_date_time=datetime_obj,
                flexible_timings=flexible_timings,
                travel_medium=travel_medium,
                asset_quantity=asset_quantity
            )