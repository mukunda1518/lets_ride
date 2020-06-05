# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "share_travel_info"
REQUEST_METHOD = "post"
URL_SUFFIX = "share_travel_info/v1/"

from .test_case_01 import TestCase01ShareTravelInfoAPITestCase

__all__ = [
    "TestCase01ShareTravelInfoAPITestCase"
]
