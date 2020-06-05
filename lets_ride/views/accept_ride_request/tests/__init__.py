# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "accept_ride_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "accept_ride_request/v1/"

from .test_case_01 import TestCase01AcceptRideRequestAPITestCase

__all__ = [
    "TestCase01AcceptRideRequestAPITestCase"
]
