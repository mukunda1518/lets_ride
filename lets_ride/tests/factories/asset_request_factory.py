import factory

from datetime import datetime, timedelta

from lets_ride.tests.factories.user_factory import UserFactory
from lets_ride.models.asset_request import AssetRequest
from lets_ride.constants.constants \
    import ASSETTYPE_LIST, ASSET_SENSITIVITY_LIST

class AssetRequestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = AssetRequest

    source = factory.Sequence(lambda n: "source%d" % n)
    destination = factory.Sequence(lambda n: "destination%d" %n)
    flexible_timings = False
    asset_quantity = 3
    asset_type = factory.Iterator(ASSETTYPE_LIST)
    asset_sensitivity = factory.Iterator(ASSET_SENSITIVITY_LIST)

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
