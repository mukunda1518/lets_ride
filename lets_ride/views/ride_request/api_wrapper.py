from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.interactors.ride_request_interactor \
    import RideRequestInteractor
from lets_ride.dtos.dtos import RideRequestDTO

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs['user']
    user_id = user_obj.id
    request_data = kwargs['request_data']
    ride_request_dto = RideRequestDTO(
        source=request_data['source'],
        destination=request_data['destination'],
        travel_date_time=request_data['travel_date_time'],
        flexible_timings=request_data['flexible_timings'],
        flexible_from_date_time=request_data['flexible_from_date_time'],
        flexible_to_date_time=request_data['flexible_to_date_time'],
        seats=request_data['seats'],
        laguage_quantity=request_data['laguage_quantity']
    )
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = RideRequestInteractor(storage=storage)

    interactor.create_ride_request_wrapper(
        user_id=user_id,
        ride_request_dto=ride_request_dto,
        presenter=presenter
    )
    return HttpResponse(status=201)
