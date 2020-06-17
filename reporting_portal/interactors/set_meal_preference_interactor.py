from datetime import datetime
from datetime import timedelta
from typing import List, Union
from reporting_portal.interactors.storages.storage_interface\
    import StorageInterface
from reporting_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from reporting_portal.exceptions.exceptions import (
    InvalidMealId,
    InvalidItemId,
    TimeOutException,
    DuplicationOfItems
)
from reporting_portal.dtos.dtos import (
    MealDetailsDto,
    MealDto,
    ItemDto
)


class SetMealPreferenceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def set_meal_preference_wrapper(
            self,
            presenter: PresenterInterface,
            meal_details_dto: MealDetailsDto
    ):
        try:
            self.set_meal_preference(meal_details_dto)
        except InvalidMealId as err:
            presenter.raise_invalid_meal_id_exception(err)
        except TimeOutException:
            presenter.raise_timeout_exception()
        except DuplicationOfItems as err:
            presenter.raise_duplication_of_items_exception(err)
        except InvalidItemId as err:
            presenter.raise_invalid_item_id_exception(err)



    def set_meal_preference(self, meal_details_dto: MealDetailsDto):
        meal_id = meal_details_dto.meal_id
        meal_dto = \
            self.storage.validate_meal_id_if_valid_returns_meal_dto(meal_id)

        meal_datetime = meal_dto.meal_datetime
        expire_meal_datetime = meal_datetime - timedelta(hours=2)
        current_datetime = datetime.now()
        if current_datetime > expire_meal_datetime:
            raise TimeOutException

        actual_items_ids_list = self._get_item_ids_list(meal_dto)
        item_ids_list = self._get_item_ids_list(meal_details_dto)
        duplication_item_ids_list = self._get_duplication_of_items_list(
            item_ids_list
        )
        if len(duplication_item_ids_list) != 0:
            raise DuplicationOfItems(duplication_item_ids_list)

        invalid_item_ids_list = self._validate_items(
            actual_items_ids_list, item_ids_list
        )
        if len(invalid_item_ids_list) != 0:
            raise InvalidItemId(invalid_item_ids_list)


    def _get_item_ids_list(
            self, meal_details_dto: Union[MealDetailsDto, MealDto]
    ):
        item_dtos = meal_details_dto.items
        item_ids_list = [
            item_dto.item_id
            for item_dto in item_dtos
        ]
        return item_ids_list

    def _get_item_quantity_list(self, meal_dto: MealDto):
        item_dtos = meal_dto.items
        item_quantity_list = [
            item_dto.item_quantity
            for item_dto in item_dtos
        ]
        return item_quantity_list


    def _get_duplication_of_items_list(
            self, items_ids_list: List[int]
    ) -> List[int]:

        duplication_of_item_list = []
        temp_item_list = []
        for item in items_ids_list:
            if item not in temp_item_list:
                temp_item_list.append(item)
            else:
                duplication_of_item_list.append(item)
        return duplication_of_item_list


    def _validate_items(
        self, actual_items_ids_list: List[int], item_ids_list: List[int]
    ) -> List[int]:
        invalid_item_ids_list = []
        for item in item_ids_list:
            if item not in actual_items_ids_list:
                invalid_item_ids_list.append(item)
        return invalid_item_ids_list

