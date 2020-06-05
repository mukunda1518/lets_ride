# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "asset_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "asset_request/v1/"

from .test_case_01 import TestCase01AssetRequestAPITestCase

__all__ = [
    "TestCase01AssetRequestAPITestCase"
]
