# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "my_travel_shares"
REQUEST_METHOD = "get"
URL_SUFFIX = "travel_info_shares/v1/"

from .test_case_01 import TestCase01MyTravelSharesAPITestCase

__all__ = [
    "TestCase01MyTravelSharesAPITestCase"
]
