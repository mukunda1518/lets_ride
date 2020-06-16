from typing import List

class InvalidMealId(Exception):

    def __init__(self, meal_id: int):
        self.meal_id = meal_id

class InvalidItemId(Exception):
    pass

class TimeOutException(Exception):
    pass

class DuplicationOfItems(Exception):
    def __init__(self, duplication_item_ids_list: List[int]):
        self.duplication_item_ids_list = duplication_item_ids_list
