from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from lets_ride.storages.accept_asset_request_storage_implementation \
    import AcceptAssetRequestStorageImplementation
from lets_ride.interactors.accept_asset_request_interactor \
    import AcceptAssetRequestInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    asset_request_id = request_data['asset_request_id']
    ride_matching_id = request_data['ride_matching_id']
    travel_matching_id = request_data['travel_matching_id']
    print("asset_request_id = ", asset_request_id)
    print("ride_matching_id = ", ride_matching_id)
    print("travel_matching_id = ", travel_matching_id)
    storage = AcceptAssetRequestStorageImplementation()
    interactor = AcceptAssetRequestInteractor(storage=storage)
    interactor.accept_asset_request_wrapper(
        user_id=user_id,
        asset_request_id=asset_request_id,
        ride_matching_id=ride_matching_id,
        travel_matching_id=travel_matching_id
    )
    return HttpResponse(status=200)

