from unittest.mock import create_autospec

import pytest

from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from freezegun import freeze_time

from reporting_portal.exceptions.exceptions import (
    InvalidMealId
)
from reporting_portal.interactors.storages.storage_interface \
    import StorageInterface
from reporting_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from reporting_portal.interactors.set_meal_preference_interactor \
    import SetMealPreferenceInteractor
from reporting_portal.dtos.dtos import (
    MealDto,
    ItemDto
)
from reporting_portal.exceptions.exceptions import (
    InvalidMealId,
    DuplicationOfItems
)


def test_raise_invalid_meal_id_exception(meal_details_dto):
    # Arrange
    meal_id = meal_details_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SetMealPreferenceInteractor(storage=storage)
    invalid_meal_id_obj = InvalidMealId(meal_id=meal_id)
    storage.validate_meal_id_if_valid_returns_meal_dto.side_effect = \
        invalid_meal_id_obj
    presenter.raise_invalid_meal_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.set_meal_preference_wrapper(
            presenter=presenter, meal_details_dto=meal_details_dto
        )

    # Assert
    storage.validate_meal_id_if_valid_returns_meal_dto.\
        assert_called_once_with(meal_id=meal_id)
    presenter.raise_invalid_meal_id_exception.assert_called_once_with(
        invalid_meal_id_obj
    )


@freeze_time("2020-06-15 03:50")
def test_with_expire_datetime_riase_timeout_exception(
    meal_dto_with_expired_date, meal_details_dto
):
    # Arrange
    meal_id = meal_details_dto.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SetMealPreferenceInteractor(storage=storage)
    storage.validate_meal_id_if_valid_returns_meal_dto.return_value = \
        meal_dto_with_expired_date
    presenter.raise_timeout_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.set_meal_preference_wrapper(
            presenter=presenter, meal_details_dto=meal_details_dto
        )

    # Assert
    storage.validate_meal_id_if_valid_returns_meal_dto.\
        assert_called_once_with(meal_id=meal_id)
    presenter.raise_timeout_exception.assert_called_once()


@freeze_time("2020-01-15 03:50")
def test_set_meal_preference_wrapper_with_duplicate_items_raise_exception(
    meal_dto, meal_details_dto_with_duplicate_items
):
    # Arrange
    meal_id = meal_details_dto_with_duplicate_items.meal_id
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = SetMealPreferenceInteractor(storage=storage)
    duplication_item_ids_list = [3,2]
    storage.validate_meal_id_if_valid_returns_meal_dto.return_value = \
        meal_dto
    presenter.raise_duplication_of_items_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.set_meal_preference_wrapper(
            presenter=presenter,
            meal_details_dto=meal_details_dto_with_duplicate_items
        )

    # Assert
    storage.validate_meal_id_if_valid_returns_meal_dto.\
        assert_called_once_with(meal_id=meal_id)
    presenter.raise_duplication_of_items_exception.assert_called_once()
    call_tuple = presenter.raise_duplication_of_items_exception.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.duplication_item_ids_list == duplication_item_ids_list


