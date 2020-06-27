import factory

from datetime import datetime, timedelta

from lets_ride.tests.factories.user_factory import UserFactory
from lets_ride.models.share_ride import ShareRide


class ShareRideFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ShareRide


    source = factory.Sequence(lambda n: "source%d" % n)
    destination = factory.Sequence(lambda n: "destination%d" %n)
    flexible_timings = False
    seats = 7
    asset_quantity = 6
    flexible_from_date_time = None
    flexible_to_date_time = None
    user = factory.SubFactory(UserFactory)

    @factory.lazy_attribute
    def travel_date_time(self):
        return datetime.now() + timedelta(10)

    class Params:
        is_flexible_timings = factory.Trait(
            flexible_timings=True,
            travel_date_time=None,
            flexible_from_date_time=factory.LazyFunction(datetime.now),
            flexible_to_date_time=factory.LazyAttribute(
                lambda obj: obj.flexible_from_date_time + timedelta(10)
            )
        )
