# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "ride_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "ride_request/v1/"

from .test_case_01 import TestCase01RideRequestAPITestCase
from .test_case_02 import TestCase02RideRequestAPITestCase
from .test_case_03 import TestCase03RideRequestAPITestCase
from .test_case_04 import TestCase04RideRequestAPITestCase
from .test_case_05 import TestCase05RideRequestAPITestCase
from .test_case_06 import TestCase06RideRequestAPITestCase
from .test_case_07 import TestCase07RideRequestAPITestCase

__all__ = [
    "TestCase01RideRequestAPITestCase",
    "TestCase02RideRequestAPITestCase",
    "TestCase03RideRequestAPITestCase",
    "TestCase04RideRequestAPITestCase",
    "TestCase05RideRequestAPITestCase",
    "TestCase06RideRequestAPITestCase",
    "TestCase07RideRequestAPITestCase"
]
