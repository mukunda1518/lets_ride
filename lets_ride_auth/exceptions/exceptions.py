from typing import List
import json

class InvaildUserName(Exception):
    pass

class InvalidPhoneNumber(Exception):
    pass

class InvalidPassword(Exception):
    pass

class UserNameAlreadyExist(Exception):
    pass

class PhoneNumberAlreadyExist(Exception):
    pass

class InvalidUserIds(Exception):

    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids

    def __str__(self):
        return json.dumps(self.user_ids)