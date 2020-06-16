from dataclasses import dataclass

from typing import List

from datetime import datetime


@dataclass
class ItemDto:
    item_id: int
    item_quantity: int


@dataclass
class MealDetailsDto:
    user_id: int
    meal_id: int
    items: List[ItemDto]


@dataclass
class MealDto:
    meal_datetime: datetime
    meal_type: str
    items: List[ItemDto]

