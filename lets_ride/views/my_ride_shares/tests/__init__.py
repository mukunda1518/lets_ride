# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "my_ride_shares"
REQUEST_METHOD = "get"
URL_SUFFIX = "ride_shares/v1/"

from .test_case_01 import TestCase01MyRideSharesAPITestCase

__all__ = [
    "TestCase01MyRideSharesAPITestCase"
]
