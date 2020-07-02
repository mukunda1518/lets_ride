from datetime import datetime

from lets_ride.exceptions.exceptions import InvalidDateTime

class DateTimeValidationMixin:

    def validate_datetime(self, datetime_obj: datetime):
        current_datetime_obj = datetime.now()

        if datetime_obj < current_datetime_obj:
            raise InvalidDateTime

