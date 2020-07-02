"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from lets_ride.utils.custom_test_utils import CustomTestUtils
from lets_ride.tests.factories.ride_request_factory \
    import RideRequestFactory

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"offset": 0, "limit": 3, "status": "PENDING", "sort_key": "seats", "sort_value": "ASC"},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write", "read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase03MyRideRequestsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super().setupUser(username=username, password=password)
        user_obj = self.foo_user
        user_id = user_obj.id
        self.ride_request_fixture_for_status_pending(user_id)

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.