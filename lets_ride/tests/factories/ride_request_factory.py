import factory

from datetime import datetime, timedelta

from lets_ride.models.ride_request import RideRequest

class RideRequestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RideRequest

    source = factory.Sequence(lambda n: "source%d" % n)
    destination = factory.Sequence(lambda n: "destination%d" %n)
    flexible_timings = False
    seats = 3
    laguage_quantity = 2
    flexible_from_date_time = None
    flexible_to_date_time = None
    user_id = 1
    accepted_by_id = None

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
        accept = factory.Trait(
            accepted_by_id=2
        )


