"""
# TODO: Update test case description
"""

import json

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from lets_ride_auth.utils.custom_test_utils import CustomTestUtils

REQUEST_BODY = """
{
    "username": "username1",
    "phone_number": "9231392457",
    "password": "username123"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write", "read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02SignUpAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(username=username, password=password)
        user_obj = self.foo_user
        user_obj.phone_number = "9231392457"
        user_obj.save()
        print("user_name = ",user_obj.username)
        print("password = ",user_obj.password)
        print("phone_number = ",user_obj.phone_number)


    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.