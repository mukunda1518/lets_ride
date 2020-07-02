"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from lets_ride.utils.custom_test_utils import CustomTestUtils
from lets_ride.models.share_ride import ShareRide


REQUEST_BODY = """
{
    "source": "Hyderabad",
    "destination": "Kurnool",
    "travel_date_time": "",
    "flexible_timings": true,
    "flexible_from_date_time": "2020-07-09 5:30 PM",
    "flexible_to_date_time": "2020-08-09 5:30 PM",
    "seats": 2,
    "asset_quantity": 1
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


class TestCase02ShareRideAPITestCase(CustomTestUtils):
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
        self.default_test_case()

        user_obj = self.foo_user
        user_id = user_obj.id
        ride_share_obj = ShareRide.objects.get(user_id=user_id)

        self.assert_match_snapshot(
            name="ride_request_id",
            value=ride_share_obj.id
        )

        self.assert_match_snapshot(
            name="source",
            value=ride_share_obj.source
        )

        self.assert_match_snapshot(
            name="destination",
            value=ride_share_obj.destination
        )

        self.assert_match_snapshot(
            name="travel_date_time",
            value=ride_share_obj.travel_date_time
        )

        self.assert_match_snapshot(
            name="flexible_timings",
            value=ride_share_obj.flexible_from_date_time
        )

        self.assert_match_snapshot(
            name="flexible_to_date_time",
            value=ride_share_obj.flexible_to_date_time
        )

        self.assert_match_snapshot(
            name="seats",
            value=ride_share_obj.seats
        )

        self.assert_match_snapshot(
            name="asset_quantity",
            value=ride_share_obj.asset_quantity
        )


        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.