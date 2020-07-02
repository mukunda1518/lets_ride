from django_swagger_utils.utils.test import CustomAPITestCase

from freezegun import freeze_time

from datetime import datetime

from lets_ride.tests.factories.ride_request_factory \
    import RideRequestFactory
from lets_ride_auth.tests.factories.user_factory \
    import UserFactory


class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(
            CustomTestUtils, self
        ).setupUser(
            username=username, password=password
        )


    @freeze_time("2020-01-20 4:50")
    def ride_request_fixture_for_status_expired(self, user_id: int):
        RideRequestFactory.create_batch(size=2, user_id=user_id)

    @freeze_time("2023-01-20 4:50")
    def ride_request_fixture_for_status_accepted(self, user_id: int):
        user_objs = UserFactory.create_batch(size=3)
        RideRequestFactory.create_batch(
            size=2, accepted_by_id=user_objs[0].id, user_id=user_id
        )
        RideRequestFactory.create_batch(
            size=2, is_flexible_timings=True,
            accepted_by_id=user_objs[1].id, user_id=user_id
        )

    @freeze_time("2023-01-20 4:50")
    def ride_request_fixture_for_status_pending(self, user_id: int):
        RideRequestFactory.create_batch(size=2, user_id=user_id)
        RideRequestFactory.create_batch(
            size=2, is_flexible_timings=True, user_id=user_id
        )

    @freeze_time("2023-01-20 4:50")
    def ride_request_fixture_for_sort_by_seats(self, user_id: int):
        RideRequestFactory(seats=10, user_id=user_id)
        RideRequestFactory(seats=8, user_id=user_id)


    def ride_request_fixture_for_sort_by_datetime(self, user_id: int):
        RideRequestFactory(
            travel_date_time = datetime(2021,7,10,4,50), user_id=user_id
        )

        RideRequestFactory(
            user_id=user_id,
            is_flexible_timings=True,
            flexible_from_date_time = datetime(2021,6,10,4,50),
            flexible_to_date_time = datetime(2021,6,20,4,50),
            flexible_timings=True
        )



