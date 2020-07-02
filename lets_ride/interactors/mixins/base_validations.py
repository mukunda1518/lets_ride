from lets_ride.exceptions.exceptions import NegativeValue


class BaseValidationMixin:

    def is_negative_value(self, value: int):
        if value < 0:
            raise NegativeValue
