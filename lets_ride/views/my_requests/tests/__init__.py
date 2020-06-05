# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "my_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "my_requests/v1/"

from .test_case_01 import TestCase01MyRequestsAPITestCase

__all__ = [
    "TestCase01MyRequestsAPITestCase"
]
