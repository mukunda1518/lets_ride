from lets_ride.models.ride_request import RideRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.interactors.storages.accept_ride_request_storage_interface \
    import AcceptRideRequestStorageInterface


class AcceptRideRequestStorageImplementation(
    AcceptRideRequestStorageInterface
):

    def update_ride_request_status(
        self, user_id: int, ride_request_id: int, ride_matching_id: int
    ):
        ride_request_obj = RideRequest.objects.get(id=ride_request_id)
        ride_request_seats = ride_request_obj.seats
        ride_request_laguage_quantity = ride_request_obj.laguage_quantity
        ride_request_obj.accepted_by_id = user_id
        ride_request_obj.save()

        ride_share_obj = ShareRide.objects.get(id=ride_matching_id)
        ride_share_seats = ride_share_obj.seats
        ride_share_asset_quantity = ride_share_obj.asset_quantity
        ride_share_obj.seats = ride_share_seats - ride_request_seats
        ride_share_obj.asset_quantity = \
            ride_share_asset_quantity - ride_request_laguage_quantity
        ride_share_obj.save()