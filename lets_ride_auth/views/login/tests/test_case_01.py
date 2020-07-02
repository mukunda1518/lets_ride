"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from lets_ride_auth.utils.custom_test_utils import CustomTestUtils


REQUEST_BODY = """
{
    "phone_number": "9231392459",
    "password": "password"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01LoginAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(username=username, password=password)
        user_obj = self.foo_user
        user_obj.phone_number = "9231392458"
        user_obj.save()
        print("user_name = ",user_obj.username)
        print("password = ",user_obj.password)
        print("phone_number = ",user_obj.phone_number)


    def test_case(self):
        #self.setupUser(username="", password="")
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.