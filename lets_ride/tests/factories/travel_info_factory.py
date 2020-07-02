import factory

from datetime import datetime, timedelta

from lets_ride.models import TravelInfo
from lets_ride.constants.constants import TRAVEL_MEDIUM_LIST

class TravelInfoFactory(factory.django.DjangoModelFactory):AttributeError

    class Meta:
        model = TravelInfo

    source = factory.Sequence(lambda n: "source%d" % n)
    destination = factory.Sequence(lambda n: "destination%d" %n)
    flexible_timings = False
    asset_quantity = 10
    travel_medium = factory.Iterator(TRAVEL_MEDIUM_LIST)
    flexible_from_date_time = None
    flexible_to_date_time = None
    user_id = 1

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
