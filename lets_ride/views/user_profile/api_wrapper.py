import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.user_storage_implementation \
    import UserStorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.user_profile_interactor \
    import UserProfileInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter,
    )
    user_dict = interactor.user_profile_wrapper(user_id=user_id)
    response_data = json.dumps(user_dict)
    return HttpResponse(response_data, status=200)
