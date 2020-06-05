# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "my_asset_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "my_requests/assets/v1/"

from .test_case_01 import TestCase01MyAssetRequestsAPITestCase

__all__ = [
    "TestCase01MyAssetRequestsAPITestCase"
]
