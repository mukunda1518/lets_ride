from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo
from lets_ride.models.asset_request import AssetRequest
from lets_ride.interactors.storages.accept_asset_request_storage_interface \
    import AcceptAssetRequestStorageInterface


class AcceptAssetRequestStorageImplementation(
    AcceptAssetRequestStorageInterface
):

    def update_asset_request_status_with_ride_matching_deatails(
        self, user_id: int, asset_request_id: int, ride_matching_id: int
    ):
        asset_request_asset_quantity = self._update_status_and_return_asset_quantity(
            user_id, asset_request_id
        )

        ride_matching_obj = ShareRide.objects.get(id=ride_matching_id)
        ride_share_asset_quantity = ride_matching_obj.asset_quantity
        update_ride_share_asset_quantity = \
            ride_share_asset_quantity - asset_request_asset_quantity

        ride_matching_obj.asset_quantity = update_ride_share_asset_quantity
        ride_matching_obj.save()


    def update_asset_request_status_with_travel_matching_deatails(
        self, user_id: int, asset_request_id: int, travel_matching_id: int
    ):
        asset_request_asset_quantity = self._update_status_and_return_asset_quantity(
            user_id, asset_request_id
        )

        travel_matching_obj = TravelInfo.objects.get(id=travel_matching_id)
        travel_asset_quantity = travel_matching_obj.asset_quantity
        update_travel_asset_quantity = \
            travel_asset_quantity - asset_request_asset_quantity

        travel_matching_obj.asset_quantity = update_travel_asset_quantity
        travel_matching_obj.save()


    def _update_status_and_return_asset_quantity(
        self, user_id: int, asset_request_id: int
    ):
        asset_request_obj = AssetRequest.objects.get(id=asset_request_id)
        asset_request_obj.accepted_by_id = user_id
        asset_request_asset_quantity = asset_request_obj.asset_quantity
        asset_request_obj.save()
        return asset_request_asset_quantity
