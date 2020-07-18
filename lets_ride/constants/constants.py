from datetime import datetime

from lets_ride.constants.enums \
    import AssetType, AssetSensitivity, TravelMedium, Status
#'%Y-%m-%d %H:%M'
DEFAULT_DATE_TIME_FORMAT = '%Y-%m-%d %I:%M %p'


ASSETTYPE = [(item.value, item.value) for item in AssetType]


TRAVEL_MEDIUM = [(item.value, item.value) for item in TravelMedium]
ASSET_SENSITIVITY = [(item.value, item.value) for item in AssetSensitivity]
STATUS = [(item.value, item.value) for item in Status]
FILTER_OPTIONS = [
    Status.ACCEPTED.value,
    Status.PENDING.value,
    Status.EXPIRED.value
]
RIDE_SORT_OPTIONS = ["seats", "date_time"]
ASSET_SORT_OPTIONS = ["asset_quantity", "date_time"]

USER_LIST = [
    {
        "username": "user1",
        "password": "user1",
        "phone_number": "1234567890"
    },
    {
        "username": "user2",
        "password": "user2",
        "phone_number": "1234567891"
    },
    {
        "username": "user3",
        "password": "user3",
        "phone_number": "1234567892"
    },
    {
        "username": "user4",
        "password": "user4",
        "phone_number": "1234567893"
    }
]
