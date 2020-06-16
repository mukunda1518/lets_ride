import enum
from enum import Enum
from ib_common.constants import BaseEnumClass


class ROLE(BaseEnumClass, enum.Enum):
    USER = 'USER'
    RP = 'RP'
    ADMIN = 'ADMIN'

class SEVERITY(BaseEnumClass, enum.Enum):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

class STATUS(BaseEnumClass, enum.Enum):
    RESOLVED = 'RESOLVED'
    CLOSED = 'CLOSED'
    REPORTED = 'REPORTED'
    ACTION_IN_PROGRESS = 'ACTION_IN_PROGRESS'


class TimeOut(Enum):
    BREAKFAST_TIMMINGS = '07:30:50'
    LUNCH_TIMMINGS = '11:30:10'
    DINNER_TIMMINGS = '18:30:30'

class MealType(Enum):
    BREAKFAST = 'BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
