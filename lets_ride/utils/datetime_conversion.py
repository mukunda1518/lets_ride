from datetime import datetime
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT

def convert_datetime_to_datetime_object(datetime_str):
    datetime_obj = datetime.strptime(
        datetime_str, DEFAULT_DATE_TIME_FORMAT
    )
    return datetime_obj

def convert_datetime_object_to_string_format(datetime_obj):
    datetime_str =datetime_obj.strftime(DEFAULT_DATE_TIME_FORMAT)
    return datetime_str