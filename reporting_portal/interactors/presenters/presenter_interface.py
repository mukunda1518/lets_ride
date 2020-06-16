from abc import abstractmethod, ABC
from reporting_portal.exceptions.exceptions import (
    InvalidMealId,
    DuplicationOfItems
)

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_meal_id_exception(self, err: InvalidMealId):
        pass

    @abstractmethod
    def raise_timeout_exception(self):
        pass

    @abstractmethod
    def raise_duplication_of_items_exception(self, err: DuplicationOfItems):
        pass