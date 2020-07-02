# pylint: disable=wrong-import-position

APP_NAME = "lets_ride_auth"
OPERATION_NAME = "sign_up"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_up/v1/"

from .test_case_01 import TestCase01SignUpAPITestCase
from .test_case_02 import TestCase02SignUpAPITestCase
from .test_case_03 import TestCase03SignUpAPITestCase

__all__ = [
    "TestCase01SignUpAPITestCase",
    "TestCase02SignUpAPITestCase",
    "TestCase03SignUpAPITestCase"
]
