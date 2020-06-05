import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.asset_requests_storage_implementation \
    import AssetRequestsStorageImplementation
from lets_ride.interactors.my_asset_requests_interactor \
    import MyAssetRequestsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = user_obj.id
    query_parameter_dict = kwargs['request_query_params'].__dict__
    offset = query_parameter_dict['offset']
    limit = query_parameter_dict['limit']
    status = query_parameter_dict['status']
    sort_key = query_parameter_dict['sort_key']
    sort_value = query_parameter_dict['sort_value']
    storage = AssetRequestsStorageImplementation()
    presenter = PresenterImplementation()
    interactor = MyAssetRequestsInteractor(
        storage=storage, presenter=presenter
    )

    my_ride_requests_dict = interactor.my_asset_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit, status=status,
        sort_key=sort_key, sort_value=sort_value
    )
    response_data = json.dumps(my_ride_requests_dict)
    return HttpResponse(response_data, status=200)

