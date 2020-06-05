# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "update_user_password"
REQUEST_METHOD = "put"
URL_SUFFIX = "update_password/v1/"

from .test_case_01 import TestCase01UpdateUserPasswordAPITestCase

__all__ = [
    "TestCase01UpdateUserPasswordAPITestCase"
]
