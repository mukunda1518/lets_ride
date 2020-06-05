# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "accept_asset_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "accept_asset_request/v1/"

from .test_case_01 import TestCase01AcceptAssetRequestAPITestCase

__all__ = [
    "TestCase01AcceptAssetRequestAPITestCase"
]
