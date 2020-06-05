# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "matching_results"
REQUEST_METHOD = "get"
URL_SUFFIX = "matching_results/v1/"

from .test_case_01 import TestCase01MatchingResultsAPITestCase

__all__ = [
    "TestCase01MatchingResultsAPITestCase"
]
