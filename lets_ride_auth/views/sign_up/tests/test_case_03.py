"""
# TODO: Update test case description
"""


import json
from unittest.mock import patch

from datetime import datetime

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from lets_ride_auth.utils.custom_test_utils import CustomTestUtils
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from lets_ride_auth.models.user import User


REQUEST_BODY = """
{
    "username": "john",
    "phone_number": "9231392457",
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


TOKEN_DTO = UserAuthTokensDTO(
        user_id=2,
        access_token="JBSJBNKJFGHJKNLKJMLTYT",
        refresh_token="DKBKVJBKJVTRTYDTYDYTFH",
        expires_in=datetime(2020,8,9,6,20,13)
    )

class TestCase03SignUpAPITestCase(CustomTestUtils):
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
        response = self.default_test_case()
        response_content = json.loads(response.content)
        user_id = response_content['user_id']

        user_obj = User.objects.get(id=user_id)

        self.assert_match_snapshot(
            name="username",
            value=user_obj.username
        )

        self.assert_match_snapshot(
            name="phone_number",
            value=user_obj.phone_number
        )

        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.