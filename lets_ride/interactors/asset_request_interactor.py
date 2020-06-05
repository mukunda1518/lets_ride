import datetime
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.utils.datetime_conversion \
    import convert_datetime_to_datetime_object

class AssertRequestInteractor:

    def __init__(
        self,
        storage: StorageInterface,
    ):
        self.storage = storage

    def asset_request_wrapper(
        self,
        user_id: int,
        source: str,
        destination: str,
        travel_date_time: str,
        flexible_timings: bool,
        flexible_travel_from_date_time: str,
        flexible_travel_to_date_time: str,
        asset_quantity: int,
        asset_type: str,
        asset_type_others: str,
        asset_sensitivity: str,
        deliver_to: str,
        phone_number: str
    ):
        if flexible_timings:
            from_datetime_obj = convert_datetime_to_datetime_object(
                flexible_travel_from_date_time
            )
            to_datetime_obj = convert_datetime_to_datetime_object(
                flexible_travel_to_date_time
            )
            self.storage.create_asset_request_with_flexible_timings(
                user_id=user_id,
                source=source,
                destination=destination,
                flexible_timings=flexible_timings,
                flexible_travel_from_date_time=from_datetime_obj,
                flexible_travel_to_date_time=to_datetime_obj,
                asset_type=asset_type,
                asset_quantity=asset_quantity,
                asset_type_others=asset_type_others,
                asset_sensitivity=asset_sensitivity,
                deliver_to=deliver_to,
                phone_number=phone_number
            )
        else:
            datetime_obj = convert_datetime_to_datetime_object(
                travel_date_time
            )
            self.storage.create_asset_request(
                user_id=user_id,
                source=source,
                destination=destination,
                travel_date_time=datetime_obj,
                flexible_timings=flexible_timings,
                asset_type=asset_type,
                asset_quantity=asset_quantity,
                asset_type_others=asset_type_others,
                asset_sensitivity=asset_sensitivity,
                deliver_to=deliver_to,
                phone_number=phone_number
            )
