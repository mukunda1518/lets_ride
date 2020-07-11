# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "my_ride_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "my_requests/rides/v1/"

from .test_case_01 import TestCase01MyRideRequestsAPITestCase
from .test_case_02 import TestCase02MyRideRequestsAPITestCase
from .test_case_03 import TestCase03MyRideRequestsAPITestCase
from .test_case_04 import TestCase04MyRideRequestsAPITestCase
from .test_case_05 import TestCase05MyRideRequestsAPITestCase
from .test_case_06 import TestCase06MyRideRequestsAPITestCase

__all__ = [
    "TestCase01MyRideRequestsAPITestCase",
    "TestCase02MyRideRequestsAPITestCase",
    "TestCase03MyRideRequestsAPITestCase",
    "TestCase04MyRideRequestsAPITestCase",
    "TestCase05MyRideRequestsAPITestCase",
    "TestCase06MyRideRequestsAPITestCase"
]
