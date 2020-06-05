from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.interactors.asset_request_interactor \
    import AssertRequestInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    source = request_data['source']
    destination = request_data['destination']
    travel_date_time = request_data['travel_date_time']
    flexible_timings = request_data['flexible_timings']
    flexible_from_date_time = request_data['flexible_from_date_time']
    flexible_to_date_time = request_data['flexible_to_date_time']
    asset_quantity = request_data['asset_quantity']
    asset_type = request_data['asset_type']
    asset_type_others = request_data['asset_type_others']
    asset_sensitivity = request_data['asset_sensitivity']
    deliver_to = request_data['deliver_to']
    phone_number = request_data['phone_number']
    storage = StorageImplementation()
    interactor = AssertRequestInteractor(storage=storage)

    interactor.asset_request_wrapper(
        user_id=user_id,
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_from_date_time,
        flexible_travel_to_date_time=flexible_to_date_time,
        asset_quantity=asset_quantity,
        asset_type=asset_type,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        phone_number=phone_number,
    )
    return HttpResponse(status=201)
