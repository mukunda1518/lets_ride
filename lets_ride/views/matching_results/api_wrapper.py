import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.matching_shares_storage_implementation \
    import MatchingSharesStorageImplementation
from lets_ride.interactors.matching_shares_results_interactors \
    import MatchingSharesResultsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = user_obj.id
    query_parameter_dict = kwargs['request_query_params'].__dict__
    offset = query_parameter_dict['offset']
    limit = query_parameter_dict['limit']
    storage = MatchingSharesStorageImplementation()
    presenter = PresenterImplementation()
    interactor = MatchingSharesResultsInteractor(
        storage=storage, presenter=presenter
    )

    ride_asset_matchings_dict = interactor.matching_share_results_wrapper(
        user_id=user_id, offset=offset, limit=limit
    )
    response_data = json.dumps(ride_asset_matchings_dict)
    return HttpResponse(response_data, status=200)
