import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.my_requests_interactor \
    import MyRequestsInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_parameter_dict = kwargs['request_query_params'].__dict__
    offset = query_parameter_dict['offset']
    limit = query_parameter_dict['limit']
    user_obj = kwargs["user"]
    user_id = user_obj.id
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = MyRequestsInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_asset_requests = interactor.my_requests_wrapper(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    response_data = json.dumps(ride_asset_requests)
    return HttpResponse(response_data, status=200)
