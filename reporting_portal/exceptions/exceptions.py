from typing import List

class InvalidMealId(Exception):

    def __init__(self, meal_id: int):
        self.meal_id = meal_id

class InvalidItemId(Exception):
    
    def __init__(self, invalid_item_ids_list: List[int]):
        self.invalid_item_ids_list = invalid_item_ids_list

class TimeOutException(Exception):
    pass

class DuplicationOfItems(Exception):
    def __init__(self, duplication_item_ids_list: List[int]):
        self.duplication_item_ids_list = duplication_item_ids_list
