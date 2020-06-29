"""
# TODO: Update test case description
"""

from datetime import datetime

from unittest.mock import patch

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from lets_ride.utils.custom_test_utils import CustomTestUtils
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


REQUEST_BODY = """
{
    "phone_number": "9231392458",
    "password": "password"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        #"securities": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write", "read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


TOKEN_DTO = UserAuthTokensDTO(
        user_id=2,
        access_token="JBSJBNKJFGHJKNLKJMLTYT",
        refresh_token="DKBKVJBKJVTRTYDTYDYTFH",
        expires_in=datetime(2020,8,9,6,20,13)
    )


class TestCase03LoginAPITestCase(CustomTestUtils):
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


    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens', return_value=TOKEN_DTO)
    def test_case(self, create_user_auth_tokens):
        self.default_test_case()
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.