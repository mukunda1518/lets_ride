import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from .validator_class import ValidatorClass
from lets_ride.storages.user_storage_implementation \
    import UserStorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.sign_in_interactor \
    import SignInInteractor
from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    phone_number = request_data['phone_number']
    password = request_data['password']
    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )
    auth_dict = interactor.login_wrapper(
        password=password,
        phone_number=phone_number
    )
    datetime = auth_dict['expires_in'].strftime("%Y-%m-%d, %H:%M:%S")
    auth_dict['expires_in'] = datetime
    response_data = json.dumps(auth_dict)
    return HttpResponse(response_data, status=200)
