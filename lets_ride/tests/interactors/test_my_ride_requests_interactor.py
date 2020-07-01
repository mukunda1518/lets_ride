import pytest

from datetime import datetime

from unittest.mock import create_autospec, Mock, patch

from freezegun import freeze_time

from lets_ride.interactors.storages.ride_requests_storage_interface \
    import RideRequestsStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.my_ride_requests_interactor \
    import MyRideRequestsInteractor
from lets_ride.constants.enums import Status
from lets_ride.adapters.auth_service import AuthService
from lets_ride_auth.interface.service_interface import ServiceInterface

from lets_ride_auth.dtos.dtos import UserDto


@pytest.fixture
def auth_user_dtos():
    user_dtos = [
        UserDto(
            user_id=2,
            username="user2",
            phone_number="1234567890",
            profile_pic=""
        )
    ]
    return user_dtos


@patch.object(AuthService, 'get_user_dtos')
def test_my_ride_requests_wrapper_without_status(
    get_user_dtos_mock,
    ride_requests_dto,
    user_dtos,
    get_my_ride_requests_response
):
    # Arrange
    user_ids = [2]
    user_id = 1
    offset = 2
    limit = 1
    status = ""
    sort_key = "seats"
    sort_value = "ASC"
    get_user_dtos_mock.return_value = user_dtos
    storage = create_autospec(RideRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyRideRequestsInteractor(storage=storage, presenter=presenter)
    storage.get_ride_requests.return_value = \
        ride_requests_dto
    presenter.get_ride_requests_response.return_value = \
        get_my_ride_requests_response

    # Act
    response = interactor.my_ride_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_ride_requests.assert_called_once_with(
        user_id=user_id, offset=offset,
        limit=limit, sort_key="seats", sort_value="ASC"
    )
    presenter.get_ride_requests_response.assert_called_once_with(
        ride_requests_dto=ride_requests_dto,
        user_dtos=user_dtos
    )
    get_user_dtos_mock.assert_called_once_with(user_ids=user_ids)
    assert response == get_my_ride_requests_response


@patch.object(AuthService, 'service_interface')
def test_my_ride_requests_wrapper_with_status_accepted(
        get_user_dtos_mock,
        ride_requests_dto,
        auth_user_dtos,
        user_dtos,
        get_my_ride_requests_response
    ):
    # Arrange
    user_ids = [2]
    user_id = 1
    offset = 2
    limit = 1
    status = Status.ACCEPTED.value
    sort_key = "seats"
    sort_value = "ASC"
    print("object = ", get_user_dtos_mock)
    print("type = ", type(get_user_dtos_mock))
    get_user_dtos_mock.get_user_dtos.return_value = auth_user_dtos
    storage = create_autospec(RideRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyRideRequestsInteractor(storage=storage, presenter=presenter)
    storage.get_ride_request_with_status_accepted.return_value = \
        ride_requests_dto
    presenter.get_ride_requests_response.return_value = \
        get_my_ride_requests_response

    # Act
    response = interactor.my_ride_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_ride_request_with_status_accepted.assert_called_once_with(
        user_id=user_id, offset=offset,
        limit=limit, sort_key=sort_key, sort_value=sort_value
    )
    presenter.get_ride_requests_response.assert_called_once_with(
        ride_requests_dto=ride_requests_dto,
        user_dtos=user_dtos
    )
    get_user_dtos_mock.get_user_dtos.assert_called_once_with(user_ids=user_ids)
    assert get_my_ride_requests_response == response



@patch.object(ServiceInterface, 'get_user_dtos')
def test_my_ride_requests_wrapper_with_flexible_timings(
        get_user_dtos_mock,
        ride_requests_dto,
        auth_user_dtos,
        user_dtos,
        get_my_ride_requests_response
    ):
    # Arrange
    user_ids = [2]
    user_id = 1
    offset = 2
    limit = 1
    status = Status.ACCEPTED.value
    sort_key = "seats"
    sort_value = "ASC"
    get_user_dtos_mock.return_value = auth_user_dtos
    storage = create_autospec(RideRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyRideRequestsInteractor(storage=storage, presenter=presenter)
    storage.get_ride_request_with_status_accepted.return_value = \
        ride_requests_dto
    presenter.get_ride_requests_response.return_value = \
        get_my_ride_requests_response

    # Act
    response = interactor.my_ride_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_ride_request_with_status_accepted.assert_called_once_with(
        user_id=user_id, offset=offset,
        limit=limit, sort_key=sort_key, sort_value=sort_value
    )
    presenter.get_ride_requests_response.assert_called_once_with(
        ride_requests_dto=ride_requests_dto,
        user_dtos=user_dtos
    )
    get_user_dtos_mock.assert_called_once_with(user_ids=user_ids)
    assert get_my_ride_requests_response == response



@freeze_time("2020-09-18 8:50")
@patch.object(AuthService, 'get_user_dtos')
def test_my_ride_requests_wrapper_with_status_pending(
    get_user_dtos_mock,
    ride_requests_dto,
    user_dtos,
    get_my_ride_requests_response
):
    # Arrange
    user_id = 1
    offset = 2
    limit = 1
    status = Status.PENDING.value
    sort_key = "laguage_quantity"
    sort_value = "ASC"
    get_user_dtos_mock.return_value = user_dtos
    #current_datetime = Mock()
    current_datetime_obj = datetime.now()
    storage = create_autospec(RideRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyRideRequestsInteractor(storage=storage, presenter=presenter)
    storage.get_ride_request_with_status_pending.return_value = \
        ride_requests_dto
    presenter.get_ride_requests_response.return_value = \
        get_my_ride_requests_response

    # Act
    response = interactor.my_ride_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_ride_request_with_status_pending.assert_called_once_with(
        user_id=user_id, offset=offset,limit=limit,
        sort_key=sort_key, sort_value=sort_value,
        current_datetime_obj=current_datetime_obj
    )
    presenter.get_ride_requests_response.assert_called_once_with(
        ride_requests_dto=ride_requests_dto,
        user_dtos=user_dtos
    )
    assert get_my_ride_requests_response == response



# def test_my_ride_requests_wrapper_with_status_expired(
#     ride_requests_dto,
#     get_my_ride_requests_response
# ):
#     # Arrange
#     user_id = 1
#     offset = 2
#     limit = 1
#     status = Status.EXPIRED.value
#     sort_key = "laguage_quantity"
#     sort_value = "ASC"
#     #current_datetime = Mock()
#     #current_datetime_obj = datetime.now()
#     storage = create_autospec(RideRequestsStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = MyRideRequestsInteractor(storage=storage, presenter=presenter)
#     storage.get_ride_request_with_status_expired.return_value = \
#         ride_requests_dto
#     presenter.get_ride_requests_response.return_value = \
#         get_my_ride_requests_response

#     # Act
#     with patch(datetime,'datetime.datetime.now', return_value = datetime.datetime(2020,3,4,5,6,7,879)):
#         response = interactor.my_ride_requests_wrapper(
#             user_id=user_id, offset=offset, limit=limit,
#             status=status, sort_key=sort_key, sort_value=sort_value
#         )

#     # Assert
#     storage.get_ride_request_with_status_expired.assert_called_once_with(
#         user_id=user_id, offset=offset,limit=limit,
#         sort_key=sort_key, sort_value=sort_value,
#         current_datetime_obj=datetime.datetime(2020,3,4,5,6,7,879)
#     )
#     presenter.get_ride_requests_response.assert_called_once_with(
#         ride_requests_dto=ride_requests_dto
#     )
#     assert get_my_ride_requests_response == response
