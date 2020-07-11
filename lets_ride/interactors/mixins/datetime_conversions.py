from datetime import datetime
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT

class DateTimeConversionsMixin:

    def convert_datetime_to_datetime_object(self, datetime_str: str):
        datetime_obj = datetime.strptime(
            datetime_str, DEFAULT_DATE_TIME_FORMAT
        )
        return datetime_obj

    def convert_datetime_object_to_string_format(
            self, datetime_obj: datetime
    ):
        datetime_str =datetime_obj.strftime(DEFAULT_DATE_TIME_FORMAT)
        return datetime_str