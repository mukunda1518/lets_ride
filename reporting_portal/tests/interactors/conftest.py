import pytest
import datetime
from reporting_portal.dtos.dtos import (
    MealDetailsDto,
    ItemDto,
    MealDto
)
from reporting_portal.constants.enums import MealType

@pytest.fixture
def item_dtos():
    item_dtos = [
        ItemDto(item_id=1, item_quantity=3),
        ItemDto(item_id=2, item_quantity=4),
        ItemDto(item_id=3, item_quantity=5)
    ]
    return item_dtos


@pytest.fixture
def meal_details_dto(item_dtos):
    meal_details_dto = MealDetailsDto(
        meal_id=1,
        user_id=2,
        items=item_dtos
    )
    return meal_details_dto


@pytest.fixture
def item_dtos_with_duplications():
    item_dtos = [
        ItemDto(item_id=1, item_quantity=3),
        ItemDto(item_id=2, item_quantity=4),
        ItemDto(item_id=3, item_quantity=5),
        ItemDto(item_id=3, item_quantity=5),
        ItemDto(item_id=2, item_quantity=4)
    ]
    return item_dtos

@pytest.fixture
def meal_dto_with_expired_date(item_dtos):
    meal_dto = MealDto(
        meal_datetime=datetime.datetime(2020,5,6,7,30),
        meal_type=MealType.BREAKFAST.value,
        items=item_dtos
    )
    return meal_dto

@pytest.fixture
def meal_details_dto_with_duplicate_items(item_dtos_with_duplications):
    meal_dto = MealDetailsDto(
        meal_id=1,
        user_id=2,
        items=item_dtos_with_duplications
    )
    return meal_dto

@pytest.fixture
def meal_dto(item_dtos):
    meal_dto = MealDto(
        meal_datetime=datetime.datetime(2020,5,6,7,30),
        meal_type=MealType.BREAKFAST.value,
        items=item_dtos
    )
    return meal_dto