# pylint: disable=wrong-import-position

APP_NAME = "lets_ride_auth"
OPERATION_NAME = "login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01LoginAPITestCase
from .test_case_02 import TestCase02LoginAPITestCase
from .test_case_03 import TestCase03LoginAPITestCase

__all__ = [
    "TestCase01LoginAPITestCase",
    "TestCase02LoginAPITestCase",
    "TestCase03LoginAPITestCase"
]
