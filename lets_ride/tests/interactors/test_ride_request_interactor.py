import datetime
import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import BadRequest
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.ride_request_interactor \
    import RideRequestInteractor


def test_create_ride_request_wrapper_with_invalid_travel_datetime(
        create_ride_request_dto_invalid_travel_datetime
):
    # Arrange
    user_id =  1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)
    presenter.raise_invalid_datetime_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest) as e:
        interactor.create_ride_request_wrapper(
            user_id=user_id,
            ride_request_dto=create_ride_request_dto_invalid_travel_datetime,
            presenter=presenter
        )

    # Assert
    assert str(e.value) == ""



def test_create_ride_request_wrapper_with_invalid_from_datetime(
        create_ride_request_dto_with_invalid_from_datetime
):
    # Arrange
    user_id =  1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)
    presenter.raise_invalid_datetime_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest) as e:
        interactor.create_ride_request_wrapper(
            user_id=user_id,
            ride_request_dto=create_ride_request_dto_with_invalid_from_datetime,
            presenter=presenter
        )

    # Assert
    assert str(e.value) == ""


def test_create_ride_request_wrapper_with_negative_no_of_seats(
        create_ride_request_wrapper_with_negative_no_of_seats
):
    # Arrange
    user_id =  1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)
    
    presenter.raise_invalid_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest) as e:
        interactor.create_ride_request_wrapper(
            user_id=user_id,
            ride_request_dto=create_ride_request_wrapper_with_negative_no_of_seats,
            presenter=presenter
        )

    # Assert
    assert str(e.value) == ""


def test_create_ride_request_wrapper_with_negative_value_for_laguage_quantity(
        create_ride_request_wrapper_with_negative_values_for_laguage_quantity
):
    # Arrange
    user_id =  1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)
    
    presenter.raise_invalid_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest) as e:
        interactor.create_ride_request_wrapper(
            user_id=user_id,
            ride_request_dto=create_ride_request_wrapper_with_negative_values_for_laguage_quantity,
            presenter=presenter
        )

    # Assert
    assert str(e.value) == ""


def test_create_ride_request_wrapper_with_invalid_to_datetime(
        create_ride_request_dto_with_invalid_to_datetime
):
    # Arrange
    user_id =  1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)
    presenter.raise_invalid_datetime_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest) as e:
        interactor.create_ride_request_wrapper(
            user_id=user_id,
            ride_request_dto=create_ride_request_dto_with_invalid_to_datetime,
            presenter=presenter
        )

    # Assert
    assert str(e.value) == ""


def test_create_ride_request_wrapper_when_flexible_timings_sets_to_false(
        create_ride_request_dto_without_flexible_timings
):
    # Arrange
    user_id =  1
    datetime_obj = datetime.datetime(2023,4,12,17,30)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)

    # Act
    interactor.create_ride_request_wrapper(
        user_id=user_id,
        ride_request_dto=create_ride_request_dto_without_flexible_timings,
        presenter=presenter
    )

    # Assert
    storage.create_ride_request.assert_called_once_with(
        user_id=user_id,
        source=create_ride_request_dto_without_flexible_timings.source,
        destination=create_ride_request_dto_without_flexible_timings.destination,
        travel_date_time=datetime_obj,
        flexible_timings=create_ride_request_dto_without_flexible_timings.flexible_timings,
        seats=create_ride_request_dto_without_flexible_timings.seats,
        laguage_quantity=create_ride_request_dto_without_flexible_timings.laguage_quantity
    )

def test_create_ride_request_wrapper_with_flexible_timings_sets_to_true(
        create_ride_request_dto_with_flexible_timings
):
    # Arrange
    user_id =  1
    from_datetime_obj = datetime.datetime(2023, 4, 12, 17, 30)
    to_datetime_obj = datetime.datetime(2023, 5, 12, 5, 30)

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(storage=storage)

    # Act
    interactor.create_ride_request_wrapper(
        user_id=user_id,
        ride_request_dto=create_ride_request_dto_with_flexible_timings,
        presenter=presenter
    )

    # Assert
    storage.create_ride_request_with_flexible_timings.assert_called_once_with(
        user_id=user_id,
        source=create_ride_request_dto_with_flexible_timings.source,
        destination=create_ride_request_dto_with_flexible_timings.destination,
        flexible_timings=create_ride_request_dto_with_flexible_timings.flexible_timings,
        flexible_travel_from_date_time=from_datetime_obj,
        flexible_travel_to_date_time=to_datetime_obj,
        seats=create_ride_request_dto_with_flexible_timings.seats,
        laguage_quantity=create_ride_request_dto_with_flexible_timings.laguage_quantity
    )

