# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "share_ride"
REQUEST_METHOD = "post"
URL_SUFFIX = "share_ride/v1/"

from .test_case_01 import TestCase01ShareRideAPITestCase

__all__ = [
    "TestCase01ShareRideAPITestCase"
]
