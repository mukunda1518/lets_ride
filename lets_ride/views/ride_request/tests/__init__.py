# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "ride_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "ride_request/v1/"

from .test_case_01 import TestCase01RideRequestAPITestCase

__all__ = [
    "TestCase01RideRequestAPITestCase"
]
