from abc import abstractmethod, ABC
from reporting_portal.dtos.dtos import MealDto

class StorageInterface(ABC):

    def validate_meal_id_if_valid_returns_meal_dto(
        self, meal_id: int
    ) -> MealDto:
        pass