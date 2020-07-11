import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.ride_requests_storage_implementation \
    import RideRequestsStorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.my_ride_requests_interactor \
    import GetRideRequestsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = user_obj.id

    query_parameter_dict = kwargs['request_query_params'].__dict__
    offset = query_parameter_dict['offset']
    limit = query_parameter_dict['limit']
    filter_by = query_parameter_dict['filter_by']
    value = query_parameter_dict['filter_value']
    sort_by = query_parameter_dict['sort_by']
    order = query_parameter_dict['order']

    from interactor.dtos.dtos import SortByDTO, FilterByDTO, RideRequestMetricsDTO
    sort_by_dto = SortByDTO(sort_by=sort_by, order=order)
    filter_by_dto = FilterByDTO(filter_by=filter_by, value=value)
    ride_request_metrics_dto = RideRequestMetricsDTO(
        user_id=user_id, offset=offset, limit=limit,
        sort_by_dto=sort_by_dto, filter_by_dto=filter_by_dto
    )

    storage = RideRequestsStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetRideRequestsInteractor(
        storage=storage
    )
    my_ride_requests_dict = interactor.get_ride_requests_wrapper(
        ride_request_metrics_dto
    )
    response_data = json.dumps(my_ride_requests_dict)
    return HttpResponse(response_data, status=200)
