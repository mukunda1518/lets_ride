import enum
from ib_common.constants import BaseEnumClass

class AssetType(BaseEnumClass, enum.Enum):
    BAG = "BAG"
    LAPTOP = "LAPTOP"
    DOCUMENTS = "DOCUMENTS"
    OTHERS = "OTHERS"

class AssetSensitivity(BaseEnumClass, enum.Enum):
    LOW = "LOW"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"

class TravelMedium(BaseEnumClass, enum.Enum):
    BUS = "BUS"
    TRAIN = "TRAIN"
    FLIGHT = "FLIGHT"

class Status(BaseEnumClass, enum.Enum):
    ACCEPTED = "ACCEPTED"
    PENDING = "PENDING"
    EXPIRED = "EXPIRED"

class FilterByEnums(BaseEnumClass, enum.Enum):
    STATUS = "STATUS"

class SortByEnums(enum.Enum):
    SEATS = "SEATS"
    DATE_TIME = "TRAVEL_DATETIME"

class OrderByEnums(enum.Enum):
    ASC = "ASC"
    DESC = "DESC"
