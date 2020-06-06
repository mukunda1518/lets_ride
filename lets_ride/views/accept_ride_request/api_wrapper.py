from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from lets_ride.storages.accept_ride_request_storage_implementaion \
    import AcceptRideRequestStorageImplementation
from lets_ride.interactors.accept_ride_request_interactor \
    import AcceptRideRequestInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    ride_request_id = request_data['ride_request_id']
    ride_matching_id = request_data['ride_matching_id']
    print("ride_request_id = ", ride_request_id)
    print("ride_matching_id = ", ride_matching_id)
    storage = AcceptRideRequestStorageImplementation()
    interactor = AcceptRideRequestInteractor(storage=storage)
    interactor.accept_ride_request_wrapper(
        user_id=user_id,
        ride_request_id=ride_request_id,
        ride_matching_id=ride_matching_id
    )
    return HttpResponse(status=200)