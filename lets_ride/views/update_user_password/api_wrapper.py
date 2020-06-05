from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.user_storage_implementation \
    import UserStorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.update_user_password_interactor \
    import UpdateUserPasswordInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    new_password = request_data['new_password']

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateUserPasswordInteractor(
        storage=storage,
        presenter=presenter,
    )
    interactor.update_user_password_wrapper(
        user_id=user_id,
        new_password=new_password
    )
    return HttpResponse(status=200)
